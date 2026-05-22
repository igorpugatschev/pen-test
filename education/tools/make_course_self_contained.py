#!/usr/bin/env python3
"""Bring the Markdown course to the self-contained source-driven model."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EDU = ROOT / "education"
LESSONS = EDU / "lessons"


GROUPS = {
    "01-08": {
        "source": "«PyCharm. Профессиональная работа на Python 2024» и «Легкий способ выучить Python 3 еще глубже».",
        "extra": "«Объектно-ориентированный Python» для аккуратной структуры локальных helpers.",
        "take": "terminal discipline, работа с файлами, Markdown evidence, локальная организация проекта, базовые CLI-навыки.",
        "apply": "превратить рабочую станцию QA в управляемую среду для безопасного сбора артефактов.",
        "boundary": "не выполнять активные проверки продукта; только подготовка среды и локальные артефакты.",
        "guided": [
            "Создайте или проверьте рабочую папку `~/security-qa-workspace` и отдельную заметку урока.",
            "Выполните команды урока на локальной машине или учебном lab-target, не затрагивая production.",
            "Сохраните минимальный вывод команды в evidence-файл без секретов и персональных данных.",
            "Добавьте 3-5 предложений: что проверено, что означает результат и как это пригодится Security QA.",
        ],
        "assessment": "Security QA workstation readiness",
    },
    "09-16": {
        "source": "«PyCharm. Профессиональная работа на Python 2024»; `Black Hat Python` только как lab-only контекст сетевых примитивов.",
        "extra": "«Легкий способ выучить Python 3 еще глубже» для работы с текстовыми выводами команд.",
        "take": "наблюдение DNS/HTTP/TLS, работа с сетевыми симптомами, сохранение воспроизводимых evidence.",
        "apply": "перевести сетевую диагностику в безопасные QA-наблюдения и ограничения тестирования.",
        "boundary": "не выполнять перебор портов и широкое сканирование Slider AI до согласованного scope.",
        "guided": [
            "Определите, какая часть темы относится к локальной сети, DNS, TCP/TLS или HTTP.",
            "Выполните одну безопасную диагностическую команду или наблюдение через браузер/DevTools.",
            "Сравните результат с ожидаемым поведением и запишите limitation, если данных недостаточно.",
            "Сохраните sanitized evidence и отметьте, не требует ли следующая проверка отдельного approval.",
        ],
        "assessment": "Safe network observation package",
    },
    "17-28": {
        "source": "«PyCharm. Профессиональная работа на Python 2024» и `Black Hat Python` только для lab-only/defensive interpretation.",
        "extra": "«Легкий способ выучить Python 3 еще глубже» для обработки запросов, текстов и простых проверочных данных.",
        "take": "разделение lab payload и product-safe marker, HTTP evidence, перевод риска OWASP в security test case.",
        "apply": "проектировать безопасные проверки Slider AI через OWASP/WSTG без destructive payloads.",
        "boundary": "учебные payloads выполнять только в DVWA/WebGoat/PortSwigger; на Slider AI использовать безопасные маркеры и passive evidence.",
        "guided": [
            "Сформулируйте риск урока как abuse case и как проверяемое ожидание защиты.",
            "Отработайте опасную технику только в lab, если урок этого требует.",
            "Для Slider AI выполните safe-marker или passive observation без извлечения данных и без destructive payload.",
            "Классифицируйте результат: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.",
        ],
        "assessment": "OWASP Test Design for Slider AI",
    },
    "29-40": {
        "source": "«PyCharm. Профессиональная работа на Python 2024» и «Паттерны разработки на Python».",
        "extra": "`Black Hat Python` только для понимания lab-only техник и defensive boundaries.",
        "take": "tool governance, false-positive review, structured output, границы ручного/passive/low-rate режима.",
        "apply": "превратить инструменты в управляемый QA-процесс с approval, stop conditions и evidence policy.",
        "boundary": "не запускать aggressive scan, brute force, wordlists или intrusive templates по Slider AI без отдельного письменного разрешения.",
        "guided": [
            "Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.",
            "Заполните tool approval card до запуска любой инструментальной проверки.",
            "Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.",
            "Проведите false-positive review и приложите только sanitized output.",
        ],
        "assessment": "Tool Governance Report",
    },
    "41-48": {
        "source": "«Легкий способ выучить Python 3 еще глубже», «Объектно-ориентированный Python», «Паттерны разработки на Python», «PyCharm. Профессиональная работа на Python 2024».",
        "extra": "`Black Hat Python` только как источник lab-only идей, которые переводятся в defensive helpers.",
        "take": "CLI, exceptions, classes, service boundaries, tests, structured JSON/Markdown output, allowlist и masking.",
        "apply": "собрать безопасный Security QA helper как продолжение SDET automation framework.",
        "boundary": "helper не должен выполнять brute force, payload injection, wide scan или работу вне allowlist.",
        "guided": [
            "Выделите один инкремент helper: allowlist, client, parser, mapper, report или test.",
            "Сначала опишите safety rule и ожидаемый отказ небезопасного действия.",
            "Реализуйте минимальную проверку с dry-run, timeout/rate limit и sanitized output.",
            "Запустите pytest или self-check и приложите результат как automation evidence.",
        ],
        "assessment": "Safe Security QA Helper",
    },
    "49-60": {
        "source": "`Black Hat Python` только lab-only, «PyCharm. Профессиональная работа на Python 2024» для write-ups и evidence discipline.",
        "extra": "«Паттерны разработки на Python» для переноса lab-навыков в поддерживаемые process artifacts.",
        "take": "lab-to-product transfer, structured notes, boundaries, write-up discipline, отделение exploitation от product QA.",
        "apply": "переносить из THM/HTB/PortSwigger только безопасные QA-аналогии и артефакты.",
        "boundary": "не переносить exploitation, privesc, bypass и aggressive enumeration на Slider AI без расширенного scope.",
        "guided": [
            "После lab выпишите навык, который был отработан, и его безопасный QA-аналог.",
            "Укажите, какие действия остаются только в lab и почему.",
            "Сделайте одну безопасную Slider AI-проверку или оформите `not applicable`/`requires approval`.",
            "Добавьте transfer card в матрицу подготовки к финальному assessment.",
        ],
        "assessment": "Lab-to-Product Transfer",
    },
    "61-72": {
        "source": "«PyCharm. Профессиональная работа на Python 2024» и «Паттерны разработки на Python».",
        "extra": "Все книги курса как справочник для финального Security QA assessment и automation appendix.",
        "take": "strategy, RoE, evidence policy, triage, remediation, retest, security regression и ownership.",
        "apply": "собрать полный безопасный assessment package для Slider AI olddev.",
        "boundary": "финальный проект остается в рамках `education/slider_ai_scope.md`; любые intrusive checks требуют отдельного approval.",
        "guided": [
            "Выберите финальный артефакт урока: RoE, checklist, finding, score, backlog, retest или appendix.",
            "Заполните шаблон процесса на безопасном Slider AI-примере без секретов.",
            "Свяжите результат с продуктовым риском, owner action и проверкой исправления.",
            "Добавьте артефакт в итоговый assessment package и отметьте limitations.",
        ],
        "assessment": "Final Security QA Assessment",
    },
}


def lesson_group(path: Path) -> str:
    return path.parent.name


def ensure_after(text: str, marker: str, addition: str) -> str:
    if addition.strip() in text:
        return text
    idx = text.find(marker)
    if idx == -1:
        return text
    end = text.find("\n", idx)
    if end == -1:
        end = len(text)
    return text[: end + 1] + addition + text[end + 1 :]


def ensure_before_section(text: str, section: str, block: str) -> str:
    if block.splitlines()[0] in text:
        return text
    idx = text.find(section)
    if idx == -1:
        return text + "\n\n" + block
    return text[:idx].rstrip() + "\n\n" + block.rstrip() + "\n\n" + text[idx:].lstrip()


def append_if_missing(text: str, heading: str, block: str) -> str:
    if heading in text:
        return text
    return text.rstrip() + "\n\n" + block.rstrip() + "\n"


def source_block(meta: dict[str, object]) -> str:
    return (
        f"**Основной источник:** {meta['source']}\n\n"
        f"**Дополнительные источники:** {meta['extra']}\n\n"
        f"**Что берем из источника:** {meta['take']}\n\n"
        f"**Как это превращается в SDET/Security QA навык:** {meta['apply']}\n\n"
        f"**Что нельзя переносить на Slider AI без отдельного разрешения:** {meta['boundary']}\n\n"
    )


def source_theory(meta: dict[str, object]) -> str:
    return f"""## Source-driven theory

Этот урок опирается на книжные источники курса как на базу автора лекции, а не как на задание студенту самостоятельно собрать теорию. Из источников берется практическая дисциплина: {meta['take']} Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке превращается в полноценную лекцию в трех шагах:

1. Объяснить модель и термины внутри урока, без внешнего поиска.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: {meta['boundary']} Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.
"""


def guided_practice(meta: dict[str, object]) -> str:
    steps = "\n".join(f"{i}. {step}" for i, step in enumerate(meta["guided"], start=1))
    return f"""## Guided practice

{steps}

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.
"""


def rubric(meta: dict[str, object]) -> str:
    return f"""## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `{meta['assessment']}`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
"""


def reading_pack(path: Path, meta: dict[str, object]) -> str:
    title = path.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
    group = lesson_group(path)
    book_paths = {
        "01-08": [
            "`docs/socraticode/pycharm-professional-python-2024-pages/`",
            "`docs/socraticode/learn-more-python-3-pages/`",
        ],
        "09-16": [
            "`docs/socraticode/pycharm-professional-python-2024-pages/`",
            "`docs/socraticode/black-hat-python-ru-pages/` только lab-only/defensive",
        ],
        "17-28": [
            "`docs/socraticode/pycharm-professional-python-2024-pages/`",
            "`docs/socraticode/black-hat-python-ru-pages/` только lab-only/defensive",
        ],
        "29-40": [
            "`docs/socraticode/pycharm-professional-python-2024-pages/`",
            "`docs/socraticode/architecture-patterns-python-pages/`",
        ],
        "41-48": [
            "`docs/socraticode/learn-more-python-3-pages/`",
            "`docs/socraticode/object-oriented-python-4th-ed-pages/`",
            "`docs/socraticode/architecture-patterns-python-pages/`",
            "`docs/socraticode/pycharm-professional-python-2024-pages/`",
        ],
        "49-60": [
            "`docs/socraticode/black-hat-python-ru-pages/` только lab-only/defensive",
            "`docs/socraticode/pycharm-professional-python-2024-pages/`",
        ],
        "61-72": [
            "`docs/socraticode/pycharm-professional-python-2024-pages/`",
            "`docs/socraticode/architecture-patterns-python-pages/`",
        ],
    }[group]
    paths = "\n".join(f"- {item}" for item in book_paths)
    return f"""## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `{title}`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

{paths}

Что обязана делать лекция на основе этих книг:

1. Объяснить термины и команды, которые прямо поддерживают тему урока.
2. Дать инженерный принцип, который переносится из SDET в Security QA.
3. Показать ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Превратить пример в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.
"""


def update_lesson(path: Path) -> None:
    meta = GROUPS[lesson_group(path)]
    text = path.read_text(encoding="utf-8")
    text = ensure_after(text, "**Связь с книгами:**", "\n" + source_block(meta))
    text = ensure_before_section(text, "## Source-driven theory", reading_pack(path, meta))
    text = ensure_before_section(text, "## Теория", source_theory(meta))
    text = ensure_before_section(text, "## Практическое занятие", guided_practice(meta))
    text = append_if_missing(text, "## Rubric", rubric(meta))
    path.write_text(text, encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def create_course_docs() -> None:
    lesson_rows = []
    for lesson in sorted(LESSONS.glob("*/*.md")):
        group = lesson_group(lesson)
        meta = GROUPS[group]
        title = lesson.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
        rel = lesson.relative_to(ROOT)
        lesson_rows.append(
            f"| `{rel}` | {title} | {meta['source']} | {meta['extra']} | {meta['take']} | {meta['apply']} | {meta['boundary']} |"
        )
    lesson_table = "\n".join(lesson_rows)
    write(
        EDU / "book_source_matrix.md",
        f"""# Поурочная карта источников

Цель: сделать курс source-driven. Каждый урок должен ссылаться на книги из `docs/socraticode/` и явно показывать, какая часть теории берется из какого источника.

## Правило покрытия

Для каждого урока:
- минимум 1 основной книжный источник;
- минимум 1 практическая связь с предыдущим SDET-курсом;
- для Python-уроков 41-48 обязательно использовать Python/OOP/Patterns/PyCharm;
- для lab-only/offensive-тем обязательно использовать `Black Hat Python` только через безопасную интерпретацию: boundaries, detection, defensive automation, lab-only practice.

## Матрица по блокам

| Уроки | Главный источник | Дополнительные источники | Что взять из книг | Как применить в уроке | Slider AI boundary |
|---|---|---|---|---|---|
| 01-08 | PyCharm 2024, Learn More Python 3 | OOP Python | terminal workflow, files, CLI notes, debugging habit | workstation setup, notes, evidence folders | no product scanning |
| 09-16 | PyCharm 2024 | Black Hat Python lab-only | network basics, observing traffic, safe diagnostics | DNS/HTTP/TLS observation | no port sweep until lesson 29 and only scoped |
| 17-28 | PyCharm 2024, Black Hat Python lab-only | Learn More Python 3 | web request evidence, payload boundaries, lab practice separation | OWASP test design and safe markers | no destructive payloads |
| 29-40 | PyCharm 2024, Patterns Python | Black Hat Python lab-only | tool governance, false-positive review, reporting discipline | manual/passive/low-rate tool workflow | no aggressive scan without approval |
| 41-48 | Learn More Python 3, OOP Python, Patterns Python, PyCharm 2024 | Black Hat Python lab-only | CLI, classes, errors, service layer, safe helpers | tested security automation | allowlist, timeout, rate limit |
| 49-60 | Black Hat Python lab-only, PyCharm 2024 | Patterns Python | lab-to-product transfer, note discipline, reporting | CTF lessons become QA checks | do not copy attack steps to Slider AI |
| 61-72 | PyCharm 2024, Patterns Python | all books as reference | strategy, evidence, triage, remediation, automation appendix | product security ownership | full safe assessment only |

## Конкретные книжные якоря

Эти диапазоны страниц используются как локальные source anchors. Если текст страницы извлечен неполно, студент все равно использует страницу как указатель на место в PDF-книге и делает конспект по оригинальному PDF.

| Блок | Основные страницы/главы в локальных книгах | Что проверяет преподаватель |
|---|---|---|
| 01-08 | `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md` (Git/VCS), `page-577.md`-`page-590.md` (remote/Linux workflow), `learn-more-python-3-pages/page-001.md`-`page-060.md` (самостоятельная Python/CLI дисциплина) | Есть рабочая папка, Git/Markdown evidence, локальные CLI-заметки |
| 09-16 | `pycharm-professional-python-2024-pages/page-338.md`-`page-369.md` (HTTP/web workflow), `black-hat-python-ru-pages/page-060.md`-`page-080.md` (сетевые примитивы только lab-only) | Студент объясняет DNS/HTTP/TLS наблюдение без активного сканирования |
| 17-28 | `pycharm-professional-python-2024-pages/page-338.md`-`page-369.md` (HTTP request/response), `black-hat-python-ru-pages/page-120.md`-`page-140.md` (Burp/fuzzing только lab-only) | Payload отделен от product-safe marker, evidence sanitized |
| 29-40 | `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md` (Git/evidence), `architecture-patterns-python-pages/page-038.md`-`page-069.md` (тестируемые boundaries/repository thinking) | Tool approval card, false-positive review, safe output |
| 41-48 | `learn-more-python-3-pages/page-001.md`-`page-120.md`, `object-oriented-python-4th-ed-pages/page-069.md`-`page-129.md`, `architecture-patterns-python-pages/page-038.md`-`page-129.md` | Helper имеет allowlist, tests, structured output |
| 49-60 | `black-hat-python-ru-pages/page-060.md`-`page-178.md` только lab-only, `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md` | Lab-навык переведен в безопасный Product QA artifact |
| 61-72 | `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md`, `page-437.md`-`page-466.md`, `architecture-patterns-python-pages/page-038.md`-`page-129.md` | Финальный assessment package связан с evidence, remediation и retest |

## Матрица по урокам

| Файл | Урок | Основной источник | Дополнительные источники | Что берем из книг | Как применить | Slider AI boundary |
|---|---|---|---|---|---|---|
{lesson_table}

## Проверка урока

Каждый урок должен явно отвечать:
1. Какой источник является основным?
2. Что конкретно берется из источника?
3. Как это превращается в SDET/Security QA навык?
4. Что нельзя переносить на Slider AI без отдельного разрешения?
""",
    )

    write(
        EDU / "lesson_template_full.md",
        """# Занятие NN. Название

## Учебная рамка

**Входные требования:**
**Результат занятия:**
**Наследуемая SDET-компетенция:**
**Security QA-компетенция:**
**Связь с книгами:**
**Основной источник:**
**Дополнительные источники:**
**Что берем из источника:**
**Как это превращается в SDET/Security QA навык:**
**Что нельзя переносить на Slider AI без отдельного разрешения:**
**Процессный артефакт:**
**Безопасная цель:**
**Среда выполнения:**
**Обязательный путь новичка:**
**Углубление:**
**Минимальная проверка успеха:**
**Эталонный вывод:**
**Критерии сдачи:**

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции, а студент получает самодостаточное объяснение ниже.

Книжные опоры урока:

- `docs/socraticode/...` — какая идея взята и как она адаптирована в безопасную лекцию.

## Source-driven theory

Полноценное объяснение, какие идеи из книг превращены в лекционный материал. Не копировать большие фрагменты. Не отправлять студенту базовую теорию на самостоятельный поиск. Объяснять так, чтобы студент с SDET-базой понял, какой QA-навык развивается, какие границы безопасности действуют и почему тема нужна для последующих уроков.

## Guided practice

### Шаг 1. Подготовка
### Шаг 2. Выполнение
### Шаг 3. Проверка результата
### Шаг 4. Evidence

## Теория

Основная лекция урока. Должна быть самодостаточной: термины, модель, механизм, безопасные примеры, разбор вывода, типичные ошибки, связь с SDET/Security QA и границы применения. Теория должна покрывать 100% понятий, которые нужны для практики текущего урока.

## Практическое занятие

## Примеры вывода

Показывать не только вывод, но и как его читать: какая строка что подтверждает, какой статус результата поставить и какой следующий безопасный шаг выбрать.

## Адаптация под macOS (M2, 8GB)

## Частые ошибки

## Вопросы на понимание

## Задачи для самостоятельного выполнения

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`
**Уровень прогрессии:**

### Минимум
### Практика Slider AI
### Углубление после изучения следующих уроков
### Артефакт сдачи
### Критерий готовности

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Минимальная практика, evidence без секретов, не вышел за scope |
| Хорошо | Есть объяснение риска, аккуратные шаги, корректный статус результата |
| Отлично | Есть связь с процессом, remediation/retest или automation appendix |

## Self-check

1. Что из предыдущего SDET-курса здесь используется?
2. Какая часть материала взята из книг?
3. Где граница безопасной практики?
4. Какой артефакт можно показать команде?
5. Что нужно изучить глубже после этого урока?
""",
    )

    assessments = {
        "block_01_16_foundation_workbook.md": ("Block Assessment 01-16: Foundation Workbook", ["Security QA workstation readiness", "Safe network observation package", "Evidence folder without secrets", "DNS/HTTP/TLS observation notes", "Limitations and stop conditions"]),
        "block_17_28_owasp_test_design.md": ("Block Assessment 17-28: OWASP Test Design for Slider AI", ["OWASP-to-Slider-AI traceability matrix", "5 safe security test cases", "2 lab-only write-ups", "1 sanitized Slider AI observation", "checks requiring approval"]),
        "block_29_40_tool_governance.md": ("Block Assessment 29-40: Tool Governance Report", ["Tool approval cards for Burp/ZAP/nmap/nuclei/sqlmap/hydra", "Safe pipeline for Slider AI", "One passive evidence sample", "False positive triage example", "Report limitations section"]),
        "block_41_48_security_helper.md": ("Block Assessment 41-48: Safe Security QA Helper", ["Repository/folder structure", "Working CLI help output", "Test output", "Dry-run output", "Sanitized Slider AI headers/status report", "README with scope and stop conditions"]),
        "block_49_60_lab_transfer.md": ("Block Assessment 49-60: Lab-to-Product Transfer", ["3 lab write-ups", "3 transfer cards", "1 safe Slider AI practice result", "1 limitations section", "Updated checklist for final assessment"]),
        "final_security_qa_assessment.md": ("Final Security QA Assessment: Slider AI olddev", ["Rules of Engagement", "Security Test Strategy", "Security Test Plan", "Threat Model", "Evidence Index", "Findings/Observations", "Triage Table", "Remediation Backlog", "Retest Plan", "Automation Appendix", "Executive Summary", "Limitations and Approval Requests"]),
    }
    for filename, (title, items) in assessments.items():
        rows = "\n".join(f"{i}. {item}." for i, item in enumerate(items, start=1))
        write(
            EDU / "assessments" / filename,
            f"""# {title}

## Сдать

{rows}

## Rubric

| Уровень | Критерий |
|---|---|
| Зачет | Пакет полный, безопасный, evidence sanitized |
| Хорошо | Есть приоритизация, связь с продуктовым риском и ограничения |
| Отлично | Есть automation appendix, remediation/retest и вклад в security regression backlog |
""",
        )

    write(
        EDU / "projects" / "security_qa_helper_spec.md",
        """# Security QA Helper Project Spec

## Goal

Build a safe helper for headers/status/link inventory that can be used as an automation appendix in the final Slider AI assessment.

## Required behavior

- allowlist target validation;
- dry-run mode;
- timeout;
- rate limit;
- secret masking;
- JSON output;
- Markdown report;
- pytest tests for safeguards and output.

## Forbidden behavior

- no brute force;
- no directory wordlist by default;
- no payload injection;
- no cookie/token persistence;
- no targets outside allowlist.

## Lesson increments

| Lesson | Increment |
|---|---|
| 41 | allowlist and target model |
| 42 | HTTP client with timeout |
| 43 | PoC verification plan, no payload execution |
| 44 | parser for prepared nmap XML |
| 45 | passive domain inventory model |
| 46 | visible URL inventory |
| 47 | CVE candidate mapper with confidence |
| 48 | integrated CLI/report/tests |
""",
    )

    write(
        EDU / "lab_transfer_matrix.md",
        """# Lab-to-Product Transfer Matrix

| Lab skill | Где тренировать | Что переносим в Slider AI | Что не переносим | Product QA artifact |
|---|---|---|---|---|
| enumeration | THM/HTB | structured notes, hypothesis list | aggressive scan | test plan |
| exploitation | lab only | risk understanding | exploit execution | finding template |
| privilege escalation | lab only | defensive hardening questions | privesc commands | limitation note |
| web payloads | PortSwigger/DVWA | safe markers and validation expectations | destructive payloads | security test case |
| reporting | any lab | evidence discipline and retest thinking | copying lab proof as product proof | security report |
""",
    )

    write(
        EDU / "glossary.md",
        """# Glossary

| Термин | Простое объяснение для SDET | Security QA пример |
|---|---|---|
| Scope | Границы разрешенной проверки | только olddev.slider-ai.ru |
| Evidence | Доказательство результата | sanitized request/response, screenshot |
| Finding | Подтвержденная проблема | воспроизводимый риск с impact |
| Observation | Наблюдение без полного подтверждения | отсутствует header, нужен owner review |
| Retest | Проверка исправления | повторить safe check после фикса |
| False positive | Инструмент ошибся или контекст не подтверждает риск | scanner alert без воспроизведения |
| Stop condition | Условие немедленной остановки проверки | всплеск 5xx, блокировка аккаунта, изменение чужих данных |
| Automation appendix | Приложение к отчету с безопасными helpers | allowlist, pytest, sanitized output |
""",
    )

    write(
        EDU / "knowledge_checks" / "README.md",
        """# Knowledge Checks

Контрольные вопросы проверяют, что студент не просто повторяет команды, а понимает SDET transfer, границы безопасности, evidence и применимость к Slider AI.
""",
    )
    for block in ["01_16", "17_28", "29_40", "41_48", "49_60", "61_72"]:
        write(
            EDU / "knowledge_checks" / f"block_{block}.md",
            f"""# Knowledge Check: Block {block}

## Questions

1. Какой SDET-навык развивается в этом блоке?
2. Где проходит безопасная граница для Slider AI?
3. Какой артефакт должен остаться после практики?
4. Как отличить finding от observation?
5. Что нужно вынести в lab-only или отдельный approval?

## Answer key

1. SDET-навык переносится в security context: planning, evidence, automation, reporting или retest.
2. Безопасная граница определяется `education/slider_ai_scope.md`, RoE и stop conditions.
3. Артефакт должен быть sanitized, воспроизводимым и полезным для команды.
4. Finding подтвержден evidence и impact; observation требует проверки, owner review или дополнительного scope.
5. Intrusive, destructive, brute force, bypass, exploitation и любые действия вне scope не выполняются на Slider AI без письменного разрешения.
""",
        )


def update_process_templates() -> None:
    for path in sorted((EDU / "security_process").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "## Мини-пример для Slider AI" not in text:
            text = text.rstrip() + """

## Мини-пример для Slider AI

- Target: `https://olddev.slider-ai.ru`.
- Scope: только функции тестового стенда, доступные QA-учетной записи.
- Evidence: sanitized Markdown, без cookies, tokens, персональных данных и чужих данных.
- Ограничения: без DoS/load, brute force, destructive payloads, secrets extraction и действий вне согласованного scope.
- Статус результата: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.
"""
            path.write_text(text, encoding="utf-8")

    tooling = EDU / "security_process" / "TOOLING_POLICY.md"
    text = tooling.read_text(encoding="utf-8")
    if "## Tool approval card" not in text:
        text = text.rstrip() + """

## Tool approval card

- Tool:
- Target:
- Mode: passive / manual / low-rate / lab-only / forbidden
- Command:
- Rate limit:
- Stop conditions:
- Expected evidence:
- False positive review:
- Owner approval:
"""
        tooling.write_text(text, encoding="utf-8")


def update_docs() -> None:
    book_map = EDU / "book_usage_map.md"
    text = book_map.read_text(encoding="utf-8")
    if "## Обязательное правило для правки уроков" not in text:
        text += """

## Обязательное правило для правки уроков

Новый материал в уроках должен сначала искать опору в книгах из `docs/socraticode/`.
Если тема отсутствует или раскрыта недостаточно, допускается краткое внешнее дополнение, но оно должно быть помечено как `дополнительная справка`, а не как основной источник курса.

Для каждого урока используется формат:

- Основной источник:
- Что берем из источника:
- Как это превращается в SDET/Security QA навык:
- Что нельзя переносить на Slider AI без отдельного разрешения:
"""
        book_map.write_text(text, encoding="utf-8")

    review = EDU / "prompt_lesson_review.md"
    text = review.read_text(encoding="utf-8")
    if "Урок считается самодостаточным только если студент может:" not in text:
        text += """

## Критерий самодостаточного урока

Урок считается самодостаточным только если студент может:
1. прочитать только Markdown-файл урока и понять тему без внешнего поиска;
2. получить внутри урока достаточную теорию: термины, модель, механизм, безопасные примеры и типичные ошибки;
3. выполнить guided practice без внешнего преподавателя;
4. получить и интерпретировать эталонный вывод;
5. сдать sanitized evidence по rubric;
6. понять, какие действия запрещены на Slider AI и почему;
7. объяснить, какие знания понадобятся в следующих уроках.

Книги курса используются как база автора лекции, а не как замена лекции. `Reading pack` не должен быть заданием “найди теорию в разных книгах”. Если материал нужен для практики текущего урока, он должен быть объяснен в самом уроке.

Урок не готов, если он представляет собой список тем, список страниц, список инструментов или набор заданий без достаточного лекционного объяснения.
"""
        review.write_text(text, encoding="utf-8")

    readme = EDU / "README.md"
    text = readme.read_text(encoding="utf-8")
    if "## Что значит пройти курс полностью" not in text:
        insert = """

## Что значит пройти курс полностью

Студент должен сдать:
- 6 block assessments;
- 1 Python security helper project;
- 1 final Slider AI Security QA assessment package;
- knowledge checks по всем блокам;
- evidence index без секретов;
- remediation/retest backlog.

Курс считается самодостаточным, если каждый урок является полноценной лекцией для самостоятельного обучения: студент получает достаточную теорию, модели, термины, безопасные примеры, разбор вывода, guided practice, безопасную Slider AI-практику, углубление, сдаваемый артефакт, rubric и self-check внутри самого Markdown-файла. Книги используются как база автора курса, но не заменяют лекцию.
"""
        text = text.replace("\n## Структура\n", insert + "\n## Структура\n")
        readme.write_text(text, encoding="utf-8")

    program = EDU / "pentest_learning_program.md"
    text = program.read_text(encoding="utf-8")
    if "## Самодостаточная модель урока" not in text:
        insert = """

## Самодостаточная модель урока

Каждый урок состоит из:
1. полноценной лекционной теории на основе книг курса;
2. guided practice;
3. safe Slider AI practice;
4. deepening/lab-only track;
5. сдаваемого артефакта;
6. rubric;
7. self-check.
"""
        text = text.replace("\n---\n\n## Месяцы 1-3", "\n" + insert + "\n---\n\n## Месяцы 1-3")
        program.write_text(text, encoding="utf-8")

    analysis = EDU / "sdet_to_pentest_transition_analysis.md"
    text = analysis.read_text(encoding="utf-8")
    if "## Критерии готовности к роли Product Security QA" not in text:
        text += """

## Критерии готовности к роли Product Security QA

- planning: может написать RoE/test strategy;
- execution: выполняет safe checks;
- automation: пишет helper с safeguards;
- reporting: оформляет findings/remediation/retest;
- communication: объясняет риск команде;
- ownership: добавляет regression checks после исправлений.
"""
        analysis.write_text(text, encoding="utf-8")


def main() -> None:
    create_course_docs()
    for lesson in sorted(LESSONS.glob("*/*.md")):
        update_lesson(lesson)
    update_process_templates()
    update_docs()


if __name__ == "__main__":
    main()
