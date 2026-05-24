# Занятие 72. Финальный Security QA assessment Slider AI

## Учебная рамка

**Входные требования:** Завершены предыдущие блоки курса; студент понимает SDET-процесс, OWASP/WSTG, PTES, CVSS/QA severity, evidence handling, safe automation и ограничения Slider AI scope.

**Результат занятия:** Студент проводит безопасную всестороннюю проверку `olddev.slider-ai.ru` как Security-aware SDET: планирует scope, выполняет безопасные проверки, оформляет findings/observations, готовит remediation backlog, retest plan и automation appendix.

**Наследуемая SDET-компетенция:** security ownership: стратегия, RoE, risk scoring, remediation, retest и коммуникация с командой.

**Security QA-компетенция:** планирование и сопровождение полного security assessment: findings, risk, remediation, retest.

**Связь с книгами:** PTES/OWASP/CVSS как методология; «PyCharm. Профессиональная работа на Python 2024» — Git/VCS, Markdown evidence, debugger/HTTP Client; «Паттерны разработки на Python» — architecture appendix для safe helpers; «Black Hat Python» — только lab-only/detection interpretation.

**Основной источник:** «PyCharm. Профессиональная работа на Python 2024» и «Паттерны разработки на Python».

**Дополнительные источники:** Все книги курса как справочник для финального Security QA assessment и automation appendix.

**Что берем из источника:** strategy, RoE, evidence policy, triage, remediation, retest, security regression и ownership.

**Как это превращается в SDET/Security QA навык:** собрать полный безопасный assessment package для Slider AI olddev.

**Что нельзя переносить на Slider AI без отдельного разрешения:** финальный проект остается в рамках правилами Slider AI olddev из пользовательской инструкции курса; любые intrusive checks требуют отдельного approval.


**Процессный артефакт:** комплект встроенных шаблонов из пользовательской инструкции: RoE, strategy, test plan, finding, remediation backlog, retest plan и automation appendix.

**Безопасная цель:** Только `https://olddev.slider-ai.ru` в рамках правилами Slider AI olddev из пользовательской инструкции курса, либо учебные lab/CTF цели с явным разрешением. Production и любые другие домены исключены.

**Среда выполнения:** macOS native, PyCharm/terminal, браузер, DevTools, Burp/ZAP passive, Python helpers из блока 41-48. Kali/cloud lab используется только для lab-only техник и не переносится на Slider AI без отдельного письменного разрешения.

**Обязательный путь новичка:** Собрать scope, test plan, безопасные manual checks, sanitized evidence index, 1-3 observations/findings и retest plan.

**Углубление:** Добавить threat model, CVSS/QA severity rationale, automation appendix, remediation backlog с owners/priorities и executive summary для команды.

**Минимальная проверка успеха:** Финальный пакет содержит scope/RoE, методологию, ограничения, evidence, findings/observations, remediation и retest; все действия остаются в безопасном scope.

**Эталонный вывод:** Сданный пакет: report, evidence index, triage table, remediation backlog, retest plan, automation appendix и короткая защита результата.

**Критерии сдачи:** Зачет: полный безопасный assessment package. Отлично: ясная бизнес-интерпретация, приоритизация, automation appendix, plan for security regression и готовность к обсуждению с командой.

## Reading pack из книг курса

Книги курса использованы автором как источники для построения этой лекции, но не как обязательное домашнее чтение. Студенту не нужно искать недостающую теорию в отдельных файлах или внешних материалах: все понятия, команды, ограничения, безопасные примеры, ожидаемые результаты и критерии сдачи для темы `Занятие 72. Финальный Security QA assessment Slider AI` должны быть понятны из текущего урока.

В этом уроке книжные идеи переведены в учебную форму: сначала объясняется модель темы, затем показывается безопасная демонстрация, затем студент выполняет практику и оформляет evidence. Если книга описывает потенциально опасную технику, в курсе она используется только как lab-only или defensive interpretation и не переносится на Slider AI olddev без отдельного approval.


## Source-driven theory

Этот раздел не является заданием найти теорию в книгах. Книги использованы автором курса как системные источники для лекции `Занятие 72. Финальный Security QA assessment Slider AI`, а студент получает полное объяснение ниже.

Для этой темы опорная идея взята из источников: «PyCharm. Профессиональная работа на Python 2024», «Паттерны разработки на Python», «Объектно-ориентированный Python». Из них в урок перенесены не страницы как домашнее чтение, а инженерные принципы: пентест как процесс: strategy, RoE, scope, test plan, evidence, severity, report, remediation, retest и security regression. Поэтому лекция строится вокруг вопроса: как SDET, уже умеющий работать с тестами, артефактами и воспроизводимостью, превращает тему `Занятие 72. Финальный Security QA assessment Slider AI` в безопасную Security QA-практику.

Книжный материал адаптирован в три слоя. Первый слой — модель: какие сущности участвуют, как они связаны и где появляется риск. Второй слой — рабочий навык: ownership безопасности продукта: планирование, коммуникация риска, автоматизация регрессии, контроль исправлений. Третий слой — границы применения: документы процесса, безопасные проверки olddev, запрос approval для неоднозначных действий. Если техника может повредить данным, создать нагрузку, извлечь секреты, перебрать учетные записи или выйти за scope, она не переносится на Slider AI и остается только в lab-only/cloud-lab формате.

Такой подход важен для повышения квалификации QA: цель не “запустить хакерский инструмент”, а научиться отвечать за безопасность продукта так же дисциплинированно, как за функциональное качество. В каждом упражнении студент должен видеть разрешенную цель, среду выполнения, ожидаемый результат, критерий остановки и sanitized evidence.

## Теория

### 1. Предмет урока: Занятие 72. Финальный Security QA assessment Slider AI

Этот блок формирует ownership: security strategy, RoE, evidence, severity, remediation, retest и regression становятся частью ответственности SDET. В этом уроке центральная модель: Slider AI olddev assessment package: scope, RoE, test plan, evidence register, findings, retest и regression. Студент должен понять ее внутри самого Markdown-файла, без необходимости искать базовую теорию в книгах или внешних статьях.

Книги курса используются как источники автора: они дают системность, терминологию и инженерный взгляд. Но учебное действие здесь выполняется в лекции: понятие объясняется, затем показывается безопасный пример, затем студент делает минимальную практику и оформляет результат как evidence.

### 2. Модель и границы: Занятие 72. Финальный Security QA assessment Slider AI

Модель `Slider AI olddev assessment package: scope, RoE, test plan, evidence register, findings, retest и regression` нужно читать как набор связанных элементов, а не как список слов. В каждом упражнении есть субъект действия, разрешенная цель, технический механизм, наблюдаемый результат и решение: это `observation`, `finding`, `not applicable`, `not reproducible` или `requires approval`.

Граница безопасности для этого урока: запрещено действия вне scope или без approval. Если такое действие технически нужно для обучения, оно переносится в lab-only/cloud lab или формулируется как запрос approval. Для Slider AI используется только `https://olddev.slider-ai.ru` и только действия, совместимые с правилами Slider AI olddev из пользовательской инструкции курса.

### 3. Ключевые понятия: Занятие 72. Финальный Security QA assessment Slider AI

`Target` — конкретная разрешенная цель: локальная папка, localhost, учебная лаборатория, cloud lab или olddev-стенд.

`Mechanism` — технический механизм урока: Slider AI olddev assessment package: scope, RoE, test plan, evidence register, findings, retest и regression. Его нужно объяснить до команды или инструмента.

`Expected result` — заранее понятный безопасный результат. Если студент не знает, что должно измениться или появиться в выводе, практика еще не готова.

`Evidence` — минимальный sanitized артефакт: среда, цель, действие, фактический результат, интерпретация и следующий шаг.

`Stop condition` — условие остановки. Оно срабатывает при ошибке scope, появлении секретов/PII, признаках нагрузки, необходимости перебора или неоднозначности разрешения.

### 4. SDET-практика: Занятие 72. Финальный Security QA assessment Slider AI

SDET подходит к теме как к тестируемому процессу. Сначала формулируется гипотеза: что именно проверяется и почему это влияет на безопасность продукта. Затем выбирается минимальное действие: локальная команда, ручной шаг, DevTools-наблюдение, lab-only payload или safe helper. После этого результат оформляется так, чтобы разработчик, тимлид или security owner мог его повторить.

Минимальный результат урока: оформить воспроизводимый артефакт по модели: Slider AI olddev assessment package: scope, RoE, test plan, evidence register, findings, retest и regression. Если результат не достигается, студент должен уметь объяснить, чего не хватает: разрешения, среды, тестовых данных, изученного инструмента или безопасной лаборатории.

### 5. Безопасная среда для урока

Базовая среда курса — macOS native на MacBook Air M2. Для macOS используются Homebrew, официальные installers, браузер, DevTools, Burp/ZAP в безопасном режиме, Python и локальные файлы. Команды Linux/Kali должны быть явно помечены как Kali/Linux или cloud lab.

Kali ARM64 VM используется как углубление, когда нужна изоляция, Kali-специфичный инструмент или экзаменационная практика. На 8GB RAM VM ограничивается 3-4GB RAM и 2 CPU. Тяжелые сценарии и CTF выполняются в TryHackMe AttackBox, HackTheBox/Pwnbox, PortSwigger Academy или аналогичной легальной среде.

### 6. Как читать результат в этой теме

Результат читается через контрольные признаки, относящиеся именно к теме урока. Для команд это target, статус выполнения, ключевая строка вывода и ошибка. Для HTTP это method, path, status code, selected headers и безопасно очищенный body fragment. Для Python helper это входные параметры, отказ policy, timeout, status и JSON/Markdown output. Для процессных документов это scope, owner, evidence, severity, remediation и retest.

Вывод инструмента или команды не является автоматическим finding. Сначала это observation. Finding появляется только после проверки контекста, влияния, воспроизводимости и границ разрешения.

### 7. Типичные ошибки: Занятие 72. Финальный Security QA assessment Slider AI

Первая ошибка — выполнять практику до понимания модели `Slider AI olddev assessment package: scope, RoE, test plan, evidence register, findings, retest и regression`. Это превращает обучение в копирование команд.

Вторая ошибка — не отделять lab-only от product-safe. То, что разрешено в CTF или deliberately vulnerable VM, не становится разрешенным на Slider AI.

Третья ошибка — сохранять лишние данные. Evidence не должен содержать cookies, токены, пароли, приватные ключи, персональные данные, полные ответы с секретами или чужие данные.

Четвертая ошибка — путать observation и finding. Наблюдение полезно, но оно требует интерпретации и triage.

### 8. Связь с книгами и SDET-базой

Из SDET Python QA Automation Apprenticeship сюда переносится дисциплина: входные требования, повторяемые шаги, фактический результат, тестовые артефакты, отчетность и регрессия. Из книг курса автор берет системность и инженерный язык, но не перекладывает обучение на студента.

Студент должен выйти из урока с рабочим пониманием: что такое Slider AI olddev assessment package: scope, RoE, test plan, evidence register, findings, retest и regression, как это безопасно проверить, что приложить как evidence и какие действия требуют approval.

### 9. Проверка понимания перед практикой

Перед практикой студент отвечает на пять вопросов:

1. Какая цель разрешена?
2. Какой механизм урока используется?
3. Какой результат ожидается?
4. Где stop condition?
5. Что будет приложено как sanitized evidence?

Если на один вопрос нет ответа, практика не выполняется. Сначала уточняется scope, выбирается lab или уменьшается действие до безопасного наблюдения.

### 10. Минимальная планка по уроку

Лекция считается освоенной, если студент может объяснить `Slider AI olddev assessment package: scope, RoE, test plan, evidence register, findings, retest и regression` своими словами, выполнить безопасный путь новичка, получить ожидаемый вывод, интерпретировать его и оформить evidence. Для темы `Занятие 72. Финальный Security QA assessment Slider AI` минимальная сдача — оформить воспроизводимый артефакт по модели: Slider AI olddev assessment package: scope, RoE, test plan, evidence register, findings, retest и regression, без нарушения ограничения: действия вне scope или без approval.


### 11. Разбор учебного артефакта

В каждом уроке студент должен уметь показать не только выполненное действие, но и его смысл. Артефакт читается так: сначала указывается среда, затем разрешенная цель, затем действие, затем фактический результат, затем интерпретация. Если артефактом является команда, важно сохранить саму команду и 3-10 строк вывода. Если артефактом является браузерное наблюдение, сохраняется путь в UI, статус запроса, выбранные headers или sanitized screenshot. Если артефактом является документ процесса, в нем должны быть scope, owner, ограничения, evidence и следующий шаг.

Ошибкой считается артефакт без интерпретации. Например, строка вывода сама по себе не доказывает навык. Студент должен объяснить, почему строка важна, какой риск она подтверждает или не подтверждает, и что команда не нарушила scope. Такой формат делает курс самодостаточным: студент учится прямо в лекции читать результат, а не искать объяснение в другом источнике.

### 12. Минимум, Slider AI и углубление

Обязательный минимум выполняется в безопасной среде: macOS native, локальный файл, localhost, браузер, DevTools или одиночное разрешенное наблюдение. Этот минимум нужен для формирования базового навыка без лишней когнитивной нагрузки. В нем не должно быть действий, которые могут повлиять на чужие данные, вызвать нагрузку или потребовать специальных разрешений.

Практика Slider AI всегда ограничена `https://olddev.slider-ai.ru` и правилами Slider AI olddev из пользовательской инструкции курса. Если тема урока потенциально опасна, Slider AI-задание формулируется как наблюдение, checklist, evidence draft, request for approval или transfer note. Углубление выполняется только после изучения следующих уроков и только в lab/cloud lab, где правила явно разрешают такие действия.

### 13. Критерии академической сдачи

Зачет по уроку требует четырех вещей: студент объясняет модель темы своими словами, выполняет безопасный путь, получает ожидаемый результат и оформляет sanitized evidence. Хороший уровень добавляет анализ ограничений: что не проверялось и почему. Отличный уровень добавляет перенос в SDET ownership: как превратить результат в regression check, finding draft, retest step или improvement для security process.

Если студент может только повторить команду, урок не засчитан как самостоятельное освоение. Если студент понимает, когда остановиться и как запросить approval, это считается частью профессиональной квалификации. Именно это отличает курс повышения квалификации QA/SDET от набора разрозненных pentest-рецептов.


### 14. Самостоятельное объяснение без внешних источников

После чтения лекции студент должен суметь пересказать тему человеку из команды, который не присутствовал на занятии. Такое объяснение должно включать четыре части. Первая часть — техническая модель: какие компоненты участвуют и почему они важны. Вторая часть — безопасная демонстрация: какое минимальное действие показывает работу модели без риска для продукта. Третья часть — evidence: какие строки, скриншоты или поля документа подтверждают результат. Четвертая часть — границы: что нельзя делать на olddev без approval и куда переносится углубление.

Этот пересказ является обязательной частью самодостаточности курса. Книги остаются источниками автора, но рабочее знание, необходимое для выполнения заданий, находится внутри урока: термины, причина, пример, безопасная команда или ручной шаг, эталон вывода и критерии сдачи.

### 15. Перенос в профессиональную работу SDET/Security QA

В реальной команде результат урока должен превращаться в рабочее действие: test case, checklist item, automation helper, finding draft, retest step или regression guard. Поэтому студент фиксирует не только “что получилось”, но и “как это поможет команде снизить риск”. Если проверка ничего не выявила, это тоже полезный результат, но он оформляется как `observation` или `not applicable`, а не как найденная уязвимость.

Профессиональная зрелость проявляется в умении остановиться. Если дальнейший шаг требует перебора, активного сканирования, payload, доступа к чужим данным, изменения состояния или анализа секретов, студент не выполняет его на Slider AI. Он записывает limitation, выбирает lab-only среду или оформляет approval request. Такая дисциплина делает курс пригодным для самообразования и для повышения квалификации QA, потому что учит не только технике, но и ответственности за безопасность продукта.

## Guided practice

1. Выберите финальный артефакт урока: RoE, checklist, finding, score, backlog, retest или appendix.
2. Заполните шаблон процесса на безопасном Slider AI-примере без секретов.
3. Свяжите результат с продуктовым риском, owner action и проверкой исправления.
4. Добавьте артефакт в итоговый assessment package и отметьте limitations.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Шаг 1. Scope и RoE

Заполните раздел `Rules of Engagement` для своего финального assessment:

```markdown
Target: https://olddev.slider-ai.ru
In scope: доступные QA функции стенда
Out of scope: production, DoS/load, brute force, destructive payloads, secrets extraction
Stop conditions: 5xx spike, account lockout, unexpected data modification, secrets in evidence
```

### Шаг 2. Strategy и test plan

Заполните в рабочих заметках встроенные шаблоны Security Test Strategy и Security Test Plan:

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

Для каждого результата заполните встроенный Finding Template. Затем перенесите итог в рабочие разделы triage, remediation и retest:

- Vulnerability Triage;
- Remediation Backlog;
- Retest Plan.

### Шаг 6. Executive summary

Напишите 5-7 предложений для команды:

- что проверялось;
- какие ограничения были соблюдены;
- сколько findings/observations получено;
- какие top risks;
- что нужно исправить первым;
- когда и как делать retest.

### План выполнения в 4 рабочие сессии

| Сессия | Цель | Артефакт | Stop condition |
|---|---|---|---|
| 1 | Scope, RoE, Evidence Policy, Tooling Policy | заполненные правила и approval boundaries | нет разрешенной цели или тестовых учеток |
| 2 | Threat Model и WSTG checklist | 3-5 entry points, role matrix, safe checklist | требуется чужой аккаунт/данные |
| 3 | Safe execution | evidence index, observations, candidate findings | нужен payload, active scan, brute force или изменение данных |
| 4 | Triage/report/retest | final package, backlog, retest plan, executive summary | evidence содержит секреты или не воспроизводится |

### Итоговый assessment package

Финальный пакет собирается в рабочих заметках студента по встроенным шаблонам из пользовательской инструкции. Минимальный индекс:

```markdown
# Slider AI olddev Security QA Assessment Package

## 1. Rules of Engagement
## 2. Security Test Strategy
## 3. Evidence Policy
## 4. Tooling Policy / Tooling Approval Card
## 5. Security Test Plan
## 6. Threat Model
## 7. WSTG / OWASP Safe Checklist
## 8. Role Matrix And Tenant Boundary Notes
## 9. Evidence Index
## 10. Findings And Observations
## 11. Vulnerability Triage
## 12. Remediation Backlog
## 13. Retest Plan
## 14. Security Automation Architecture / Appendix
## 15. Executive Summary
```

### Acceptance checklist

- [ ] Target указан только как `https://olddev.slider-ai.ru`.
- [ ] Production и любые другие домены явно out of scope.
- [ ] Есть Rules of Engagement и stop conditions.
- [ ] Есть Evidence Policy и примеры redaction.
- [ ] Есть Tooling Policy для Burp/ZAP/Python helpers.
- [ ] Threat Model содержит assets, actors, trust boundaries, entry points и abuse cases.
- [ ] Role matrix отделяет owner/editor/viewer/anonymous или доступные QA-роли.
- [ ] WSTG checklist покрывает information gathering, config, auth/session, authorization, input validation, error handling.
- [ ] Access Control/IDOR отмечен как safe matrix или `requires approval`, а не как перебор ID.
- [ ] API Security отражает REST/OpenAPI/JWT/CORS/GraphQL как безопасные observations или lab-only.
- [ ] File upload, path traversal, command injection, SSTI, deserialization, SSRF и race conditions имеют boundaries.
- [ ] Burp/ZAP использованы в passive/manual режиме либо отмечены как approval-required.
- [ ] Python helper имеет allowlist, timeout, output contract и pytest evidence.
- [ ] Evidence не содержит cookies, tokens, passwords, PII, чужих данных и полных sensitive responses.
- [ ] Каждый результат имеет статус `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.
- [ ] Findings содержат business impact, steps, evidence, recommendation и retest criteria.
- [ ] Remediation backlog содержит owner/action/priority/acceptance criteria.
- [ ] Retest plan показывает, как подтвердить исправление без unsafe действий.
- [ ] Executive summary понятен продуктовой команде, а не только security-специалисту.
- [ ] Все ограничения и непроверенные области записаны как limitations.

## Примеры вывода

Минимальный эталонный артефакт для сдачи по теме `Занятие 72. Финальный Security QA assessment Slider AI`:

```markdown
Environment: macOS native, Apple Silicon
Target: https://olddev.slider-ai.ru
Scope status: allowed observation within пользовательской инструкцией курса
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

**Ограничения безопасности:** соблюдать правилами Slider AI olddev из пользовательской инструкции курса; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Final Security QA assessment

### Минимум

Соберите единый индекс артефактов: scope, test plan, checklist, observations, findings, retest items.

### Практика Slider AI

Подготовьте финальный отчет по `olddev.slider-ai.ru` с executive summary, technical findings/observations, evidence index, remediation backlog и retest plan.

### Углубление после изучения следующих уроков

После обсуждения с командой добавьте security regression backlog: какие checks должны стать регулярной частью QA/SDET процесса.

### Артефакт сдачи

Markdown-пакет по правилам Slider AI olddev из пользовательской инструкции курса: scope, strategy, test plan, threat model, findings, triage, remediation, retest, automation appendix.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемые sanitized артефакты и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `Final Security QA Assessment`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
