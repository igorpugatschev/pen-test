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
pip install requests
```

## Практическое занятие

Напишем скрипт, который отправляет различные HTTP-запросы и анализирует ответы сервера.

```python
import requests
import json
from urllib.parse import urljoin

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
    # Отключаем предупреждения о небезопасных SSL-сертификатах
    requests.packages.urllib3.disable_warnings()
    
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
