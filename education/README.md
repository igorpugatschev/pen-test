# Pen-Test Learning Program

Учебные материалы для курса по безопасному тестированию на проникновение как продолжению `SDET Python QA Automation Apprenticeship`.

Цель курса — не просто научить отдельным приемам пентеста, а перевести SDET из роли инженера функционального качества в роль **Security-aware SDET / Product Security QA**: специалиста, который отвечает за качество и безопасность продукта, умеет планировать security-проверки, работать в согласованном scope, собирать evidence, автоматизировать безопасные проверки, оформлять findings и сопровождать remediation/retest.

Практический контур курса — тестовый стенд Slider AI `https://olddev.slider-ai.ru` в рамках `education/slider_ai_scope.md`. Все intrusive-техники остаются только в учебных лабораториях, CTF/сертификационных окружениях или выполняются после отдельного письменного разрешения.


## Что значит пройти курс полностью

Студент должен сдать:
- 6 block assessments;
- 1 Python security helper project;
- 1 final Slider AI Security QA assessment package;
- knowledge checks по всем блокам;
- evidence index без секретов;
- remediation/retest backlog.

Курс считается самодостаточным, если каждый урок является полноценной лекцией для самостоятельного обучения: студент получает достаточную теорию, модели, термины, безопасные примеры, разбор вывода, guided practice, Slider AI-практику, углубление, сдаваемый артефакт, rubric и self-check внутри самого Markdown-файла. Книги используются как база автора курса, но не заменяют лекцию и не превращают урок в список страниц для самостоятельного поиска.

## Структура

```
education/
├── lessons/           # Уроки по блокам (01-08, 09-16, 17-28, 29-40, 41-48, 49-60, 61-72)
├── security_process/  # Шаблоны процесса Security QA: strategy, RoE, test plan, evidence, findings, retest
├── tools/             # Вспомогательные скрипты проверки и исправления
├── lecture_requirements.md  # Канонический стандарт полноценных самодостаточных лекций
├── book_usage_map.md  # Карта использования 5 книг в блоках курса
└── pentest_learning_program.md  # Полная программа курса как SDET -> Security QA transition
```

## Требования к лекциям

Канонический стандарт качества уроков зафиксирован в `education/lecture_requirements.md`.

Коротко:
- урок не может быть списком тем или указателем на книги;
- вся теория, необходимая для практики текущего урока, должна быть внутри урока;
- `Reading pack` является академическим следом источников, а не заменой лекции;
- `Source-driven theory` объясняет, какие идеи из книг превращены в SDET/Security QA навык;
- раздел `Теория` является основной лекцией с моделями, терминами, примерами и разбором вывода;
- практика идет по лестнице: минимум -> Slider AI в scope -> углубление после нужной теории;
- валидатор заголовков не равен методической готовности.

## Связь с SDET-курсом

Предыдущий курс `SDET Python QA Automation Apprenticeship` дал базу: Python, pytest, Playwright, API-клиенты, Pydantic-модели, DB verification, Allure/CI, PyCharm, test strategy, test plan, evidence и сопровождение автотестового фреймворка.

Этот курс использует ту же инженерную дисциплину, но переносит ее в безопасность:
- test design превращается в abuse cases и security test cases;
- API/UI/DB evidence превращается в security evidence;
- bug report дополняется security finding, CVSS/QA severity и remediation plan;
- automation framework развивается в safe security automation helpers;
- release checklist дополняется security regression и retest.

## Основные источники

- «Легкий способ выучить Python 3 еще глубже» — CLI, файлы, текстовая обработка, SQL-мышление, самостоятельные Python-задачи.
- «Объектно-ориентированный Python, 4-е издание» — классы, исключения, коллекции, тестируемый код и поддерживаемые security helpers.
- «Паттерны разработки на Python» — service layer, repository, dependency inversion, архитектура безопасных инструментов.
- «PyCharm. Профессиональная работа на Python 2024» — IDE workflow, debugger, HTTP Client, Git/VCS, DB tools, inspections, profiler, Markdown evidence.
- «Black Hat Python. Программирование для хакеров и пентестеров» — источник идей для lab-only и defensive security automation; unsafe-темы изучаются через boundaries, detection и reporting.

## Блоки уроков

### 01-08: Linux основы (8 уроков)
- Урок 01: Введение в Linux и Kali Linux
- Урок 02: Терминал и основные команды
- Урок 03: Права доступа и файловая система
- Урок 04: Процессы и управление ими
- Урок 05: Сетевые настройки в Linux
- Урок 06: Поиск файлов и текста
- Урок 07: Bash-скрипты для пентестера
- Урок 08: Итоговое задание по Linux

### 09-16: Сетевые технологии (8 уроков)
- Урок 09: Модель OSI и TCP/IP
- Урок 10: Протоколы TCP/IP
- Урок 11: DNS - как это работает
- Урок 12: HTTP и HTTPS
- Урок 13: Wireshark - анализ трафика
- Урок 14: Маршрутизация и трассировка
- Урок 15: Фаерволы и правила фильтрации
- Урок 16: Практика: сетевой анализ

### 17-28: OWASP Top 10 (12 уроков + 5 доп.)
- Урок 17: Введение в OWASP Top 10
- Урок 17b: A04 - Insecure Design
- Урок 17c: A05 - Security Misconfiguration
- Урок 17d: A06 - Vulnerable and Outdated Components
- Урок 17e: A08 - Software and Data Integrity Failures
- Урок 17f: A09 - Security Logging and Monitoring Failures
- Урок 18: A03 - SQL Injection
- Урок 19: SQLMap - автоматизация SQLi
- Урок 20: A07 - Cross-Site Scripting (XSS)
- Урок 21: DOM-based XSS
- Урок 22: A08 - Cross-Site Request Forgery (CSRF)
- Урок 23: A07 - Broken Authentication
- Урок 24: A02 - Cryptographic Failures (Sensitive Data)
- Урок 25: A05 - XML External Entities (XXE)
- Урок 26: A10 - Server-Side Request Forgery (SSRF)
- Урок 27: Введение в Burp Suite
- Урок 28: Практика с Burp Suite

### 29-40: Инструменты пентеста (12 уроков)
- Урок 29: Nmap - основы сканирования
- Урок 30: Nmap NSE скрипты
- Урок 31: Amass - разведка поддоменов
- Урок 32: Subfinder и другие инструменты
- Урок 33: Dirsearch и FFuf
- Урок 34: Nuclei - автоматизация
- Урок 35: OWASP ZAP
- Урок 36: Hydra и Patator
- Урок 37: Searchsploit и Exploit-DB
- Урок 38: Shodan и Censys
- Урок 39: Практика с инструментами
- Урок 40: Создание отчетов

### 41-48: Security automation engineering (8 уроков)
- Урок 41: Безопасные сетевые helpers на Python
- Урок 42: HTTP inventory через requests/httpx
- Урок 43: PoC как контролируемый verification artifact
- Урок 44: Парсинг Nmap XML без запуска scan по продукту
- Урок 45: Subdomain discovery boundaries и passive inventory
- Урок 46: URL inventory вместо directory brute force по умолчанию
- Урок 47: CVE/version mapping с confidence и ручной проверкой
- Урок 48: Итоговый Security QA helper с allowlist, tests и report output

### 49-60: Практика на площадках (12 уроков)
- Урок 49: Введение в TryHackMe
- Урок 50: TryHackMe Jr. Penetration Tester
- Урок 51: HackTheBox - старт
- Урок 52: HackTheBox - easy машины
- Урок 53: HackTheBox - Active Directory
- Урок 54: PortSwigger Web Security Academy
- Урок 55: Linux Privilege Escalation
- Урок 56: Отчеты в практике
- Урок 57: OSINT практика
- Урок 58: WAF обход
- Урок 59: Полный пентест (симуляция)
- Урок 60: Подготовка к EJPT

### 61-72: Security ownership, методология и сертификация (12 уроков)
- Урок 61: PTES - стандарт пентеста
- Урок 62: OWASP Testing Guide
- Урок 63: Написание отчетов
- Урок 64: CVSS v3.1 scoring
- Урок 65: Коммерческие сканеры
- Урок 66: Qualys и Rapid7
- Урок 67: Подготовка к EJPT
- Урок 68: Экзамен EJPT
- Урок 69: Основы OSCP
- Урок 70: Атаки на Active Directory
- Урок 71: Post-Exploitation
- Урок 72: Финальный Security QA assessment Slider AI

## Сквозной процесс Security QA

Каждый урок должен оставлять не только технический результат, но и процессный след:
- `scope/RoE`: что разрешено и что запрещено;
- `test plan`: что проверяется, почему и какими stop conditions;
- `evidence`: sanitized доказательства без секретов;
- `finding/observation`: результат в профессиональном формате;
- `remediation/retest`: что исправить и как перепроверить;
- `automation appendix`: если проверка автоматизирована, код должен иметь allowlist, timeout, rate limit, тесты и понятный output.

## Проверка уроков

Используйте скрипты в папке `tools/`:
```bash
cd tools
bash check_lessons.sh        # Проверка структуры
python3 final_fix_all.py     # Исправление ошибок
```

## Рабочая среда: MacBook Air M2 (8GB)

MacBook используется как рабочая станция QA/пентестера, а не как единственная среда для всех инструментов. Каждый урок должен явно выбирать путь выполнения:
- **Основной путь новичка:** macOS native, Homebrew, браузер, DevTools, Burp/ZAP, `curl`, `nmap`, Python.
- **Углубление:** Kali Linux ARM64 VM в UTM/VMware Fusion/Parallels, если нужны Linux/Kali-специфичные инструменты, снапшоты или изоляция.
- **Cloud lab:** TryHackMe AttackBox, HackTheBox/Pwnbox, PortSwigger Academy и другие легальные стенды для тяжелых сценариев.

Правило установки:
- `brew`, официальный macOS installer или `pipx/pip3` — для macOS native.
- `apt` — только для явно помеченной Kali/Linux-среды.
- VirtualBox на Apple Silicon не использовать для x86/x64 guest OS; если VM нужна локально, выбирать ARM64-образы и лимит 3-4GB RAM.

## Полная программа

См. файл `pentest_learning_program.md` для детального описания всех уроков.
