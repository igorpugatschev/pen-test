# Занятие 27. Burp Suite база: Proxy, Repeater, Intruder

## Теория

**Burp Suite** — это интегрированная платформа для тестирования безопасности веб-приложений. Состоит из нескольких инструментов (табов).

### Основные инструменты

1. **Proxy**: Перехватывает трафик между браузером и сервером
2. **Repeater**: Позволяет повторять и изменять запросы вручную
3. **Intruder**: Автоматизированная атака (брутфорс, перебор)
4. **Decoder**: Кодирование/декодирование данных
5. **Comparer**: Сравнение двух данных (запросов, ответов)
6. **Scanner** (Pro): Автоматическое сканирование уязвимостей
7. **Sequencer**: Анализ случайности токенов/сессий
8. **Extender**: Плагины (BApp Store)

### Как работает Proxy

1. Браузер настроен на использование прокси 127.0.0.1:8080
2. Весь трафик идет через Burp
3. Burp может:
   - Просто пропускать (Forward)
   - Остановить для анализа (Intercept on/off)
   - Изменить запрос перед отправкой

### Repeater — назначение

Используется для:
- Изучения ответов сервера на модифицированные запросы
- Тестирования SQL Injection, XSS вручную
- Проверки граничных случаев

### Intruder — назначение

Используется для:
- Брутфорса паролей
- Перебора ID (enumeration)
- Fuzzing параметров
- Поиска уязвимостей через словари

### Типы атак Intruder

1. **Sniper**: Одна позиция, один словарь
2. **Battering ram**: Одно значение подставляется во все позиции
3. **Pitchfork**: Уникальные значения из нескольких словарей (параллельно)
4. **Cluster bomb**: Все комбинации из нескольких словарей

---

## Практическое занятие

### Установка и настройка Burp Suite

1. Скачайте Community Edition: https://portswigger.net/burp/communitydownload
2. Запустите Burp Suite
3. Убедитесь, что вкладка **Proxy** → **Proxy settings** показывает:
   - Running on: 127.0.0.1:8080

### Настройка браузера

**Firefox (рекомендуется):**
1. Откройте Settings → Network Settings → Manual proxy configuration
2. HTTP Proxy: `127.0.0.1`, Port: `8080`
3. Check "Also use this proxy for HTTPS"

**Или используйте FoxyProxy** (расширение для быстрого переключения).

### Установка CA-сертификата Burp (критично для HTTPS)

Для перехвата HTTPS-трафика необходимо установить CA-сертификат Burp в браузер.

**Шаг 1: Скачивание сертификата**
1. В Burp Suite убедитесь, что Proxy запущен
2. В браузере (через прокси Burp) откройте: `http://burp`
3. Нажмите **CA Certificate** — файл `cacert.der` скачается

**Шаг 2: Установка в Firefox**
1. Откройте Firefox → Settings → Privacy & Security → Certificates → View Certificates
2. Нажмите **Import**, выберите скачанный `cacert.der`
3. Поставьте галочку **Trust this CA to identify websites**
4. Нажмите OK

**Шаг 3: Проверка**
1. В Burp включите **Intercept on**
2. В браузере откройте `https://www.google.com`
3. В Burp должен появиться перехваченный HTTPS-запрос

**Для macOS (M2):**
```bash
# Установка Burp Suite через Homebrew
brew install --cask burp-suite
```

После установки сертификата, экспортируйте его:
1. В Burp: Proxy → Proxy settings → Import / Export CA certificate
2. Export → Certificate in DER format → Save as `burp_ca.der`
3. В macOS дважды кликните файл → добавится в Keychain Access
4. В Keychain найдите "PortSwigger CA" → ПКМ → Get Info → Trust → Always Trust

### Практика: Proxy и перехват

**Шаг 1: Перехват запроса**
1. В Burp включите **Intercept on** (Proxy → Intercept)
2. В браузере откройте http://192.168.0.x (DVWA)
3. В Burp появится запрос — нажмите **Forward** чтобы пропустить
4. Попробуйте войти в DVWA, запрос появится в Proxy

**Шаг 2: Изменение запроса**
1. Перехватите запрос логина
2. Измените `password=password` на `password=wrong`
3. Нажмите **Forward**
4. DVWA покажет ошибку входа

**Шаг 3: Отключение перехвата**
Нажмите **Intercept off** — теперь Burp просто пропускает трафик, но записывает в HTTP history.

### Практика: Repeater

**Шаг 1: Отправка запроса в Repeater**
1. В Proxy → HTTP history найдите запрос к `/vulnerabilities/sqli/?id=1`
2. ПКМ → **Send to Repeater**

**Шаг 2: Модификация и отправка**
1. В Repeater измените `id=1` на `id=1' OR '1'='1`
2. Нажмите **Send**
3. Посмотрите ответ в нижней части (Response)
4. Найдите в ответе данные пользователей (first_name, surname)

**Шаг 3: Изучение заголовков**
В Repeater посмотрите вкладки:
- **Headers**: заголовки запроса и ответа
- **Body**: тело ответа
- **Hex**: шестнадцатеричный вид

### Практика: Intruder (базовый)

**Шаг 1: Настройка позиций**
1. Отправьте запрос логина в Intruder (ПКМ → Send to Intruder)
2. В Intruder → Positions нажмите **Clear §**
3. Выделите значение пароля, нажмите **Add §**: `password=§test§`

**Шаг 2: Настройка пейлоадов**
1. Перейдите в Intruder → Payloads
2. В Payload Options добавьте: `password`, `123456`, `admin`, `letmein`
3. Или загрузите словарь

**Шаг 3: Запуск атаки**
1. Нажмите **Start Attack**
2. В открывшемся окне найдите строку с отличающейся длиной (Length)
3. Эта строка — успешный вход

### Скриншоты для отчета

1. **Скриншот 1**: Burp Proxy — перехваченный запрос, виден Intercept on
2. **Скриншот 2**: Burp Repeater — запрос с модифицированным параметром, ответ содержит данные
3. **Скриншот 3**: Burp Intruder — результат атаки, найден правильный пароль

### Примеры вывода

**Burp Proxy — перехваченный запрос:**
```
GET /vulnerabilities/sqli/?id=1 HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
Cookie: PHPSESSID=abc123; security=low
Connection: close

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1234

<html>...<pre>First name: admin<br>Surname: admin</pre>...</html>
```

**Burp Repeater — измененный запрос и ответ:**
```
Request:
GET /vulnerabilities/sqli/?id=1' OR '1'='1 HTTP/1.1
Host: localhost
Cookie: PHPSESSID=abc123; security=low

Response:
HTTP/1.1 200 OK
<pre>First name: admin<br>Surname: admin</pre>
<pre>First name: Gordon<br>Surname: Brown</pre>
... (все пользователи)
```

**Burp Intruder — результаты атаки:**
```
Payload     | Status | Length | Result
test        | 302    | 0       |
password    | 302    | 0       | ← SUCCESS (редирект на главную)
123456      | 302    | 0       |
```

### Частые ошибки

1. **Забыть включить Intercept** — трафик не перехватывается
2. **Неправильный прокси в браузере** — должен быть 127.0.0.1:8080
3. **Не установлен CA-сертификат** — HTTPS трафик не виден (failed to handshake)
4. **Forward вместо Drop** — когда перехватили запрос, но не хотели его менять

### Вопросы на понимание

1. В чем разница между Proxy (Intercept on) и Repeater?
2. Когда использовать Intruder типа Sniper, а когда Cluster bomb?
3. Зачем нужен CA-сертификат Burp для HTTPS?
4. Как найти успешный пейлоад в Intruder (кроме кода ответа)?

### Адаптация под macOS (M2)

```bash
# Установка Burp Suite через Homebrew
brew install --cask burp-suite

# Экспорт сертификата через командную строку (если Burp уже запущен)
# Откройте в браузере: http://127.0.0.1:8080/cert
# Скачается cacert.der

# Импорт в Keychain (автоматически)
security add-trusted-cert -d -r trustRoot -k ~/Library/Keychains/login.keychain cacert.der

# Проверка, что сертификат добавлен
security find-certificate -c "PortSwigger CA"
```

---


## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. **Настройка Burp**: Установите Burp Suite Community Edition. Настройте браузер Firefox на работу через прокси 127.0.0.1:8080. Сделайте скриншот окна Burp с вкладкой Proxy, где видно, что прокси запущен.

2. **Перехват и модификация**: Используя Burp Proxy, перехватите запрос к DVWA (XSS Reflected). Модифицируйте параметр `name` добавив XSS-пейлоад `<script>alert(1)</script>`. Пропустите запрос и убедитесь, что XSS сработал. Сделайте скриншот Repeater с результатом.

3. **Repeater для SQLi**: Отправьте запрос SQL Injection из DVWA в Repeater. Выполните пейлоады:
   - `id=1' OR '1'='1`
   - `id=1' UNION SELECT user(), version()#`
   
   Опишите ответы сервера, какие данные удалось получить.

4. **Intruder для перебора ID**: В DVWA перейдите в **SQL Injection (Blind)**. Используйте Repeater для перебора ID пользователей (1, 2, 3...). Затем используйте Intruder с payloads 1-10. Опишите, какие ID существуют (по разнице в ответах).

5. **Decoder**: В Burp Suite откройте вкладку **Decoder**. Закодируйте строку `<script>alert(1)</script>` в:
   - URL-encoding
   - Base64
   - HTML-encoding
   
   Сделайте скриншот Decoder с результатами. В каком виде лучше передавать XSS-пейлоады?
