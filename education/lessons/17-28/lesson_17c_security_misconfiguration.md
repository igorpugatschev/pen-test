# Занятие 17c. OWASP A05: Security Misconfiguration — Неправильная конфигурация

## Теория

**A05:2021 – Security Misconfiguration** — это неправильная настройка компонентов приложения, сервера или облачной инфраструктуры, приводящая к уязвимостям.

### Типичные примеры

1. **Отладочные режимы в продакшене** — подробные ошибки раскрывают структуру БД, пути к файлам
2. **Дефолтные пароли** — admin/admin на оборудовании, в БД, в приложениях
3. **Открытые порты** — лишние сервисы (SSH, RDP) доступны из интернета
4. **Ненужные функции** — включенные админ-панели, тестовые страницы, phpinfo()
5. **Устаревшие конфиги** — старые протоколы (TLS 1.0), слабые шифры

### Где искать

| Компонент | Что проверять |
|-----------|---------------|
| Веб-сервер | .git, .env, backup файлы, directory listing |
| Приложение | Debug mode, default credentials, error messages |
| База данных | Пароль root пустой, доступ извне |
| Cloud | Открытые S3 бакеты, неверные IAM политики |
| Фреймворк | Стандартные пути (/admin, /phpmyadmin) |

### Пример уязвимости

**Сценарий**: Веб-приложение запущено с `APP_DEBUG=true` (Laravel) или `display_errors=On` (PHP).

Запрос:
```
GET /nonexistent-page HTTP/1.1
Host: vulnerable.com
```

Ответ содержит stack trace:
```
Fatal error: Uncaught PDOException: SQLSTATE[HY000] [1045] 
Access denied for user 'dbuser'@'localhost' (using password: 'secret123')
in /var/www/html/config/database.php on line 42
```
Пароль от БД утек в ошибке!

---

## Практическое занятие

### Поиск конфигурационных ошибок в DVWA

**Шаг 1: Проверка отладочной информации**
1. Включите Burp Proxy
2. Откройте http://192.168.0.x/vulnerabilities/sqli/?id=1'
3. Посмотрите ответ сервера

Пример вывода (SQL ошибка раскрывает структуру запроса):
```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''1''' at line 1

Full query: SELECT first_name, last_name FROM users WHERE user_id = '1''
```
Ошибка показывает структуру запроса — это информация для атакующего.

**Шаг 2: Поиск скрытых файлов и директорий**
Попробуйте открыть:
- http://192.168.0.x/phpinfo.php
- http://192.168.0.x/info.php
- http://192.168.0.x/.git/
- http://192.168.0.x/config.php
- http://192.168.0.x/backup/

Пример ответа:
```
GET /config.php
→ HTTP/1.1 200 OK
→ Content-Type: text/html

// Database configuration
$db_host = 'localhost';
$db_user = 'root';
$db_pass = '';
```
Если файл доступен — это Security Misconfiguration.

**Шаг 3: Проверка заголовков безопасности**
В Burp Proxy → HTTP history найдите ответ DVWA, посмотрите заголовки:

```
HTTP/1.1 200 OK
Server: Apache/2.4.25 (Debian)
X-Powered-By: PHP/5.6.30
Set-Cookie: PHPSESSID=abc123; path=/
```

**Отсутствуют заголовки:**
- `Content-Security-Policy`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Strict-Transport-Security` (для HTTPS)

**Шаг 4: Проверка bWAPP**
1. Откройте http://192.168.0.x/robots.txt
2. Посмотрите, какие пути закрыты от индексации
3. Попробуйте открыть `/admin/`, `/docs/`, `/install.php`

Пример robots.txt:
```
User-agent: *
Disallow: /admin/
Disallow: /docs/
```
Но пути всё равно доступны!

---

## Частые ошибки

1. **Оставлять дефолтные пароли** — самая частая ошибка (admin/admin, root/пусто)
2. **Забывать выключить debug mode** при деплое
3. **Не закрывать ненужные порты** — оставлять phpMyAdmin, админки открытыми
4. **Игнорировать заголовки безопасности** — без CSP, X-Frame-Options сайт уязвим к кликджекингу

---

## Вопросы на понимание

1. Почему отладочная информация в продакшене — это уязвимость?
2. Какие заголовки безопасности должны быть в каждом HTTP-ответе?
3. Почему дефолтные пароли — это Security Misconfiguration, а не Broken Authentication?
4. Как проверить, не остались ли backup-файлы в публичной директории?

---

## Адаптация под macOS (M2)

```bash
# Сканирование портов (nmap работает на M2)
brew install nmap
nmap -sV -p 1-1000 localhost

# Поиск конфигов через gobuster (работает на M2 через Docker)
docker run -t orik/gobuster dir -u http://192.168.0.x -w /wordlist.txt

# Установка nikto для проверки конфигурации веб-сервера
brew install nikto
nikto -h http://192.168.0.x
```

---


## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.



## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. **Сканирование портов**: Используя `nmap`, просканируйте хост с DVWA. Какие порты открыты? Есть ли лишние сервисы? Сделайте скриншот вывода nmap.

2. **Поиск скрытых файлов**: В bWAPP попробуйте открыть:
   - `/config.php`
   - `/install.php`
   - `/backup/`
   - `/phpinfo.php`
   
   Опишите, какие файлы доступны без авторизации, какие данные раскрыты.

3. **Проверка заголовков**: Используя Burp Suite, проверьте заголовки ответов DVWA. Каких заголовков безопасности не хватает? Напишите, какие заголовки нужно добавить и с какими значениями.

4. **Nikto scan**: Запустите `nikto -h http://192.168.0.x` для проверки конфигурации веб-сервера. Опишите найденные проблемы (минимум 3). Сделайте скриншот вывода.

5. **Исправление конфигурации**: Напишите список (минимум 5 пунктов), что нужно исправить в конфигурации DVWA/bWAPP, чтобы устранить Security Misconfiguration.
