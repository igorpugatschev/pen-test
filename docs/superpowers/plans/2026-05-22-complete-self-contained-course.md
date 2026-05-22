# Complete Self-Contained Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Превратить `Pen-Test Learning Program` в полный и самодостаточный курс перехода `SDET Python QA Automation Apprenticeship -> Security-aware SDET / Product Security QA`, где большая часть учебного содержания опирается на 5 книг, уже добавленных в проект.

**Architecture:** Курс остается Markdown-first: уроки живут в `education/lessons/`, процессные шаблоны в `education/security_process/`, книги в `docs/socraticode/`. Полнота достигается не расширением списка тем, а добавлением source-driven lesson packs: чтение из книг, конспект, guided practice, Slider AI practice, углубление, рубрика сдачи, контрольные точки и capstone assessments.

**Tech Stack:** Markdown, shell validation scripts, existing SocratiCode book pages under `docs/socraticode/`, `education/tools/check_lessons.sh`, optional Python helper scripts in `education/tools/`.

---

## Current State

- В курсе 77 Markdown-уроков в `education/lessons/`.
- В проекте есть 5 книжных источников в `docs/socraticode/`:
  - `learn-more-python-3-pages/`
  - `object-oriented-python-4th-ed-pages/`
  - `architecture-patterns-python-pages/`
  - `pycharm-professional-python-2024-pages/`
  - `black-hat-python-ru-pages/`
- Уже есть `education/book_usage_map.md`, но карта пока блочная, а не поурочная.
- Уже есть `education/security_process/`, но шаблоны короткие и требуют учебных примеров заполнения.
- Уроки уже имеют двухслойную модель `обязательный путь новичка / углубление`, но не везде содержат достаточно book-derived explanation, guided exercises, grading rubrics и проверяемые datasets/fixtures.

## Definition of Complete and Self-Contained

Курс считается полным, если студент может пройти его без внешних объяснений преподавателя и получить проверяемые артефакты:

1. Для каждого урока указаны конкретные страницы или главы из книг, которые закрывают 60-70% теории урока.
2. Для каждого урока есть `Source-driven theory`: короткое объяснение своими словами, основанное на книгах, без копирования больших фрагментов.
3. Для каждого урока есть `Guided practice`: пошаговая практика с ожидаемым результатом.
4. Для каждого урока есть `Minimum / Slider AI / Deepening` с постепенным ростом сложности.
5. Для каждого урока есть `Rubric`: что считается `зачет`, `хорошо`, `отлично`.
6. Для каждого блока есть `Block assessment`: мини-проект или контрольная работа.
7. Для dangerous/offensive-тем есть lab-only путь и defensive/product-QA перевод.
8. Для Slider AI есть полный безопасный assessment path: strategy, RoE, test plan, evidence, findings, triage, remediation, retest, automation appendix.
9. Есть проверка структуры, которая автоматически ловит отсутствие источников, практики, рубрик и safety boundaries.

---

### Task 1: Add Source Matrix for Every Lesson

**Files:**
- Create: `education/book_source_matrix.md`
- Modify: `education/book_usage_map.md`
- Test: `education/tools/check_lessons.sh`

- [ ] **Step 1: Create per-lesson source matrix**

Create `education/book_source_matrix.md` with this structure:

```markdown
# Поурочная карта источников

Цель: сделать курс source-driven. Каждый урок должен ссылаться на книги из `docs/socraticode/` и явно показывать, какая часть теории берется из какого источника.

## Правило покрытия

Для каждого урока:
- минимум 1 основной книжный источник;
- минимум 1 практическая связь с предыдущим SDET-курсом;
- для Python-уроков 41-48 обязательно использовать Python/OOP/Patterns/PyCharm;
- для lab-only/offensive-тем обязательно использовать `Black Hat Python` только через безопасную интерпретацию: boundaries, detection, defensive automation, lab-only practice.

## Формат строки

| Урок | Главный источник | Дополнительные источники | Что взять из книг | Как применить в уроке | Slider AI boundary |
|---|---|---|---|---|---|
```

- [ ] **Step 2: Fill lesson groups in the matrix**

Add rows for all lesson ranges:

```markdown
| 01-08 | PyCharm 2024, Learn More Python 3 | OOP Python | terminal workflow, files, CLI notes, debugging habit | workstation setup, notes, evidence folders | no product scanning |
| 09-16 | PyCharm 2024 | Black Hat Python lab-only | network basics, observing traffic, safe diagnostics | DNS/HTTP/TLS observation | no port sweep until lesson 29 and only scoped |
| 17-28 | PyCharm 2024, Black Hat Python lab-only | Learn More Python 3 | web request evidence, payload boundaries, lab practice separation | OWASP test design and safe markers | no destructive payloads |
| 29-40 | PyCharm 2024, Patterns Python | Black Hat Python lab-only | tool governance, false-positive review, reporting discipline | manual/passive/low-rate tool workflow | no aggressive scan without approval |
| 41-48 | Learn More Python 3, OOP Python, Patterns Python, PyCharm 2024 | Black Hat Python lab-only | CLI, classes, errors, service layer, safe helpers | tested security automation | allowlist, timeout, rate limit |
| 49-60 | Black Hat Python lab-only, PyCharm 2024 | Patterns Python | lab-to-product transfer, note discipline, reporting | CTF lessons become QA checks | do not copy attack steps to Slider AI |
| 61-72 | PyCharm 2024, Patterns Python | all books as reference | strategy, evidence, triage, remediation, automation appendix | product security ownership | full safe assessment only |
```

- [ ] **Step 3: Update `book_usage_map.md`**

Add a section:

```markdown
## Обязательное правило для правки уроков

Новый материал в уроках должен сначала искать опору в книгах из `docs/socraticode/`.
Если тема отсутствует или раскрыта недостаточно, допускается краткое внешнее дополнение, но оно должно быть помечено как `дополнительная справка`, а не как основной источник курса.

Для каждого урока используется формат:

- Основной источник:
- Что берем из источника:
- Как это превращается в SDET/Security QA навык:
- Что нельзя переносить на Slider AI без отдельного разрешения:
```

- [ ] **Step 4: Extend validation**

Update `education/tools/check_lessons.sh` so every lesson must contain:

```bash
required_patterns=(
  "Связь с книгами"
  "Основной источник"
  "Что берем из источника"
  "SDET"
  "Security QA"
  "Практика на Slider AI"
  "Критерий готовности"
)
```

Run:

```bash
bash education/tools/check_lessons.sh
```

Expected:

```text
Проблем: 0
```

- [ ] **Step 5: Commit**

```bash
git add education/book_source_matrix.md education/book_usage_map.md education/tools/check_lessons.sh
git commit -m "docs: add source-driven lesson matrix"
```

---

### Task 2: Create a Full Lesson Template

**Files:**
- Create: `education/lesson_template_full.md`
- Modify: `education/prompt_lesson_review.md`
- Test: `education/tools/check_lessons.sh`

- [ ] **Step 1: Create the canonical lesson template**

Create `education/lesson_template_full.md`:

```markdown
# Занятие NN. Название

## Учебная рамка

**Входные требования:**
**Результат занятия:**
**Наследуемая SDET-компетенция:**
**Security QA-компетенция:**
**Основной источник:**
**Дополнительные источники:**
**Что берем из источника:**
**Процессный артефакт:**
**Безопасная цель:**
**Среда выполнения:**
**Обязательный путь новичка:**
**Углубление:**
**Минимальная проверка успеха:**
**Эталонный вывод:**
**Критерии сдачи:**

## Source-driven theory

Короткое объяснение темы на основе книг. Не копировать большие фрагменты. Объяснять так, чтобы студент с SDET-базой понял, какой QA-навык развивается.

## Guided practice

### Шаг 1. Подготовка
### Шаг 2. Выполнение
### Шаг 3. Проверка результата
### Шаг 4. Evidence

## Slider AI practice

### Минимум
### Практика Slider AI
### Углубление после следующих уроков
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
```

- [ ] **Step 2: Update lesson review prompt**

In `education/prompt_lesson_review.md`, add the rule:

```markdown
Урок считается самодостаточным только если студент может:
1. понять тему через book-derived explanation;
2. выполнить guided practice без внешнего преподавателя;
3. получить эталонный вывод;
4. сдать артефакт по rubric;
5. понять, какие действия запрещены на Slider AI.
```

- [ ] **Step 3: Validate**

Run:

```bash
bash education/tools/check_lessons.sh
```

Expected:

```text
Проблем: 0
```

- [ ] **Step 4: Commit**

```bash
git add education/lesson_template_full.md education/prompt_lesson_review.md education/tools/check_lessons.sh
git commit -m "docs: define self-contained lesson template"
```

---

### Task 3: Rewrite Lessons 01-16 as Foundation Workbooks

**Files:**
- Modify: `education/lessons/01-08/*.md`
- Modify: `education/lessons/09-16/*.md`
- Modify: `education/slider_ai_progression_matrix.md`
- Test: `education/tools/check_lessons.sh`

- [ ] **Step 1: Add book-derived learning blocks**

For each lesson 01-16, add:

```markdown
**Основной источник:** `PyCharm. Профессиональная работа на Python 2024` / `Легкий способ выучить Python 3 еще глубже`
**Что берем из источника:** terminal discipline, project navigation, files, text processing, debugging workflow, HTTP Client/DevTools-style evidence.
```

- [ ] **Step 2: Convert tasks into workbooks**

Each lesson must include:

```markdown
## Guided practice

1. Выполнить команду.
2. Сохранить вывод в evidence.
3. Объяснить, что этот вывод означает для QA.
4. Отметить, применимо ли это к Slider AI.
```

- [ ] **Step 3: Add block assessment after lesson 08**

In `lesson_08_linux_summary.md`, add:

```markdown
## Block assessment: Security QA workstation readiness

Сдать:
- структуру рабочей папки;
- проверку прав доступа;
- индекс заметок;
- минимальный evidence policy;
- короткий README: как хранить артефакты без секретов.
```

- [ ] **Step 4: Add block assessment after lesson 16**

In `lesson_16_network_practice.md`, add:

```markdown
## Block assessment: Safe network observation package

Сдать:
- DNS observation;
- HTTPS status/header observation;
- route/accessibility note;
- DevTools Network screenshot without secrets;
- limitations section.
```

- [ ] **Step 5: Validate and commit**

```bash
bash education/tools/check_lessons.sh
git add education/lessons/01-08 education/lessons/09-16 education/slider_ai_progression_matrix.md
git commit -m "docs: turn foundation lessons into self-contained workbooks"
```

---

### Task 4: Rewrite OWASP Lessons 17-28 as Test-Design Modules

**Files:**
- Modify: `education/lessons/17-28/*.md`
- Create: `education/assessments/block_17_28_owasp_test_design.md`
- Test: `education/tools/check_lessons.sh`

- [ ] **Step 1: Add source-driven OWASP lesson pattern**

For every lesson 17-28, add this structure:

```markdown
## Source-driven theory

- Что объясняет книга/источник.
- Как SDET превращает риск в test case.
- Как отличить lab payload от product-safe marker.
- Что запрещено на Slider AI без отдельного approval.
```

- [ ] **Step 2: Split lab and Slider AI practice**

Every offensive topic must have:

```markdown
## Lab-only practice

Цель: DVWA, WebGoat, PortSwigger или другой разрешенный lab.
Разрешено: учебные payloads внутри lab.
Запрещено переносить payload на Slider AI.

## Slider AI safe practice

Использовать безопасный маркер, DevTools/Burp passive evidence, observation/finding classification.
```

- [ ] **Step 3: Create block assessment**

Create `education/assessments/block_17_28_owasp_test_design.md`:

```markdown
# Block Assessment 17-28: OWASP Test Design for Slider AI

## Сдать

1. OWASP-to-Slider-AI traceability matrix.
2. 5 safe security test cases.
3. 2 lab-only write-ups.
4. 1 sanitized Slider AI observation.
5. Список checks, требующих approval.

## Rubric

| Уровень | Критерий |
|---|---|
| Зачет | Есть матрица и безопасные тест-кейсы |
| Хорошо | Есть evidence и корректная классификация риска |
| Отлично | Есть remediation/retest для подтвержденного finding или объяснение `not applicable` |
```

- [ ] **Step 4: Validate and commit**

```bash
bash education/tools/check_lessons.sh
git add education/lessons/17-28 education/assessments/block_17_28_owasp_test_design.md
git commit -m "docs: deepen OWASP lessons with source-driven test design"
```

---

### Task 5: Rewrite Tools Lessons 29-40 as Governance and Evidence Modules

**Files:**
- Modify: `education/lessons/29-40/*.md`
- Create: `education/assessments/block_29_40_tool_governance.md`
- Modify: `education/security_process/TOOLING_POLICY.md`
- Test: `education/tools/check_lessons.sh`

- [ ] **Step 1: Add tool decision table to each lesson**

Each lesson 29-40 must include:

```markdown
| Режим | Где разрешен | Что можно делать | Что нельзя делать |
|---|---|---|---|
| Manual/passive | Slider AI | observation, headers, visible URLs | intrusive checks |
| Low-rate scoped | Slider AI only after approval | one host, explicit limits | broad scan |
| Lab-only | DVWA/THM/HTB/local VM | aggressive options | product target |
```

- [ ] **Step 2: Expand `TOOLING_POLICY.md`**

Add required fields:

```markdown
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
```

- [ ] **Step 3: Create block assessment**

Create `education/assessments/block_29_40_tool_governance.md`:

```markdown
# Block Assessment 29-40: Tool Governance Report

## Сдать

1. Tool approval cards for Burp/ZAP/nmap/nuclei/sqlmap/hydra.
2. Safe pipeline for Slider AI.
3. One passive evidence sample.
4. False positive triage example.
5. Report section with limitations.
```

- [ ] **Step 4: Validate and commit**

```bash
bash education/tools/check_lessons.sh
git add education/lessons/29-40 education/security_process/TOOLING_POLICY.md education/assessments/block_29_40_tool_governance.md
git commit -m "docs: make tool lessons governance-driven"
```

---

### Task 6: Add Real Python Automation Project Track

**Files:**
- Modify: `education/lessons/41-48/*.md`
- Create: `education/projects/security_qa_helper_spec.md`
- Create: `education/assessments/block_41_48_security_helper.md`
- Test: `education/tools/check_lessons.sh`

- [ ] **Step 1: Define the project spec**

Create `education/projects/security_qa_helper_spec.md`:

```markdown
# Security QA Helper Project Spec

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
```

- [ ] **Step 2: Align lessons 41-48 to the project**

Each lesson must add exactly one project increment:

```markdown
41 allowlist and target model
42 HTTP client with timeout
43 PoC verification plan, no payload execution
44 parser for prepared nmap XML
45 passive domain inventory model
46 visible URL inventory
47 CVE candidate mapper with confidence
48 integrated CLI/report/tests
```

- [ ] **Step 3: Create assessment**

Create `education/assessments/block_41_48_security_helper.md`:

```markdown
# Block Assessment 41-48: Safe Security QA Helper

## Сдать

1. Repository/folder structure.
2. Working CLI help output.
3. Test output.
4. One dry-run output.
5. One sanitized Slider AI headers/status report.
6. README with scope and stop conditions.
```

- [ ] **Step 4: Validate and commit**

```bash
bash education/tools/check_lessons.sh
git add education/lessons/41-48 education/projects/security_qa_helper_spec.md education/assessments/block_41_48_security_helper.md
git commit -m "docs: add full security helper project track"
```

---

### Task 7: Add Lab-to-Product Transfer Track for Lessons 49-60

**Files:**
- Modify: `education/lessons/49-60/*.md`
- Create: `education/lab_transfer_matrix.md`
- Create: `education/assessments/block_49_60_lab_transfer.md`
- Test: `education/tools/check_lessons.sh`

- [ ] **Step 1: Create transfer matrix**

Create `education/lab_transfer_matrix.md`:

```markdown
# Lab-to-Product Transfer Matrix

| Lab skill | Где тренировать | Что переносим в Slider AI | Что не переносим | Product QA artifact |
|---|---|---|---|---|
| enumeration | THM/HTB | structured notes, hypothesis list | aggressive scan | test plan |
| exploitation | lab only | risk understanding | exploit execution | finding template |
| privilege escalation | lab only | defensive hardening questions | privesc commands | limitation note |
| web payloads | PortSwigger/DVWA | safe markers and validation expectations | destructive payloads | security test case |
```

- [ ] **Step 2: Update lessons 49-60**

Each lesson must include:

```markdown
## Transfer rule

После lab студент записывает:
1. какой навык отработан;
2. какой безопасный QA-аналог применим к Slider AI;
3. какие действия запрещены;
4. какой артефакт остается в отчете.
```

- [ ] **Step 3: Create assessment**

Create `education/assessments/block_49_60_lab_transfer.md`:

```markdown
# Block Assessment 49-60: Lab-to-Product Transfer

## Сдать

1. 3 lab write-ups.
2. 3 transfer cards.
3. 1 safe Slider AI practice result.
4. 1 limitations section.
5. Updated checklist for final assessment.
```

- [ ] **Step 4: Validate and commit**

```bash
bash education/tools/check_lessons.sh
git add education/lessons/49-60 education/lab_transfer_matrix.md education/assessments/block_49_60_lab_transfer.md
git commit -m "docs: add lab-to-product transfer track"
```

---

### Task 8: Deepen Process and Final Assessment Lessons 61-72

**Files:**
- Modify: `education/lessons/61-72/*.md`
- Modify: `education/security_process/*.md`
- Create: `education/assessments/final_security_qa_assessment.md`
- Test: `education/tools/check_lessons.sh`

- [ ] **Step 1: Add worked examples to process templates**

Every file in `education/security_process/` must include:

```markdown
## Мини-пример для Slider AI

Пример должен быть безопасным, sanitized, без cookies/tokens/секретов и без утверждений, которые нельзя подтвердить evidence.
```

- [ ] **Step 2: Add final assessment packet**

Create `education/assessments/final_security_qa_assessment.md`:

```markdown
# Final Security QA Assessment: Slider AI olddev

## Required package

1. Rules of Engagement.
2. Security Test Strategy.
3. Security Test Plan.
4. Threat Model.
5. Evidence Index.
6. Findings/Observations.
7. Triage Table.
8. Remediation Backlog.
9. Retest Plan.
10. Automation Appendix.
11. Executive Summary.
12. Limitations and Approval Requests.

## Passing criteria

Зачет: пакет полный, безопасный, evidence sanitized.
Хорошо: есть приоритизация и связь с продуктовым риском.
Отлично: есть automation appendix, regression backlog и готовность обсуждать remediation с командой.
```

- [ ] **Step 3: Update lessons 61-72**

Each lesson must contribute one final artifact:

```markdown
61 RoE
62 WSTG checklist
63 report structure
64 scoring rationale
65 scanner governance
66 enterprise VM workflow
67 readiness gap analysis
68 timed assessment discipline
69 OSCP-style note discipline
70 AD/SSO defensive checklist
71 post-exploitation boundaries and evidence handling
72 full package assembly
```

- [ ] **Step 4: Validate and commit**

```bash
bash education/tools/check_lessons.sh
git add education/lessons/61-72 education/security_process education/assessments/final_security_qa_assessment.md
git commit -m "docs: complete security ownership assessment track"
```

---

### Task 9: Add Glossary, Knowledge Checks, and Answer Keys

**Files:**
- Create: `education/glossary.md`
- Create: `education/knowledge_checks/README.md`
- Create: `education/knowledge_checks/block_01_16.md`
- Create: `education/knowledge_checks/block_17_28.md`
- Create: `education/knowledge_checks/block_29_40.md`
- Create: `education/knowledge_checks/block_41_48.md`
- Create: `education/knowledge_checks/block_49_60.md`
- Create: `education/knowledge_checks/block_61_72.md`

- [ ] **Step 1: Create glossary**

Create `education/glossary.md` with terms:

```markdown
# Glossary

| Термин | Простое объяснение для SDET | Security QA пример |
|---|---|---|
| Scope | Границы разрешенной проверки | только olddev.slider-ai.ru |
| Evidence | Доказательство результата | sanitized request/response, screenshot |
| Finding | Подтвержденная проблема | воспроизводимый риск с impact |
| Observation | Наблюдение без полного подтверждения | отсутствует header, нужен owner review |
| Retest | Проверка исправления | повторить safe check после фикса |
| False positive | Инструмент ошибся или контекст не подтверждает риск | scanner alert без воспроизведения |
```

- [ ] **Step 2: Create knowledge checks**

Each block file must include:

```markdown
# Knowledge Check: Block NN

## Questions

1. Вопрос на терминологию.
2. Вопрос на безопасную границу.
3. Вопрос на SDET transfer.
4. Вопрос на evidence.
5. Вопрос на Slider AI application.

## Answer key

1. Эталонный ответ.
2. Эталонный ответ.
3. Эталонный ответ.
4. Эталонный ответ.
5. Эталонный ответ.
```

- [ ] **Step 3: Commit**

```bash
git add education/glossary.md education/knowledge_checks
git commit -m "docs: add glossary and knowledge checks"
```

---

### Task 10: Add Completeness Validator

**Files:**
- Create: `education/tools/check_course_completeness.py`
- Modify: `education/tools/check_lessons.sh`

- [ ] **Step 1: Create validator**

Create `education/tools/check_course_completeness.py` that checks every lesson for:

```python
REQUIRED = [
    "Входные требования",
    "Результат занятия",
    "Наследуемая SDET-компетенция",
    "Security QA-компетенция",
    "Основной источник",
    "Что берем из источника",
    "Guided practice",
    "Практика на Slider AI",
    "Минимум",
    "Углубление",
    "Артефакт сдачи",
    "Критерий готовности",
    "Rubric",
]
```

Expected CLI behavior:

```text
OK: 77 lessons checked
Missing sections: 0
```

- [ ] **Step 2: Wire it into shell check**

Add to `education/tools/check_lessons.sh`:

```bash
python3 education/tools/check_course_completeness.py
```

Use a path-safe implementation so the command works from repository root.

- [ ] **Step 3: Run validation**

```bash
bash education/tools/check_lessons.sh
```

Expected:

```text
Проблем: 0
OK: 77 lessons checked
Missing sections: 0
```

- [ ] **Step 4: Commit**

```bash
git add education/tools/check_course_completeness.py education/tools/check_lessons.sh
git commit -m "test: validate course completeness requirements"
```

---

### Task 11: Update README and Program as a Complete Course Contract

**Files:**
- Modify: `education/README.md`
- Modify: `education/pentest_learning_program.md`
- Modify: `education/sdet_to_pentest_transition_analysis.md`

- [ ] **Step 1: Add course contract to README**

Add:

```markdown
## Что значит пройти курс полностью

Студент должен сдать:
- 6 block assessments;
- 1 Python security helper project;
- 1 final Slider AI Security QA assessment package;
- knowledge checks по всем блокам;
- evidence index без секретов;
- remediation/retest backlog.
```

- [ ] **Step 2: Add self-contained learning model**

In `education/pentest_learning_program.md`, add:

```markdown
## Самодостаточная модель урока

Каждый урок состоит из:
1. book-derived theory;
2. guided practice;
3. safe Slider AI practice;
4. deepening/lab-only track;
5. сдаваемого артефакта;
6. rubric;
7. self-check.
```

- [ ] **Step 3: Update transition analysis**

Add:

```markdown
## Критерии готовности к роли Product Security QA

- planning: может написать RoE/test strategy;
- execution: выполняет safe checks;
- automation: пишет helper с safeguards;
- reporting: оформляет findings/remediation/retest;
- communication: объясняет риск команде;
- ownership: добавляет regression checks после исправлений.
```

- [ ] **Step 4: Commit**

```bash
git add education/README.md education/pentest_learning_program.md education/sdet_to_pentest_transition_analysis.md
git commit -m "docs: define complete course contract"
```

---

### Task 12: Final Verification and SocratiCode Reindex

**Files:**
- No content files required unless validation finds issues.

- [ ] **Step 1: Run structural checks**

```bash
bash education/tools/check_lessons.sh
python3 education/tools/check_course_completeness.py
```

Expected:

```text
Проблем: 0
OK: 77 lessons checked
Missing sections: 0
```

- [ ] **Step 2: Check git diff quality**

```bash
git diff --check
```

Expected: no output.

- [ ] **Step 3: Reindex with SocratiCode**

Run SocratiCode index for `/Users/formacepht/PycharmProjects/pen-test`.

Expected:

```text
Indexing complete
Progress: 100%
```

- [ ] **Step 4: Final commit**

```bash
git add education docs/superpowers/plans
git commit -m "docs: complete self-contained security qa course"
```

---

## Execution Order

Recommended order:

1. Source matrix and lesson template.
2. Foundation blocks 01-16.
3. OWASP block 17-28.
4. Tools block 29-40.
5. Python project block 41-48.
6. Lab transfer block 49-60.
7. Ownership/final block 61-72.
8. Glossary and knowledge checks.
9. Completeness validator.
10. README/program/course contract.
11. Final verification and SocratiCode reindex.

## Main Risk

Главный риск — случайно превратить курс в набор пересказов книг. Чтобы этого избежать, каждый книжный блок должен завершаться действием: SDET-навык, безопасная проверка, evidence, finding/observation или process artifact.

## Self-Review

- Spec coverage: план покрывает полноту, самодостаточность, связь с 5 книгами, SDET-to-Security QA переход, Slider AI practice, process/reporting/remediation/retest.
- Placeholder scan: intentionally no `TBD`, `TODO`, `implement later`; all created files have concrete skeletons.
- Execution safety: dangerous techniques are separated into lab-only and defensive/product-QA transfer.
