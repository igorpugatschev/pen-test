# Занятие 72. Финальный Security QA assessment Slider AI

## Учебная рамка

**Входные требования:** Завершены предыдущие блоки курса; студент понимает SDET-процесс, OWASP/WSTG, PTES, CVSS/QA severity, evidence handling, safe automation и ограничения Slider AI scope.

**Результат занятия:** Студент проводит безопасную всестороннюю проверку `olddev.slider-ai.ru` как Security-aware SDET: планирует scope, выполняет безопасные проверки, оформляет findings/observations, готовит remediation backlog, retest plan и automation appendix.

**Наследуемая SDET-компетенция:** security ownership: стратегия, RoE, risk scoring, remediation, retest и коммуникация с командой.

**Security QA-компетенция:** планирование и сопровождение полного security assessment: findings, risk, remediation, retest.

**Связь с книгами:** PTES/OWASP/CVSS как методология; «PyCharm. Профессиональная работа на Python 2024» — Git/VCS, Markdown evidence, debugger/HTTP Client; «Паттерны разработки на Python» — architecture appendix для safe helpers; «Black Hat Python» — только lab-only/detection interpretation.

**Процессный артефакт:** `RULES_OF_ENGAGEMENT.md`, `SECURITY_TEST_STRATEGY.md`, `SECURITY_TEST_PLAN.md`, `SECURITY_FINDING_TEMPLATE.md`, `REMEDIATION_BACKLOG.md`, `RETEST_PLAN.md` и `SECURITY_AUTOMATION_ARCHITECTURE.md`.

**Безопасная цель:** Только `https://olddev.slider-ai.ru` в рамках `education/slider_ai_scope.md`, либо учебные lab/CTF цели с явным разрешением. Production и любые другие домены исключены.

**Среда выполнения:** macOS native, PyCharm/terminal, браузер, DevTools, Burp/ZAP passive, Python helpers из блока 41-48. Kali/cloud lab используется только для lab-only техник и не переносится на Slider AI без отдельного письменного разрешения.

**Обязательный путь новичка:** Собрать scope, test plan, безопасные manual checks, sanitized evidence index, 1-3 observations/findings и retest plan.

**Углубление:** Добавить threat model, CVSS/QA severity rationale, automation appendix, remediation backlog с owners/priorities и executive summary для команды.

**Минимальная проверка успеха:** Финальный пакет содержит scope/RoE, методологию, ограничения, evidence, findings/observations, remediation и retest; все действия остаются в безопасном scope.

**Эталонный вывод:** Сданный пакет: report, evidence index, triage table, remediation backlog, retest plan, automation appendix и короткая защита результата.

**Критерии сдачи:** Зачет: полный безопасный assessment package. Отлично: ясная бизнес-интерпретация, приоритизация, automation appendix, plan for security regression и готовность к обсуждению с командой.

## Теория

Финальный проект закрепляет новую роль: SDET отвечает не только за функциональное качество, но и за проверяемую безопасность продукта. Это не “разовая атака”, а управляемый security QA process.

### Что меняется относительно обычного пентеста

1. **Scope first:** SDET работает внутри продукта и обязан соблюдать границы стенда, данных и ролей.
2. **Evidence discipline:** любое доказательство должно быть sanitized и воспроизводимым.
3. **Risk-based thinking:** observation не равен finding; tool output не равен подтвержденной уязвимости.
4. **Automation with guardrails:** helpers должны иметь allowlist, timeout, rate limit, tests и понятный output.
5. **Remediation ownership:** задача не заканчивается отчетом; нужен backlog, owner, priority и retest.

### Итоговые артефакты

| Артефакт | Назначение |
|---|---|
| Rules of Engagement | Границы, запреты, contacts, stop conditions |
| Security Test Strategy | Риски, слои проверки, entry/exit criteria |
| Security Test Plan | Конкретные проверки, tools, safety limits |
| Threat Model | Entry points, abuse cases, expected controls |
| Evidence Index | Где лежат sanitized доказательства |
| Findings/Observations | Профессиональное описание результатов |
| Vulnerability Triage | Confidence, impact, severity, next action |
| Remediation Backlog | Что исправлять, кому и в каком порядке |
| Retest Plan | Как подтвердить исправление |
| Automation Appendix | Какие safe helpers использовались и какие guards есть |

## Практическое занятие

### Шаг 1. Scope и RoE

Заполните `education/security_process/RULES_OF_ENGAGEMENT.md` для своего финального assessment:

```markdown
Target: https://olddev.slider-ai.ru
In scope: доступные QA функции стенда
Out of scope: production, DoS/load, brute force, destructive payloads, secrets extraction
Stop conditions: 5xx spike, account lockout, unexpected data modification, secrets in evidence
```

### Шаг 2. Strategy и test plan

Заполните `SECURITY_TEST_STRATEGY.md` и `SECURITY_TEST_PLAN.md`:

- какие функции Slider AI проверяются;
- какие OWASP/WSTG категории применимы;
- какие checks выполняются manual/passive;
- какие checks требуют отдельного approval;
- какие helpers из блока 41-48 можно использовать безопасно.

### Шаг 3. Safe execution

Минимальный набор безопасных проверок:

1. HTTP/TLS/security headers через браузер, DevTools или безопасный helper.
2. Auth/session UX: сообщения ошибок, cookie flags, logout behavior без brute force.
3. Input handling через безопасные маркеры без script/SQL payload.
4. Access control через собственные QA-роли и разрешенные данные.
5. Public asset inventory без скачивания закрытого кода и без aggressive scan.
6. Passive Burp/ZAP review без active scan.

Каждый результат помечается статусом:

```text
finding / observation / not reproducible / not applicable / requires approval
```

### Шаг 4. Automation appendix

Используйте только safe helpers из блока 41-48:

```bash
python -m security_qa_helper --target https://olddev.slider-ai.ru --check headers --output evidence/headers.md
pytest tests/
```

В appendix укажите:

- helper name;
- allowlist;
- timeout/rate limit;
- what was collected;
- what was not collected;
- pytest result;
- link to sanitized output.

### Шаг 5. Findings, triage, remediation

Для каждого результата заполните `SECURITY_FINDING_TEMPLATE.md`. Затем перенесите итог в:

- `VULNERABILITY_TRIAGE.md`;
- `REMEDIATION_BACKLOG.md`;
- `RETEST_PLAN.md`.

### Шаг 6. Executive summary

Напишите 5-7 предложений для команды:

- что проверялось;
- какие ограничения были соблюдены;
- сколько findings/observations получено;
- какие top risks;
- что нужно исправить первым;
- когда и как делать retest.

## Примеры вывода

```text
$ pytest tests/
8 passed in 0.42s

$ python -m security_qa_helper --target https://olddev.slider-ai.ru --check headers --dry-run
{"target":"https://olddev.slider-ai.ru","check":"headers","dry_run":true,"secrets_masked":true}
```

Пример triage строки:

```markdown
| SEC-001 | Missing security header | observation | Medium QA | Header evidence | add header, retest with helper |
```

## Адаптация под macOS (M2, 8GB)

- Основной путь: PyCharm, terminal, browser, DevTools, Burp/ZAP passive, Python `.venv`.
- Не поднимайте тяжелую multi-VM инфраструктуру ради финального проекта.
- Для lab-only техник используйте THM/HTB/PortSwigger/INE cloud окружения.
- Все файлы отчета храните локально в `~/security-qa-workspace` или в согласованной папке проекта без секретов.

## Частые ошибки

1. Начать с инструментов, а не со scope/RoE.
2. Считать scanner output подтвержденной уязвимостью.
3. Вкладывать в evidence cookies, tokens, персональные данные или чужие данные.
4. Писать PoC без approval и stop conditions.
5. Завершить отчетом без remediation backlog и retest plan.
6. Не связать finding с продуктовым риском и owner.

## Вопросы на понимание

1. Чем финальный проект Security-aware SDET отличается от CTF write-up?
2. Почему observation и finding имеют разные критерии?
3. Какие checks требуют отдельного письменного approval?
4. Как доказать, что automation helper безопасен?
5. Что должно попасть в remediation backlog?
6. Как retest превращает finding обратно в контроль качества?

## Задачи для самостоятельного выполнения

1. Заполните RoE и test strategy для Slider AI.
2. Создайте threat model по 3-5 entry points.
3. Проведите безопасные manual/passive checks.
4. Оформите 1-3 findings/observations с sanitized evidence.
5. Подготовьте remediation backlog и retest plan.
6. Добавьте automation appendix по helper из блока 41-48.
7. Напишите executive summary для команды.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Final Security QA assessment

### Минимум

Соберите единый индекс артефактов: scope, test plan, checklist, observations, findings, retest items.

### Практика Slider AI

Подготовьте финальный отчет по `olddev.slider-ai.ru` с executive summary, technical findings/observations, evidence index, remediation backlog и retest plan.

### Углубление после изучения следующих уроков

После обсуждения с командой добавьте security regression backlog: какие checks должны стать регулярной частью QA/SDET процесса.

### Артефакт сдачи

Markdown-пакет по шаблонам из `education/security_process/` и `education/slider_ai_scope.md`: scope, strategy, test plan, threat model, findings, triage, remediation, retest, automation appendix.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемые sanitized артефакты и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.
