# Пользовательская инструкция по прохождению курса

Эта инструкция описывает, как проходить Pen-Test Learning Program самостоятельно и безопасно. Курс рассчитан на QA/SDET-специалиста, который уже знаком с Python и базовой инженерной дисциплиной, но постепенно осваивает security testing.

## 1. Как устроено обучение

Проходите занятия последовательно. Не переходите к углублению, если не выполнен обязательный безопасный путь текущего урока.

Рекомендуемый ритм:

- 3 занятия в неделю;
- 1-2 часа на занятие;
- 70% времени на практику и evidence;
- 30% времени на чтение теории и ответы на вопросы.

Каждый урок нужно закрывать не “прочитал”, а артефактом: Markdown-заметкой, sanitized выводом команды, checklist, finding draft, helper output, report fragment или retest note.

## 2. Как читать лекцию

В каждой лекции сначала изучите учебную рамку:

- входные требования;
- результат занятия;
- безопасная цель;
- среда выполнения;
- минимальная проверка успеха;
- эталонный вывод;
- критерии сдачи.

После этого прочитайте теорию и выполните guided practice. Если вы не можете объяснить модель урока своими словами, практику пока не запускайте.

## 3. Два слоя практики

Обязательный безопасный путь новичка выполняется на macOS native, localhost, локальных файлах, браузере, DevTools или одиночном разрешенном наблюдении. Он не должен создавать нагрузку, менять чужие данные или требовать специальных разрешений.

Углубление выполняется только после освоения базовой темы. Для углубления используются Kali ARM64 VM, TryHackMe AttackBox, HackTheBox/Pwnbox, PortSwigger Academy или локальные deliberately vulnerable приложения.

## 4. Slider AI olddev

Единственная разрешенная продуктовая цель курса:

```text
https://olddev.slider-ai.ru
```

На Slider AI olddev разрешены только безопасные действия, явно совместимые с уроком: ручное наблюдение, DevTools, одиночные low-impact запросы, заполнение checklist, оформление evidence, finding draft, limitation и request for approval.

Запрещено:

- тестировать production;
- выполнять DoS/load/stress;
- выполнять brute force/password guessing;
- запускать destructive payloads;
- извлекать или сохранять secrets;
- сохранять cookies, tokens, passwords, PII;
- менять чужие данные;
- сканировать вне scope;
- переносить lab-only технику на olddev без отдельного written approval.

Если сомневаетесь, классифицируйте следующий шаг как `requires approval`.

## 5. Evidence

Каждый артефакт должен содержать:

- дату и номер урока;
- среду выполнения;
- target;
- scope status;
- команду или ручной шаг;
- 3-10 строк sanitized output или краткое описание UI-наблюдения;
- интерпретацию;
- limitation;
- следующий безопасный шаг.

Evidence не должен содержать cookies, tokens, passwords, private keys, PII, чужие данные и полные ответы, где могут быть секреты.

Минимальный формат:

```markdown
Lesson:
Environment:
Target:
Scope status:
Action:
Evidence:
Interpretation:
Limitations:
Next safe step:
Status: observation | finding | not applicable | not reproducible | requires approval
```

## 6. Рабочая среда MacBook Air M2

Базовый путь:

- macOS native;
- Homebrew или официальные installers;
- браузер и DevTools;
- Burp/ZAP в безопасном режиме;
- Python 3;
- nmap для разрешенных одиночных или lab-only проверок.

Kali Linux ARM64 VM используйте только как углубление. Рекомендуемый лимит для MacBook Air M2 8GB: 3-4GB RAM и 2 CPU. Тяжелые сценарии переносите в cloud lab.

VirtualBox и x86/x64 VM не являются базовым путем для Apple Silicon.

## 6.1. Единая карта локальных портов

Чтобы лаборатории не конфликтовали с proxy-инструментами, в курсе используется фиксированная карта портов:

| Назначение | URL или endpoint | Комментарий |
|---|---|---|
| Burp Proxy | `127.0.0.1:8080` | Только proxy в браузере, не учебное приложение |
| DVWA | `http://127.0.0.1:8081` | Docker mapping `8081:80` |
| bWAPP | `http://127.0.0.1:8082` | Docker mapping `8082:80` |
| WebGoat | `http://127.0.0.1:8083/WebGoat` | Docker mapping `8083:8080` |
| OWASP ZAP Proxy | `127.0.0.1:8090` | Чтобы не конфликтовать с Burp |
| Mock internal SSRF service | `http://127.0.0.1:8888` | Только локальная имитация внутреннего сервиса |
| Mock cloud metadata | `http://127.0.0.1:9000/latest/meta-data/` | Без обращения к реальному cloud metadata endpoint |

Если в выводе Docker появился другой порт, студент фиксирует это в evidence и явно объясняет отличие. На Slider AI olddev не переносятся lab-only payloads, перебор портов, brute force, destructive payloads и active scan без отдельного approval.

## 7. Критерии зачета урока

Зачет:

- теория объяснена своими словами;
- выполнен обязательный безопасный путь;
- получен ожидаемый результат;
- оформлен sanitized evidence.

Хорошо:

- добавлены ограничения, scope и причина выбора среды;
- результат классифицирован как observation/finding/not applicable/not reproducible/requires approval.

Отлично:

- результат превращен в SDET/Security QA артефакт: test case, checklist item, automation helper, finding draft, remediation note или retest step.

## 8. Как использовать книги

Книги являются источниками автора курса. Это значит, что лекции уже должны содержать достаточную теорию для выполнения заданий.

К книгам можно обращаться для углубленного понимания, но это не должно быть условием выполнения текущего урока. Если для задания не хватает термина, команды, примера, ожидаемого вывода или критерия сдачи внутри лекции, это дефект лекции.

## 9. Финальный результат курса

К концу курса студент должен собрать assessment package для Slider AI olddev:

- security test strategy;
- Rules of Engagement;
- safe checklist по OWASP/WSTG;
- sanitized evidence index;
- findings/observations;
- remediation backlog;
- retest plan;
- automation appendix на Python;
- итоговый отчет для команды.

## 10. Встроенные шаблоны курса

Все шаблоны ниже являются частью курса. Их не нужно искать в отдельных файлах или внешних источниках. В каждом уроке студент копирует нужный шаблон в свои рабочие заметки и заполняет только безопасные поля без cookies, tokens, passwords, PII и чужих данных.

### Rules of Engagement

```markdown
# Rules of Engagement

Target:
Environment:
Authorized owner:
In scope:
Out of scope:
Allowed actions:
Forbidden actions:
Stop conditions:
Evidence rules:
Approval needed for:
Communication channel:
Retest window:
```

Минимальная сдача: явно указаны `Target`, `In scope`, `Out of scope`, `Forbidden actions` и `Stop conditions`. Для Slider AI target всегда только `https://olddev.slider-ai.ru`.

### Security Test Strategy

```markdown
# Security Test Strategy

Product area:
Business risk:
Security objective:
Relevant OWASP/WSTG areas:
Assumptions:
Constraints:
Safe baseline checks:
Lab-only checks:
Approval-required checks:
Evidence format:
Definition of done:
```

Стратегия отвечает на вопрос “зачем проверяем”. Она не должна начинаться с инструмента. Сначала фиксируется риск продукта, затем безопасный способ проверки.

### Security Test Plan

```markdown
# Security Test Plan

Check ID:
Feature:
Preconditions:
Environment:
Target:
Steps:
Expected result:
Actual result:
Evidence:
Status: observation | finding | not applicable | not reproducible | requires approval
Limitations:
Next safe step:
```

План отвечает на вопрос “как проверяем”. Если шаг требует payload, перебора, активного сканирования, изменения данных или доступа к чужим данным, статус шага должен быть `requires approval` или `lab-only`.

### Threat Model

```markdown
# Threat Model

Feature:
Assets:
Actors:
Trust boundaries:
Entry points:
Data flows:
Abuse case:
Expected control:
Missing or weak control:
Safe verification:
Residual risk:
```

Для базовой версии используйте STRIDE как словарь вопросов: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. В курсе DoS не выполняется как практика на Slider AI, а только фиксируется как риск и stop condition.

### Evidence Policy

```markdown
# Evidence Policy

Allowed evidence:
Forbidden evidence:
Sanitization rule:
Storage location:
Retention:
Sharing rule:
Example safe snippet:
Example redaction:
```

Evidence должен подтверждать наблюдение, но не должен становиться утечкой. Достаточно 3-10 строк вывода или короткого описания UI-наблюдения.

### Tooling Policy / Tooling Approval Card

```markdown
# Tooling Policy / Tooling Approval Card

Tool:
Mode:
Target:
Why this tool is needed:
Expected requests or actions:
Rate limit:
Data collected:
Data explicitly not collected:
Safety guard:
Stop condition:
Approval status: allowed | lab-only | requires approval | forbidden
```

Эта карточка заполняется до запуска любого scanner, wordlist-инструмента, brute-force-инструмента, exploit helper или active scan. Для Slider AI default status для активных инструментов: `requires approval`.

Минимальная сдача: указан инструмент, режим, target, collected data, rate limit, stop condition и approval status. Если студент не может заполнить карточку до запуска, инструмент не запускается.

### Finding Template

```markdown
# Security Finding

Title:
Status: finding | observation | not reproducible | not applicable | requires approval
Severity:
Affected area:
Business impact:
Technical description:
Steps to reproduce:
Evidence:
Why this is in scope:
What was not tested:
Recommendation:
Owner:
Retest criteria:
```

Finding появляется только после проверки контекста, влияния, воспроизводимости и scope. Вывод инструмента сам по себе является observation.

### Vulnerability Triage

```markdown
# Vulnerability Triage

Candidate:
Source:
Confidence:
Scope status:
Exploitability:
Business impact:
False-positive checks:
Decision:
Owner action:
Retest need:
```

Triage нужен, чтобы не превращать каждый scanner output в дефект. Студент обязан указать confidence и false-positive checks.

### Remediation Backlog

```markdown
# Remediation Backlog

Item:
Risk:
Recommended fix:
Owner:
Priority:
Dependency:
Due date:
Acceptance criteria:
Retest method:
Status:
```

Backlog связывает security finding с инженерным действием команды. Хорошая рекомендация проверяема: после исправления понятно, каким шагом делать retest.

### Retest Plan

```markdown
# Retest Plan

Original finding:
Fix summary:
Environment:
Preconditions:
Retest steps:
Expected secure behavior:
Evidence to collect:
Regression check:
Result:
Remaining risk:
```

Retest подтверждает, что риск снижен, а не просто “дефект закрыт”. Если исходный тест был lab-only, retest тоже остается lab-only или выполняется только после approval.

### Security Automation Architecture / Security Automation Appendix

```markdown
# Security Automation Architecture / Security Automation Appendix

Helper name:
Purpose:
Allowed targets:
Forbidden targets:
Safety controls:
Timeout/rate limit:
Input contract:
Output contract:
Tests:
Sanitization:
Example output:
How to use in retest:
```

Automation appendix показывает, что Python helper является частью SDET ownership: его можно ревьюить, тестировать, повторять и безопасно использовать для regression.

## 11. Индекс финального assessment package

Финальный проект не требует отдельных шаблонных файлов в репозитории курса. Студент собирает рабочий Markdown-пакет в своей учебной папке, копируя встроенные шаблоны из этой инструкции.

Минимальный состав пакета:

```markdown
# Slider AI olddev Security QA Assessment Package

## 1. Rules of Engagement
Copy: Rules of Engagement

## 2. Security Test Strategy
Copy: Security Test Strategy

## 3. Evidence Policy
Copy: Evidence Policy

## 4. Tooling Policy
Copy: Tooling Policy / Tooling Approval Card

## 5. Security Test Plan
Copy: Security Test Plan

## 6. Threat Model
Copy: Threat Model

## 7. Evidence Index
| ID | Area | Action | Evidence | Status | Sanitized |
|---|---|---|---|---|---|

## 8. Findings And Observations
Copy: Finding Template for each confirmed item or observation

## 9. Vulnerability Triage
Copy: Vulnerability Triage

## 10. Remediation Backlog
Copy: Remediation Backlog

## 11. Retest Plan
Copy: Retest Plan

## 12. Security Automation Architecture / Appendix
Copy: Security Automation Architecture / Security Automation Appendix

## 13. Executive Summary
5-7 sentences for team decision making
```

Пакет считается готовым, если каждый раздел содержит конкретные данные по `https://olddev.slider-ai.ru`, явно указывает ограничения и не содержит секретов. Пустой шаблон не считается выполненной работой.
