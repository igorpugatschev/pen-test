# Занятие 45: Subdomain bruteforce — скрипт на базе словаря (aiohttp)

## Теория

**Subdomain bruteforce (перебор поддоменов)** — это техника разведки, при которой перебираются возможные поддомены целевого домена с использованием словаря. Это позволяет найти скрытые или забытые поддомены, которые могут содержать уязвимые сервисы.

**Зачем нужно:**
- Расширение поверхности атаки (больше поддоменов = больше целей)
- Поиск тестовых/админских поддоменов (admin.example.com, test.example.com)
- Обнаружение поддоменов, которые не индексируются поисковиками
- Поиск облачных сервисов (S3 buckets, GitHub Pages и т.д.)

**Библиотека `aiohttp`:**
- Асинхронная библиотека для HTTP-запросов
- Позволяет отправлять множество запросов параллельно
- Значительно быстрее синхронных аналогов (requests)

**Установка:**
```bash
pip3 install aiohttp
```

**Примечание для macOS (M2):** aiohttp полностью поддерживает архитектуру ARM64, проблем с установкой на M2 Mac не должно быть.

**Альтернативы:**
- `asyncio` + `aiohttp` (используем)
- `massdns` (высокопроизводительный инструмент на C)
- `sublist3r`, `amass` (готовые инструменты, но мы пишем свой)

## Практическое занятие

Напишем асинхронный скрипт для перебора поддоменов с использованием aiohttp.

```python
import asyncio
import aiohttp
import socket
import argparse
import json
import time
from datetime import datetime
from typing import List, Dict, Set

class SubdomainBruteforcer:
    """Асинхронный перебор поддоменов"""
    
    def __init__(self, domain: str, wordlist: str = None, threads: int = 50, timeout: int = 5):
        """
        Инициализация
        :param domain: целевой домен (например, example.com)
        :param wordlist: путь к словарю (если None, используется встроенный)
        :param threads: количество одновременных запросов
        :param timeout: таймаут для запросов
        """
        self.domain = domain.strip().lower()
        if self.domain.startswith('http://') or self.domain.startswith('https://'):
            self.domain = self.domain.split('://')[1]
        if self.domain.endswith('/'):
            self.domain = self.domain.rstrip('/')
        
        self.wordlist_path = wordlist
        self.threads = threads
        self.timeout = timeout
        self.found_subdomains: Set[str] = set()
        self.results: List[Dict] = []
        
        # Встроенный мини-словарь (если файл не предоставлен)
        self.builtin_words = [
            'www', 'mail', 'ftp', 'admin', 'blog', 'webmail', 'login', 'test',
            'dev', 'staging', 'api', 'app', 'secure', 'vpn', 'remote', 'portal',
            'shop', 'store', 'support', 'help', 'wiki', 'docs', 'git', 'gitlab',
            'jenkins', 'jira', 'confluence', 'grafana', 'kibana', 'prometheus',
            'ns1', 'ns2', 'smtp', 'pop', 'imap', 'dns', 'proxy', 'firewall',
            'router', 'switch', 'monitor', 'backup', 'db', 'sql', 'mysql', 'oracle',
            'mongo', 'redis', 'elastic', 'kafka', 'zookeeper', 'consul', 'vault',
            'auth', 'sso', 'oauth', 'ldap', 'ad', 'dc', 'exchange', 'owa',
            'cloud', 'aws', 'azure', 'gcp', 's3', 'cdn', 'static', 'assets',
            'img', 'images', 'video', 'stream', 'media', 'download', 'upload',
            'files', 'share', 'private', 'internal', 'intranet', 'extranet',
            'demo', 'beta', 'alpha', 'old', 'new', 'archive', 'legacy', 'mobile',
            'm', 'wap', 'touch', 'ios', 'android', 'app', 'apps', 'api-v1', 'api-v2'
        ]
    
    async def resolve_dns(self, subdomain: str) -> List[str]:
        """
        DNS-резолвинг поддомена
        :param subdomain: поддомен для проверки
        :return: список IP-адресов или пустой список
        """
        full_domain = f"{subdomain}.{self.domain}"
        try:
            # Используем asyncio для неблокирующего DNS-запроса
            loop = asyncio.get_event_loop()
            ips = await loop.run_in_executor(None, lambda: socket.gethostbyname_ex(full_domain)[2])
            return ips
        except socket.gaierror:
            return []
        except Exception:
            return []
    
    async def check_subdomain(self, session: aiohttp.ClientSession, subdomain: str):
        """
        Проверка одного поддомена
        :param session: aiohttp сессия
        :param subdomain: поддомен
        """
        full_domain = f"{subdomain}.{self.domain}"
        
        # Сначала DNS-резолвинг
        ips = await self.resolve_dns(subdomain)
        if not ips:
            return
        
        # Если DNS резолвится, пробуем HTTP/HTTPS
        result = {
            'subdomain': full_domain,
            'ips': ips,
            'http_status': None,
            'https_status': None,
            'content_length': None,
            'redirect': None
        }
        
        # Пробуем HTTPS
        url = f"https://{full_domain}"
        try:
            async with session.get(url, timeout=self.timeout, allow_redirects=False) as response:
                result['https_status'] = response.status
                if response.status in [301, 302, 303, 307, 308]:
                    result['redirect'] = response.headers.get('Location')
                result['content_length'] = response.headers.get('Content-Length')
        except (aiohttp.ClientError, asyncio.TimeoutError):
            pass
        
        # Если HTTPS не работает, пробуем HTTP
        if result['https_status'] is None:
            url = f"http://{full_domain}"
            try:
                async with session.get(url, timeout=self.timeout, allow_redirects=False) as response:
                    result['http_status'] = response.status
                    if response.status in [301, 302, 303, 307, 308]:
                        result['redirect'] = response.headers.get('Location')
                    result['content_length'] = response.headers.get('Content-Length')
            except (aiohttp.ClientError, asyncio.TimeoutError):
                pass
        
        # Если что-то нашли, добавляем в результаты
        if result['https_status'] or result['http_status']:
            self.found_subdomains.add(full_domain)
            self.results.append(result)
            
            status_str = ""
            if result['https_status']:
                status_str += f"HTTPS:{result['https_status']}"
            if result['http_status']:
                status_str += f" HTTP:{result['http_status']}"
            
            print(f"[+] Найден: {full_domain} -> {', '.join(ips)} [{status_str}]")
            
            if result['redirect']:
                print(f"    Редирект: {result['redirect']}")
    
    async def run_bruteforce(self):
        """Основной метод запуска перебора"""
        print(f"\n{'='*60}")
        print(f"Subdomain Bruteforce для {self.domain}")
        print(f"{'='*60}\n")
        
        # Загружаем словарь
        if self.wordlist_path:
            try:
                with open(self.wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                    words = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                print(f"[+] Загружено слов из файла: {len(words)}")
            except FileNotFoundError:
                print(f"[-] Файл словаря не найден: {self.wordlist_path}")
                print(f"[-] Используем встроенный словарь ({len(self.builtin_words)} слов)")
                words = self.builtin_words
        else:
            print(f"[+] Используем встроенный словарь ({len(self.builtin_words)} слов)")
            words = self.builtin_words
        
        # Проверяем, что домен резолвится
        try:
            base_ip = socket.gethostbyname(self.domain)
            print(f"[+] Базовый домен резолвится: {self.domain} -> {base_ip}\n")
        except socket.gaierror:
            print(f"[-] Базовый домен не резолвится: {self.domain}")
            print("[-] Проверьте правильность домена")
            return
        
        start_time = time.time()
        
        # Создаем aiohttp сессию
        connector = aiohttp.TCPConnector(ssl=False, limit=self.threads)
        timeout = aiohttp.ClientTimeout(total=self.timeout)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            # Создаем задачи для всех слов
            tasks = []
            for word in words:
                task = asyncio.create_task(self.check_subdomain(session, word))
                tasks.append(task)
            
            # Запускаем с семафором для ограничения одновременных запросов
            semaphore = asyncio.Semaphore(self.threads)
            
            async def bounded_check(subdomain):
                async with semaphore:
                    await self.check_subdomain(session, subdomain)
            
            # Запускаем все задачи
            await asyncio.gather(*[bounded_check(word) for word in words])
        
        elapsed = time.time() - start_time
        
        print(f"\n{'='*60}")
        print(f"Сканирование завершено за {elapsed:.2f} секунд")
        print(f"Найдено поддоменов: {len(self.found_subdomains)}")
        print(f"Скорость: {len(words) / elapsed:.2f} запросов/сек")
        print(f"{'='*60}\n")
    
    def save_results(self, output_file: str = None):
        """Сохранение результатов"""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"subdomains_{self.domain}_{timestamp}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'domain': self.domain,
                'scan_time': datetime.now().isoformat(),
                'found_count': len(self.found_subdomains),
                'results': self.results
            }, f, indent=2, ensure_ascii=False)
        
        print(f"[+] Результаты сохранены: {output_file}")
        
        # Также сохраняем простой список поддоменов
        txt_file = output_file.replace('.json', '.txt')
        with open(txt_file, 'w', encoding='utf-8') as f:
            for result in self.results:
                f.write(f"{result['subdomain']}\n")
        print(f"[+] Список поддоменов сохранен: {txt_file}")

async def main():
    """Точка входа"""
    parser = argparse.ArgumentParser(description='Асинхронный перебор поддоменов')
    parser.add_argument('domain', help='Целевой домен (например, example.com)')
    parser.add_argument('-w', '--wordlist', help='Путь к словарю')
    parser.add_argument('-t', '--threads', type=int, default=50, help='Количество потоков (по умолчанию: 50)')
    parser.add_argument('-o', '--output', help='Файл для сохранения результатов')
    
    args = parser.parse_args()
    
    bruteforcer = SubdomainBruteforcer(
        domain=args.domain,
        wordlist=args.wordlist,
        threads=args.threads
    )
    
    await bruteforcer.run_bruteforce()
    bruteforcer.save_results(args.output)

if __name__ == "__main__":
    asyncio.run(main())
```

**Объяснение кода:**
1. Используем `asyncio` для асинхронного выполнения
2. `aiohttp.ClientSession` — для HTTP-запросов
3. `socket.gethostbyname` — для DNS-резолвинга (синхронный, но запускается в executor)
4. Семафор ограничивает количество одновременных запросов
5. Проверяем и HTTPS, и HTTP
6. Сохраняем результаты в JSON и простой текст

**Запуск:**
```bash
# С встроенным словарём
python lesson_45_subdomain.py example.com

# Со своим словарём
python lesson_45_subdomain.py example.com -w /path/to/wordlist.txt -t 100

# Сохранение в файл
python lesson_45_subdomain.py example.com -o results.json
```

**Где взять словари:**
- `/usr/share/wordlists/SecLists/Discovery/DNS/` (в Kali Linux)
- https://github.com/danielmiessler/SecLists
- Создайте свой список часто встречающихся поддоменов

## Примеры вывода

Пример успешного выполнения скрипта для `example.com`:

```
============================================================
Subdomain Bruteforce для example.com
============================================================

[+] Используем встроенный словарь (50 слов)

[+] Базовый домен резолвится: example.com -> 93.184.216.34

[+] Найден: www.example.com -> ['93.184.216.34'] [HTTPS:200]
[+] Найден: mail.example.com -> ['93.184.216.35'] [HTTPS:200]
[+] Найден: admin.example.com -> ['93.184.216.36'] [HTTP:301]
    Редирект: https://admin.example.com/login

============================================================
Сканирование завершено за 2.34 секунд
Найдено поддоменов: 3
Скорость: 21.37 запросов/сек
============================================================
```

## Частые ошибки

1. **`asyncio.exceptions.TimeoutError`** — Превышен таймаут запроса. Увеличьте параметр `timeout` или уменьшите количество потоков.
2. **`aiohttp.ClientConnectorCertificateError`** — Ошибка SSL-сертификата. Убедитесь, что используете `connector = aiohttp.TCPConnector(ssl=False)` вместо передачи `ssl=False` в `get()`.
3. **`socket.gaierror: [Errno 8] nodename nor servname provided`** — Домен не резолвится. Проверьте правильность написания цели.
4. **Слишком медленная работа** — Увеличьте количество потоков (`-t 100`), но на M2 с 8GB RAM не стоит превышать 50-70.

## Вопросы на понимание

1. **Почему для перебора поддоменов используется асинхронный подход (asyncio), а не многопоточность?**
   <details>
   <summary>Ответ</summary>
   Асинхронность позволяет обрабатывать тысячи соединений в одном потоке, переключаясь между задачами при ожидании I/O. Это эффективнее многопоточности для сетевых задач, так как меньше накладных расходов на создание и переключение потоков.
   </details>

2. **Зачем нужен семафор (`asyncio.Semaphore`) в коде?**
   <details>
   <summary>Ответ</summary>
   Семафор ограничивает количество одновременно выполняющихся задач. Без него при 1000 поддоменах запустятся 1000 одновременных запросов, что может привести к исчерпанию ресурсов системы или блокировке со стороны цели.
   </details>

3. **В чем разница между `socket.gethostbyname()` и `socket.gethostbyname_ex()`?**
   <details>
   <summary>Ответ</summary>
   `gethostbyname()` возвращает только основной IP-адрес. `gethostbyname_ex()` возвращает кортеж, включающий имя хоста, псевдонимы и список всех IP-адресов, что полезно для доменов с несколькими A-записями.
   </details>

## Задачи для самостоятельного выполнения

1. **Расширенный словарь:** Скачайте SecLists и протестируйте скрипт на реальном домене (с разрешения владельца). Сравните результаты со встроенным словарём.

2. **Wildcard detection:** Добавьте проверку на wildcard DNS-записи. Если домен имеет wildcard (*.example.com), то любой поддомен будет резолвиться. Это даст много ложноположительных результатов. Нужно определить наличие wildcard и игнорировать его.

3. **HTTP заголовки:** Расширьте скрипт для получения и сохранения интересных HTTP-заголовков: Server, X-Powered-By, технологии (по заголовкам или по response body).

4. **Screenshot (опционально):** Интегрируйте возможность сделать скриншоты найденных поддоменов с использованием библиотеки `playwright` или `selenium`.

5. **Takeover проверка:** Добавьте проверку на возможность subdomain takeover (например, CNAME указывает на несуществующий ресурс GitHub Pages, S3 и т.д.).

6. **Поиск в коде:** Добавьте проверку, не светятся ли поддомены в исходном коде главного домена (парсинг HTML, поиск ссылок на поддомены).

7. **Certificate transparency:** Интегрируйте поиск поддоменов через Certificate Transparency logs (API: https://crt.sh/?q=example.com). Это пассивный метод, который не генерирует трафик к цели.

## Адаптация под macOS (M2, 8GB)

При выполнении заданий на компьютере Mac с процессором M2 и 8GB оперативной памяти учитывайте следующие особенности:

- Для установки библиотек используйте `pip3 install <package>`, а не `pip install`.
- На M2 можно использовать `asyncio`, он поддерживает ARM.
- На 8GB RAM проект может быть тяжелым, используйте легковесные библиотеки.
- Для aiohttp: `connector = aiohttp.TCPConnector(ssl=False)` вместо `ssl=False` в get()
