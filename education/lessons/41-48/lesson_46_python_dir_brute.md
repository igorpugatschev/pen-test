# Занятие 46: Directory bruteforce — скрипт поиска директорий (как dirsearch)

## Теория

**Directory bruteforce (перебор директорий и файлов)** — это техника поиска скрытых файлов и папок на веб-сервере путем перебора возможных путей. Это один из этапов разведки веб-приложений.

**Зачем нужно:**
- Поиск административных панелей (/admin, /administrator)
- Поиск файлов конфигурации (/config.php, /.env)
- Поиск резервных копий (/backup.zip, /db.sql)
- Поиск тестовых/отладочных страниц
- Обнаружение скрытых API эндпоинтов

**Инструменты:**
- `dirsearch` (Python)
- `gobuster` (Go)
- `ffuf` (Go, очень быстрый)
- `wfuzz` (Python)

**Библиотеки:**
- `aiohttp` или `httpx` — для асинхронных HTTP-запросов
- `asyncio` — для асинхронности

**Установка:**
```bash
pip install aiohttp
```

## Практическое занятие

Напишем асинхронный скрипт для перебора директорий, аналогичный dirsearch.

```python
import asyncio
import aiohttp
import argparse
import json
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Set

class DirectoryBruteforcer:
    """Перебор директорий и файлов на веб-сервере"""
    
    def __init__(
        self,
        target_url: str,
        wordlist: str = None,
        extensions: List[str] = None,
        threads: int = 50,
        timeout: int = 10,
        exclude_codes: List[int] = None,
        include_codes: List[int] = None
    ):
        """
        Инициализация
        :param target_url: целевой URL
        :param wordlist: путь к словарю
        :param extensions: список расширений (например, ['php', 'html', 'txt'])
        :param threads: количество потоков
        :param timeout: таймаут запроса
        :param exclude_codes: коды ответа для исключения (например, [404])
        :param include_codes: коды ответа для включения (если указано, другие игнорируются)
        """
        self.target_url = target_url.rstrip('/') if target_url else ""
        self.wordlist_path = wordlist
        self.extensions = extensions or []
        self.threads = threads
        self.timeout = timeout
        self.exclude_codes = exclude_codes or [404]
        self.include_codes = include_codes
        
        self.found_paths: List[Dict] = []
        self.tested_count = 0
        self.start_time = None
        
        # Встроенный мини-словарь
        self.builtin_words = [
            'admin', 'administrator', 'login', 'logout', 'register', 'signup',
            'dashboard', 'panel', 'cp', 'control', 'manage', 'manager',
            'backup', 'backups', 'old', 'new', 'test', 'dev', 'staging', 'prod',
            'api', 'api/v1', 'api/v2', 'api/v3', 'rest', 'soap', 'graphql',
            'config', 'configuration', 'settings', 'setup', 'install', 'installer',
            'db', 'database', 'sql', 'mysql', 'mongo', 'redis',
            'logs', 'log', 'debug', 'info', 'status', 'health', 'metrics',
            'assets', 'static', 'css', 'js', 'images', 'img', 'uploads', 'files',
            'upload', 'file', 'download', 'downloads', 'media', 'video', 'audio',
            'docs', 'doc', 'documentation', 'help', 'support', 'faq',
            'robots.txt', 'sitemap.xml', 'favicon.ico', '.htaccess', '.env',
            'web.config', 'phpinfo.php', 'info.php', 'test.php', 'phpinfo',
            'console', 'shell', 'cmd', 'terminal', 'root', 'home',
            'user', 'users', 'profile', 'account', 'accounts',
            'mail', 'email', 'smtp', 'pop3', 'imap',
            'cgi-bin', 'cgi', 'bin', 'sbin', 'usr', 'var', 'etc',
            'src', 'source', 'code', 'git', '.git', 'svn', '.svn', 'cvs',
            'backup.zip', 'backup.tar.gz', 'db.sql', 'dump.sql',
            'private', 'secret', 'hidden', 'secure', 'security',
            'wp-admin', 'wp-login.php', 'wp-config.php', 'wordpress',
            'joomla', 'drupal', 'magento', 'shop', 'store',
            'app', 'application', 'services', 'service', 'healthcheck'
        ]
    
    def generate_paths(self, word: str) -> List[str]:
        """
        Генерация путей из слова (с учетом расширений)
        :param word: слово из словаря
        :return: список путей
        """
        paths = [word]
        
        # Если слово уже содержит точку (файл), не добавляем расширения
        if '.' in word:
            return paths
        
        # Добавляем расширения
        for ext in self.extensions:
            paths.append(f"{word}.{ext}")
        
        return paths
    
    async def check_path(self, session: aiohttp.ClientSession, path: str):
        """
        Проверка одного пути
        :param session: aiohttp сессия
        :param path: путь для проверки
        """
        url = urljoin(self.target_url + '/', path)
        
        try:
            async with session.get(url, timeout=self.timeout, allow_redirects=False) as response:
                status = response.status
                self.tested_count += 1
                
                # Проверяем, нужно ли включать этот код ответа
                if self.include_codes and status not in self.include_codes:
                    return
                
                # Проверяем, нужно ли исключать этот код ответа
                if status in self.exclude_codes:
                    return
                
                # Получаем информацию о ответе
                content_length = response.headers.get('Content-Length', '0')
                content_type = response.headers.get('Content-Type', 'unknown')
                redirect_location = None
                
                if status in [301, 302, 303, 307, 308]:
                    redirect_location = response.headers.get('Location')
                
                result = {
                    'url': url,
                    'status': status,
                    'content_length': content_length,
                    'content_type': content_type,
                    'redirect': redirect_location,
                    'path': path
                }
                
                self.found_paths.append(result)
                
                # Красивый вывод
                status_color = ""
                if status == 200:
                    status_color = "[200]"  # Можно добавить цвета
                elif status == 301 or status == 302:
                    status_color = f"[{status} -> {redirect_location}]"
                elif status == 403:
                    status_color = "[403]"
                else:
                    status_color = f"[{status}]"
                
                print(f"{status_color:15} {url:50} {content_length:10} {content_type[:30]}")
                
        except aiohttp.ClientError as e:
            self.tested_count += 1
            # Игнорируем ошибки соединения
            pass
        except asyncio.TimeoutError:
            self.tested_count += 1
            print(f"[TIMEOUT]        {url}")
        except Exception as e:
            self.tested_count += 1
            pass
    
    async def run_bruteforce(self):
        """Основной метод запуска перебора"""
        print(f"\n{'='*70}")
        print(f"Directory Bruteforce")
        print(f"Цель: {self.target_url}")
        print(f"{'='*70}\n")
        
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
        
        # Генерируем все пути (с учетом расширений)
        all_paths = []
        for word in words:
            all_paths.extend(self.generate_paths(word))
        
        print(f"[+] Всего путей для проверки: {len(all_paths)}")
        if self.extensions:
            print(f"[+] Расширения: {', '.join(self.extensions)}")
        print(f"[+] Потоков: {self.threads}")
        print(f"\n{'='*70}")
        print(f"{'Статус':15} {'URL':50} {'Размер':10} {'Тип'}")
        print(f"{'='*70}")
        
        self.start_time = time.time()
        
        # Создаем сессию
        connector = aiohttp.TCPConnector(ssl=False, limit=self.threads)
        timeout = aiohttp.ClientTimeout(total=self.timeout)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            # Семафор для ограничения одновременных запросов
            semaphore = asyncio.Semaphore(self.threads)
            
            async def bounded_check(path):
                async with semaphore:
                    await self.check_path(session, path)
            
            # Запускаем все проверки
            await asyncio.gather(*[bounded_check(path) for path in all_paths])
        
        elapsed = time.time() - self.start_time
        
        print(f"\n{'='*70}")
        print(f"Сканирование завершено за {elapsed:.2f} секунд")
        print(f"Проверено путей: {self.tested_count}")
        print(f"Найдено путей: {len(self.found_paths)}")
        print(f"Скорость: {self.tested_count / elapsed:.2f} запросов/сек")
        print(f"{'='*70}\n")
    
    def save_results(self, output_file: str = None):
        """Сохранение результатов"""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            parsed = urlparse(self.target_url)
            domain = parsed.netloc or parsed.path
            output_file = f"dir_brute_{domain}_{timestamp}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'target': self.target_url,
                'scan_time': datetime.now().isoformat(),
                'tested_count': self.tested_count,
                'found_count': len(self.found_paths),
                'results': self.found_paths
            }, f, indent=2, ensure_ascii=False)
        
        print(f"[+] Результаты сохранены: {output_file}")
        
        # Сохраняем только найденные URL
        txt_file = output_file.replace('.json', '.txt')
        with open(txt_file, 'w', encoding='utf-8') as f:
            for result in self.found_paths:
                f.write(f"{result['url']}\n")
        print(f"[+] Список URL сохранен: {txt_file}")

async def main():
    """Точка входа"""
    parser = argparse.ArgumentParser(description='Directory Bruteforce (аналог dirsearch)')
    parser.add_argument('url', help='Целевой URL (например, http://example.com)')
    parser.add_argument('-w', '--wordlist', help='Путь к словарю')
    parser.add_argument('-e', '--extensions', help='Расширения через запятую (например, php,html,txt)')
    parser.add_argument('-t', '--threads', type=int, default=50, help='Количество потоков (по умолчанию: 50)')
    parser.add_argument('-o', '--output', help='Файл для сохранения результатов')
    parser.add_argument('-x', '--exclude-codes', help='Коды для исключения (например, 404,500)')
    parser.add_argument('-i', '--include-codes', help='Коды для включения (например, 200,301,403)')
    
    args = parser.parse_args()
    
    # Парсим расширения
    extensions = []
    if args.extensions:
        extensions = [ext.strip() for ext in args.extensions.split(',')]
    
    # Парсим коды ответов
    exclude_codes = [404]
    if args.exclude_codes:
        exclude_codes = [int(code.strip()) for code in args.exclude_codes.split(',')]
    
    include_codes = None
    if args.include_codes:
        include_codes = [int(code.strip()) for code in args.include_codes.split(',')]
    
    bruteforcer = DirectoryBruteforcer(
        target_url=args.url,
        wordlist=args.wordlist,
        extensions=extensions,
        threads=args.threads,
        exclude_codes=exclude_codes,
        include_codes=include_codes
    )
    
    await bruteforcer.run_bruteforce()
    bruteforcer.save_results(args.output)

if __name__ == "__main__":
    asyncio.run(main())
```

**Объяснение кода:**
1. Генерирует пути из словаря, добавляя расширения (если указаны)
2. Асинхронно проверяет каждый путь через aiohttp
3. Фильтрует ответы по кодам (исключает 404 по умолчанию)
4. Выводит красивый прогресс с информацией о найденных путях
5. Сохраняет результаты в JSON и текстовый файл

**Запуск:**
```bash
# Базовый запуск
python lesson_46_dir_brute.py http://example.com

# Со словарём и расширениями
python lesson_46_dir_brute.py http://example.com -w wordlist.txt -e php,html,txt,js,css

# С фильтрацией кодов
python lesson_46_dir_brute.py http://example.com -i 200,301,302,403

# Больше потоков
python lesson_46_dir_brute.py http://example.com -t 100
```

**Где взять словари:**
- `/usr/share/wordlists/dirbuster/` (Kali Linux)
- `/usr/share/wordlists/dirb/` (Kali Linux)
- SecLists: https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content

## Задачи для самостоятельного выполнения

1. **Recursive bruteforce:** Добавьте возможность рекурсивного перебора. Если найдена директория (например, `/admin/`), продолжить перебор внутри неё (`/admin/config`, `/admin/users` и т.д.).

2. **Response diffing:** Добавьте анализ ответов для уменьшения ложноположительных срабатываний. Сравните ответы с 404 ошибкой (кастомная страница 404 может возвращать 200). Используйте длину контента, хэш контента или ключевые слова.

3. **Authentication:** Добавьте поддержку аутентификации: Basic Auth, Cookie, Headers (для доступа к защищенным областям).

4. **Proxy support:** Добавьте возможность отправки запросов через прокси (SOCKS5/HTTP). Полезно для анонимности или обхода блокировок.

5. **Extensions from response:** Добавьте автоопределение расширений на основе технологий сайта (например, если видим PHP-заголовки, добавляем .php в перебор).

6. **Backup file detection:** Создайте отдельную функцию для поиска файлов резервных копий. Например, для `config.php` искать `config.php.bak`, `config.php~`, `config.php.old`, `config.php.2024` и т.д.

7. **Integration с Burp Suite:** Добавьте возможность отправки найденных путей в Burp Suite (через Burp API или просто сохранение в формате, понятном Burp).
