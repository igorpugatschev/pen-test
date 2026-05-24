# Карта использования книг в Pen-Test Learning Program

Цель карты — связать текущий курс с предыдущим `SDET Python QA Automation Apprenticeship` и использовать доступные книги не как архив, а как опорные источники для практики Security-aware SDET.

## Доступные источники

| Источник | Где лежит | Роль в курсе |
|---|---|---|
| «Легкий способ выучить Python 3 еще глубже» | `docs/socraticode/learn-more-python-3-pages/` и `docs/socraticode/legkij-sposob-vyuchit-python-3-eshe-glubzhe.md` | Самостоятельная Python-практика, CLI, файлы, текстовая обработка, SQL-мышление |
| «Объектно-ориентированный Python, 4-е издание» | `docs/socraticode/object-oriented-python-4th-ed-pages/` | Классы, исключения, коллекции, тестируемый код, поддерживаемые helpers |
| «Паттерны разработки на Python» | `docs/socraticode/architecture-patterns-python-pages/` | Service Layer, Repository, Dependency Inversion, архитектура security automation |
| «PyCharm. Профессиональная работа на Python 2024» | `docs/socraticode/pycharm-professional-python-2024-pages/` | IDE workflow, debugger, HTTP Client, Git/VCS, DB tools, profiler, Markdown evidence |
| «Black Hat Python. Программирование для хакеров и пентестеров» | `docs/socraticode/black-hat-python-ru-pages/` | Lab-only источник идей для security automation, detection и defensive thinking |

## Правила использования Black Hat Python

`Black Hat Python` нельзя превращать в инструкции для выполнения атак по Slider AI. В продуктовой практике эта книга используется только так:

- понять, какие классы техник существуют;
- переписать идею в безопасный helper с allowlist/dry-run;
- реализовать detection/reporting вокруг риска;
- отработать потенциально опасную технику только в CTF/lab, где это явно разрешено;
- сформулировать boundaries, evidence и remediation.

## Карта по блокам

| Блок | Основные книги | Как применять |
|---|---|---|
| 01-08 Linux/workstation | PyCharm 2024, Learn More Python 3 | Настроить рабочую среду, terminal discipline, Git/Markdown evidence, локальные scripts |
| 09-16 networks | PyCharm 2024, Black Hat Python lab-only | Понимать сетевые примитивы, но использовать только безопасную диагностику и наблюдение |
| 17-28 OWASP | PyCharm 2024, Black Hat Python lab-only | Переводить web-риски в test cases, DevTools/HTTP evidence, no destructive payloads |
| 29-40 tools/reporting | PyCharm 2024, Patterns Python | Строить tool governance, triage false positives, превращать output в findings |
| 41-48 security automation | Learn More Python 3, OOP Python, Patterns Python, Black Hat Python lab-only | Писать безопасные helpers: allowlist, rate limit, pytest, Pydantic/JSON/Markdown output |
| 49-60 lab transfer | Black Hat Python lab-only, PyCharm 2024 | Переносить lab-навыки в продуктовый QA только через transfer matrix и scope boundaries |
| 61-72 ownership | PyCharm 2024, Patterns Python | Strategy, RoE, evidence, remediation, retest, security automation architecture |

## Минимальное ожидание для урока

Каждый урок должен отвечать на 3 вопроса:

1. Какая SDET-компетенция из предыдущего курса здесь используется?
2. Какой security risk или security process развивается?
3. Какой источник помогает углубить материал без подмены безопасной практики опасной техникой?


## Обязательное правило для правки уроков

Новый материал в уроках должен сначала искать опору в книгах из `docs/socraticode/`.
Если тема отсутствует или раскрыта недостаточно, допускается краткое внешнее дополнение, но оно должно быть помечено как `дополнительная справка`, а не как основной источник курса.

Для каждого урока используется формат:

- Основной источник:
- Что берем из источника:
- Как это превращается в SDET/Security QA навык:
- Что нельзя переносить на Slider AI без отдельного разрешения:

## Операционная карта переписывания блоков

Эта карта используется автором курса перед правкой каждого блока. Она не является списком обязательного чтения для студента. Студент получает самодостаточную лекцию в Markdown-файле урока, а книги остаются источниками автора и академическим следом.

### Block 01-08: Linux/workstation

Primary source ideas:

- рабочая среда как воспроизводимый инструмент инженера;
- terminal discipline: команда, аргументы, вывод, файл, рабочая директория;
- Markdown evidence и локальная организация проекта;
- различие macOS native и Linux/Kali без подмены одного другим.

Books used:

- `PyCharm. Профессиональная работа на Python 2024` — IDE, Git, Markdown, Python tooling, различия сред;
- `Легкий способ выучить Python 3 еще глубже` — маленькие упражнения, CLI, файлы, текстовый вывод;
- `Объектно-ориентированный Python` — аккуратная структура проекта и ответственность компонентов.

Course transformation:

- студент не ищет основы терминала в книгах;
- лекция объясняет shell, filesystem, stdout/stderr, права и evidence напрямую;
- Slider AI используется только для подготовки scope/evidence, без активных проверок.

### Block 09-16: Networks For Security QA

Primary source ideas:

- network model, addressing, ports, DNS, HTTP/TLS and observable behavior;
- how a symptom becomes reproducible QA evidence;
- safe distinction between diagnostics and active probing.

Books used:

- `PyCharm. Профессиональная работа на Python 2024` — рабочая станция, HTTP Client, воспроизводимые настройки;
- `Black Hat Python` — сетевое мышление только как defensive/lab-only источник;
- `Легкий способ выучить Python 3 еще глубже` — CLI-практика и текстовая обработка результатов.

Course transformation:

- лекция объясняет TCP/IP, DNS, HTTP and TLS без внешнего поиска;
- macOS native используется для базовой диагностики;
- Kali ARM64 VM и cloud lab используются только для углубления.

### Block 17-28: OWASP Web Security

Primary source ideas:

- уязвимость как ошибка модели доверия;
- request/response evidence;
- безопасное разделение lab payload и product-safe observation.

Books used:

- `PyCharm. Профессиональная работа на Python 2024` — HTTP Client, debugging, Git/Markdown reports;
- `Black Hat Python` — lab-only понимание offensive mechanics;
- `Паттерны разработки на Python` — границы системы, service boundaries, testability.

Course transformation:

- каждая уязвимость объясняется через модель, причину, безопасный пример и критерии evidence;
- payload-практика уходит в PortSwigger/THM/local lab;
- Slider AI получает только scope-safe checks and observations.

### Block 29-40: Tools And Reporting

Primary source ideas:

- tool governance;
- false-positive review;
- structured output;
- approval and stop conditions.

Books used:

- `PyCharm. Профессиональная работа на Python 2024` — Git, Markdown, IDE workflow, reports;
- `Паттерны разработки на Python` — управляемые boundaries and interfaces;
- `Black Hat Python` — lab-only предупреждение о рисках автоматизации.

Course transformation:

- инструмент объясняется перед запуском;
- aggressive modes are lab-only;
- output is converted into observation/finding only after triage.

### Block 41-48: Python Security Automation

Primary source ideas:

- CLI helper as maintainable code;
- exceptions, classes, service layer, dependency boundaries;
- allowlist, dry-run, timeout, tests and structured reports.

Books used:

- `Легкий способ выучить Python 3 еще глубже` — CLI scripts and file processing;
- `Объектно-ориентированный Python` — classes, exceptions, testable design;
- `Паттерны разработки на Python` — service layer and dependency inversion;
- `Black Hat Python` — lab-only ideas rewritten into defensive helpers.

Course transformation:

- scripts are safe tools, not exploit shortcuts;
- every helper has allowlist/dry-run/sanitized output;
- product checks use conservative SDET ownership rules.

### Block 49-60: Lab Transfer And Certification Bridge

Primary source ideas:

- legal lab practice;
- write-up discipline;
- transfer matrix from CTF to product QA;
- separation of exploitation skill and product responsibility.

Books used:

- `Black Hat Python` — lab-only mechanics;
- `PyCharm. Профессиональная работа на Python 2024` — reports, artifacts, Git;
- `Паттерны разработки на Python` — process boundaries and automation architecture.

Course transformation:

- TryHackMe, HackTheBox and PortSwigger never replace the lecture;
- lab work is converted into safe product test cases;
- Slider AI practice remains professional QA, not CTF behavior.

### Block 61-72: Security Ownership

Primary source ideas:

- strategy, RoE, evidence policy, triage, remediation, retest;
- security regression as SDET responsibility;
- final report as engineering artifact.

Books used:

- `PyCharm. Профессиональная работа на Python 2024` — project workflow, VCS, documentation;
- `Паттерны разработки на Python` — architecture and maintainable process;
- `Объектно-ориентированный Python` — maintainable automation structures.

Course transformation:

- standards are taught as process, not lists;
- final project requires scope, plan, evidence, findings, retest and regression checklist;
- uncertain actions are marked `requires approval`.
