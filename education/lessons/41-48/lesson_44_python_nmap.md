# Занятие 44: Автоматизация Nmap — обработка XML-вывода через Python

## Теория

**Nmap** — самый популярный инструмент для сканирования сети и аудита безопасности. Он поддерживает вывод результатов в различных форматах, включая XML, который удобно парсить программно.

**Зачем автоматизировать Nmap через Python:**
- Обработка больших объемов данных сканирования
- Интеграция результатов в отчеты
- Фильтрация и поиск специфических сервисов/уязвимостей
- Создание собственных инструментов на базе Nmap

**Библиотеки:**
- `xml.etree.ElementTree` (стандартная) — для парсинга XML
- `subprocess` (стандартная) — для запуска Nmap
- `re` — для регулярных выражений
- `nmap` (опционально) — Python-обертка для Nmap (требует установки)

**Установка Nmap:**
```bash
# macOS
brew install nmap

# Linux (Ubuntu/Debian)
sudo apt-get install nmap

# Windows: скачать с https://nmap.org/download.html
```

**Установка библиотеки python-nmap (опционально):**
```bash
pip install python-nmap
```

## Практическое занятие

Напишем скрипт, который запускает Nmap, сохраняет результат в XML и парсит его для извлечения полезной информации.

```python
import subprocess
import xml.etree.ElementTree as ET
import os
import json
from datetime import datetime

class NmapParser:
    """Класс для автоматизации Nmap и парсинга результатов"""
    
    def __init__(self, output_dir="nmap_results"):
        """
        Инициализация
        :param output_dir: директория для сохранения результатов
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.scan_results = {}
    
    def run_nmap_scan(self, target, options="-sV -sC -p- --open", output_file=None):
        """
        Запуск Nmap сканирования
        :param target: цель (IP, диапазон, подсеть)
        :param options: опции Nmap
        :param output_file: имя файла для сохранения (если None, генерируется автоматически)
        :return: путь к XML-файлу с результатами
        """
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"scan_{target.replace('/', '_')}_{timestamp}.xml"
        
        output_path = os.path.join(self.output_dir, output_file)
        
        # Формируем команду Nmap с выводом в XML
        cmd = [
            'nmap',
            target,
            options.split(),
            '-oX', output_path  # XML output
        ]
        # Разворачиваем список опций
        cmd = ['nmap'] + options.split() + ['-oX', output_path, target]
        
        print(f"[+] Запуск Nmap сканирования: {target}")
        print(f"    Команда: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=3600  # Таймаут 1 час
            )
            
            if result.returncode == 0:
                print(f"[+] Сканирование завершено успешно")
                print(f"    Результаты сохранены: {output_path}")
                return output_path
            else:
                print(f"[-] Ошибка Nmap: {result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            print("[-] Превышен таймаут сканирования (1 час)")
            return None
        except FileNotFoundError:
            print("[-] Nmap не установлен. Установите: brew install nmap (macOS) или apt install nmap (Linux)")
            return None
        except Exception as e:
            print(f"[-] Ошибка при запуске Nmap: {e}")
            return None
    
    def parse_nmap_xml(self, xml_file):
        """
        Парсинг XML-файла Nmap
        :param xml_file: путь к XML-файлу
        :return: словарь с результатами
        """
        print(f"\n[+] Парсинг результатов: {xml_file}")
        
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
        except Exception as e:
            print(f"[-] Ошибка парсинга XML: {e}")
            return None
        
        results = {
            'scan_info': {},
            'hosts': [],
            'raw_xml': xml_file
        }
        
        # Информация о сканировании
        scaninfo = root.find('scaninfo')
        if scaninfo is not None:
            results['scan_info'] = {
                'type': scaninfo.get('type'),
                'protocol': scaninfo.get('protocol'),
                'numservices': scaninfo.get('numservices'),
                'services': scaninfo.get('services')
            }
        
        # Парсим хосты
        for host in root.findall('host'):
            host_data = {
                'addresses': [],
                'hostnames': [],
                'ports': [],
                'status': host.find('status').get('state') if host.find('status') is not None else 'unknown'
            }
            
            # IP и MAC адреса
            for addr in host.findall('address'):
                addr_info = {
                    'addr': addr.get('addr'),
                    'addrtype': addr.get('addrtype'),
                    'vendor': addr.get('vendor', 'unknown')
                }
                host_data['addresses'].append(addr_info)
            
            # Имена хостов
            hostnames = host.find('hostnames')
            if hostnames is not None:
                for hn in hostnames.findall('hostname'):
                    host_data['hostnames'].append({
                        'name': hn.get('name'),
                        'type': hn.get('type')
                    })
            
            # Порты
            ports = host.find('ports')
            if ports is not None:
                for port in ports.findall('port'):
                    port_data = {
                        'portid': port.get('portid'),
                        'protocol': port.get('protocol'),
                        'state': 'unknown',
                        'service': {},
                        'scripts': []
                    }
                    
                    # Состояние порта
                    state = port.find('state')
                    if state is not None:
                        port_data['state'] = state.get('state')
                    
                    # Информация о сервисе
                    service = port.find('service')
                    if service is not None:
                        port_data['service'] = {
                            'name': service.get('name'),
                            'product': service.get('product', ''),
                            'version': service.get('version', ''),
                            'extrainfo': service.get('extrainfo', ''),
                            'ostype': service.get('ostype', ''),
                            'method': service.get('method')
                        }
                    
                    # Результаты скриптов Nmap (NSE)
                    for script in port.findall('script'):
                        script_data = {
                            'id': script.get('id'),
                            'output': script.get('output')
                        }
                        port_data['scripts'].append(script_data)
                    
                    host_data['ports'].append(port_data)
            
            results['hosts'].append(host_data)
        
        self.scan_results = results
        print(f"    Найдено хостов: {len(results['hosts'])}")
        total_ports = sum(len(h['ports']) for h in results['hosts'])
        print(f"    Всего портов: {total_ports}")
        
        return results
    
    def filter_open_ports(self):
        """Фильтрация только открытых портов"""
        open_ports = []
        for host in self.scan_results.get('hosts', []):
            if host['status'] != 'up':
                continue
            for port in host['ports']:
                if port['state'] == 'open':
                    open_ports.append({
                        'host': host['addresses'][0]['addr'] if host['addresses'] else 'unknown',
                        'port': port['portid'],
                        'protocol': port['protocol'],
                        'service': port['service'].get('name', 'unknown'),
                        'product': port['service'].get('product', ''),
                        'version': port['service'].get('version', '')
                    })
        return open_ports
    
    def find_service(self, service_name):
        """
        Поиск сервисов по имени
        :param service_name: имя сервиса (например, 'http', 'ssh')
        """
        found = []
        for host in self.scan_results.get('hosts', []):
            for port in host['ports']:
                if port['state'] == 'open':
                    svc_name = port['service'].get('name', '').lower()
                    if service_name.lower() in svc_name:
                        found.append({
                            'host': host['addresses'][0]['addr'] if host['addresses'] else 'unknown',
                            'port': port['portid'],
                            'service': port['service']
                        })
        return found
    
    def print_summary(self):
        """Вывод краткой сводки по результатам"""
        if not self.scan_results:
            print("[-] Нет данных для вывода")
            return
        
        print("\n" + "="*60)
        print("СВОДКА ПО СКАНИРОВАНИЮ NMAP")
        print("="*60)
        
        print(f"\nТип сканирования: {self.scan_results['scan_info'].get('type', 'N/A')}")
        print(f"Протокол: {self.scan_results['scan_info'].get('protocol', 'N/A')}")
        
        for i, host in enumerate(self.scan_results['hosts'], 1):
            print(f"\n--- Хост #{i} ---")
            print(f"Статус: {host['status']}")
            
            # Адреса
            for addr in host['addresses']:
                print(f"IP: {addr['addr']} ({addr['addrtype']})")
                if addr['vendor'] != 'unknown':
                    print(f"  Вендор: {addr['vendor']}")
            
            # Имена
            if host['hostnames']:
                print(f"Имена: {', '.join([h['name'] for h in host['hostnames']])}")
            
            # Открытые порты
            open_ports = [p for p in host['ports'] if p['state'] == 'open']
            if open_ports:
                print(f"\nОткрытые порты ({len(open_ports)}):")
                for port in open_ports:
                    svc = port['service']
                    svc_str = svc.get('name', 'unknown')
                    if svc.get('product'):
                        svc_str += f" ({svc['product']}"
                        if svc.get('version'):
                            svc_str += f" {svc['version']}"
                        svc_str += ")"
                    print(f"  {port['portid']}/{port['protocol']}: {svc_str}")
                    
                    # Вывод результатов скриптов (если есть)
                    if port['scripts']:
                        for script in port['scripts']:
                            print(f"    [NSE] {script['id']}: {script['output'][:100]}...")
        
        print("\n" + "="*60)
    
    def save_to_json(self, output_file="nmap_results.json"):
        """Сохранение результатов в JSON"""
        output_path = os.path.join(self.output_dir, output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.scan_results, f, indent=2, ensure_ascii=False)
        print(f"\n[+] Результаты сохранены в JSON: {output_path}")
        return output_path

if __name__ == "__main__":
    parser = NmapParser(output_dir="nmap_results")
    
    # Пример 1: Сканирование локального хоста (быстрое)
    # В реальном пентесте замените на реальную цель
    target = "127.0.0.1"
    options = "-sV -p 22,80,443,3306,8080 --open"  # Быстрое сканирование
    
    print("[*] ВНИМАНИЕ: Запуск Nmap требует прав. Для сканирования некоторых портов может потребоваться sudo.")
    print("[*] Используйте только на системах, на которые у вас есть разрешение!\n")
    
    # Запускаем сканирование
    xml_file = parser.run_nmap_scan(target, options)
    
    if xml_file and os.path.exists(xml_file):
        # Парсим результаты
        results = parser.parse_nmap_xml(xml_file)
        
        if results:
            # Выводим сводку
            parser.print_summary()
            
            # Фильтруем открытые порты
            open_ports = parser.filter_open_ports()
            print(f"\n[+] Найдено открытых портов: {len(open_ports)}")
            for op in open_ports:
                print(f"    {op['host']}:{op['port']} - {op['service']} ({op['product']} {op['version']})")
            
            # Поиск конкретных сервисов
            http_services = parser.find_service("http")
            if http_services:
                print(f"\n[+] Найдены HTTP-сервисы: {len(http_services)}")
                for svc in http_services:
                    print(f"    {svc['host']}:{svc['port']}")
            
            # Сохраняем в JSON
            parser.save_to_json()
    else:
        print("\n[-] Сканирование не удалось или Nmap не установлен.")
        print("[-] Для демонстрации парсинга можно использовать существующий XML-файл.")
        print("[-] Пример: python script.py (и вручную вызвать parse_nmap_xml('file.xml'))")
```

**Объяснение кода:**
1. `run_nmap_scan()` — запускает Nmap через subprocess с выводом в XML
2. `parse_nmap_xml()` — парсит XML, извлекает информацию о хостах, портах, сервисах
3. `filter_open_ports()` — фильтрует только открытые порты
4. `find_service()` — ищет конкретные сервисы (например, все HTTP)
5. `print_summary()` — красиво выводит результаты
6. `save_to_json()` — сохраняет результаты в JSON для дальнейшей обработки

**Запуск:**
```bash
python lesson_44_nmap.py
```

## Задачи для самостоятельного выполнения

1. **Парсинг существующего XML:** Напишите скрипт, который парсит уже существующий XML-файл Nmap без запуска сканирования. Протестируйте на реальном выводе Nmap.

2. **Поиск уязвимостей:** Расширьте парсер для извлечения результатов NSE-скриптов, которые находят уязвимости (например, `vuln-*`). Выводите список найденных уязвимостей.

3. **Сравнение сканов:** Напишите функцию, которая сравнивает два XML-файла сканирования (например, до и после изменений в инфраструктуре) и выводит различия (новые порты, изменившиеся сервисы).

4. **Экспорт в CSV:** Добавьте метод для экспорта результатов в CSV-файл (удобно для Excel). Формат: IP, Port, Protocol, Service, Product, Version, State.

5. **Асинхронное сканирование:** Используйте `asyncio` и `asyncio.subprocess` для запуска нескольких Nmap сканирований параллельно (например, сканирование нескольких подсетей).

6. **Интеграция с Vulners:** Добавьте использование Nmap скрипта `vulners` (требует установки скрипта) для поиска CVE по версиям сервисов. Парсите результаты и выводите список CVE.

7. **Генерация отчета:** Создайте HTML-отчет на основе результатов сканирования. Используйте простые строки HTML или шаблонизатор (например, Jinja2). Отчет должен включать: таблицу хостов, портов, сервисов, найденных уязвимостей.
