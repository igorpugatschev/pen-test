# Занятие 47: CVE/version mapper

## Учебная рамка

**Входные требования:** Завершен SDET Python QA Automation Apprenticeship или освоены pytest/API/UI/DB basics; студент умеет запускать Python из терминала и читать traceback.

**Результат занятия:** CVE-кандидаты с confidence, source и ручной проверкой.

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 47: CVE/version mapper`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: CLI, exceptions, classes, service boundaries, tests, structured JSON/Markdown output, allowlist и masking. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: helper не должен выполнять brute force, payload injection, wide scan или работу вне allowlist. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

## Теория

CVE automation должна помогать triage, а не создавать ложные findings. Версия компонента, найденная в UI/header/asset, становится candidate только с источником, confidence и ручной проверкой применимости.

Security automation в этом курсе наследует SDET-подход:

1. Сначала определяется риск и scope.
2. Затем пишется минимальный helper с безопасными дефолтами.
3. Опасное поведение блокируется тестами.
4. Output становится evidence, а не “сырым логом”.
5. Tool output не является finding без ручной валидации.

## Guided practice

1. Выделите один инкремент helper: allowlist, client, parser, mapper, report или test.
2. Сначала опишите safety rule и ожидаемый отказ небезопасного действия.
3. Реализуйте минимальную проверку с dry-run, timeout/rate limit и sanitized output.
4. Запустите pytest или self-check и приложите результат как automation evidence.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

```python
def make_cve_candidate(component: str, version: str, cve_id: str, source: str) -> dict:
    return {
        "component": component,
        "version": version,
        "cve_id": cve_id,
        "source": source,
        "confidence": "candidate",
        "finding_status": "needs manual validation"
    }
```

Минимальный output не должен утверждать уязвимость без проверки affected configuration.


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

```text
$ pytest tests/test_safeguards.py
1 passed in 0.05s

$ python -m security_qa_helper --target https://olddev.slider-ai.ru --dry-run
{"target":"https://olddev.slider-ai.ru","dry_run":true,"secrets_masked":true,"status":"observation"}
```

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

**Уровень прогрессии:** CVE mapping

### Минимум

Покажите safety guard: helper должен отказаться от действия, если target/action не входит в безопасный scope.

### Практика Slider AI

Составьте таблицу `component/version/source/CVE candidate/confidence`; finding появляется только после ручной валидации.

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
