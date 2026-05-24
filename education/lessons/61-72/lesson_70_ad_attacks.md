# Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync

## Учебная рамка

**Входные требования:** Понимание полного цикла пентеста, базовые навыки отчетности и опыт работы с учебными лабораториями.

**Результат занятия:** Студент применяет методологию, оформляет артефакт профессионального уровня и отделяет факты от предположений.

**Наследуемая SDET-компетенция:** security ownership: стратегия, RoE, risk scoring, remediation, retest и коммуникация с командой.

**Security QA-компетенция:** планирование и сопровождение полного security assessment: findings, risk, remediation, retest.

**Связь с книгами:** PTES, OWASP Testing Guide, CVSS и «PyCharm. Профессиональная работа на Python 2024» для reporting, Git/VCS, Markdown evidence и процесса.

**Основной источник:** «PyCharm. Профессиональная работа на Python 2024» и «Паттерны разработки на Python».

**Дополнительные источники:** Все книги курса как справочник для финального Security QA assessment и automation appendix.

**Что берем из источника:** strategy, RoE, evidence policy, triage, remediation, retest, security regression и ownership.

**Как это превращается в SDET/Security QA навык:** собрать полный безопасный assessment package для Slider AI olddev.

**Что нельзя переносить на Slider AI без отдельного разрешения:** финальный проект остается в рамках `education/slider_ai_scope.md`; любые intrusive checks требуют отдельного approval.


**Процессный артефакт:** `REMEDIATION_BACKLOG.md` или `RETEST_PLAN.md`: приоритизация, владелец, retest evidence.

**Безопасная цель:** Учебный scope, подписанный RoE, собственная лаборатория или платформа с явным разрешением. Реальные организации только с письменным согласием.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Заполнить шаблон документа/чек-листа по учебному кейсу и связать каждую находку с доказательством.

**Углубление:** Добавить приоритизацию рисков, executive summary, ограничения тестирования и план повторной проверки.

**Минимальная проверка успеха:** Документ содержит scope, методологию, доказательства, ограничения и понятные рекомендации.

**Эталонный вывод:** Сданный артефакт: отчет, чек-лист, RoE, матрица рисков или презентация с проверяемыми доказательствами.

**Критерии сдачи:** Зачет: полный артефакт по шаблону. Отлично: ясная бизнес-интерпретация, приоритизация и план remediation.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/pycharm-professional-python-2024-pages/`
- `docs/socraticode/architecture-patterns-python-pages/`

Конкретные страницы для этого блока: `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md`; `page-437.md`-`page-466.md`; `architecture-patterns-python-pages/page-038.md`-`page-129.md`.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот раздел не является заданием найти теорию в книгах. Книги использованы автором курса как системные источники для лекции `Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync`, а студент получает полное объяснение ниже.

Для этой темы опорная идея взята из источников: «PyCharm. Профессиональная работа на Python 2024», «Паттерны разработки на Python», «Объектно-ориентированный Python». Из них в урок перенесены не страницы как домашнее чтение, а инженерные принципы: пентест как процесс: strategy, RoE, scope, test plan, evidence, severity, report, remediation, retest и security regression. Поэтому лекция строится вокруг вопроса: как SDET, уже умеющий работать с тестами, артефактами и воспроизводимостью, превращает тему `Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync` в безопасную Security QA-практику.

Книжный материал адаптирован в три слоя. Первый слой — модель: какие сущности участвуют, как они связаны и где появляется риск. Второй слой — рабочий навык: ownership безопасности продукта: планирование, коммуникация риска, автоматизация регрессии, контроль исправлений. Третий слой — границы применения: документы процесса, безопасные проверки olddev, запрос approval для неоднозначных действий. Если техника может повредить данным, создать нагрузку, извлечь секреты, перебрать учетные записи или выйти за scope, она не переносится на Slider AI и остается только в lab-only/cloud-lab формате.

Такой подход важен для повышения квалификации QA: цель не “запустить хакерский инструмент”, а научиться отвечать за безопасность продукта так же дисциплинированно, как за функциональное качество. В каждом упражнении студент должен видеть разрешенную цель, среду выполнения, ожидаемый результат, критерий остановки и sanitized evidence.

## Теория

### 1. Зачем SDET изучает эту тему

Тема `Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync` нужна не как отдельный набор команд, а как часть профессионального перехода от обычного QA/SDET к специалисту, который отвечает за качество и безопасность продукта. SDET уже привык проверять поведение системы, фиксировать воспроизводимые шаги, отделять факт от предположения и оформлять результат так, чтобы разработчик мог его повторить. В Security QA добавляется еще один слой: каждое действие должно быть разрешенным, ограниченным по scope и безопасным для данных, пользователей и инфраструктуры.

В этой лекции базовая задача состоит в том, чтобы понять модель `пентест как процесс: strategy, RoE, scope, test plan, evidence, severity, report, remediation, retest и security regression` и научиться превращать ее в проверяемый артефакт. Артефактом может быть команда, скриншот DevTools, HTTP history, лог, Markdown-заметка, JSON-вывод helper-скрипта, checklist или черновик finding. Главное требование: другой инженер должен понять, что было проверено, где, с каким разрешением и почему результат имеет значение.

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

Для темы `Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync` минимальная планка такая: студент понимает пентест как процесс: strategy, RoE, scope, test plan, evidence, severity, report, remediation, retest и security regression, выполняет безопасную практику в среде `документы процесса, безопасные проверки olddev, запрос approval для неоднозначных действий`, объясняет результат через ownership безопасности продукта: планирование, коммуникация риска, автоматизация регрессии, контроль исправлений и не выходит за ограничения Slider AI. Все, что требует более агрессивной техники, переносится в углубление после изучения следующих уроков или оформляется как `requires approval`.

### 11. Контроль понимания перед практикой

Перед переходом к заданиям студент должен остановиться и проговорить тему как инженерную процедуру. Нужно назвать разрешенную цель, среду выполнения, минимальное действие, ожидаемый безопасный результат и критерий остановки. Если хотя бы один пункт неясен, практика не начинается: сначала уточняется scope или выбирается локальная лабораторная цель. Такой контроль снижает риск случайно выполнить активную проверку там, где требовалось только наблюдение.

Второй контрольный вопрос: какие данные попадут в evidence? В отчет нельзя переносить cookies, токены, персональные данные, приватные ключи, полные ответы с секретами и любые сведения, которые не нужны для доказательства результата. Хороший SDET собирает ровно столько фактов, сколько нужно для воспроизведения и принятия решения.


### 12. Предметная часть урока

Для темы `Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync` предметная суть — управление процессом безопасности как частью качества продукта. Стандарт, метрика, отчет или финальный проект не должны оставаться списком пунктов. Каждый пункт превращается в действие: определить scope, выбрать test case, собрать evidence, классифицировать риск, назначить owner action, проверить исправление и добавить regression coverage.

Процессный урок учит не только “что такое PTES/OWASP/CVSS”, а как применить эти рамки к реальному SDET workflow. Severity без evidence бесполезна. Report без retest plan неполон. Test plan без RoE опасен. Automation без ownership быстро превращается в шум. Поэтому каждый документ курса должен отвечать на практический вопрос: какое решение команда может принять на основе этого артефакта?

Для Slider AI процессная практика безопасна: студент строит план, checklist, evidence register, finding draft и retest plan на olddev-scope. Все неоднозначные активные действия получают статус `requires approval`, а финальный проект показывает зрелость специалиста: он умеет не только найти риск, но и провести его через remediation и regression.


## Guided practice

1. Выберите финальный артефакт урока: RoE, checklist, finding, score, backlog, retest или appendix.
2. Заполните шаблон процесса на безопасном Slider AI-примере без секретов.
3. Свяжите результат с продуктовым риском, owner action и проверкой исправления.
4. Добавьте артефакт в итоговый assessment package и отметьте limitations.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Настройка лаборатории AD

**Варианты:**
1. **GOAD (Game of Active Directory)** — готовая лаборатория с уязвимостями
   - GitHub: https://github.com/Orange-Cyberdefense/GOAD
   - Требует VirtualBox/Vagrant или Proxmox и не подходит как локальный базовый путь для MacBook Air M2 8GB
   - 5+ машин, реалистичная структура

2. **DetectionLab** — лаборатория для тестирования защиты
   - GitHub: https://github.com/clong/DetectionLab
   - Требует значительных ресурсов; для M2 8GB предпочтительнее cloud lab

3. **Простая лаба (ручная настройка):**
   - 1x Windows Server 2019 (Domain Controller)
   - 1x Windows 10 (клиент домена)
   - Kali Linux (атакующий)
   
   Настройте DC, создайте несколько пользователей, настройте SPN для одного пользователя, установите слабый пароль.

Для MacBook Air M2 (8GB) основной путь этого урока — HackTheBox Academy AD Path или TryHackMe AD Rooms. Локальные AD-лаборатории из нескольких Windows VM считать углублением вне базовой конфигурации.

### Lab-only awareness: как читать write-up, не превращая его в действие по продукту

Этот раздел не является обязательным hands-on путем для MacBook Air M2 8GB и не применяется к Slider AI. Используйте его только для разбора write-up в HTB/THM/INE AD lab, где такие техники явно разрешены.

#### Kerberoasting risk flow

```bash
# LAB-ONLY PSEUDOCODE:
# 1. Identify service accounts with SPN in the authorized AD lab.
# 2. Request a service ticket in the lab.
# 3. Record defensive evidence: weak service-account policy, missing monitoring, excessive privileges.
# 4. Do not run this flow against Slider AI or any real AD without written RoE.
```

#### ASREPRoasting risk flow

```bash
# LAB-ONLY PSEUDOCODE:
# 1. In an authorized AD lab, identify accounts without pre-authentication.
# 2. Document why this creates offline guessing risk.
# 3. Convert the result into a defensive checklist: enable pre-auth, monitor events, enforce password policy.
```

#### DCSync risk flow

```bash
# LAB-ONLY PSEUDOCODE:
# 1. In an authorized AD lab, review which accounts have replication rights.
# 2. Explain why replication rights can expose domain secrets.
# 3. Do not collect or print hashes in course artifacts.
# 4. Document defensive controls: least privilege, alerting, Event ID review, krbtgt rotation procedure.
```

### BloodHound сбор данных и анализ

```bash
# На Windows-цели (скомпрометированная машина):
# Скачать SharpHound: https://github.com/BloodHoundAD/SharpHound
SharpHound.exe -c All

# Или использовать bloodhound-python с Kali:
pip3 install bloodhound
bloodhound-python -u user -p password -d CORP.local -dc dc01.corp.local -c all

# Запустить Neo4j и BloodHound
neo4j start
bloodhound

# Загрузить .json файлы через интерфейс BloodHound
# Запустить встроенные запросы:
# - Find all Domain Admins
# - Find Shortest Paths to Domain Admins
# - List all Kerberoastable users
# - List all ASREPRoastable users
```



## Примеры вывода

Минимальный эталонный артефакт для сдачи по теме `Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync`:

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

- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`; для явно помеченной Kali/Linux-среды допустим `apt`.
- Kali/Linux VM запускайте только как углубление и выделяйте не более 3-4GB RAM на MacBook Air M2 (8GB)
- Если нужна Kali/Linux VM на Apple Silicon, используйте ARM64-образ в UTM/VMware Fusion/Parallels; не используйте x86/x64 VM как базовый путь.
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты


## Задачи для самостоятельного выполнения

1. **Kerberoasting defensive lab**: В HTB/THM/INE AD lab разберите готовый write-up или выполните разрешенную lab-задачу. В отчете не публикуйте хеши/пароли; опишите риск, признаки detection и remediation.

2. **ASREPRoasting defensive lab**: Опишите, почему `DONT_REQ_PREAUTH` опасен, какие политики должны быть включены и какие события мониторить. Hands-on только в cloud lab с явным разрешением.

3. **BloodHound Analysis**: Установите BloodHound, соберите данные из тестового домена (или GOAD). Найдите 3 пути к Domain Admin. Сделайте скриншоты графов.

4. **Mitigation Research**: Напишите рекомендации по защите от Kerberoasting, ASREPRoasting и DCSync. Что должны делать администраторы? Какие политики настроить? Какие инструменты мониторинга использовать?

5. **DCSync detection**: Изучите, какие права и события связаны с DCSync. Напишите detection/remediation checklist, не описывая пошаговое получение хешей и не публикуя секреты.

## Частые ошибки

1. **Неправильная настройка SharpHound** — запуск без прав администратора домена может привести к неполным данным.
2. **Игнорирование латерального движения** — компрометация одной машины не означает доступ к AD. Нужно искать пути к Domain Admin.
3. **Плохой подбор паролей** — для Kerberoasting и ASREPRoasting используйте актуальные словари (rockyou.txt, сгенерированные cewl).
4. **Неправильное использование CrackMapExec** — запуск без указания правильных протоколов может привести к пропуску уязвимых хостов.

## Вопросы на понимание

1. В чем разница между Kerberoasting и ASREPRoasting?
2. Что такое DCSync и какие права нужны для его выполнения?
3. Как собрать данные для BloodHound с помощью SharpHound?
4. Почему на Mac с 8GB RAM нельзя запускать локальные AD лабы?
5. Как установить CrackMapExec и для чего он используется?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** AD attacks as theory for QA

### Минимум

Не применять AD-атаки к Slider AI; определить, есть ли SSO/AD как область вопросов к владельцам.

### Практика Slider AI

Составьте defensive checklist: MFA, service accounts, logs, least privilege, owner.

### Углубление после изучения следующих уроков

После отдельного AD scope используйте только лабораторные техники, не продуктовый стенд.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

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
