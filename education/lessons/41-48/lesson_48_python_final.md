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
│   ├── scanner.py       # Сканирование портов (из урока 41)
│   ├── http_utils.py    # HTTP запросы (из урока 42)
│   ├── dir_brute.py     # Перебор директорий (из урока 46)
│   ├── subdomain.py     # Перебор поддоменов (из урока 45)
│   ├── nmap_parser.py   # Парсинг Nmap (из урока 44)
│   ├── cve_search.py    # Поиск CVE (из урока 47)
│   └── utils.py         # Вспомогательные функции
└── tests/               # Тесты (опционально)
```

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

# Импорт модулей инструмента
from scanner import PortScanner
from http_utils import HTTPRequester
from dir_brute import DirectoryBruteforcer
from subdomain import SubdomainBruteforcer
from nmap_parser import NmapParser
from cve_search import CVESearcher

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
