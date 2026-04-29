# Занятие 62. OWASP Testing Guide: структура теста веб-приложений

## Теория

OWASP Testing Guide (OTF) — это комплексное руководство по тестированию безопасности веб-приложений, признанное мировым стандартом.

### Структура OWASP Testing Guide v4.2

**Раздел 1: Введение и основы**
- Принципы тестирования
- Фазы теста
- Модель зрелости процесса тестирования (TMM)

**Раздел 2: Сбор информации (Information Gathering)**
- OWASP WSTG-INFO-001: Поиск публичной информации
- WSTG-INFO-002: Сканирование портов и сервисов
- WSTG-INFO-003: Анализ веб-сервера
- WSTG-INFO-004: Анализ метаданных приложения
- WSTG-INFO-005: Перечисление директорий и файлов
- WSTG-INFO-006: Анализ конфигурации облачных сервисов
- WSTG-INFO-007: Поиск репозиториев с кодом
- WSTG-INFO-008: Определение технологий (fingerprinting)
- WSTG-INFO-009: Определение фреймворка приложения
- WSTG-INFO-010: Сбор информации о пользователях

**Раздел 3: Конфигурационное тестирование (Configuration Testing)**
- WSTG-CONF-001: Проверка учетных записей по умолчанию
- WSTG-CONF-002: Проверка неиспользуемых страниц и сервисов
- WSTG-CONF-003: Проверка заголовков безопасности
- WSTG-CONF-004: Проверка файлов cookie
- WSTG-CONF-005: Проверка политик CORS
- WSTG-CONF-006: Проверка SSL/TLS
- WSTG-CONF-007: Проверка HTTP-методов
- WSTG-CONF-008: Проверка RIA (Rich Internet Applications)
- WSTG-CONF-009: Проверка конфигурации облачных сервисов

**Раздел 4: Управление идентификацией (Identity Management)**
- WSTG-IDNT-001: Регистрация пользователей
- WSTG-IDNT-002: Сброс пароля
- WSTG-IDNT-003: Смена пароля
- WSTG-IDNT-004: Условия сложности пароля
- WSTG-IDNT-005: Проверка блокировки учетной записи
- WSTG-IDNT-006: Обход аутентификации
- WSTG-IDNT-007: Проверка политик Remember Me
- WSTG-IDNT-008: Проверка PII (персональных данных)
- WSTG-IDNT-009: Проверка политик криптографии

**Раздел 5: Аутентификация (Authentication Testing)**
- WSTG-ATHN-001: Проверка учетных записей по умолчанию
- WSTG-ATHN-002: Брутфорс логинов
- WSTG-ATHN-003: Проверка регистрации
- WSTG-ATHN-004: Проверка сброса пароля
- WSTG-ATHN-005: Проверка капчи
- WSTG-ATHN-006: Проверка многофакторной аутентификации
- WSTG-ATHN-007: Проверка remember me
- WSTG-ATHN-008: Проверка смены пароля
- WSTG-ATHN-009: Проверка кэширования
- WSTG-ATHN-010: Проверка таймаута сессии
- WSTG-ATHN-011: Проверка разделения ролей

**Раздел 6: Управление авторизацией (Authorization Testing)**
- WSTG-ATHZ-001: Обход контроля доступа
- WSTG-ATHZ-002: Недостатки CORS
- WSTG-ATHZ-003: Тестирование привилегий
- WSTG-ATHZ-004: Небезопасное прямое обращение к объектам (IDOR)
- WSTG-ATHZ-005: Обход авторизации через недостатки метаданных

**Раздел 7: Управление сессией (Session Management)**
- WSTG-SESS-001: Анализ токенов сессии
- WSTG-SESS-002: Обход аутентификации через куки
- WSTG-SESS-003: Фиксация сессии
- WSTG-SESS-004: Перехват сессии
- WSTG-SESS-005: Утечка токенов в логах
- WSTG-SESS-006: Cross-site request forgery (CSRF)
- WSTG-SESS-007: Проверка логики сессий

**Раздел 8: Внедрение ввода (Input Validation)**
- WSTG-INPV-001: SQL Injection
- WSTG-INPV-002: NoSQL Injection
- WSTG-INPV-003: LDAP Injection
- WSTG-INPV-004: XML Injection
- WSTG-INPV-005: XXE (XML External Entity)
- WSTG-INPV-006: XSS (Cross-Site Scripting)
- WSTG-INPV-007: HTML Injection
- WSTG-INPV-008: CSS Injection
- WSTG-INPV-009: Command Injection
- WSTG-INPV-010: Format String
- WSTG-INPV-011: Buffer Overflow
- WSTG-INPV-012: Integer Overflow
- WSTG-INPV-013: Server-Side Includes
- WSTG-INPV-014: Import/Upload файлов
- WSTG-INPV-015: Path Traversal
- WSTG-INPV-016: Local File Inclusion (LFI)
- WSTG-INPV-017: Remote File Inclusion (RFI)
- WSTG-INPV-018: Web/API Cache deception
- WSTG-INPV-019: HTTP Parameter Pollution
- WSTG-INPV-020: URL Redirector Abuse

**Раздел 9: Тестирование ошибок (Error Handling)**
- WSTG-ERRH-001: Анализ кодов ошибок
- WSTG-ERRH-002: Проверка утечек в сообщениях об ошибках

**Раздел 10: Криптография (Cryptography)**
- WSTG-CRYP-001: Проверка слабого шифрования
- WSTG-CRYP-002: Проверка неправильного хранения
- WSTG-CRYP-003: Проверка недостатков в алгоритмах

**Раздел 11: Логика (Business Logic)**
- WSTG-BUSL-001: Тестирование логики
- WSTG-BUSL-002: Обход workflow
- WSTG-BUSL-003: Нарушение целостности данных
- WSTG-BUSL-004: Нарушение процессов аутентификации
- WSTG-BUSL-005: Нарушение процессов авторизации
- WSTG-BUSL-006: Нарушение процессов управления
- WSTG-BUSL-007: Нарушение процессов обработки данных
- WSTG-BUSL-008: Нарушение процессов связи
- WSTG-BUSL-009: Нарушение процессов времени
- WSTG-BUSL-010: Нарушение процессов исключений

**Раздел 12: Клиентская проверка (Client-Side)**
- WSTG-CLNT-001: DOM XSS
- WSTG-CLNT-002: JavaScript Injection
- WSTG-CLNT-003: WebSocket Testing
- WSTG-CLNT-004: Web Storage
- WSTG-CLNT-005: Офлайн веб-приложения

### Жизненный цикл теста по OWASP
1. **Пассивный анализ**: изучение без взаимодействия с целью
2. **Активный анализ**: сканирование, probing
3. **Тестирование уязвимостей**: проверка по чек-листу OWASP
4. **Эксплуатация**: подтверждение находок
5. **Анализ рисков**: оценка влияния
6. **Отчет**: документирование

## Практическое занятие

### Создание чек-листа OWASP для конкретного приложения

Создайте файл `owasp_checklist.md` для тестирования интернет-магазина:

```markdown
# OWASP Testing Checklist: Интернет-магазин "TechShop"

## Информация о проекте
- URL: https://shop.techshop.ru
- Тип: E-commerce, платформа Magento
- Дата тестирования: [дата]
- Тестировщик: [ФИО]

## 1. Information Gathering
- [ ] WSTG-INFO-001: Поиск в Google (site:shop.techshop.ru)
- [ ] WSTG-INFO-002: Сканирование портов (nmap -sV -sC)
- [ ] WSTG-INFO-003: Анализ заголовков (curl -I)
- [ ] WSTG-INFO-004: Проверка robots.txt, sitemap.xml
- [ ] WSTG-INFO-005: Перечисление директорий (gobuster/ffuf)
- [ ] WSTG-INFO-006: Проверка конфигурации AWS S3
- [ ] WSTG-INFO-007: Поиск репозиториев на GitHub
- [ ] WSTG-INFO-008: Определение технологий (Wappalyzer)
- [ ] WSTG-INFO-009: Определение версии Magento
- [ ] WSTG-INFO-010: Сбор email-адресов сотрудников

## 2. Configuration Testing
- [ ] WSTG-CONF-001: Проверка admin/admin, root/root
- [ ] WSTG-CONF-002: Поиск неиспользуемых страниц (backup, test)
- [ ] WSTG-CONF-003: Проверка заголовков (HSTS, CSP, X-Frame-Options)
- [ ] WSTG-CONF-004: Проверка флагов cookie (Secure, HttpOnly, SameSite)
- [ ] WSTG-CONF-005: Проверка CORS политики
- [ ] WSTG-CONF-006: Тест SSL/TLS (testssl.sh, ssllabs.com)
- [ ] WSTG-CONF-007: Проверка разрешенных HTTP-методов (OPTIONS)
- [ ] WSTG-CONF-008: Проверка Flash/Silverlight (если есть)
- [ ] WSTG-CONF-009: Проверка конфигурации облака

## 3. Identity Management
- [ ] WSTG-IDNT-001: Тест регистрации (валидация email, телефона)
- [ ] WSTG-IDNT-002: Тест сброса пароля (token exposure)
- [ ] WSTG-IDNT-003: Тест смены пароля (требование сложности)
- [ ] WSTG-IDNT-004: Проверка сложности пароля
- [ ] WSTG-IDNT-005: Проверка блокировки после N попыток
- [ ] WSTG-IDNT-006: Попытка обхода аутентификации
- [ ] WSTG-IDNT-007: Проверка Remember Me (срок действия)
- [ ] WSTG-IDNT-008: Проверка утечки PII в профиле
- [ ] WSTG-IDNT-009: Проверка шифрования паролей (bcrypt, Argon2)

## 4. Authentication Testing
- [ ] WSTG-ATHN-001: Проверка дефолтных учеток админа
- [ ] WSTG-ATHN-002: Брутфорс логина (hydra/brute)
- [ ] WSTG-ATHN-003: Проверка процесса регистрации
- [ ] WSTG-ATHN-004: Тест сброса пароля (IDOR в токене)
- [ ] WSTG-ATHN-005: Проверка капчи (обход через OCR)
- [ ] WSTG-ATHN-006: Проверка 2FA (обход, повторное использование)
- [ ] WSTG-ATHN-007: Тест Remember Me (persistent cookie)
- [ ] WSTG-ATHN-008: Тест смены пароля (CSRF)
- [ ] WSTG-ATHN-009: Проверка кэширования страниц входа
- [ ] WSTG-ATHN-010: Проверка таймаута сессии
- [ ] WSTG-ATHN-011: Проверка разделения admin/user

## 5. Authorization Testing (IDOR, Privilege Escalation)
- [ ] WSTG-ATHZ-001: Обход контроля доступа к админке
- [ ] WSTG-ATHZ-002: Тест CORS (cross-origin запросы)
- [ ] WSTG-ATHZ-003: Проверка привилегий (user → admin)
- [ ] WSTG-ATHZ-004: Тест IDOR (изменение order_id в URL)
- [ ] WSTG-ATHZ-005: Проверка метаданных JWT

## 6. Session Management
- [ ] WSTG-SESS-001: Анализ энтропии session ID
- [ ] WSTG-SESS-002: Проверка cookie без Secure/HttpOnly
- [ ] WSTG-SESS-003: Фиксация сессии (session fixation)
- [ ] WSTG-SESS-004: Перехват сессии (MITM)
- [ ] WSTG-SESS-005: Утечка session ID в URL/логах
- [ ] WSTG-SESS-006: Проверка CSRF (отсутствие токена)
- [ ] WSTG-SESS-007: Логика сессий (logout = invalidation)

## 7. Input Validation (Injection)
- [ ] WSTG-INPV-001: SQL Injection (поиск, логин, корзина)
- [ ] WSTG-INPV-002: NoSQL Injection (если MongoDB)
- [ ] WSTG-INPV-005: XXE (загрузка XML файлов)
- [ ] WSTG-INPV-006: XSS (Reflected, Stored, DOM)
- [ ] WSTG-INPV-009: Command Injection (ping, traceroute)
- [ ] WSTG-INPV-014: Upload файлов (.php, .jsp)
- [ ] WSTG-INPV-015: Path Traversal (../../)
- [ ] WSTG-INPV-016: LFI (include file)
- [ ] WSTG-INPV-019: HTTP Parameter Pollution

## 8. Error Handling
- [ ] WSTG-ERRH-001: Анализ кодов 500, 404, 403
- [ ] WSTG-ERRH-002: Утечки в сообщениях об ошибках (SQL, stack trace)

## 9. Cryptography
- [ ] WSTG-CRYP-001: Слабое шифрование (DES, MD5)
- [ ] WSTG-CRYP-002: Хранение паролей (plaintext, weak hash)
- [ ] WSTG-CRYP-003: Недостатки в алгоритмах

## 10. Business Logic
- [ ] WSTG-BUSL-001: Отрицательные суммы в корзине
- [ ] WSTG-BUSL-002: Обход оплаты (изменение цены в запросе)
- [ ] WSTG-BUSL-003: Нарушение целостности (изменение order_id)
- [ ] WSTG-BUSL-004: Обход 2FA
- [ ] WSTG-BUSL-005: Повышение привилегий через API
- [ ] WSTG-BUSL-006: Манипуляция количеством товара
- [ ] WSTG-BUSL-007: Нарушение процесса оформления заказа
- [ ] WSTG-BUSL-008: Подделка email-уведомлений
- [ ] WSTG-BUSL-009: Race condition при оплате
- [ ] WSTG-BUSL-010: Обработка исключений (неоплаченный заказ)

## 11. Client-Side
- [ ] WSTG-CLNT-001: DOM XSS
- [ ] WSTG-CLNT-002: JavaScript Injection
- [ ] WSTG-CLNT-003: WebSocket Testing
- [ ] WSTG-CLNT-004: Web Storage (localStorage, sessionStorage)
- [ ] WSTG-CLNT-005: Офлайн режим

## Результаты
| ID | Уязвимость | Серьезность | Статус | Пруф |
|----|------------|-------------|--------|------|
|    |            |             |        |      |

## Заключение
[Краткое резюме]
```

### Практика: заполнение чек-листа
Протестируйте демо-приложение (например, OWASP Juice Shop или DVWA) по чек-листу. Заполните таблицу результатов для 5 найденных уязвимостей.



## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.




## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты


## Задачи для самостоятельного выполнения

1. **Сравнение OWASP Top 10 и Testing Guide**: Сопоставьте OWASP Top 10 2021 с разделами OWASP Testing Guide. Какие тесты покрывают каждый пункт Top 10?

2. **Кастомизация чек-листа**: Адаптируйте OWASP чек-лист для тестирования REST API. Добавьте специфичные для API проверки (JWT, rate limiting, versioning, GraphQL).

3. **Автоматизация**: Напишите скрипт на Python, который генерирует OWASP чек-лист в формате Markdown на основе JSON-конфигурации.

4. **Тестирование**: Протестируйте учебное приложение (bWAPP, WebGoat) по методологии OWASP Testing Guide. Заполните чек-лист минимум на 20 пунктов.

5. **Report template**: Создайте шаблон отчета по результатам OWASP-тестирования, включающий разделы: Summary, Vulnerability Details (с CVSS), Remediation.

## Частые ошибки

1. **Поверхностное тестирование** — выполнение только автоматизированного сканирования без ручной проверки.
2. **Игнорирование Business Logic** — большинство уязвимостей в веб-приложениях находятся в логике, а не в коде.
3. **Неправильное использование чек-листа** — выполнение пунктов "для галочки" без понимания сути.
4. **Пропуск Client-Side тестов** — XSS и DOM-уязвимости часто упускаются.

## Вопросы на понимание

1. Сколько разделов в OWASP Testing Guide v4.2?
2. Что такое WSTG-INPV-006?
3. Почему важно тестировать Business Logic?
4. Какие инструменты используются для Information Gathering?
5. В чем разница между Input Validation и Authorization Testing?
