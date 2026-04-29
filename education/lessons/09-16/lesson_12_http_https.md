# Занятие 12. HTTP/HTTPS: методы GET/POST, коды ответов, заголовки, TLS

## Теория

HTTP (Hypertext Transfer Protocol) — протокол прикладного уровня для передачи гипертекстовых документов. HTTPS — защищенная версия с использованием TLS/SSL.

### Методы HTTP

**GET** — запрос ресурса
```
GET /index.html HTTP/1.1
Host: example.com
```

**POST** — отправка данных на сервер
```
POST /login HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

username=admin&password=secret
```

**PUT** — замена ресурса
**DELETE** — удаление ресурса
**HEAD** — как GET, но без тела ответа
**OPTIONS** — получение поддерживаемых методов
**PATCH** — частичное изменение ресурса

### Коды ответов HTTP

**1xx — Информационные**
- 100 Continue

**2xx — Успешные**
- 200 OK — запрос успешен
- 201 Created — ресурс создан
- 204 No Content — успешно, но нет содержимого

**3xx — Перенаправления**
- 301 Moved Permanently — ресурс переехал навсегда
- 302 Found — временное перенаправление
- 304 Not Modified — кэш актуален

**4xx — Ошибки клиента**
- 400 Bad Request — некорректный запрос
- 401 Unauthorized — требуется аутентификация
- 403 Forbidden — доступ запрещен
- 404 Not Found — ресурс не найден
- 405 Method Not Allowed — метод не поддерживается

**5xx — Ошибки сервера**
- 500 Internal Server Error — внутренняя ошибка
- 502 Bad Gateway — ошибка шлюза
- 503 Service Unavailable — сервис недоступен

### Важные заголовки HTTP

**Запроса:**
- Host — целевой хост
- User-Agent — информация о клиенте
- Accept — какие типы контента принимает клиент
- Authorization — данные для аутентификации
- Cookie — куки сессии
- Content-Type — тип отправляемых данных
- Referer — откуда пришел запрос

**Ответа:**
- Server — информация о сервере
- Set-Cookie — установка куки
- Content-Type — тип содержимого
- Location — URL для перенаправления
- WWW-Authenticate — требуемый метод аутентификации
- Strict-Transport-Security — принудительный HTTPS

### HTTPS и TLS

TLS (Transport Layer Security) — криптографический протокол, обеспечивающий:
- **Конфиденциальность** — данные шифруются
- **Целостность** — данные не изменяются в пути
- **Аутентификацию** — сервер подтверждает личность сертификатом

**Процесс TLS-handshake:**
1. Client Hello — клиент отправляет поддерживаемые шифры
2. Server Hello — сервер выбирает шифр, отправляет сертификат
3. Клиент проверяет сертификат
4. Обмен ключами
5. Установление защищенного канала

### Cookies и сессии

- **Session cookies** — удаляются при закрытии браузера
- **Persistent cookies** — сохраняются на диск
- **Secure flag** — куки только через HTTPS
- **HttpOnly flag** — куки недоступны через JavaScript
- **SameSite** — защита от CSRF

## Практическое занятие

### Задача 1: Ручной HTTP-запрос через netcat

1. Установите соединение с сервером:
```bash
nc example.com 80
```

2. Отправьте HTTP-запрос вручную:
```
GET / HTTP/1.1
Host: example.com

```
(Нажмите Enter дважды после Host)

3. Проанализируйте ответ: код, заголовки, тело

### Задача 2: Использование curl для тестирования

1. GET-запрос с выводом заголовков:
```bash
curl -i http://example.com
```

2. POST-запрос с данными:
```bash
curl -X POST -d "username=admin&password=test" http://example.com/login
```

3. Отправка куки:
```bash
curl -b "session=abc123" http://example.com/profile
```

4. Установка заголовков:
```bash
curl -H "User-Agent: PentestBot/1.0" -H "X-Custom: test" http://example.com
```

### Задача 3: Анализ HTTPS и сертификатов

1. Просмотр сертификата сайта:
```bash
openssl s_client -connect example.com:443 -showcerts
```

2. Проверка поддерживаемых протоколов TLS:
```bash
nmap --script ssl-enum-ciphers -p 443 example.com
```

3. Проверка уязвимостей SSL/TLS:
```bash
testssl.sh example.com
```

### Задача 4: Перехват трафика с mitmproxy

1. Установите mitmproxy:
```bash
sudo apt install mitmproxy
```

2. Запустите прокси:
```bash
mitmproxy
```

3. Настройте браузер на использование прокси 127.0.0.1:8080
4. Зайдите на сайт через HTTP (не HTTPS) и посмотрите запросы в mitmproxy

## Задачи для самостоятельного выполнения

1. **Создание HTTP-клиента на Python**: Напишите скрипт, который делает GET и POST запросы к тестовому серверу (можно использовать httpbin.org). Скрипт должен выводить код ответа, все заголовки и тело ответа. Используйте только стандартную библиотеку `http.client` или `socket`.

2. **Анализ заголовков безопасности**: Проверьте 5 популярных сайтов на наличие заголовков безопасности (Strict-Transport-Security, Content-Security-Policy, X-Frame-Options, X-Content-Type-Options). Составьте таблицу с результатами. Каких заголовков не хватает? К чему это может привести?

3. **Работа с куки**: Используя curl или Python, авторизуйтесь на тестовом сайте (например, OWASP Juice Shop или DVWA), получите куки сессии и используйте их для доступа к защищенным страницам. Опишите процесс.

4. **Исследование TLS**: С помощью `sslyze` или `testssl.sh` просканируйте свой локальный сервер (или публичный сайт) на поддержку устаревших протоколов (SSLv2, SSLv3, TLS 1.0, TLS 1.1). Найдите рекомендации по их отключению.

5. **HTTP-smuggling теория**: Изучите концепцию HTTP Request Smuggling (CL.TE, TE.CL). Опишите суть уязвимости и приведите пример того, как разница в обработке заголовков Content-Length и Transfer-Encoding может привести к атаке.
