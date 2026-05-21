# Занятие 44: Nmap XML parser

## Учебная рамка

**Входные требования:** Завершен SDET Python QA Automation Apprenticeship или освоены pytest/API/UI/DB basics; студент умеет запускать Python из терминала и читать traceback.

**Результат занятия:** парсер готового lab XML без запуска scan по продукту.

**Наследуемая SDET-компетенция:** security automation engineering: тестируемый Python-код, allowlist, rate limit, structured output и review.

**Security QA-компетенция:** создание безопасных security QA helpers с отказом от опасных действий по умолчанию.

**Связь с книгами:** «Легкий способ выучить Python 3 еще глубже» — CLI/файлы/текст; «Объектно-ориентированный Python» — классы и исключения; «Паттерны разработки на Python» — service boundaries; «Black Hat Python» — только lab-only идеи и defensive interpretation.

**Процессный артефакт:** `education/security_process/SECURITY_AUTOMATION_ARCHITECTURE.md`: helper, тесты, allowlist, output contract.

**Безопасная цель:** `127.0.0.1`, локальный тестовый HTTP-сервер, заранее подготовленный lab-файл или `https://olddev.slider-ai.ru` только в безопасном scope из `education/slider_ai_scope.md`.

**Среда выполнения:** macOS native, PyCharm/terminal, Python 3.12+, `.venv`, pytest. Kali/cloud lab используется только для lab-only техник, явно вынесенных в углубление.

**Обязательный путь новичка:** Реализовать минимальный безопасный helper, добавить отказ от небезопасного target/action и один pytest-тест этого отказа.

**Углубление:** Добавить Pydantic/typed output, Markdown/JSON report, CI-like команду, code review checklist и интеграцию с process template.

**Минимальная проверка успеха:** Helper запускается без traceback, опасное действие блокируется, output не содержит секретов, pytest-тесты проходят.

**Эталонный вывод:** Команда запуска, один sanitized JSON/Markdown фрагмент, результат pytest и короткое объяснение safety guard.

**Критерии сдачи:** Зачет: безопасный helper + тест отказа + artifact. Отлично: typed output, README, review checklist и automation appendix для отчета.

## Теория

SDET переносит навык обработки structured output: Nmap XML из лаборатории парсится как входной артефакт, а не генерируется широким scan по продукту. Код должен отличать “обнаруженный сервис” от “подтвержденной уязвимости”.

Security automation в этом курсе наследует SDET-подход:

1. Сначала определяется риск и scope.
2. Затем пишется минимальный helper с безопасными дефолтами.
3. Опасное поведение блокируется тестами.
4. Output становится evidence, а не “сырым логом”.
5. Tool output не является finding без ручной валидации.

## Практическое занятие

```python
import xml.etree.ElementTree as ET


def parse_nmap_xml(path: str) -> list[dict]:
    root = ET.parse(path).getroot()
    rows = []
    for host in root.findall("host"):
        address = host.find("address").attrib.get("addr", "unknown")
        for port in host.findall(".//port"):
            service = port.find("service")
            rows.append({
                "host": address,
                "port": int(port.attrib["portid"]),
                "protocol": port.attrib.get("protocol"),
                "service": service.attrib.get("name") if service is not None else "unknown",
                "finding_status": "observation"
            })
    return rows
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

**Уровень прогрессии:** Parsing nmap safely

### Минимум

Покажите safety guard: helper должен отказаться от действия, если target/action не входит в безопасный scope.

### Практика Slider AI

Используйте учебный XML из lab; по Slider AI парсите только заранее согласованный single-port вывод, если он уже получен законно.

### Углубление после изучения следующих уроков

Добавьте результат в `education/security_process/SECURITY_AUTOMATION_ARCHITECTURE.md` или в свой локальный automation appendix: что проверяется, какие ограничения стоят, какой output попадает в отчет.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.
