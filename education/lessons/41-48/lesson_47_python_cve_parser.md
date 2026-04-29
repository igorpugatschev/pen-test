# Занятие 47: Парсер уязвимостей — сбор данных с CVE/NVD через API

## Теория

**CVE (Common Vulnerabilities and Exposures)** — это словарь общих уязвимостей и воздействий. Каждая уязвимость получает уникальный идентификатор (например, CVE-2021-44228 — Log4Shell).

**NVD (National Vulnerability Database)** — это база данных уязвимостей, поддерживаемая NIST (США). Она содержит подробную информацию о CVE: описание, CVSS score, ссылки, патчи и т.д.

**Зачем нужно:**
- Поиск уязвимостей в конкретных продуктах/версиях
- Автоматизация сбора информации об уязвимостях при аудите
- Создание собственной базы данных уязвимостей
- Интеграция с другими инструментами (например, сканерами портов)

**API NVD:**
- Официальный API: https://nvd.nist.gov/developers/vulnerabilities
- Требует API ключ (бесплатно, до 50 запросов в 30 секунд)
- Возвращает данные в формате JSON

**Альтернативные источники:**
- CIRCL CVE API: https://cve.circl.lu/
- MITRE CVE API
- GitHub Security Advisories API
- Exploit-DB API

**Библиотеки:**
- `requests` — для HTTP-запросов
- `json` — для парсинга JSON
- `sqlite3` (стандартная) — для локального кэширования

**Установка:**
```bash
pip install requests
```

## Практическое занятие

Напишем скрипт для поиска CVE по названию продукта и сохранения их в локальную базу данных.

```python
import requests
import json
import sqlite3
import time
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class CVEParser:
    """Парсер уязвимостей CVE через NVD API"""
    
    NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    CIRCL_API_URL = "https://cve.circl.lu/api"
    
    def __init__(self, api_key: str = None, use_cache: bool = True, cache_db: str = "cve_cache.db"):
        """
        Инициализация
        :param api_key: API ключ NVD (получить: https://nvd.nist.gov/developers/request-an-api-key)
        :param use_cache: использовать ли локальный кэш (SQLite)
        :param cache_db: файл базы данных для кэша
        """
        self.api_key = api_key
        self.use_cache = use_cache
        self.cache_db = cache_db
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CVE-Parser/1.0 (Educational Purpose)'
        })
        
        if self.api_key:
            self.session.headers.update({
                'apiKey': self.api_key
            })
        
        # Инициализация кэша
        if self.use_cache:
            self._init_cache()
    
    def _init_cache(self):
        """Инициализация базы данных SQLite для кэширования"""
        self.conn = sqlite3.connect(self.cache_db)
        self.cursor = self.conn.cursor()
        
        # Создаем таблицы, если они не существуют
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cve (
                id TEXT PRIMARY KEY,
                description TEXT,
                published TEXT,
                last_modified TEXT,
                cvss_score REAL,
                cvss_vector TEXT,
                severity TEXT,
                cpe TEXT,
                references TEXT,
                cached_time TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS search_history (
                query TEXT,
                timestamp TEXT,
                results_count INTEGER
            )
        ''')
        
        self.conn.commit()
        print(f"[+] Кэш инициализирован: {self.cache_db}")
    
    def _get_from_cache(self, cve_id: str) -> Optional[Dict]:
        """Получение CVE из кэша"""
        if not self.use_cache:
            return None
        
        self.cursor.execute('SELECT * FROM cve WHERE id = ?', (cve_id,))
        row = self.cursor.fetchone()
        
        if row:
            return {
                'id': row[0],
                'description': row[1],
                'published': row[2],
                'last_modified': row[3],
                'cvss_score': row[4],
                'cvss_vector': row[5],
                'severity': row[6],
                'cpe': row[7],
                'references': json.loads(row[8]) if row[8] else [],
                'cached': True
            }
        return None
    
    def _save_to_cache(self, cve_data: Dict):
        """Сохранение CVE в кэш"""
        if not self.use_cache:
            return
        
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO cve 
                (id, description, published, last_modified, cvss_score, cvss_vector, severity, cpe, references, cached_time)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                cve_data['id'],
                cve_data['description'],
                cve_data['published'],
                cve_data['last_modified'],
                cve_data['cvss_score'],
                cve_data['cvss_vector'],
                cve_data['severity'],
                cve_data['cpe'],
                json.dumps(cve_data['references']),
                datetime.now().isoformat()
            ))
            self.conn.commit()
        except Exception as e:
            print(f"[-] Ошибка сохранения в кэш: {e}")
    
    def search_by_cpe(self, cpe: str, results_per_page: int = 20) -> List[Dict]:
        """
        Поиск CVE по CPE (Common Platform Enumeration)
        Пример CPE: cpe:2.3:a:apache:log4j:2.14.0:*:*:*:*:*:*:*
        :param cpe: CPE строка
        :param results_per_page: количество результатов на страницу
        """
        print(f"\n[+] Поиск CVE по CPE: {cpe}")
        
        params = {
            'cpeName': cpe,
            'resultsPerPage': results_per_page
        }
        
        try:
            response = self.session.get(self.NVD_API_URL, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                vulnerabilities = data.get('vulnerabilities', [])
                print(f"    Найдено уязвимостей: {len(vulnerabilities)}")
                return self._parse_nvd_response(vulnerabilities)
            elif response.status_code == 403:
                print("[-] Ошибка 403: Превышен лимит запросов или неверный API ключ")
                print("[-] Рекомендуется использовать API ключ (бесплатно)")
            else:
                print(f"[-] Ошибка API: {response.status_code}")
                print(f"    Ответ: {response.text[:200]}")
        
        except requests.exceptions.RequestException as e:
            print(f"[-] Ошибка запроса: {e}")
        
        return []
    
    def search_by_keyword(self, keyword: str, results_per_page: int = 20) -> List[Dict]:
        """
        Поиск CVE по ключевому слову
        :param keyword: ключевое слово (например, "log4j", "wordpress")
        :param results_per_page: количество результатов
        """
        print(f"\n[+] Поиск CVE по ключевому слову: {keyword}")
        
        params = {
            'keywordSearch': keyword,
            'resultsPerPage': results_per_page
        }
        
        try:
            response = self.session.get(self.NVD_API_URL, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                vulnerabilities = data.get('vulnerabilities', [])
                print(f"    Найдено уязвимостей: {len(vulnerabilities)}")
                
                # Сохраняем историю поиска
                if self.use_cache:
                    self.cursor.execute('''
                        INSERT INTO search_history (query, timestamp, results_count)
                        VALUES (?, ?, ?)
                    ''', (keyword, datetime.now().isoformat(), len(vulnerabilities)))
                    self.conn.commit()
                
                return self._parse_nvd_response(vulnerabilities)
            else:
                print(f"[-] Ошибка API: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"[-] Ошибка запроса: {e}")
        
        return []
    
    def search_by_cve_id(self, cve_id: str) -> Optional[Dict]:
        """
        Поиск конкретного CVE по ID
        :param cve_id: ID уязвимости (например, CVE-2021-44228)
        """
        # Проверяем кэш
        cached = self._get_from_cache(cve_id)
        if cached:
            print(f"[+] Найдено в кэше: {cve_id}")
            return cached
        
        print(f"\n[+] Поиск CVE: {cve_id}")
        
        params = {
            'cveId': cve_id
        }
        
        try:
            response = self.session.get(self.NVD_API_URL, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                vulnerabilities = data.get('vulnerabilities', [])
                
                if vulnerabilities:
                    parsed = self._parse_nvd_response(vulnerabilities)
                    if parsed:
                        # Сохраняем в кэш
                        self._save_to_cache(parsed[0])
                        return parsed[0]
                else:
                    print(f"[-] CVE {cve_id} не найден")
            else:
                print(f"[-] Ошибка API: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"[-] Ошибка запроса: {e}")
        
        return None
    
    def _parse_nvd_response(self, vulnerabilities: List[Dict]) -> List[Dict]:
        """
        Парсинг ответа NVD API
        :param vulnerabilities: список уязвимостей из ответа
        :return: список словарей с информацией о CVE
        """
        results = []
        
        for vuln in vulnerabilities:
            cve = vuln.get('cve', {})
            
            cve_id = cve.get('id', 'Unknown')
            descriptions = cve.get('descriptions', [])
            description = next((d['value'] for d in descriptions if d['lang'] == 'en'), 'No description')
            
            published = cve.get('published', '')
            last_modified = cve.get('lastModified', '')
            
            # CVSS метрики (пробуем v3.1, затем v3.0, затем v2)
            cvss_score = None
            cvss_vector = None
            severity = None
            
            metrics = cve.get('metrics', {})
            
            if 'cvssMetricV31' in metrics:
                cvss_data = metrics['cvssMetricV31'][0]['cvssData']
                cvss_score = cvss_data.get('baseScore')
                cvss_vector = cvss_data.get('vectorString')
                severity = metrics['cvssMetricV31'][0].get('baseSeverity', 'Unknown')
            elif 'cvssMetricV30' in metrics:
                cvss_data = metrics['cvssMetricV30'][0]['cvssData']
                cvss_score = cvss_data.get('baseScore')
                cvss_vector = cvss_data.get('vectorString')
                severity = metrics['cvssMetricV30'][0].get('baseSeverity', 'Unknown')
            elif 'cvssMetricV2' in metrics:
                cvss_data = metrics['cvssMetricV2'][0]['cvssData']
                cvss_score = cvss_data.get('baseScore')
                cvss_vector = cvss_data.get('vectorString')
                severity = metrics['cvssMetricV2'][0].get('baseSeverity', 'Unknown')
            
            # CPE конфигурации (уязвимые продукты)
            configurations = cve.get('configurations', {})
            cpe_list = []
            for node in configurations.get('nodes', []):
                for cpe_match in node.get('cpeMatch', []):
                    if cpe_match.get('vulnerable'):
                        cpe_list.append(cpe_match.get('criteria', ''))
            
            # Ссылки
            references = []
            for ref in cve.get('references', []):
                references.append({
                    'url': ref.get('url', ''),
                    'source': ref.get('source', ''),
                    'tags': ref.get('tags', [])
                })
            
            result = {
                'id': cve_id,
                'description': description,
                'published': published,
                'last_modified': last_modified,
                'cvss_score': cvss_score,
                'cvss_vector': cvss_vector,
                'severity': severity,
                'cpe': '; '.join(cpe_list[:5]),  # Первые 5 CPE
                'references': references
            }
            
            results.append(result)
        
        return results
    
    def print_cve(self, cve: Dict):
        """Красивый вывод информации о CVE"""
        print(f"\n{'='*70}")
        print(f"CVE: {cve['id']}")
        print(f"{'='*70}")
        print(f"Опубликовано: {cve['published']}")
        print(f"Изменено: {cve['last_modified']}")
        
        if cve['cvss_score']:
            print(f"CVSS Score: {cve['cvss_score']} ({cve['severity']})")
        if cve['cvss_vector']:
            print(f"CVSS Vector: {cve['cvss_vector']}")
        
        print(f"\nОписание:")
        print(f"  {cve['description'][:500]}...")
        
        if cve['cpe']:
            print(f"\nУязвимые продукты (CPE):")
            for cpe in cve['cpe'].split('; '):
                print(f"  - {cpe}")
        
        if cve['references']:
            print(f"\nСсылки ({len(cve['references'])}):")
            for ref in cve['references'][:5]:  # Первые 5 ссылок
                print(f"  - {ref['url']}")
                if ref['tags']:
                    print(f"    Tags: {', '.join(ref['tags'])}")
        
        print(f"{'='*70}\n")
    
    def export_to_json(self, cve_list: List[Dict], output_file: str = None):
        """Экспорт списка CVE в JSON"""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"cve_export_{timestamp}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(cve_list, f, indent=2, ensure_ascii=False)
        
        print(f"[+] Экспортировано {len(cve_list)} CVE в файл: {output_file}")
    
    def close(self):
        """Закрытие соединения с БД"""
        if self.use_cache and hasattr(self, 'conn'):
            self.conn.close()

def main():
    """Точка входа"""
    parser = argparse.ArgumentParser(description='Парсер уязвимостей CVE/NVD')
    parser.add_argument('--api-key', help='API ключ NVD (получить: https://nvd.nist.gov/developers/request-an-api-key)')
    parser.add_argument('--no-cache', action='store_true', help='Отключить кэширование')
    
    subparsers = parser.add_subparsers(dest='command', help='Команды')
    
    # Поиск по ключевому слову
    search_parser = subparsers.add_parser('search', help='Поиск по ключевому слову')
    search_parser.add_argument('keyword', help='Ключевое слово (например, log4j)')
    search_parser.add_argument('-n', '--number', type=int, default=20, help='Количество результатов')
    search_parser.add_argument('-o', '--output', help='Файл для сохранения (JSON)')
    
    # Поиск по CVE ID
    cve_parser = subparsers.add_parser('cve', help='Поиск конкретного CVE')
    cve_parser.add_argument('cve_id', help='ID CVE (например, CVE-2021-44228)')
    
    # Поиск по CPE
    cpe_parser = subparsers.add_parser('cpe', help='Поиск по CPE')
    cpe_parser.add_argument('cpe', help='CPE строка (например, cpe:2.3:a:apache:log4j:2.14.0)')
    cpe_parser.add_argument('-n', '--number', type=int, default=20, help='Количество результатов')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    parser_obj = CVEParser(api_key=args.api_key, use_cache=not args.no_cache)
    
    try:
        if args.command == 'search':
            results = parser_obj.search_by_keyword(args.keyword, args.number)
            if results:
                print(f"\n[+] Найдено {len(results)} уязвимостей:")
                for cve in results[:10]:  # Показываем первые 10
                    parser_obj.print_cve(cve)
                
                if args.output:
                    parser_obj.export_to_json(results, args.output)
        
        elif args.command == 'cve':
            cve = parser_obj.search_by_cve_id(args.cve_id)
            if cve:
                parser_obj.print_cve(cve)
        
        elif args.command == 'cpe':
            results = parser_obj.search_by_cpe(args.cpe, args.number)
            if results:
                print(f"\n[+] Найдено {len(results)} уязвимостей:")
                for cve in results[:10]:
                    parser_obj.print_cve(cve)
    
    finally:
        parser_obj.close()

if __name__ == "__main__":
    main()
```

**Объяснение кода:**
1. Использует NVD API 2.0 для поиска CVE
2. Кэширует результаты в SQLite для уменьшения запросов к API
3. Поддерживает поиск по ключевому слову, CVE ID, CPE
4. Парсит CVSS метрики (v3.1, v3.0, v2)
5. Сохраняет результаты в JSON

**Запуск:**
```bash
# Поиск по ключевому слову
python lesson_47_cve_parser.py search log4j

# Поиск конкретного CVE
python lesson_47_cve_parser.py cve CVE-2021-44228

# Поиск по CPE (продукт)
python lesson_47_cve_parser.py cpe "cpe:2.3:a:apache:log4j:2.14.0"

# С API ключом (рекомендуется)
python lesson_47_cve_parser.py --api-key YOUR_KEY search wordpress -n 50 -o wordpress_cve.json
```

## Примеры вывода

Пример успешного поиска CVE-2021-44228:

```
======================================================================
CVE: CVE-2021-44228
======================================================================
Опубликовано: 2021-12-10T14:15:00.000
Изменено: 2023-06-26T18:15:09.723
CVSS Score: 10.0 (CRITICAL)
CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H

Описание:
  Apache Log4j2 <=2.14.1 JNDI features used in configuration, log messag...

Уязвимые продукты (CPE):
  - cpe:2.3:a:apache:log4j:2.14.0:*:*:*:*:*:*:*

Ссылки (3):
  - https://nvd.nist.gov/vuln/detail/CVE-2021-44228
    Tags: exploit, vendor-advisory
======================================================================
```

## Частые ошибки

1. **`requests.exceptions.HTTPError: 403 Client Error`** — Превышен лимит запросов. Получите бесплатный API ключ или увеличьте задержку между запросами.
2. **`json.JSONDecodeError`** — Ответ от API не является JSON. Возможно, NVD API изменил формат ответа или сервер вернул ошибку.
3. **Пустые результаты поиска** — Проверьте правильность написания ключевого слова или CPE строки. CPE чувствителен к регистру и формату.
4. **`sqlite3.OperationalError: database is locked`** — База данных SQLite заблокирована. Закройте другие процессы, использующие файл, или увеличьте таймаут.

## Вопросы на понимание

1. **Зачем нужно кэширование результатов в SQLite при работе с NVD API?**
   <details>
   <summary>Ответ</summary>
   NVD API имеет лимиты (50 запросов в 30 секунд). Кэширование позволяет избежать повторных запросов и экономит квоту. Также это ускоряет работу при частых запросах одних и тех же CVE.
   </details>

2. **В чем разница между CVSS v2 и v3.x?**
   <details>
   <summary>Ответ</summary>
   CVSS v2 использует шкалу 0-10 с меньшим количеством метрик. CVSS v3.x (v3.0, v3.1) более детальный, учитывает современные угрозы (например, Scope change) и имеет измененную формулу расчета. В коде мы проверяем наличие v3.1, затем v3.0, затем v2.
   </details>

3. **Почему поиск по CPE более точен, чем по ключевому слову?**
   <details>
   <summary>Ответ</summary>
   CPE (Common Platform Enumeration) точно идентифицирует продукт, его вендора и версию. Ключевые слова могут давать много шума (например, слово "log4j" может встречаться в описаниях других уязвимостей).
   </details>


## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. **Получение API ключа:** Зарегистрируйтесь и получите бесплатный API ключ NVD. Сравните скорость работы с ключом и без.

2. **Поиск по диапазону дат:** Добавьте возможность поиска CVE, опубликованных в определенном диапазоне дат (параметры `pubStartDate` и `pubEndDate` в API).

3. **Фильтрация по severity:** Добавьте фильтрацию результатов по уровню серьезности (CRITICAL, HIGH, MEDIUM, LOW). Выводите только критические и высокие уязвимости.

4. **Интеграция с Nmap:** Напишите скрипт, который берет результаты Nmap (из прошлого занятия), извлекает названия и версии сервисов, формирует CPE и ищет для них CVE.

5. **Exploit-DB интеграция:** Добавьте поиск эксплойтов для найденных CVE через API Exploit-DB (https://www.exploit-db.com/). Ссылки на эксплойты полезны для PoC.

6. **Уведомления:** Добавьте функцию мониторинга: сохраняйте дату последней проверки и при следующем запуске ищите только новые CVE (опубликованные после последней проверки).

7. **Генерация отчета:** Создайте функцию генерации HTML-отчета со списком найденных уязвимостей, отсортированных по CVSS score. Отчет должен включать таблицу с колонками: CVE ID, Описание, Score, Ссылки, Продукты.
