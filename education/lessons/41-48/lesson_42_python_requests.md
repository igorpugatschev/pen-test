# Занятие 42: HTTP inventory client

## Учебная рамка

**Входные требования:** Завершен SDET Python QA Automation Apprenticeship или освоены pytest/API/UI/DB basics; студент умеет запускать Python из терминала и читать traceback.

**Результат занятия:** безопасный HTTP HEAD/GET helper с timeout, headers allowlist и sanitized output.

**Наследуемая SDET-компетенция:** security automation engineering: тестируемый Python-код, allowlist, rate limit, structured output и review.

**Security QA-компетенция:** создание безопасных security QA helpers с отказом от опасных действий по умолчанию.

**Связь с книгами:** «Легкий способ выучить Python 3 еще глубже» — CLI/файлы/текст; «Объектно-ориентированный Python» — классы и исключения; «Паттерны разработки на Python» — service boundaries; «Black Hat Python» — только lab-only идеи и defensive interpretation.

**Основной источник:** «Легкий способ выучить Python 3 еще глубже», «Объектно-ориентированный Python», «Паттерны разработки на Python», «PyCharm. Профессиональная работа на Python 2024».

**Дополнительные источники:** `Black Hat Python` только как источник lab-only идей, которые переводятся в defensive helpers.

**Что берем из источника:** CLI, exceptions, classes, service boundaries, tests, structured JSON/Markdown output, allowlist и masking.

**Как это превращается в SDET/Security QA навык:** собрать безопасный Security QA helper как продолжение SDET automation framework.

**Что нельзя переносить на Slider AI без отдельного разрешения:** helper не должен выполнять brute force, payload injection, wide scan или работу вне allowlist.


**Процессный артефакт:** `education/security_process/SECURITY_AUTOMATION_ARCHITECTURE.md`: helper, тесты, allowlist, output contract.

**Безопасная цель:** `127.0.0.1`, локальный тестовый HTTP-сервер, заранее подготовленный lab-файл или `https://olddev.slider-ai.ru` только в безопасном scope из `education/slider_ai_scope.md`.

**Среда выполнения:** macOS native, PyCharm/terminal, Python 3.12+, `.venv`, pytest. Kali/cloud lab используется только для lab-only техник, явно вынесенных в углубление.

**Обязательный путь новичка:** Реализовать минимальный безопасный helper, добавить отказ от небезопасного target/action и один pytest-тест этого отказа.

**Углубление:** Добавить Pydantic/typed output, Markdown/JSON report, CI-like команду, code review checklist и интеграцию с process template.

**Минимальная проверка успеха:** Helper запускается без traceback, опасное действие блокируется, output не содержит секретов, pytest-тесты проходят.

**Эталонный вывод:** Команда запуска, один sanitized JSON/Markdown фрагмент, результат pytest и короткое объяснение safety guard.

**Критерии сдачи:** Зачет: безопасный helper + тест отказа + artifact. Отлично: typed output, README, review checklist и automation appendix для отчета.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 42: HTTP inventory client`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/learn-more-python-3-pages/`
- `docs/socraticode/object-oriented-python-4th-ed-pages/`
- `docs/socraticode/architecture-patterns-python-pages/`
- `docs/socraticode/pycharm-professional-python-2024-pages/`

Конкретные страницы для этого блока: `learn-more-python-3-pages/page-001.md`-`page-120.md`; `object-oriented-python-4th-ed-pages/page-069.md`-`page-129.md`; `architecture-patterns-python-pages/page-038.md`-`page-129.md`.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот раздел не является заданием найти теорию в книгах. Книги использованы автором курса как системные источники для лекции `Занятие 42: HTTP inventory client`, а студент получает полное объяснение ниже.

Для этой темы опорная идея взята из источников: «Легкий способ выучить Python 3 еще глубже», «Объектно-ориентированный Python», «Паттерны разработки на Python», «Black Hat Python» как lab-only источник идей. Из них в урок перенесены не страницы как домашнее чтение, а инженерные принципы: безопасный helper: allowlist, dry-run, timeout, обработка ошибок, structured output, тестируемая архитектура и отчетность. Поэтому лекция строится вокруг вопроса: как SDET, уже умеющий работать с тестами, артефактами и воспроизводимостью, превращает тему `Занятие 42: HTTP inventory client` в безопасную Security QA-практику.

Книжный материал адаптирован в три слоя. Первый слой — модель: какие сущности участвуют, как они связаны и где появляется риск. Второй слой — рабочий навык: автоматизация проверок безопасности без потери контроля, unit/smoke tests, JSON/Markdown evidence, поддерживаемый код. Третий слой — границы применения: локальные targets, dry-run, allowlist; Slider AI только через явно разрешенные безопасные проверки. Если техника может повредить данным, создать нагрузку, извлечь секреты, перебрать учетные записи или выйти за scope, она не переносится на Slider AI и остается только в lab-only/cloud-lab формате.

Такой подход важен для повышения квалификации QA: цель не “запустить хакерский инструмент”, а научиться отвечать за безопасность продукта так же дисциплинированно, как за функциональное качество. В каждом упражнении студент должен видеть разрешенную цель, среду выполнения, ожидаемый результат, критерий остановки и sanitized evidence.

## Теория

### 1. Зачем SDET изучает эту тему

Тема `Занятие 42: HTTP inventory client` нужна не как отдельный набор команд, а как часть профессионального перехода от обычного QA/SDET к специалисту, который отвечает за качество и безопасность продукта. SDET уже привык проверять поведение системы, фиксировать воспроизводимые шаги, отделять факт от предположения и оформлять результат так, чтобы разработчик мог его повторить. В Security QA добавляется еще один слой: каждое действие должно быть разрешенным, ограниченным по scope и безопасным для данных, пользователей и инфраструктуры.

В этой лекции базовая задача состоит в том, чтобы понять модель `безопасный helper: allowlist, dry-run, timeout, обработка ошибок, structured output, тестируемая архитектура и отчетность` и научиться превращать ее в проверяемый артефакт. Артефактом может быть команда, скриншот DevTools, HTTP history, лог, Markdown-заметка, JSON-вывод helper-скрипта, checklist или черновик finding. Главное требование: другой инженер должен понять, что было проверено, где, с каким разрешением и почему результат имеет значение.

### 2. Базовая модель урока

Модель этой темы можно читать как цепочку `цель -> действие -> наблюдение -> интерпретация -> решение`. Цель должна быть разрешенной: локальный файл, localhost, учебный lab, cloud lab, PortSwigger Academy, TryHackMe, HackTheBox или `https://olddev.slider-ai.ru` в рамках `education/slider_ai_scope.md`. Действие должно быть минимальным: сначала наблюдение и ручная проверка, затем low-rate инструмент, затем lab-only углубление. Наблюдение должно быть фактическим: строка вывода, статус HTTP, заголовок, имя файла, код возврата, сообщение ошибки или запись в отчете.

Интерпретация не равна выводу инструмента. Инструмент может сказать `open`, `possible`, `vulnerable`, `interesting`, но SDET обязан проверить контекст. Например, открытый порт сам по себе не является уязвимостью; это observation. Ошибка валидации может быть нормальным поведением; это not applicable. Неожиданный доступ к чужим данным может быть finding, но только если evidence sanitized и проверка не нарушила scope.

### 3. Термины, которые нельзя пропускать

`Target` — разрешенная цель проверки. Для курса это обычно локальная среда, lab или `https://olddev.slider-ai.ru`.

`Scope` — границы разрешенных действий. Scope отвечает на вопрос “что можно проверять, какими методами и когда нужно остановиться”.

`Evidence` — доказательство результата. Хорошее evidence содержит среду выполнения, цель, действие, фактический результат, интерпретацию и sanitization note.

`Observation` — безопасное наблюдение, которое может быть полезно, но еще не доказывает уязвимость.

`Finding` — подтвержденная проблема с влиянием, воспроизводимыми шагами и рекомендацией по исправлению.

`Requires approval` — статус для действия, которое потенциально допустимо в профессиональном тестировании, но не разрешено текущим scope.

`Lab-only` — техника, которую можно изучать только в учебной лаборатории или CTF, а не на продуктовой среде.

### 4. Безопасная рабочая среда

MacBook Air M2 с 8GB RAM используется как рабочая станция QA/пентестера. Это не значит, что все инструменты должны выполняться локально. Базовый путь новичка: macOS native, Homebrew или официальный installer, браузер, DevTools, Burp/ZAP в безопасном режиме, `curl`, `dig`, Python и локальные файлы. Этот путь снижает когнитивную нагрузку: студент учится видеть результат, а не бороться с виртуализацией.

Kali Linux ARM64 VM нужна как углубление, когда инструмент Linux/Kali-специфичен, нужна изоляция, снапшоты или сертификационная практика. На 8GB RAM VM должна получать 3-4GB RAM и 2 CPU. x86/x64 VirtualBox VM не является базовым путем на Apple Silicon. Для тяжелых сценариев используются cloud lab: TryHackMe AttackBox, HackTheBox/Pwnbox, PortSwigger Academy или другие легальные стенды.

### 5. Как выполнять практику без нарушения scope

Перед практикой студент делает короткую проверку разрешения. Первый вопрос: “Моя цель точно разрешена?” Второй: “Мое действие минимально для результата?” Третий: “Может ли действие создать нагрузку, изменить данные, перебрать учетные записи или раскрыть секреты?” Если ответ “да” или “не уверен”, действие получает статус `requires approval` и не выполняется на Slider AI.

Для `https://olddev.slider-ai.ru` допустимы только безопасные Security QA-действия: наблюдение поведения UI, DevTools, заголовки, ручная проверка валидации без destructive payloads, проверка сообщений об ошибках, сбор sanitized evidence, оформление test case и report draft. Запрещены DoS/load, brute force, destructive payloads, массовые wordlists, изменение чужих данных, попытки извлечения secrets и выход за scope.

### 6. Как читать результат

Результат читается не целиком, а по контрольным строкам. В командном выводе ищем версию инструмента, target, статус выполнения, ключевые строки результата и ошибки. В HTTP evidence смотрим method, URL path, status code, headers, cookies без секретных значений, redirect, cache/TLS признаки и response behavior. В браузере смотрим видимое поведение, сетевые запросы, сообщения в консоли и отсутствие лишних персональных данных в evidence.

Хорошая интерпретация отвечает на три вопроса. Что произошло фактически? Почему это важно для качества или безопасности? Какой следующий безопасный шаг? Например: “Получен `HTTP/2 200` от olddev, это подтверждает доступность стенда, но не является finding. Следующий шаг — зафиксировать baseline headers и не выполнять активные проверки без approval”.

### 7. Как оформлять evidence

Evidence должно быть коротким, проверяемым и безопасным. Минимальная форма:

```markdown
Environment: macOS native, Apple Silicon
Target: https://olddev.slider-ai.ru
Scope status: allowed observation
Action: checked response headers with curl -I
Observed result: HTTP status and selected sanitized headers captured
Interpretation: baseline observation, no vulnerability confirmed
Risk status: observation
Sanitization notes: cookies, tokens and personal data are not stored
```

Если результат получен в lab, target указывается как lab target, а не Slider AI. Если действие требовало бы intrusive-проверки на продуктовой среде, evidence фиксирует не выполнение атаки, а решение: `requires approval`, обоснование и безопасный lab-only follow-up.

### 8. Типичные ошибки новичка

Первая ошибка — запускать команду ради команды. В Security QA команда не имеет смысла без цели, scope и критерия сдачи.

Вторая ошибка — считать любой вывод инструмента подтвержденной уязвимостью. Большая часть вывода сначала является observation и требует проверки контекста.

Третья ошибка — смешивать macOS и Kali/Linux команды. Если команда использует `apt`, `ip addr`, Linux paths или root-only поведение, урок должен явно сказать, что это Kali/Linux или cloud lab.

Четвертая ошибка — сохранять слишком много данных. Evidence должно быть sanitized: без cookies, JWT, паролей, приватных ключей, персональных данных и чужих секретов.

Пятая ошибка — переносить lab-техники на Slider AI. То, что разрешено в CTF, не становится автоматически разрешенным на тестовом стенде продукта.

### 9. Связь с предыдущими и следующими уроками

Эта тема опирается на уже изученные SDET-навыки: аккуратная работа с файлами, повторяемые команды, понимание входных требований, фиксация ожидаемого и фактического результата. В следующих уроках тот же принцип будет расширяться: из отдельных действий получится test plan, из наблюдений — triage, из повторяемых шагов — regression checklist, из helper-скриптов — поддерживаемая security automation.

Поэтому в текущем уроке важно не только выполнить практику, но и объяснить ее. Студент должен уметь сказать: “Я выбрал такую цель, потому что она разрешена; я выбрал такой режим, потому что он минимален; я получил такой результат; это observation/finding/not applicable; следующий шаг безопасен или требует approval”.

### 10. Минимальная профессиональная планка

Лекция считается освоенной, когда студент может без внешнего поиска объяснить модель темы, выполнить обязательный безопасный путь, получить эталонный вывод, интерпретировать его и оформить sanitized evidence. Для SDET это и есть переход от “я попробовал инструмент” к “я провел контролируемую Security QA-проверку”.

Для темы `Занятие 42: HTTP inventory client` минимальная планка такая: студент понимает безопасный helper: allowlist, dry-run, timeout, обработка ошибок, structured output, тестируемая архитектура и отчетность, выполняет безопасную практику в среде `локальные targets, dry-run, allowlist; Slider AI только через явно разрешенные безопасные проверки`, объясняет результат через автоматизация проверок безопасности без потери контроля, unit/smoke tests, JSON/Markdown evidence, поддерживаемый код и не выходит за ограничения Slider AI. Все, что требует более агрессивной техники, переносится в углубление после изучения следующих уроков или оформляется как `requires approval`.

### 11. Контроль понимания перед практикой

Перед переходом к заданиям студент должен остановиться и проговорить тему как инженерную процедуру. Нужно назвать разрешенную цель, среду выполнения, минимальное действие, ожидаемый безопасный результат и критерий остановки. Если хотя бы один пункт неясен, практика не начинается: сначала уточняется scope или выбирается локальная лабораторная цель. Такой контроль снижает риск случайно выполнить активную проверку там, где требовалось только наблюдение.

Второй контрольный вопрос: какие данные попадут в evidence? В отчет нельзя переносить cookies, токены, персональные данные, приватные ключи, полные ответы с секретами и любые сведения, которые не нужны для доказательства результата. Хороший SDET собирает ровно столько фактов, сколько нужно для воспроизведения и принятия решения.


### 12. Предметная часть урока

Для темы `Занятие 42: HTTP inventory client` предметная основа — путь данных от клиента к серверу. IP отвечает за адресацию, TCP/UDP — за транспорт, DNS — за превращение имени в адрес, HTTP — за прикладной запрос, TLS — за защищенный канал, routing — за выбор пути, firewall — за разрешение или блокировку трафика. Эти уровни нельзя смешивать: ошибка DNS не равна ошибке HTTP, а `403` от приложения не равен сетевой недоступности.

Безопасная диагностика начинается с наблюдения. `dig` показывает DNS-ответ, `curl -I` показывает HTTP status и headers, браузерные DevTools показывают request/response без извлечения секретов, `traceroute` помогает увидеть путь до цели, но не доказывает уязвимость. Wireshark используется сначала на локальном или lab-трафике; перехват чужого трафика и анализ данных без разрешения запрещены.

Для Slider AI допустима только легкая проверка доступности и поведения в scope: статус ответа, redirect, базовые headers, TLS-наблюдения, DevTools waterfall. Любая активная сетевая проверка, массовое сканирование, нагрузка или попытка обойти защиту оформляется как `requires approval` или переносится в cloud lab.


## Guided practice

1. Выделите один инкремент helper: allowlist, client, parser, mapper, report или test.
2. Сначала опишите safety rule и ожидаемый отказ небезопасного действия.
3. Реализуйте минимальную проверку с dry-run, timeout/rate limit и sanitized output.
4. Запустите pytest или self-check и приложите результат как automation evidence.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

```python
from urllib.parse import urlparse
import requests

ALLOWED_HOSTS = {"olddev.slider-ai.ru"}
SAFE_HEADERS = {"content-type", "server", "location", "strict-transport-security", "x-frame-options"}


def ensure_allowed_url(url: str) -> None:
    host = urlparse(url).hostname
    if host not in ALLOWED_HOSTS:
        raise ValueError(f"Target is not allowed: {host}")


def collect_http_inventory(url: str) -> dict:
    ensure_allowed_url(url)
    response = requests.head(url, timeout=5, allow_redirects=False, headers={"User-Agent": "SliderAI-SecurityQA-Learning"})
    headers = {k.lower(): v for k, v in response.headers.items() if k.lower() in SAFE_HEADERS}
    return {"url": url, "status_code": response.status_code, "headers": headers, "secrets_masked": True}
```


### Минимальная структура сдачи

```text
security_qa_helper/
├── safeguards/
├── reports/
├── tests/
└── README.md
```

### Команды проверки

```bash
python -m pytest tests/
python -m security_qa_helper --help
```

## Примеры вывода

Минимальный эталонный артефакт для сдачи по теме `Занятие 42: HTTP inventory client`:

```markdown
Environment: macOS native, Apple Silicon
Target: https://olddev.slider-ai.ru
Scope status: allowed observation within education/slider_ai_scope.md
Action: safe manual or low-impact check from this lesson
Evidence:
  - Command or browser path is recorded.
  - Output contains only sanitized technical lines.
  - Cookies, tokens, passwords and personal data are not stored.
Observed result: baseline behavior captured without destructive action
Interpretation: observation; no vulnerability is confirmed without additional proof
Next step: document result, request approval for intrusive follow-up, or repeat in lab-only environment
```

Пример локального вывода для обязательного безопасного пути:

```text
Environment: macOS native
Target: local workspace or explicitly allowed olddev observation
Result status: observation
Evidence saved: evidence/current_lesson/notes.md
Sanitization: secrets and personal data excluded
```

Такой вывод считается эталонным не потому, что строки всегда будут идентичными, а потому что в нем есть все обязательные элементы профессионального evidence: среда, разрешенная цель, действие, наблюдение, интерпретация, sanitization и следующий безопасный шаг.

## Адаптация под macOS (M2, 8GB)

- Используйте `.venv` и PyCharm interpreter из SDET-курса.
- Устанавливайте зависимости через `python -m pip install ...` внутри venv.
- Не запускайте тяжелые scan/wordlist процессы локально без необходимости.
- Для lab-only техник используйте cloud lab или легкую ARM64 VM.

## Частые ошибки

1. Писать script, который по умолчанию атакует любой target.
2. Не тестировать safety guard.
3. Сохранять cookies/tokens в output.
4. Называть candidate finding подтвержденной уязвимостью.
5. Подменять security process “интересной техникой”.

## Вопросы на понимание

1. Какой SDET-навык переносится в этот helper?
2. Какой unsafe action должен быть заблокирован тестом?
3. Почему output инструмента не равен finding?
4. Какие поля нужны в sanitized evidence?
5. Как этот helper будет использоваться в retest?

## Задачи для самостоятельного выполнения

1. Добавьте pytest-тест на отказ от target вне allowlist.
2. Добавьте README-раздел `Scope and stop conditions`.
3. Сохраните output в Markdown или JSON.
4. Проведите self-review по `TOOLING_POLICY.md`.
5. Опишите, как helper попадет в финальный отчет как automation appendix.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** HTTP inventory

### Минимум

Покажите safety guard: helper должен отказаться от действия, если target/action не входит в безопасный scope.

### Практика Slider AI

Сделайте один `HEAD` к `https://olddev.slider-ai.ru`, сохраните только status/headers без cookies и токенов.

### Углубление после изучения следующих уроков

Добавьте результат в `education/security_process/SECURITY_AUTOMATION_ARCHITECTURE.md` или в свой локальный automation appendix: что проверяется, какие ограничения стоят, какой output попадает в отчет.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `Safe Security QA Helper`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
