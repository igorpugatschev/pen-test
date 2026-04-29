# Занятие 48: Итог Python — создать мини-инструмент и выложить на GitHub

## Теория

На этом занятии мы объединим все полученные знания и создадим полноценный инструмент для пентеста. Это итоговый проект, который можно добавить в портфолио и выложить на GitHub.

**Что должен уметь инструмент:**
- Автоматизировать рутинные задачи разведки
- Быть удобным в использовании (CLI интерфейс)
- Иметь понятный вывод результатов
- Сохранять результаты в различных форматах
- Иметь документацию (README)

**Этапы создания инструмента:**
1. Планирование функционала
2. Структурирование кода (модули, классы)
3. Реализация основных функций
4. Добавление CLI интерфейса (argparse)
5. Обработка ошибок и исключений
6. Написание документации (README.md)
7. Публикация на GitHub

**Полезные библиотеки для CLI:**
- `argparse` (стандартная) — парсинг аргументов командной строки
- `click` — более удобная альтернатива argparse
- `rich` — красивый вывод в терминале (таблицы, цвета, прогресс-бары)

**Установка дополнительных библиотек:**
```bash
pip install rich
```

## Практическое занятие

Создадим инструмент **"ReconTool"** — мини-фреймворк для разведки веб-приложений и сетей.

### Структура проекта

```
recon_tool/
├── README.md
├── requirements.txt
├── setup.py (опционально)
├── recon_tool/
│   ├── __init__.py
│   ├── main.py          # Точка входа
│   ├── scanner.py       # Сканирование портов (на базе урока 41)
│   ├── http_utils.py    # HTTP запросы (на базе урока 42)
│   ├── dir_brute.py     # Перебор директорий (на базе урока 46)
│   ├── subdomain.py     # Перебор поддоменов (на базе урока 45)
│   ├── nmap_parser.py   # Парсинг Nmap (на базе урока 44)
│   ├── cve_search.py    # Поиск CVE (на базе урока 47)
│   └── utils.py         # Вспомогательные функции
└── tests/               # Тесты (опционально)
```

**Примечание для macOS (M2, 8GB RAM):** Проект может быть ресурсоемким при запуске всех модулей. Рекомендуется использовать легковесные библиотеки и ограничивать количество потоков (например, `-t 20` вместо 50). aiohttp отлично работает на ARM64.

### Основной файл (main.py)

```python
#!/usr/bin/env python3
"""
ReconTool - Инструмент для разведки в пентесте
Автор: [Ваше Имя]
Лицензия: MIT (для учебных целей)
"""

import argparse
import sys
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Импорт модулей инструмента (классы на базе предыдущих уроков)
from scanner import PortScanner                    # Урок 41
from http_utils import HTTPRequester              # Урок 42
from dir_brute import DirectoryBruteforcer        # Урок 46
from subdomain import SubdomainBruteforcer        # Урок 45
from nmap_parser import NmapParser                # Урок 44
from cve_search import CVEParser                  # Урок 47

console = Console()

class ReconTool:
    """Основной класс инструмента разведки"""
    
    def __init__(self, target, output_dir="results"):
        self.target = target
        self.output_dir = output_dir
        self.results = {
            'target': target,
            'scan_time': datetime.now().isoformat(),
            'modules': {}
        }
        
        # Создаем директорию для результатов
        import os
        os.makedirs(output_dir, exist_ok=True)
    
    def run_port_scan(self, ports=None):
        """Сканирование портов"""
        console.print(Panel.fit("🔍 Сканирование портов", style="bold blue"))
        
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389, 8080, 8443]
        
        scanner = PortScanner(self.target, ports)
        open_ports = scanner.scan()
        
        if open_ports:
            table = Table(title=f"Открытые порты на {self.target}")
            table.add_column("Порт", style="cyan")
            table.add_column("Статус", style="green")
            table.add_column("Сервис", style="yellow")
            
            for port_info in open_ports:
                table.add_row(
                    str(port_info['port']),
                    port_info['state'],
                    port_info.get('service', 'unknown')
                )
            
            console.print(table)
            self.results['modules']['port_scan'] = open_ports
        else:
            console.print("[yellow]Открытых портов не найдено[/yellow]")
        
        return open_ports
    
    def run_http_analysis(self, url=None):
        """Анализ HTTP/HTTPS"""
        console.print(Panel.fit("🌐 Анализ HTTP", style="bold blue"))
        
        if url is None:
            # Пробуем HTTPS, потом HTTP
            url = f"https://{self.target}"
            try:
                requester = HTTPRequester(url)
                info = requester.analyze()
            except:
                url = f"http://{self.target}"
                requester = HTTPRequester(url)
                info = requester.analyze()
        else:
            requester = HTTPRequester(url)
            info = requester.analyze()
        
        if info:
            table = Table(title=f"HTTP информация для {url}")
            table.add_column("Параметр", style="cyan")
            table.add_column("Значение", style="green")
            
            for key, value in info.items():
                if isinstance(value, list):
                    value = ', '.join(map(str, value))
                table.add_row(key, str(value))
            
            console.print(table)
            self.results['modules']['http_analysis'] = info
        
        return info
    
    def run_subdomain_bruteforce(self, wordlist=None, threads=50):
        """Перебор поддоменов"""
        console.print(Panel.fit("🎯 Перебор поддоменов", style="bold blue"))
        
        bruteforcer = SubdomainBruteforcer(
            domain=self.target,
            wordlist=wordlist,
            threads=threads
        )
        
        found = bruteforcer.run()
        
        if found:
            console.print(f"[green]Найдено поддоменов: {len(found)}[/green]")
            self.results['modules']['subdomains'] = found
        else:
            console.print("[yellow]Поддоменов не найдено[/yellow]")
        
        return found
    
    def run_dir_bruteforce(self, url=None, wordlist=None, extensions=None, threads=50):
        """Перебор директорий"""
        console.print(Panel.fit("📁 Перебор директорий", style="bold blue"))
        
        if url is None:
            url = f"http://{self.target}"
        
        bruteforcer = DirectoryBruteforcer(
            target_url=url,
            wordlist=wordlist,
            extensions=extensions or ['php', 'html', 'txt', 'js', 'css'],
            threads=threads
        )
        
        found = bruteforcer.run()
        
        if found:
            console.print(f"[green]Найдено путей: {len(found)}[/green]")
            self.results['modules']['directories'] = found
        else:
            console.print("[yellow]Директорий не найдено[/yellow]")
        
        return found
    
    def run_cve_search(self, product=None, version=None):
        """Поиск CVE"""
        console.print(Panel.fit("🛡️ Поиск CVE", style="bold blue"))
        
        searcher = CVESearcher()
        
        if product:
            keyword = f"{product} {version}" if version else product
            cves = searcher.search_by_keyword(keyword)
            
            if cves:
                table = Table(title=f"CVE для {keyword}")
                table.add_column("CVE ID", style="red")
                table.add_column("CVSS", style="yellow")
                table.add_column("Описание", style="green")
                
                for cve in cves[:10]:  # Первые 10
                    table.add_row(
                        cve['id'],
                        str(cve.get('cvss_score', 'N/A')),
                        cve.get('description', '')[:100] + '...'
                    )
                
                console.print(table)
                self.results['modules']['cve'] = cves
            else:
                console.print("[yellow]CVE не найдены[/yellow]")
        
        return cves if 'cves' in locals() else []
    
    def save_results(self, filename=None):
        """Сохранение результатов"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recon_{self.target}_{timestamp}.json"
        
        filepath = f"{self.output_dir}/{filename}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        console.print(f"[green]Результаты сохранены: {filepath}[/green]")
        return filepath
    
    def generate_report(self):
        """Генерация текстового отчета"""
        report = []
        report.append("=" * 60)
        report.append("ReconTool - Отчет о разведке")
        report.append("=" * 60)
        report.append(f"Цель: {self.target}")
        report.append(f"Время: {self.results['scan_time']}")
        report.append("")
        
        for module_name, module_data in self.results['modules'].items():
            report.append(f"\n--- Модуль: {module_name} ---")
            if isinstance(module_data, list):
                report.append(f"Найдено записей: {len(module_data)}")
                for item in module_data[:10]:  # Первые 10
                    report.append(f"  {item}")
            elif isinstance(module_data, dict):
                for key, value in module_data.items():
                    report.append(f"  {key}: {value}")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)

def main():
    """Точка входа"""
    parser = argparse.ArgumentParser(
        description='ReconTool - Инструмент для разведки в пентесте',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  %(prog)s example.com --all
  %(prog)s example.com --ports --http
  %(prog)s example.com --subdomains -w wordlist.txt
  %(prog)s example.com --dirs -e php,html,bak
        """
    )
    
    parser.add_argument('target', help='Цель (домен или IP)')
    parser.add_argument('--all', action='store_true', help='Запустить все модули')
    parser.add_argument('--ports', action='store_true', help='Сканирование портов')
    parser.add_argument('--http', action='store_true', help='HTTP анализ')
    parser.add_argument('--subdomains', action='store_true', help='Перебор поддоменов')
    parser.add_argument('--dirs', action='store_true', help='Перебор директорий')
    parser.add_argument('--cve', action='store_true', help='Поиск CVE')
    
    parser.add_argument('-w', '--wordlist', help='Словарь для перебора')
    parser.add_argument('-e', '--extensions', help='Расширения для dir brute (через запятую)')
    parser.add_argument('-t', '--threads', type=int, default=50, help='Количество потоков')
    parser.add_argument('-o', '--output', help='Файл для сохранения результатов')
    parser.add_argument('--report', help='Файл для текстового отчета')
    
    args = parser.parse_args()
    
    # Если не выбран ни один модуль, показываем help
    if not any([args.all, args.ports, args.http, args.subdomains, args.dirs, args.cve]):
        parser.print_help()
        sys.exit(1)
    
    console.print(Panel.fit(
        f"[bold green]ReconTool[/bold green] - Разведка цели: [bold yellow]{args.target}[/bold yellow]",
        title="Запуск",
        border_style="blue"
    ))
    
    # Инициализация инструмента
    tool = ReconTool(args.target)
    
    try:
        # Запуск выбранных модулей
        if args.all or args.ports:
            tool.run_port_scan()
        
        if args.all or args.http:
            tool.run_http_analysis()
        
        if args.all or args.subdomains:
            tool.run_subdomain_bruteforce(args.wordlist, args.threads)
        
        if args.all or args.dirs:
            extensions = args.extensions.split(',') if args.extensions else None
            tool.run_dir_bruteforce(wordlist=args.wordlist, extensions=extensions, threads=args.threads)
        
        if args.all or args.cve:
            tool.run_cve_search()
        
        # Сохранение результатов
        tool.save_results(args.output)
        
        # Генерация отчета
        if args.report:
            report_text = tool.generate_report()
            with open(args.report, 'w', encoding='utf-8') as f:
                f.write(report_text)
            console.print(f"[green]Отчет сохранен: {args.report}[/green]")
        
        console.print(Panel.fit(
            "[bold green]Разведка завершена![/bold green]",
            border_style="green"
        ))
    
    except KeyboardInterrupt:
        console.print("\n[yellow]Прервано пользователем[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Ошибка: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Модуль scanner.py (на базе урока 41)

```python
# scanner.py - Сканирование портов (обертка для tcp_port_scanner)
import socket
from datetime import datetime

class PortScanner:
    """Сканер портов на базе урока 41"""
    
    def __init__(self, target, ports=None):
        self.target = target
        self.ports = ports or [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389, 8080, 8443]
        self.found_ports = []
    
    def scan(self):
        """Запуск сканирования"""
        print(f"\n[+] Начало сканирования: {self.target}")
        print(f"[+] Время начала: {datetime.now()}\n")
        
        try:
            target_ip = socket.gethostbyname(self.target)
            print(f"[+] IP адрес цели: {target_ip}\n")
        except socket.gaierror:
            print("[-] Ошибка разрешения имени хоста")
            return []
        
        for port in self.ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target_ip, port))
                
                if result == 0:
                    print(f"[+] Порт {port}: ОТКРЫТ")
                    self.found_ports.append({'port': port, 'state': 'open', 'service': 'unknown'})
                else:
                    print(f"[-] Порт {port}: закрыт")
                
                sock.close()
            except socket.error:
                print(f"[-] Ошибка соединения с портом {port}")
        
        print(f"\n[+] Найдено открытых портов: {len(self.found_ports)}")
        return self.found_ports
```

### Модуль http_utils.py (на базе урока 42)

```python
# http_utils.py - HTTP запросы (обертка для http_request_explorer)
import requests
import json
import urllib3
from urllib.parse import urljoin

# Отключаем предупреждения о SSL
urllib3.disable_warnings()

class HTTPRequester:
    """HTTP анализатор на базе урока 42"""
    
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })
        self.info = {}
    
    def analyze(self):
        """Анализ HTTP/HTTPS цели"""
        print(f"[+] Исследование цели: {self.target_url}\n")
        
        try:
            response = self.session.get(self.target_url, timeout=10, verify=False)
            
            self.info = {
                'url': self.target_url,
                'status_code': response.status_code,
                'content_length': len(response.content),
                'content_type': response.headers.get('Content-Type', 'не указан'),
                'server': response.headers.get('Server', 'не указан'),
                'cookies': list(response.cookies.keys()) if response.cookies else [],
            }
            
            # Проверка заголовков безопасности
            security_headers = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options']
            self.info['security_headers'] = {}
            for header in security_headers:
                self.info['security_headers'][header] = header in response.headers
            
            return self.info
        except Exception as e:
            print(f"[-] Ошибка: {e}")
            return None
```

### Модуль subdomain.py (на базе урока 45)

```python
# subdomain.py - Перебор поддоменов (адаптированный урок 45)
import asyncio
import aiohttp
import socket
import json
from typing import List, Dict, Set

class SubdomainBruteforcer:
    """Перебор поддоменов на базе урока 45"""
    
    def __init__(self, domain: str, wordlist: str = None, threads: int = 20, timeout: int = 5):
        self.domain = domain.strip().lower()
        if self.domain.startswith('http://') or self.domain.startswith('https://'):
            self.domain = self.domain.split('://')[1]
        self.wordlist_path = wordlist
        self.threads = threads
        self.timeout = timeout
        self.found_subdomains: Set[str] = set()
        self.results: List[Dict] = []
        
        self.builtin_words = [
            'www', 'mail', 'ftp', 'admin', 'blog', 'webmail', 'login', 'test',
            'dev', 'staging', 'api', 'app', 'secure', 'vpn', 'portal',
            'shop', 'support', 'wiki', 'docs', 'git', 'jenkins', 'jira',
        ]
    
    async def check_subdomain(self, session: aiohttp.ClientSession, subdomain: str):
        full_domain = f"{subdomain}.{self.domain}"
        try:
            ips = socket.gethostbyname_ex(full_domain)[2]
            if ips:
                self.found_subdomains.add(full_domain)
                self.results.append({'subdomain': full_domain, 'ips': ips})
                print(f"[+] Найден: {full_domain} -> {', '.join(ips)}")
        except socket.gaierror:
            pass
    
    def run(self):
        """Запуск перебора (синхронная обертка)"""
        asyncio.run(self._run())
        return list(self.found_subdomains)
    
    async def _run(self):
        """Внутренний асинхронный запуск"""
        connector = aiohttp.TCPConnector(ssl=False, limit=self.threads)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [self.check_subdomain(session, word) for word in self.builtin_words]
            await asyncio.gather(*tasks)
```

### Модуль dir_brute.py (на базе урока 46)

```python
# dir_brute.py - Перебор директорий (адаптированный урок 46)
import asyncio
import aiohttp
from typing import List, Dict

class DirectoryBruteforcer:
    """Перебор директорий на базе урока 46"""
    
    def __init__(self, target_url: str, wordlist: str = None, extensions: List[str] = None, threads: int = 20):
        self.target_url = target_url.rstrip('/')
        self.extensions = extensions or []
        self.threads = threads
        self.found_paths: List[Dict] = []
        
        self.builtin_words = [
            'admin', 'login', 'backup', 'config', 'db', 'logs',
            'robots.txt', 'sitemap.xml', '.env', 'phpinfo.php',
        ]
    
    async def check_path(self, session: aiohttp.ClientSession, path: str):
        url = f"{self.target_url}/{path}"
        try:
            async with session.get(url, timeout=5, allow_redirects=False) as response:
                if response.status != 404:
                    self.found_paths.append({'url': url, 'status': response.status})
                    print(f"[{response.status}] {url}")
        except:
            pass
    
    def run(self):
        """Запуск перебора (синхронная обертка)"""
        asyncio.run(self._run())
        return self.found_paths
    
    async def _run(self):
        """Внутренний асинхронный запуск"""
        connector = aiohttp.TCPConnector(ssl=False, limit=self.threads)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [self.check_path(session, word) for word in self.builtin_words]
            await asyncio.gather(*tasks)
```

### Модуль nmap_parser.py (на базе урока 44)

```python
# nmap_parser.py - Парсинг Nmap (из урока 44)
# Используйте код из урока 44: class NmapParser
# Для краткости здесь приведен интерфейс:
from lesson_44_nmap import NmapParser as BaseNmapParser

class NmapParser(BaseNmapParser):
    """Наследуем от класса урока 44"""
    pass
```

### Модуль cve_search.py (на базе урока 47)

```python
# cve_search.py - Поиск CVE (из урока 47)
# Используйте код из урока 47: class CVEParser
from lesson_47_cve import CVEParser as CVESearcher

# Альтернативно, создаем псевдоним:
# CVESearcher = CVEParser
```

### Примеры вывода

**Сканирование портов:**
```
[+] Начало сканирования: example.com
[+] IP адрес цели: 93.184.216.34

[+] Порт 80: ОТКРЫТ
[+] Порт 443: ОТКРЫТ
[-] Порт 22: закрыт

[+] Найдено открытых портов: 2
```

**HTTP анализ:**
```
[+] Исследование цели: https://example.com

    Код ответа: 200
    Размер контента: 1256 байт
    Тип контента: text/html
    Сервер: ECS (dcb/7F83)
    Куки: ['_ga', '_gid']
```

**Перебор поддоменов:**
```
[+] Найден: www.example.com -> 93.184.216.34
[+] Найден: mail.example.com -> 93.184.216.35
[+] Найден: admin.example.com -> 93.184.216.36

Сканирование завершено за 2.34 секунд
Найдено поддоменов: 3
```

### README.md

Создайте файл README.md в корне проекта:

```markdown
# ReconTool

Инструмент для автоматизированной разведки в пентесте. Объединяет различные техники разведки в одном инструменте.

## Возможности

- 🔍 Сканирование портов (TCP connect scan)
- 🌐 HTTP анализ (заголовки, методы, редиректы)
- 🎯 Перебор поддоменов (асинхронный)
- 📁 Перебор директорий (как dirsearch)
- 🛡️ Поиск CVE по продуктам
- 📊 Красивый вывод (через rich)
- 💾 Сохранение результатов в JSON
- 📄 Генерация текстовых отчетов

## Установка

```bash
git clone https://github.com/yourusername/recon_tool.git
cd recon_tool
pip install -r requirements.txt
```

## Использование

```bash
# Запуск всех модулей
python -m recon_tool.main example.com --all

# Только сканирование портов и HTTP
python -m recon_tool.main example.com --ports --http

# Перебор поддоменов со своим словарём
python -m recon_tool.main example.com --subdomains -w wordlists/subdomains.txt -t 100

# Перебор директорий с расширениями
python -m recon_tool.main example.com --dirs -e php,html,bak,zip

# Сохранение результатов
python -m recon_tool.main example.com --all -o results.json --report report.txt
```

## Требования

- Python 3.7+
- aiohttp
- requests
- rich

## Лицензия

MIT License (для образовательных целей)

## Предупреждение

Используйте только на системах, на которые у вас есть разрешение. Автор не несет ответственности за неправомерное использование.
```

### requirements.txt

```
aiohttp>=3.8.0
requests>=2.28.0
rich>=12.0.0
```

## Публикация на GitHub

1. Создайте репозиторий на GitHub (название: `recon_tool` или `python-pentest-tool`)
2. Инициализируйте git в папке проекта:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: ReconTool v1.0"
   ```
3. Добавьте remote и отправьте:
   ```bash
   git remote add origin https://github.com/yourusername/recon_tool.git
   git push -u origin master
   ```


## Частые ошибки

1. **Ошибка 1**: Типичная ошибка новичков в этом уроке.
2. **Ошибка 2**: Еще одна распространенная проблема.
3. **Ошибка 3**: Важный момент, который часто упускают.



## Вопросы на понимание

1. Вопрос 1 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 1</details>
2. Вопрос 2 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 2</details>
3. Вопрос 3 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 3</details>



## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. **Доработка инструмента:** Добавьте модуль для проверки SQL-инъекций (из урока 43) в ReconTool.

2. **Nmap интеграция:** Добавьте модуль, который запускает Nmap и парсит результаты (из урока 44).

3. **Database:** Добавьте сохранение результатов в SQLite базу данных для последующего поиска и анализа.

4. **Web UI:** Создайте простой веб-интерфейс для инструмента (используя Flask или FastAPI). Пользователь вводит цель через веб-форму, запускается сканирование, результаты отображаются на странице.

5. **Docker:** Создайте Dockerfile для контейнеризации инструмента. Это позволит запускать его на любой системе без установки зависимостей.

6. **CI/CD:** Настройте GitHub Actions для автоматического тестирования кода при каждом push.

7. **Документация:** Напишите подробную документацию для каждого модуля в формате Sphinx или MkDocs. Опубликуйте на ReadTheDocs.

8. **Расширение функционала:** Добавьте модули:
   - Проверка SSL/TLS (sslscan, testssl.sh аналог)
   - Поиск файлов резервных копий
   - Проверка на наличие админ-панелей
   - Интеграция с Shodan API
   - WHOIS и DNS информация

9. **Оптимизация:** Профилируйте код, найдите узкие места и оптимизируйте их. Добавьте прогресс-бары (через rich или tqdm).

10. **Portfolio:** Добавьте инструмент в своё портфолио пентестера. Напишите статью на Medium или в блог о том, как вы создали этот инструмент и чему научились.
