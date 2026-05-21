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
