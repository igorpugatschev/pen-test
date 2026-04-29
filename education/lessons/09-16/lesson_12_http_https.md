# Занятие 12. HTTP/HTTPS: методы GET/POST, коды ответов, заголовки, TLS

> **⚠️ ВНИМАНИЕ: Легальность.** Все действия в этом уроке выполняются только в учебной лаборатории. Атаки на чужие веб-сайты без разрешения незаконны (УК РФ ст. 272, CFAA в США). Используйте PortSwigger Academy, TryHackMe.

## Теория:

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
# macOS: brew install mitmproxy
# Linux: sudo apt install mitmproxy
brew install mitmproxy
```

2. Запустите прокси:
```bash
mitmproxy
```

3. Настройте браузер на использование прокси 127.0.0.1:8080
4. Зайдите на сайт через HTTP (не HTTPS) и посмотрите запросы в mitmproxy

## Примеры вывода

### curl -i http://example.com
```
HTTP/1.1 200 OK
Accept-Ranges: bytes
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Mon, 29 Apr 2024 12:00:00 GMT
Etag: "3147526947+ident"
Expires: Mon, 06 May 2024 12:00:00 GMT
Server: ECS (sac/2547)
X-Cache: HIT
Content-Length: 1256

<!doctype html>
<html>
<head>
    <title>Example Domain</title>
...
```

### curl -X POST -d "username=admin&password=test" http://example.com/login
```
HTTP/1.1 401 Unauthorized
Content-Type: text/html
Content-Length: 123

<h1>Unauthorized</h1>
<p>Invalid credentials</p>
```

### openssl s_client -connect example.com:443 -showcerts
```
CONNECTED(00000003)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
verify return:1
depth=1 C = US, O = DigiCert Inc, CN = DigiCert TLS RSA SHA256 2020 CA1
verify return:1
depth=0 C = US, ST = California, L = Los Angeles, O = Internet Corporation for Assigned Names and Numbers, CN = www.example.org
verify return:1
---
Certificate chain
 0 s:CN = www.example.org
   i:C = US, O = DigiCert Inc, CN = DigiCert TLS RSA SHA256 2020 CA1
...
```

### nmap --script ssl-enum-ciphers -p 443 example.com
```
PORT    STATE SERVICE
443/tcp open  https
| ssl-enum-ciphers:
|   TLSv1.2:
|     ciphers:
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A
|     compressors:
|       NULL
|     cipher preference: server
|_  least strength: A
```

## Частые ошибки

1. **Путаница кодов ответов**: 301 — постоянное перенаправление, 302 — временное. 401 — нужна аутентификация, 403 — доступ запрещен (даже с аутентификацией).
2. **HTTP vs HTTPS**: Данные HTTP передаются в открытом виде. Используйте HTTPS для чувствительной информации.
3. **Забывание двойного Enter**: При ручном HTTP-запросе через netcat нужно нажать Enter дважды после заголовков, иначе сервер не поймет конец запроса.
4. **HttpOnly и Secure flags**: Если у куки нет флага HttpOnly, её можно украсть через XSS. Если нет Secure — она передается по HTTP.

## Вопросы на понимание

1. В чем разница между методами GET и POST?
    <details><summary>Ответ</summary>GET передает параметры в URL, POST — в теле запроса. POST безопаснее для чувствительных данных, но оба метода видны при перехвате без HTTPS</details>
2. Что означает код ответа 403 Forbidden?
    <details><summary>Ответ</summary>Сервер понял запрос, но отказывается его выполнять (нет прав доступа к ресурсу)</details>
3. Зачем нужен заголовок Strict-Transport-Security?
    <details><summary>Ответ</summary>Принуждает браузер использовать только HTTPS для подключения к сайту, защищает от SSL-stripping</details>
4. Как TLS защищает данные?
    <details><summary>Ответ</summary>Обеспечивает конфиденциальность (шифрование), целостность (проверка изменений) и аутентификацию (сертификат сервера)</details>

## Задачи для самостоятельного выполнения

1. **Создание HTTP-клиента на Python**: Напишите скрипт, который делает GET и POST запросы к тестовому серверу (можно использовать httpbin.org). Скрипт должен выводить код ответа, все заголовки и тело ответа. Используйте только стандартную библиотеку `http.client` или `socket`.

2. **Анализ заголовков безопасности**: Проверьте 5 популярных сайтов на наличие заголовков безопасности (Strict-Transport-Security, Content-Security-Policy, X-Frame-Options, X-Content-Type-Options). Составьте таблицу с результатами. Каких заголовков не хватает? К чему это может привести?

3. **Работа с куки**: Используя curl или Python, авторизуйтесь на тестовом сайте (например, OWASP Juice Shop или DVWA), получите куки сессии и используйте их для доступа к защищенным страницам. Опишите процесс.

4. **Исследование TLS**: С помощью `sslyze` или `testssl.sh` просканируйте свой локальный сервер (или публичный сайт) на поддержку устаревших протоколов (SSLv2, SSLv3, TLS 1.0, TLS 1.1). Найдите рекомендации по их отключению.

5. **HTTP-smuggling теория**: Изучите концепцию HTTP Request Smuggling (CL.TE, TE.CL). Опишите суть уязвимости и приведите пример того, как разница в обработке заголовков Content-Length и Transfer-Encoding может привести к атаке.

## Адаптация под macOS (M2, 8GB)

Для пользователей macOS (особенно на чипах M1/M2 и с 8GB RAM):

- **Установка инструментов**: Используйте `brew install` вместо `apt install`:
  ```bash
  brew install curl
  brew install openssl
  brew install nmap
  brew install mitmproxy
  ```

- **testssl.sh на macOS**: Не устанавливается через brew. Скачайте с GitHub:
  ```bash
  git clone https://github.com/drwetter/testssl.sh.git
  cd testssl.sh
  ./testssl.sh example.com
  ```

- **sslyze на macOS**: Установка через pip:
  ```bash
  pip3 install sslyze
  ```

- **Виртуализация**: Вместо VirtualBox (который может быть нестабилен на M2) рекомендуется использовать:
  - **UTM** — нативный для Apple Silicon, бесплатный
  - **Parallels** — платный, но быстрый на M-чипах
  
  На 8GB RAM запускайте VM с 3-4GB памяти.

- **Устаревшие команды**: Везде, где в уроке упоминаются `ifconfig`, `netstat`, `arp` — эти команды считаются устаревшими. Используйте современные аналоги:
  - `ifconfig` → `ip addr` / `ip link`
  - `netstat -tunap` → `ss -tunap`
  - `arp -n` → `ip neigh`
  - `route -n` → `ip route`

- **Ограничения 8GB RAM**: Не запускайте одновременно много тяжелых VM. Оптимально: 1 Kali (3GB) + 1 Metasploitable (512MB) = 3.5GB + хост ~4GB.
