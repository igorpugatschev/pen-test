# Занятие 42: Python requests — HTTP-запросы, парсинг ответов

## Теория

Библиотека `requests` — это самая популярная библиотека Python для работы с HTTP-запросами. Она предоставляет простой и интуитивно понятный интерфейс для отправки HTTP-запросов и обработки ответов.

**Зачем нужно:**
- Взаимодействие с веб-приложениями при тестировании на проникновение
- Отправка специально сформированных запросов для проверки уязвимостей
- Парсинг веб-страниц и API-ответов
- Автоматизация веб-атак (брутфорс, сканирование директорий и т.д.)

**Основные возможности:**
- GET, POST, PUT, DELETE, HEAD, OPTIONS запросы
- Работа с заголовками, куки, параметрами URL
- Обработка редиректов и сессий
- Работа с SSL-сертификатами
- Парсинг JSON-ответов

**Установка:**
```bash
pip3 install requests
```

## Практическое занятие

Напишем скрипт, который отправляет различные HTTP-запросы и анализирует ответы сервера.

```python
import requests
import json
import urllib3
from urllib.parse import urljoin

# Отключаем предупреждения о небезопасных SSL-сертификатах
urllib3.disable_warnings()

def http_request_explorer(target_url):
    """
    Исследование HTTP-ответов с помощью библиотеки requests
    :param target_url: целевой URL
    """
    print(f"[+] Исследование цели: {target_url}\n")
    
    # Создаем сессию для сохранения куки и заголовков
    session = requests.Session()
    
    # Настраиваем заголовки (имитируем браузер)
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    })
    
    try:
        # 1. GET-запрос
        print("[1] Выполняем GET-запрос...")
        response = session.get(target_url, timeout=10, verify=False)
        
        print(f"    Код ответа: {response.status_code}")
        print(f"    Размер контента: {len(response.content)} байт")
        print(f"    Тип контента: {response.headers.get('Content-Type', 'не указан')}")
        print(f"    Сервер: {response.headers.get('Server', 'не указан')}")
        
        # Анализ куки
        if response.cookies:
            print(f"    Куки: {list(response.cookies.keys())}")
        
        # 2. Получение заголовков (HEAD-запрос)
        print("\n[2] Выполняем HEAD-запрос для получения только заголовков...")
        head_response = session.head(target_url, timeout=10)
        print("    Заголовки ответа:")
        for key, value in head_response.headers.items():
            print(f"      {key}: {value}")
        
        # 3. POST-запрос с данными
        print("\n[3] Выполняем POST-запрос с данными...")
        post_data = {
            'username': 'admin',
            'password': 'password123',
            'submit': 'Login'
        }
        # Попробуем отправить на тестовый эндпоинт (если есть)
        login_url = urljoin(target_url, '/login')
        try:
            post_response = session.post(login_url, data=post_data, timeout=10, allow_redirects=False)
            print(f"    Код ответа: {post_response.status_code}")
            if post_response.status_code in [301, 302, 303, 307, 308]:
                print(f"    Редирект на: {post_response.headers.get('Location')}")
        except requests.exceptions.RequestException as e:
            print(f"    Ошибка POST-запроса: {e}")
        
        # 4. Парсинг JSON-ответа (если API)
        print("\n[4] Проверяем, является ли ответ JSON...")
        try:
            json_data = response.json()
            print(f"    Ответ содержит JSON: {json.dumps(json_data, indent=2)[:200]}...")
        except json.JSONDecodeError:
            print("    Ответ не является JSON, это HTML-страница")
            # Показываем первые 200 символов HTML
            print(f"    Первые 200 символов: {response.text[:200]}...")
        
        # 5. Проверка интересных заголовков безопасности
        print("\n[5] Проверка заголовков безопасности...")
        security_headers = [
            'Strict-Transport-Security',
            'Content-Security-Policy',
            'X-Frame-Options',
            'X-Content-Type-Options',
            'X-XSS-Protection'
        ]
        for header in security_headers:
            if header in response.headers:
                print(f"    [+] {header}: {response.headers[header]}")
            else:
                print(f"    [-] {header}: НЕ УСТАНОВЛЕН")
        
        # 6. Информация о редиректах
        if len(response.history) > 0:
            print(f"\n[6] История редиректов ({len(response.history)}):")
            for i, resp in enumerate(response.history):
                print(f"    {i+1}. {resp.url} -> {resp.status_code}")
        
    except requests.exceptions.Timeout:
        print("[-] Ошибка: Превышено время ожидания (timeout)")
    except requests.exceptions.ConnectionError:
        print("[-] Ошибка: Не удалось подключиться к серверу")
    except requests.exceptions.RequestException as e:
        print(f"[-] Ошибка запроса: {e}")
    except Exception as e:
        print(f"[-] Неожиданная ошибка: {e}")

if __name__ == "__main__":
    # Тестовый URL (можно заменить на реальную цель)
    target = "http://httpbin.org/get"
    http_request_explorer(target)
```

**Объяснение кода:**
1. Используем `Session()` для сохранения состояния между запросами (куки, заголовки)
2. Настраиваем User-Agent, чтобы запросы выглядели как от браузера
3. Выполняем разные типы запросов: GET, HEAD, POST
4. Анализируем коды ответов, заголовки, куки
5. Проверяем наличие JSON в ответе
6. Проверяем заголовки безопасности (важно для пентеста)
7. Обрабатываем редиректы и ошибки

**Запуск:**
```bash
python lesson_42_requests.py
```

## Примеры вывода

Пример успешного выполнения скрипта для `http://httpbin.org/get`:

```
[+] Исследование цели: http://httpbin.org/get

[1] Выполняем GET-запрос...
    Код ответа: 200
    Размер контента: 306 байт
    Тип контента: application/json
    Сервер: gunicorn/19.9.0
    Куки: ['_ga', '_gid']

[2] Выполняем HEAD-запрос для получения только заголовков...
    Заголовки ответа:
      Content-Type: application/json
      Content-Length: 306
      Server: gunicorn/19.9.0
      ...

[4] Проверяем, является ли ответ JSON...
    Ответ содержит JSON: {
  "args": {},
  "headers": {
    "Accept": "text/html,application/xhtml+...",
    "Host": "httpbin.org"
  },
  ...

[5] Проверка заголовков безопасности...
    [+] Strict-Transport-Security: max-age=15724800; includeSubDomains
    [-] Content-Security-Policy: НЕ УСТАНОВЛЕН
    [+] X-Frame-Options: DENY
```

## Частые ошибки

1. **`requests.exceptions.SSLError`** — Ошибка SSL-сертификата. Решение: добавить `verify=False` в запрос или исправить сертификат.
2. **`urllib3.disable_warnings()` не работает** — В новых версиях нужно явно импортировать `import urllib3` перед вызовом. Убедитесь, что используете правильный синтаксис:
   ```python
   import urllib3
   urllib3.disable_warnings()
   ```
3. **`requests.exceptions.Timeout`** — Превышено время ожидания. Увеличьте параметр `timeout` или проверьте доступность цели.
4. **`NameError: name 'urllib3' is not defined`** — Забыли импортировать библиотеку. Добавьте `import urllib3` перед использованием.

## Вопросы на понимание

1. **В чем разница между `requests.get()` и `session.get()`?**
   <details>
   <summary>Ответ</summary>
   `requests.get()` создает новый запрос каждый раз. `session.get()` использует сессию, которая сохраняет куки, заголовки и другие параметры между запросами, что важно для сохранения состояния (например, после авторизации).
   </details>

2. **Зачем нужен параметр `verify=False` и чем он опасен?**
   <details>
   <summary>Ответ</summary>
   `verify=False` отключает проверку SSL-сертификата. Это опасно, так как делает запрос уязвимым к MITM-атакам (подмене сертификата). Используйте только для тестирования на известных целях.
   </details>

3. **Чем отличается `allow_redirects=False` от отсутствия этого параметра?**
   <details>
   <summary>Ответ</summary>
   По умолчанию `requests` следует редиректам (коды 301, 302 и т.д.). При `allow_redirects=False` библиотека не будет переходить по редиректам, а вернет ответ с кодом 3xx и заголовком Location.
   </details>

## Задачи для самостоятельного выполнения

1. **Базовая аутентификация:** Добавьте поддержку HTTP Basic Auth в скрипт. Используйте параметр `auth=(username, password)` в запросах.

2. **Работа с прокси:** Добавьте возможность отправки запросов через прокси-сервер (SOCKS/HTTP). Используйте параметр `proxies` в запросах.

3. **Парсинг HTML:** Используйте библиотеку `beautifulsoup4` для парсинга HTML-страницы. Извлеките все ссылки (`<a href="...">`) и формы (`<form>`).

4. **Проверка уязвимостей:** Напишите функцию, которая проверяет наличие распространенных уязвимостей:
   - Отсутствие заголовков безопасности (реализовано выше)
   - Информация о сервере (версия в заголовке Server)
   - Наличие административных панелей (попробуйте /admin, /phpmyadmin и т.д.)

5. **Rate limiting:** Добавьте задержку между запросами (модуль `time`) и реализуйте простой механизм повторных попыток при получении кода 429 (Too Many Requests).

6. **Сохранение ответов:** Добавьте возможность сохранения HTML-ответов в файлы для последующего анализа. Создайте структуру папок по URL.

7. **Fuzzer параметров:** Напишите функцию, которая подставляет различные значения в GET-параметры и анализирует изменения в ответе (размер, код ответа).

## Адаптация под macOS (M2, 8GB)

При выполнении заданий на компьютере Mac с процессором M2 и 8GB оперативной памяти учитывайте следующие особенности:

- Для установки библиотек используйте `pip3 install <package>`, а не `pip install`.
- На M2 можно использовать `asyncio`, он поддерживает ARM.
- На 8GB RAM проект может быть тяжелым, используйте легковесные библиотеки.
- Для работы с aiohttp в будущих уроках используйте `connector = aiohttp.TCPConnector(ssl=False)` вместо передачи `ssl=False` напрямую в `get()`.
