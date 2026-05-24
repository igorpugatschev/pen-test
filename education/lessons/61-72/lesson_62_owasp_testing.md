# Занятие 62. OWASP Testing Guide: структура теста веб-приложений

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

**Что нельзя переносить на Slider AI без отдельного разрешения:** финальный проект остается в рамках правилами Slider AI olddev из пользовательской инструкции курса; любые intrusive checks требуют отдельного approval.


**Процессный артефакт:** встроенный remediation backlog или retest plan из пользовательской инструкции: приоритизация, владелец, retest evidence.

**Безопасная цель:** Учебный scope, подписанный RoE, собственная лаборатория или платформа с явным разрешением. Реальные организации только с письменным согласием.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Заполнить шаблон документа/чек-листа по учебному кейсу и связать каждую находку с доказательством.

**Углубление:** Добавить приоритизацию рисков, executive summary, ограничения тестирования и план повторной проверки.

**Минимальная проверка успеха:** Документ содержит scope, методологию, доказательства, ограничения и понятные рекомендации.

**Эталонный вывод:** Сданный артефакт: отчет, чек-лист, RoE, матрица рисков или презентация с проверяемыми доказательствами.

**Критерии сдачи:** Зачет: полный артефакт по шаблону. Отлично: ясная бизнес-интерпретация, приоритизация и план remediation.

## Reading pack из книг курса

Книги курса использованы автором как источники для построения этой лекции, но не как обязательное домашнее чтение. Студенту не нужно искать недостающую теорию в отдельных файлах или внешних материалах: все понятия, команды, ограничения, безопасные примеры, ожидаемые результаты и критерии сдачи для темы `Занятие 62. OWASP Testing Guide: структура теста веб-приложений` должны быть понятны из текущего урока.

В этом уроке книжные идеи переведены в учебную форму: сначала объясняется модель темы, затем показывается безопасная демонстрация, затем студент выполняет практику и оформляет evidence. Если книга описывает потенциально опасную технику, в курсе она используется только как lab-only или defensive interpretation и не переносится на Slider AI olddev без отдельного approval.


## Source-driven theory

Этот раздел не является заданием найти теорию в книгах. Книги использованы автором курса как системные источники для лекции `Занятие 62. OWASP Testing Guide: структура теста веб-приложений`, а студент получает полное объяснение ниже.

Для этой темы опорная идея взята из источников: «PyCharm. Профессиональная работа на Python 2024», «Паттерны разработки на Python», «Объектно-ориентированный Python». Из них в урок перенесены не страницы как домашнее чтение, а инженерные принципы: пентест как процесс: strategy, RoE, scope, test plan, evidence, severity, report, remediation, retest и security regression. Поэтому лекция строится вокруг вопроса: как SDET, уже умеющий работать с тестами, артефактами и воспроизводимостью, превращает тему `Занятие 62. OWASP Testing Guide: структура теста веб-приложений` в безопасную Security QA-практику.

Книжный материал адаптирован в три слоя. Первый слой — модель: какие сущности участвуют, как они связаны и где появляется риск. Второй слой — рабочий навык: ownership безопасности продукта: планирование, коммуникация риска, автоматизация регрессии, контроль исправлений. Третий слой — границы применения: документы процесса, безопасные проверки olddev, запрос approval для неоднозначных действий. Если техника может повредить данным, создать нагрузку, извлечь секреты, перебрать учетные записи или выйти за scope, она не переносится на Slider AI и остается только в lab-only/cloud-lab формате.

Такой подход важен для повышения квалификации QA: цель не “запустить хакерский инструмент”, а научиться отвечать за безопасность продукта так же дисциплинированно, как за функциональное качество. В каждом упражнении студент должен видеть разрешенную цель, среду выполнения, ожидаемый результат, критерий остановки и sanitized evidence.

## Теория

### 1. Предмет урока: Занятие 62. OWASP Testing Guide: структура теста веб-приложений

Этот блок формирует ownership: security strategy, RoE, evidence, severity, remediation, retest и regression становятся частью ответственности SDET. В этом уроке центральная модель: WSTG category, test objective, safe test case, evidence register, status и approval boundary. Студент должен понять ее внутри самого Markdown-файла, без необходимости искать базовую теорию в книгах или внешних статьях.

Книги курса используются как источники автора: они дают системность, терминологию и инженерный взгляд. Но учебное действие здесь выполняется в лекции: понятие объясняется, затем показывается безопасный пример, затем студент делает минимальную практику и оформляет результат как evidence.

### 2. Модель и границы: структура теста веб-приложений

Модель `WSTG category, test objective, safe test case, evidence register, status и approval boundary` нужно читать как набор связанных элементов, а не как список слов. В каждом упражнении есть субъект действия, разрешенная цель, технический механизм, наблюдаемый результат и решение: это `observation`, `finding`, `not applicable`, `not reproducible` или `requires approval`.

Граница безопасности для этого урока: запрещено действия вне scope или без approval. Если такое действие технически нужно для обучения, оно переносится в lab-only/cloud lab или формулируется как запрос approval. Для Slider AI используется только `https://olddev.slider-ai.ru` и только действия, совместимые с правилами Slider AI olddev из пользовательской инструкции курса.

### 3. Ключевые понятия: структура теста веб-приложений

`Target` — конкретная разрешенная цель: локальная папка, localhost, учебная лаборатория, cloud lab или olddev-стенд.

`Mechanism` — технический механизм урока: WSTG category, test objective, safe test case, evidence register, status и approval boundary. Его нужно объяснить до команды или инструмента.

`Expected result` — заранее понятный безопасный результат. Если студент не знает, что должно измениться или появиться в выводе, практика еще не готова.

`Evidence` — минимальный sanitized артефакт: среда, цель, действие, фактический результат, интерпретация и следующий шаг.

`Stop condition` — условие остановки. Оно срабатывает при ошибке scope, появлении секретов/PII, признаках нагрузки, необходимости перебора или неоднозначности разрешения.

### 4. SDET-практика: структура теста веб-приложений

SDET подходит к теме как к тестируемому процессу. Сначала формулируется гипотеза: что именно проверяется и почему это влияет на безопасность продукта. Затем выбирается минимальное действие: локальная команда, ручной шаг, DevTools-наблюдение, lab-only payload или safe helper. После этого результат оформляется так, чтобы разработчик, тимлид или security owner мог его повторить.

Минимальный результат урока: оформить воспроизводимый артефакт по модели: WSTG category, test objective, safe test case, evidence register, status и approval boundary. Если результат не достигается, студент должен уметь объяснить, чего не хватает: разрешения, среды, тестовых данных, изученного инструмента или безопасной лаборатории.

### 5. Безопасная среда для урока

Базовая среда курса — macOS native на MacBook Air M2. Для macOS используются Homebrew, официальные installers, браузер, DevTools, Burp/ZAP в безопасном режиме, Python и локальные файлы. Команды Linux/Kali должны быть явно помечены как Kali/Linux или cloud lab.

Kali ARM64 VM используется как углубление, когда нужна изоляция, Kali-специфичный инструмент или экзаменационная практика. На 8GB RAM VM ограничивается 3-4GB RAM и 2 CPU. Тяжелые сценарии и CTF выполняются в TryHackMe AttackBox, HackTheBox/Pwnbox, PortSwigger Academy или аналогичной легальной среде.

### 6. Как читать результат в этой теме

Результат читается через контрольные признаки, относящиеся именно к теме урока. Для команд это target, статус выполнения, ключевая строка вывода и ошибка. Для HTTP это method, path, status code, selected headers и безопасно очищенный body fragment. Для Python helper это входные параметры, отказ policy, timeout, status и JSON/Markdown output. Для процессных документов это scope, owner, evidence, severity, remediation и retest.

Вывод инструмента или команды не является автоматическим finding. Сначала это observation. Finding появляется только после проверки контекста, влияния, воспроизводимости и границ разрешения.

### 7. Типичные ошибки: структура теста веб-приложений

Первая ошибка — выполнять практику до понимания модели `WSTG category, test objective, safe test case, evidence register, status и approval boundary`. Это превращает обучение в копирование команд.

Вторая ошибка — не отделять lab-only от product-safe. То, что разрешено в CTF или deliberately vulnerable VM, не становится разрешенным на Slider AI.

Третья ошибка — сохранять лишние данные. Evidence не должен содержать cookies, токены, пароли, приватные ключи, персональные данные, полные ответы с секретами или чужие данные.

Четвертая ошибка — путать observation и finding. Наблюдение полезно, но оно требует интерпретации и triage.

### 8. Связь с книгами и SDET-базой

Из SDET Python QA Automation Apprenticeship сюда переносится дисциплина: входные требования, повторяемые шаги, фактический результат, тестовые артефакты, отчетность и регрессия. Из книг курса автор берет системность и инженерный язык, но не перекладывает обучение на студента.

Студент должен выйти из урока с рабочим пониманием: что такое WSTG category, test objective, safe test case, evidence register, status и approval boundary, как это безопасно проверить, что приложить как evidence и какие действия требуют approval.

### 9. Проверка понимания перед практикой

Перед практикой студент отвечает на пять вопросов:

1. Какая цель разрешена?
2. Какой механизм урока используется?
3. Какой результат ожидается?
4. Где stop condition?
5. Что будет приложено как sanitized evidence?

Если на один вопрос нет ответа, практика не выполняется. Сначала уточняется scope, выбирается lab или уменьшается действие до безопасного наблюдения.

### 10. Минимальная планка по уроку

Лекция считается освоенной, если студент может объяснить `WSTG category, test objective, safe test case, evidence register, status и approval boundary` своими словами, выполнить безопасный путь новичка, получить ожидаемый вывод, интерпретировать его и оформить evidence. Для темы `Занятие 62. OWASP Testing Guide: структура теста веб-приложений` минимальная сдача — оформить воспроизводимый артефакт по модели: WSTG category, test objective, safe test case, evidence register, status и approval boundary, без нарушения ограничения: действия вне scope или без approval.


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

### Создание safe OWASP WSTG checklist для Slider AI olddev

В этом уроке не нужно тестировать вымышленный внешний магазин и не нужно запускать intrusive-проверки. Задача — научиться превращать OWASP WSTG в безопасный план проверки для разрешенного стенда `https://olddev.slider-ai.ru`.

Создайте в своих рабочих заметках раздел `OWASP WSTG Safe Checklist`:

```markdown
# OWASP WSTG Safe Checklist: Slider AI olddev

## Scope
- Target: https://olddev.slider-ai.ru
- Environment: macOS native, browser, DevTools, optional Burp/ZAP passive mode
- Rule: no production, no DoS/load, no brute force, no destructive payloads, no secret extraction
- Stop condition: any action requiring account enumeration, data modification, aggressive scanning or payload execution becomes requires approval

## 1. Information Gathering: safe observation only
- [ ] Record visible application entry points by manual navigation.
- [ ] Capture selected response headers with `curl -I https://olddev.slider-ai.ru`.
- [ ] Record technologies only from passive browser/DevTools observation.
- [ ] Do not run directory brute force, subdomain enumeration or external scanners without approval.

## 2. Configuration Review
- [ ] Check presence of security headers visible in a single safe response.
- [ ] Check cookie flags only if cookies are created during normal authorized use.
- [ ] Mark missing evidence as `not assessed`, not as finding.

## 3. Authentication And Session: no brute force
- [ ] Review login and logout behavior manually if a test account is available.
- [ ] Check whether errors reveal excessive information.
- [ ] Do not test password guessing, account lockout bypass or MFA bypass without written approval.

## 4. Authorization And Access Control
- [ ] Identify roles/features that require separate approval before testing.
- [ ] Do not access, modify or enumerate other users' data.
- [ ] If an IDOR-style check is needed, mark it `requires approval` unless a dedicated test dataset is provided.

## 5. Input Validation
- [ ] Observe validation messages using harmless strings such as `qa-test-123`.
- [ ] Do not send SQLi/XSS/SSRF/XXE/destructive payloads to olddev in this lesson.
- [ ] Move payload mechanics to PortSwigger Academy or local lab.

## 6. Error Handling And Logging Signals
- [ ] Record whether visible errors expose stack traces, SQL errors or internal paths.
- [ ] Sanitize screenshots and never store tokens, cookies or personal data.

## Evidence Register
| WSTG area | Safe action | Evidence | Status | Follow-up |
|---|---|---|---|---|
| INFO | curl -I baseline | selected headers | observation | review headers |
| AUTH | manual login behavior | sanitized screenshot | observation | no brute force |
| INPV | harmless validation string | UI message | observation | payloads lab-only |
```

### Product Security QA coverage matrix

OWASP WSTG нужно перевести в покрытие продукта. Для Slider AI olddev обязательная работа в этом уроке — матрица, а не атака.

| Тема | Что покрывает | Минимальный учебный результат | Где выполнять |
|---|---|---|---|
| Access Control / IDOR | владелец объекта, роль, tenant boundary | role/object matrix и список approval-required проверок | olddev passive + test data request |
| Authorization testing | действия по ролям и состояниям | 5 test cases: allowed/forbidden/edge/expired/anonymous | olddev только безопасные роли |
| API Security | REST/OpenAPI/JWT/CORS/GraphQL | API checklist с безопасными headers/status observations | macOS native, один low-impact запрос |
| File upload | тип, размер, хранение, исполнение | upload risk model без загрузки опасных файлов | lab-only или approved test file |
| Path traversal / LFI / RFI | доступ к файлам вне разрешенного пути | payload mechanics только lab-only; на olddev limitation | PortSwigger/local lab |
| Command injection | выполнение команд через input | только threat model и lab-only demonstration | lab-only |
| Deserialization / SSTI | выполнение логики из данных | explain-and-classify worksheet | lab-only |
| SSRF / cloud metadata | сервер делает запросы внутрь сети | mock metadata `127.0.0.1:9000`, not real metadata | local mock/cloud lab |
| Race conditions | конкурирующие действия | sequence diagram и stop condition | не выполнять на olddev |
| Business logic flaws | обход порядка/лимитов/состояний | abuse case + expected control | olddev safe walkthrough |
| SAST/DAST/SCA/secrets/SBOM | security gates в SDLC | CI gate proposal с false-positive handling | локальные учебные артефакты |

Матрица считается заполненной, если по каждой строке есть `safe action`, `lab-only or approval boundary`, `evidence type` и `owner action`. Это делает урок самодостаточным: студенту не нужно искать WSTG mapping снаружи, чтобы понять, что именно покрывать.

### Практика: заполнение чек-листа

1. Заполните минимум 6 строк checklist на основе безопасных наблюдений olddev.
2. Для каждого пункта укажите статус: `observation`, `not applicable`, `not assessed` или `requires approval`.
3. Если пункт OWASP требует intrusive-действия, не выполняйте его. Запишите, какая лаборатория подойдет для изучения механики: PortSwigger Academy, TryHackMe, HackTheBox или локальный deliberately vulnerable app.
4. Итоговый артефакт должен показывать зрелость SDET: вы умеете выбрать безопасную проверку и остановиться там, где нужен approval.


## Примеры вывода

Минимальный эталонный артефакт для сдачи по теме `Занятие 62. OWASP Testing Guide: структура теста веб-приложений`:

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

- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`. Для явно помеченной Kali/Linux-среды допустим `apt`.
- Kali/Linux VM запускайте только как углубление и выделяйте не более 3-4GB RAM на MacBook Air M2 (8GB)
- Если нужна Kali/Linux VM на Apple Silicon, используйте ARM64-образ в UTM/VMware Fusion/Parallels; не используйте x86/x64 VM как базовый путь.
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты


## Задачи для самостоятельного выполнения

1. **Сравнение OWASP Top 10 и Testing Guide**: Сопоставьте OWASP Top 10 2021 с разделами OWASP Testing Guide. Какие тесты покрывают каждый пункт Top 10?

2. **Кастомизация чек-листа**: Адаптируйте OWASP чек-лист для тестирования REST API. Добавьте специфичные для API проверки (JWT, rate limiting, versioning, GraphQL).

3. **Автоматизация**: Напишите скрипт на Python, который генерирует OWASP чек-лист в формате Markdown на основе JSON-конфигурации.

4. **Тестирование**: Протестируйте учебное приложение (bWAPP, WebGoat) по методологии OWASP Testing Guide. Заполните чек-лист минимум на 20 пунктов.

5. **Report template**: Создайте шаблон отчета по результатам OWASP-тестирования, включающий разделы: Summary, Vulnerability Details (с CVSS), Remediation.

## Частые ошибки

1. **Поверхностное тестирование** — выполнение только автоматизированного сканирования без ручной проверки.
2. **Игнорирование Business Logic** — большинство уязвимостей в веб-приложениях находятся в логике, а не в коде.
3. **Неправильное использование чек-листа** — выполнение пунктов "для галочки" без понимания сути.
4. **Пропуск Client-Side тестов** — XSS и DOM-уязвимости часто упускаются.

## Вопросы на понимание

1. Сколько разделов в OWASP Testing Guide v4.2?
2. Что такое WSTG-INPV-006?
3. Почему важно тестировать Business Logic?
4. Какие инструменты используются для Information Gathering?
5. В чем разница между Input Validation и Authorization Testing?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать правилами Slider AI olddev из пользовательской инструкции курса; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** OWASP checklist

### Минимум

Создайте OWASP WSTG чек-лист только для функций Slider AI, доступных QA.

### Практика Slider AI

Пометьте каждый пункт: tested, not tested, not applicable, requires approval.

### Углубление после изучения следующих уроков

После нескольких findings обновите checklist приоритетами риска.

### Артефакт сдачи

Markdown-запись по шаблону из правилами Slider AI olddev из пользовательской инструкции курса: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

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
