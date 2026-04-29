# Занятие 28. Burp Suite практика: Перехват, изменение параметров, атака


### OWASP ZAP — бесплатная альтернатива Burp Suite

**Zed Attack Proxy (ZAP)** — бесплатный инструмент от OWASP, работающий на macOS ARM (M2) нативно.

**Установка на macOS (M2):**
```bash
brew install --cask owasp-zap
```

**Преимущества перед Burp Suite:**
- Полностью бесплатный (Burp имеет ограничения в Community Edition)
- Нативная поддержка ARM64 (не требует эмуляции)
- Простой интерфейс для начинающих

**Основные функции:**
- Проксирование трафика (Proxy)
- Сканирование уязвимостей (Active Scan)
- Пассивное сканирование (Passive Scan)
- Паук (Spider) для обхода сайта

> **Для M2 8GB:** ZAP потребляет меньше ресурсов чем Burp Suite, что критично при ограниченной RAM.

## Теория

Комплексное использование Burp Suite объединяет все изученные инструменты для проведения реального пентеста веб-приложения.

### Рабочий процесс пентеста с Burp

1. **Reconnaissance**: Изучение приложения через Target → Site Map
2. **Interception**: Перехват и анализ запросов через Proxy
3. **Manual Testing**: Проверка уязвимостей через Repeater
4. **Automation**: Массовое тестирование через Intruder
5. **Analysis**: Сравнение ответов через Comparer, декодирование через Decoder

### Продвинутые функции Burp

- **Target → Site Map**: Полная карта сайта, все запросы/ответы
- **Proxy → HTTP History**: Фильтрация, поиск по ключевым словам
- **Repeater → Inspector**: Визуальное редактирование параметров, headers, JSON
- **Intruder → Grep**: Поиск строки в ответах (например, "error", "admin")
- **Decoder**: URL, Base64, HTML, Hex декодирование/кодирование
- **Comparer**: Сравнение двух запросов или ответов (побайтово)

### Тактика атаки

1. Найти точки ввода (параметры URL, формы, cookies, заголовки)
2. Протестировать базовые пейлоады (SQLi, XSS, XXE)
3. Использовать Intruder для перебора или fuzzing
4. Анализировать разницу в ответах

---

## Практическое занятие

### Комплексная атака на DVWA через Burp

**Шаг 1: Сбор информации (Site Map)**
1. В Burp откройте **Target → Site Map**
2. В браузере пройдитесь по всем разделам DVWA (SQLi, XSS, CSRF, Brute Force)
3. В Site Map появится структура сайта — изучите все эндпоинты

**Шаг 2: Перехват и модификация SQL Injection**
1. Включите **Intercept on**
2. В DVWA откройте SQL Injection, введите `1`
3. В Burp перехватите запрос: `GET /vulnerabilities/sqli/?id=1&Submit=Submit`
4. Измените `id=1` на `id=1' UNION SELECT user(),version()#`
5. Нажмите **Forward**
6. В браузере увидите результат UNION-запроса

**Шаг 3: Тестирование через Repeater**
1. Отправьте перехваченный запрос в Repeater (ПКМ → Send to Repeater)
2. В Repeater измените `id` на:
   - `1' OR '1'='1` (все пользователи)
   - `1' UNION SELECT table_name,2 FROM information_schema.tables#`
3. Нажимайте **Send** и анализируйте ответы внизу

**Шаг 4: Fuzzing параметров через Intruder**
1. Отправьте запрос в Intruder
2. В Positions очистите все §, добавьте § вокруг `id=§1§`
3. В Payloads → Load загрузите список:
   ```
   1
   1'
   1" 
   1' OR '1'='1
   1' UNION SELECT 1,2#
   ```
4. В Options → Grep - Match добавьте строку `Surname:` (появляется при успешном SQLi)
5. Запустите атаку — найдите пейлоады с зеленой галочкой (совпадение найдено)

**Шаг 5: Перехват и изменение XSS**
1. Откройте XSS (Reflected), включите Intercept
2. Введите `<script>alert(1)</script>`
3. В Burp найдите пейлоад в параметре `name=`
4. Измените на `<img src=x onerror=alert(document.cookie)>`
5. Forward — увидите cookie в alert

### Использование Comparer

1. В Repeater отправьте два разных запроса (успешный и неуспешный)
2. Выделите оба ответа → ПКМ → **Send to Comparer**
3. В Comparer нажмите **Words** или **Bytes** — увидите разницу

### Скриншоты для отчета

1. **Скриншот 1**: Target → Site Map — карта сайта DVWA со всеми эндпоинтами
2. **Скриншот 2**: Repeater — модифицированный SQLi запрос, ответ содержит версию БД
3. **Скриншот 3**: Intruder — атака завершена, найдены успешные пейлоады (с Grep match)
4. **Скриншот 4**: Comparer — сравнение двух ответов, видна разница

### Примеры вывода

**Target → Site Map — структура DVWA:**
```
http://192.168.0.x/
├── index.php
├── login.php
├── logout.php
├── security.php
├── setup.php
└── vulnerabilities/
    ├── sqli/
    ├── sqli_blind/
    ├── xss_r/
    ├── xss_s/
    ├── xss_d/
    ├── csrf/
    ├── exec/
    ├── brute/
    └── upload/
```

**Comparer — побайтовое сравнение (Bytes view):**
```
Line 15:
< Surname: admin         (Response 1 - success)
> Surname:               (Response 2 - fail)
```

**Decoder — результаты кодирования:**
```
Original: <script>alert(1)</script>
URL-encoded: %3Cscript%3Ealert%281%29%3C%2Fscript%3E
Base64: PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
HTML-entity: &lt;script&gt;alert(1)&lt;/script&gt;
```

### Частые ошибки

1. **Не менять User-Agent в Intruder** — многие WAF блокируют дефолтный Burp
2. **Забыть про Grep-Match** — сложно найти успешные пейлоады без поиска по ответу
3. **Игнорировать Site Map** — можно пропустить важные эндпоинты
4. **Неправильно использовать Comparer** — сравнивайте похожие запросы (успех vs провал)

### Вопросы на понимание

1. В чем преимущество использования Site Map перед ручным изучением сайта?
2. Как Grep-Match помогает при фаззинге?
3. Когда использовать Comparer (Words vs Bytes)?
4. Зачем менять User-Agent при атаке через Intruder?

### Адаптация под macOS (M2)

```bash
# Экспорт результатов Burp для отчета (на macOS)
# В Burp: Intruder → Attack → Results → Save → Results Table

# Использование ярлыков на macOS для Burp:
# Cmd+Shift+P — открыть Repeater
# Cmd+Shift+I — открыть Intruder
# Cmd+Shift+T — открыть Target

# Скриншоты через встроенную утилиту macOS
screencapture -x /tmp/burp_screenshot_$(date +%s).png

# Автоматизация через AppleScript (открытие Burp)
osascript -e 'tell application "Burp Suite Community Edition" to activate'
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

1. **Полный пентест одной уязвимости**: Выберите XSS (Stored) в DVWA. Используя Burp Suite:
   - Перехватите запрос отправки сообщения
   - Модифицируйте его в Repeater с разными XSS-пейлоадами
   - Найдите пейлоад, который выполняется
   - Сделайте скриншот Repeater с успешным выполнением

2. **Fuzzing параметров**: В DVWA перейдите в **Brute Force**. Используйте Intruder для перебора:
   - Параметр: `username` (словарь: admin, root, user, test)
   - Параметр: `password` (словарь: password, 123456, admin, qwerty)
   - Тип атаки: Cluster bomb (все комбинации)
   
   Сколько комбинаций было проверено? Какая пара сработала?

3. **Анализ через Site Map**: В Burp Target → Site Map найдите все страницы DVWA, доступные без авторизации (до входа). Сделайте скриншот Site Map с фильтром "Show only unvisited items". Какие страницы доступны без логина?

4. **Использование Decoder**: Перехватите запрос с cookie. Скопируйте значение PHPSESSID в Decoder. Выполните:
   - URL-decode
   - Base64-decode (если возможно)
   - Hex view
   
   Сделайте скриншот Decoder с результатами. Похож ли PHPSESSID на зашифрованные данные?

5. **Комплексная атака**: Объедините SQLi + Burp для получения всех данных из DVWA:
   - Используйте Repeater для поиска уязвимых параметров
   - Используйте Intruder с UNION-запросами для перебора таблиц
   - Найдите хеши паролей всех пользователей
   
   Опишите шаги и сделайте скриншоты каждого этапа.
