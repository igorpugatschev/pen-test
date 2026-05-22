# Занятие 17c. OWASP A05: Security Misconfiguration — Неправильная конфигурация

## Учебная рамка

**Входные требования:** Базовое понимание HTTP, форм, параметров URL и работы браузера/DevTools.

**Результат занятия:** Студент воспроизводит уязвимость только в учебном приложении и объясняет условие ее возникновения и способ защиты.

**Наследуемая SDET-компетенция:** test design, negative testing, API/UI evidence и перевод OWASP-риска в проверяемый QA-кейс.

**Security QA-компетенция:** моделирование web-рисков OWASP и безопасная ручная проверка Slider AI.

**Связь с книгами:** OWASP/WSTG как основной security reference; «PyCharm. Профессиональная работа на Python 2024» — DevTools/HTTP Client/evidence workflow.

**Основной источник:** «PyCharm. Профессиональная работа на Python 2024» и `Black Hat Python` только для lab-only/defensive interpretation.

**Дополнительные источники:** «Легкий способ выучить Python 3 еще глубже» для обработки запросов, текстов и простых проверочных данных.

**Что берем из источника:** разделение lab payload и product-safe marker, HTTP evidence, перевод риска OWASP в security test case.

**Как это превращается в SDET/Security QA навык:** проектировать безопасные проверки Slider AI через OWASP/WSTG без destructive payloads.

**Что нельзя переносить на Slider AI без отдельного разрешения:** учебные payloads выполнять только в DVWA/WebGoat/PortSwigger; на Slider AI использовать безопасные маркеры и passive evidence.


**Процессный артефакт:** `THREAT_MODEL.md` или `SECURITY_FINDING_TEMPLATE.md`: abuse case, evidence и expected control.

**Безопасная цель:** DVWA, WebGoat, bWAPP, PortSwigger Web Security Academy или локальная учебная VM. Запрещены реальные сайты без письменного разрешения.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Пройти демонстрационный сценарий на низком уровне сложности, сделать скриншот/лог запроса и описать причину уязвимости.

**Углубление:** Повторить на более высоком уровне сложности, сравнить поведение фильтров и предложить безопасную реализацию.

**Минимальная проверка успеха:** Уязвимость подтверждена в учебной среде, payload не направлялся на реальные сервисы, студент может назвать защитную меру.

**Эталонный вывод:** Отчет содержит URL учебной лаборатории, введенный payload, фрагмент ответа и объяснение риска простыми словами.

**Критерии сдачи:** Зачет: подтверждена учебная уязвимость и описана защита. Отлично: добавлен разбор, почему payload работает или перестает работать.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 17c. OWASP A05: Security Misconfiguration — Неправильная конфигурация`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/pycharm-professional-python-2024-pages/`
- `docs/socraticode/black-hat-python-ru-pages/` только lab-only/defensive

Конкретные страницы для этого блока: `pycharm-professional-python-2024-pages/page-338.md`-`page-369.md`; `black-hat-python-ru-pages/page-120.md`-`page-140.md` только lab-only.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: разделение lab payload и product-safe marker, HTTP evidence, перевод риска OWASP в security test case. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: учебные payloads выполнять только в DVWA/WebGoat/PortSwigger; на Slider AI использовать безопасные маркеры и passive evidence. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

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

## Guided practice

1. Сформулируйте риск урока как abuse case и как проверяемое ожидание защиты.
2. Отработайте опасную технику только в lab, если урок этого требует.
3. Для Slider AI выполните safe-marker или passive observation без извлечения данных и без destructive payload.
4. Классифицируйте результат: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

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

Минимальный эталонный артефакт для сдачи:

```markdown
Environment: macOS native / Kali ARM64 VM / cloud lab / Slider AI olddev
Target: <разрешенная учебная цель или https://olddev.slider-ai.ru>
Action: <выполненная безопасная команда или ручной шаг>
Evidence: <санитизированный фрагмент вывода, скриншота или HTTP history>
Result status: finding / observation / not reproducible / not applicable / requires approval
Next step: <retest, remediation, approval request или lab-only follow-up>
```

В отчете студент указывает среду выполнения, безопасную цель, команду или ручные шаги и коротко объясняет, какая строка подтверждает результат.



## Адаптация под macOS (M2, 8GB)

- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`; для явно помеченной Kali/Linux-среды допустим `apt`.
- Kali/Linux VM запускайте только как углубление и выделяйте не более 3-4GB RAM на MacBook Air M2 (8GB)
- Если нужна Kali/Linux VM на Apple Silicon, используйте ARM64-образ в UTM/VMware Fusion/Parallels; не используйте x86/x64 VM как базовый путь.
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

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Security Misconfiguration

### Минимум

Проверьте видимые признаки конфигурации: error pages, debug banners, headers, directory listing.

### Практика Slider AI

Сохраните только неинтрузивные наблюдения из браузера/DevTools/curl.

### Углубление после изучения следующих уроков

После урока 35 проверьте те же признаки passive scan в ZAP.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `OWASP Test Design for Slider AI`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
