# Занятие 27. Burp Suite база: Proxy, Repeater, Intruder

## Учебная рамка

**Входные требования:** Базовое понимание HTTP, форм, параметров URL и работы браузера/DevTools.

**Результат занятия:** Студент настраивает Burp Suite как HTTP proxy, повторяет безопасный запрос в Repeater, сохраняет sanitized HTTP evidence и объясняет, когда Intruder допустим только в lab/approval-сценарии.

**Наследуемая SDET-компетенция:** test design, negative testing, API/UI evidence и перевод OWASP-риска в проверяемый QA-кейс.

**Security QA-компетенция:** моделирование web-рисков OWASP и безопасная ручная проверка Slider AI.

**Связь с книгами:** OWASP/WSTG как основной security reference; «PyCharm. Профессиональная работа на Python 2024» — DevTools/HTTP Client/evidence workflow.

**Основной источник:** «PyCharm. Профессиональная работа на Python 2024» и `Black Hat Python` только для lab-only/defensive interpretation.

**Дополнительные источники:** «Легкий способ выучить Python 3 еще глубже» для обработки запросов, текстов и простых проверочных данных.

**Что берем из источника:** разделение lab payload и product-safe marker, HTTP evidence, перевод риска OWASP в security test case.

**Как это превращается в SDET/Security QA навык:** проектировать безопасные проверки Slider AI через OWASP/WSTG без destructive payloads.

**Что нельзя переносить на Slider AI без отдельного разрешения:** учебные payloads выполнять только в DVWA/WebGoat/PortSwigger; на Slider AI использовать безопасные маркеры и passive evidence.


**Процессный артефакт:** `THREAT_MODEL.md` или `SECURITY_FINDING_TEMPLATE.md`: abuse case, evidence и expected control.

**Безопасная цель:** DVWA, WebGoat, bWAPP, PortSwigger Web Security Academy или локальная учебная VM. Запрещены реальные сайты без письменного разрешения.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Настроить proxy и CA-сертификат, перехватить учебный запрос, повторить его в Repeater без разрушительных изменений и сохранить sanitized request/response.

**Углубление:** Разобрать Intruder только на DVWA/PortSwigger/локальной лаборатории с малым набором payload и явно описать, почему этот режим нельзя применять к Slider AI без письменного approval.

**Минимальная проверка успеха:** Burp перехватывает HTTPS-запрос, Repeater повторяет один безопасный запрос, evidence не содержит cookies/tokens, а Intruder помечен как lab-only/approval.

**Эталонный вывод:** Отчет содержит proxy setup, один sanitized GET/response из HTTP history, Repeater screenshot/summary и раздел `Intruder boundary`.

**Критерии сдачи:** Зачет: Burp proxy и Repeater настроены, evidence sanitized. Отлично: добавлены CA-сертификат, boundary для Intruder и план безопасного использования в lab.

### OWASP ZAP — бесплатная альтернатива Burp Suite

**Zed Attack Proxy (ZAP)** — бесплатный инструмент от OWASP, работающий на macOS ARM (M2) нативно.

**Установка на macOS (M2):**
```bash
brew install --cask owasp-zap
```

**Преимущества перед Burp Suite:**
- Полностью бесплатный (Burp имеет ограничения в Community Edition)
- Нативная поддержка ARM64 (не требует эмуляции)
- Простой интерфейс для начинающих

**Основные функции:**
- Проксирование трафика (Proxy)
- Сканирование уязвимостей (Active Scan)
- Пассивное сканирование (Passive Scan)
- Паук (Spider) для обхода сайта

> **Для M2 8GB:** ZAP потребляет меньше ресурсов чем Burp Suite, что критично при ограниченной RAM.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 27. Burp Suite база: Proxy, Repeater, Intruder`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/pycharm-professional-python-2024-pages/`
- `docs/socraticode/black-hat-python-ru-pages/` только lab-only/defensive

Конкретные страницы для этого блока: `pycharm-professional-python-2024-pages/page-338.md`-`page-369.md`; `black-hat-python-ru-pages/page-120.md`-`page-140.md` только lab-only.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот раздел не является заданием найти теорию в книгах. Книги использованы автором курса как системные источники для лекции `Занятие 27. Burp Suite база: Proxy, Repeater, Intruder`, а студент получает полное объяснение ниже.

Для этой темы опорная идея взята из источников: «PyCharm. Профессиональная работа на Python 2024», «Black Hat Python» только как lab-only источник идей, «Паттерны разработки на Python». Из них в урок перенесены не страницы как домашнее чтение, а инженерные принципы: уязвимость как сбой модели доверия: входные данные, состояние, авторизация, сессия, серверная обработка, логирование и evidence. Поэтому лекция строится вокруг вопроса: как SDET, уже умеющий работать с тестами, артефактами и воспроизводимостью, превращает тему `Занятие 27. Burp Suite база: Proxy, Repeater, Intruder` в безопасную Security QA-практику.

Книжный материал адаптирован в три слоя. Первый слой — модель: какие сущности участвуют, как они связаны и где появляется риск. Второй слой — рабочий навык: перевод web-риска в test case, безопасная проверка, sanitized evidence, triage и retest. Третий слой — границы применения: PortSwigger/THM/локальная лаборатория для payload, Slider AI olddev только для безопасных наблюдений внутри scope. Если техника может повредить данным, создать нагрузку, извлечь секреты, перебрать учетные записи или выйти за scope, она не переносится на Slider AI и остается только в lab-only/cloud-lab формате.

Такой подход важен для повышения квалификации QA: цель не “запустить хакерский инструмент”, а научиться отвечать за безопасность продукта так же дисциплинированно, как за функциональное качество. В каждом упражнении студент должен видеть разрешенную цель, среду выполнения, ожидаемый результат, критерий остановки и sanitized evidence.

## Теория

### 1. Зачем SDET изучает эту тему

Тема `Занятие 27. Burp Suite база: Proxy, Repeater, Intruder` нужна не как отдельный набор команд, а как часть профессионального перехода от обычного QA/SDET к специалисту, который отвечает за качество и безопасность продукта. SDET уже привык проверять поведение системы, фиксировать воспроизводимые шаги, отделять факт от предположения и оформлять результат так, чтобы разработчик мог его повторить. В Security QA добавляется еще один слой: каждое действие должно быть разрешенным, ограниченным по scope и безопасным для данных, пользователей и инфраструктуры.

В этой лекции базовая задача состоит в том, чтобы понять модель `уязвимость как сбой модели доверия: входные данные, состояние, авторизация, сессия, серверная обработка, логирование и evidence` и научиться превращать ее в проверяемый артефакт. Артефактом может быть команда, скриншот DevTools, HTTP history, лог, Markdown-заметка, JSON-вывод helper-скрипта, checklist или черновик finding. Главное требование: другой инженер должен понять, что было проверено, где, с каким разрешением и почему результат имеет значение.

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

Для темы `Занятие 27. Burp Suite база: Proxy, Repeater, Intruder` минимальная планка такая: студент понимает уязвимость как сбой модели доверия: входные данные, состояние, авторизация, сессия, серверная обработка, логирование и evidence, выполняет безопасную практику в среде `PortSwigger/THM/локальная лаборатория для payload, Slider AI olddev только для безопасных наблюдений внутри scope`, объясняет результат через перевод web-риска в test case, безопасная проверка, sanitized evidence, triage и retest и не выходит за ограничения Slider AI. Все, что требует более агрессивной техники, переносится в углубление после изучения следующих уроков или оформляется как `requires approval`.

### 11. Контроль понимания перед практикой

Перед переходом к заданиям студент должен остановиться и проговорить тему как инженерную процедуру. Нужно назвать разрешенную цель, среду выполнения, минимальное действие, ожидаемый безопасный результат и критерий остановки. Если хотя бы один пункт неясен, практика не начинается: сначала уточняется scope или выбирается локальная лабораторная цель. Такой контроль снижает риск случайно выполнить активную проверку там, где требовалось только наблюдение.

Второй контрольный вопрос: какие данные попадут в evidence? В отчет нельзя переносить cookies, токены, персональные данные, приватные ключи, полные ответы с секретами и любые сведения, которые не нужны для доказательства результата. Хороший SDET собирает ровно столько фактов, сколько нужно для воспроизведения и принятия решения.


### 12. Предметная часть урока

Для темы `Занятие 27. Burp Suite база: Proxy, Repeater, Intruder` ключевая модель — доверительная граница web-приложения. Пользовательский ввод, cookies, headers, URL-параметры, body запроса, server-side integrations и session state не должны автоматически считаться надежными. Уязвимость появляется там, где приложение принимает данные, принимает решение или обращается к другому ресурсу без достаточной проверки.

Практика строится через безопасную лестницу. Сначала студент изучает нормальное поведение: какой запрос отправляется, какой status code возвращается, как меняются cookies, какие ошибки видны пользователю. Затем в lab-only среде разбирается механика payload и exploit path. Только после этого формируется продуктовый Security QA test case: что можно проверить на olddev без разрушения данных и что требует approval.

Для Slider AI запрещено использовать destructive payloads, извлекать секреты, читать чужие данные, выполнять brute force, менять чужие записи или отправлять массовые автоматизированные запросы. Допустимы безопасные наблюдения: наличие валидации, корректные ошибки, защитные headers, отсутствие утечки stack trace, корректная обработка сессии и sanitized evidence из DevTools/Burp history.


## Guided practice

1. Сформулируйте риск урока как abuse case и как проверяемое ожидание защиты.
2. Отработайте опасную технику только в lab, если урок этого требует.
3. Для Slider AI выполните safe-marker или passive observation без извлечения данных и без destructive payload.
4. Классифицируйте результат: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Установка и настройка Burp Suite

1. Скачайте Community Edition: https://portswigger.net/burp/communitydownload
2. Запустите Burp Suite
3. Убедитесь, что вкладка **Proxy** → **Proxy settings** показывает:
   - Running on: 127.0.0.1:8080

### Настройка браузера

**Firefox (рекомендуется):**
1. Откройте Settings → Network Settings → Manual proxy configuration
2. HTTP Proxy: `127.0.0.1`, Port: `8080`
3. Check "Also use this proxy for HTTPS"

**Или используйте FoxyProxy** (расширение для быстрого переключения).

### Установка CA-сертификата Burp (критично для HTTPS)

Для перехвата HTTPS-трафика необходимо установить CA-сертификат Burp в браузер.

**Шаг 1: Скачивание сертификата**
1. В Burp Suite убедитесь, что Proxy запущен
2. В браузере (через прокси Burp) откройте: `http://burp`
3. Нажмите **CA Certificate** — файл `cacert.der` скачается

**Шаг 2: Установка в Firefox**
1. Откройте Firefox → Settings → Privacy & Security → Certificates → View Certificates
2. Нажмите **Import**, выберите скачанный `cacert.der`
3. Поставьте галочку **Trust this CA to identify websites**
4. Нажмите OK

**Шаг 3: Проверка**
1. В Burp включите **Intercept on**
2. В браузере откройте `https://www.google.com`
3. В Burp должен появиться перехваченный HTTPS-запрос

**Для macOS (M2):**
```bash
# Установка Burp Suite через Homebrew
brew install --cask burp-suite
```

После установки сертификата, экспортируйте его:
1. В Burp: Proxy → Proxy settings → Import / Export CA certificate
2. Export → Certificate in DER format → Save as `burp_ca.der`
3. В macOS дважды кликните файл → добавится в Keychain Access
4. В Keychain найдите "PortSwigger CA" → ПКМ → Get Info → Trust → Always Trust

### Практика: Proxy и перехват

**Шаг 1: Перехват запроса**
1. В Burp включите **Intercept on** (Proxy → Intercept)
2. В браузере откройте http://192.168.0.x (DVWA)
3. В Burp появится запрос — нажмите **Forward** чтобы пропустить
4. Попробуйте войти в DVWA, запрос появится в Proxy

**Шаг 2: Изменение запроса**
1. Перехватите запрос логина
2. Измените `password=password` на `password=wrong`
3. Нажмите **Forward**
4. DVWA покажет ошибку входа

**Шаг 3: Отключение перехвата**
Нажмите **Intercept off** — теперь Burp просто пропускает трафик, но записывает в HTTP history.

### Практика: Repeater

**Шаг 1: Отправка запроса в Repeater**
1. В Proxy → HTTP history найдите запрос к `/vulnerabilities/sqli/?id=1`
2. ПКМ → **Send to Repeater**

**Шаг 2: Модификация и отправка**
1. В Repeater измените `id=1` на `id=1' OR '1'='1`
2. Нажмите **Send**
3. Посмотрите ответ в нижней части (Response)
4. Найдите в ответе данные пользователей (first_name, surname)

**Шаг 3: Изучение заголовков**
В Repeater посмотрите вкладки:
- **Headers**: заголовки запроса и ответа
- **Body**: тело ответа
- **Hex**: шестнадцатеричный вид

### Практика: Intruder (lab-only, базовый)

Этот блок выполняется только в DVWA/PortSwigger/локальной лаборатории. Для Slider AI Intruder запрещен без отдельного письменного разрешения, потому что даже малый перебор может стать brute force, enumeration или нагрузочным тестом.

**Шаг 1: Настройка позиций**
1. Отправьте запрос логина в Intruder (ПКМ → Send to Intruder)
2. В Intruder → Positions нажмите **Clear §**
3. Выделите значение пароля, нажмите **Add §**: `password=§test§`

**Шаг 2: Настройка пейлоадов**
1. Перейдите в Intruder → Payloads
2. В Payload Options добавьте: `password`, `123456`, `admin`, `letmein`
3. Или загрузите словарь

**Шаг 3: Запуск lab-only демонстрации**
1. Проверьте, что цель — только DVWA/локальная лаборатория.
2. Ограничьте payload до 3-5 учебных значений.
3. Нажмите **Start Attack** только в lab.
4. В открывшемся окне сравните строки по `Status` и `Length`; не делайте вывод об успешном входе без ручной проверки.

### Скриншоты для отчета

1. **Скриншот 1**: Burp Proxy — перехваченный запрос, виден Intercept on
2. **Скриншот 2**: Burp Repeater — запрос с модифицированным параметром, ответ содержит данные
3. **Скриншот 3**: Burp Intruder в lab — видны разные `Status/Length`, без публикации реальных учетных данных

### Примеры вывода

**Burp Proxy — перехваченный запрос:**
```
GET /vulnerabilities/sqli/?id=1 HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
Cookie: PHPSESSID=abc123; security=low
Connection: close

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1234

<html>...<pre>First name: admin<br>Surname: admin</pre>...</html>
```

**Burp Repeater — измененный запрос и ответ:**
```
Request:
GET /vulnerabilities/sqli/?id=1' OR '1'='1 HTTP/1.1
Host: localhost
Cookie: PHPSESSID=abc123; security=low

Response:
HTTP/1.1 200 OK
<pre>First name: admin<br>Surname: admin</pre>
<pre>First name: Gordon<br>Surname: Brown</pre>
... (все пользователи)
```

**Burp Intruder — результаты атаки:**
```
Payload     | Status | Length | Interpretation
marker-1    | 200    | 1420   | baseline
marker-2    | 200    | 1420   | same response
marker-3    | 403    | 980    | different response; requires manual review
```

### Частые ошибки

1. **Забыть включить Intercept** — трафик не перехватывается
2. **Неправильный прокси в браузере** — должен быть 127.0.0.1:8080
3. **Не установлен CA-сертификат** — HTTPS трафик не виден (failed to handshake)
4. **Forward вместо Drop** — когда перехватили запрос, но не хотели его менять

### Вопросы на понимание

1. В чем разница между Proxy (Intercept on) и Repeater?
2. Когда использовать Intruder типа Sniper, а когда Cluster bomb?
3. Зачем нужен CA-сертификат Burp для HTTPS?
4. Как найти успешный пейлоад в Intruder (кроме кода ответа)?

### Адаптация под macOS (M2)

```bash
# Установка Burp Suite через Homebrew
brew install --cask burp-suite

# Экспорт сертификата через командную строку (если Burp уже запущен)
# Откройте в браузере: http://127.0.0.1:8080/cert
# Скачается cacert.der

# Импорт в Keychain (автоматически)
security add-trusted-cert -d -r trustRoot -k ~/Library/Keychains/login.keychain cacert.der

# Проверка, что сертификат добавлен
security find-certificate -c "PortSwigger CA"
```

---


## Адаптация под macOS (M2, 8GB)

- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`; для явно помеченной Kali/Linux-среды допустим `apt`.
- Kali/Linux VM запускайте только как углубление и выделяйте не более 3-4GB RAM на MacBook Air M2 (8GB)
- Если нужна Kali/Linux VM на Apple Silicon, используйте ARM64-образ в UTM/VMware Fusion/Parallels; не используйте x86/x64 VM как базовый путь.
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. **Настройка Burp**: Установите Burp Suite Community Edition. Настройте браузер Firefox на работу через прокси 127.0.0.1:8080. Сделайте скриншот окна Burp с вкладкой Proxy, где видно, что прокси запущен.

2. **Перехват и модификация**: Используя Burp Proxy, перехватите запрос к DVWA или PortSwigger lab. В Repeater замените значение параметра на безопасный маркер `qa-marker-lesson-27`, сравните ответы и сохраните sanitized evidence.

3. **Repeater для SQLi в lab**: Отправьте запрос SQL Injection из DVWA в Repeater. Выполните пейлоады только в DVWA:
   - `id=1' OR '1'='1`
   - `id=1' UNION SELECT user(), version()#`
   
   Опишите ответы сервера, какие данные удалось получить.

4. **Intruder boundary**: В DVWA опишите, как Intruder мог бы подставлять 3-5 учебных маркеров. Не выполняйте перебор учетных данных или ID на Slider AI. В отчете укажите stop conditions и почему это lab-only.

5. **Decoder**: В Burp Suite откройте вкладку **Decoder**. Закодируйте строку `<script>alert(1)</script>` в:
   - URL-encoding
   - Base64
   - HTML-encoding
   
   Сделайте скриншот Decoder с результатами. Объясните, почему такие payload используются только в lab, а на Slider AI применяются безопасные маркеры.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Burp proxy setup

### Минимум

Настройте браузер через Burp и откройте только главную страницу Slider AI.

### Практика Slider AI

Сохраните один GET-запрос и один ответ из HTTP history, удалив cookies и токены из артефакта.

### Углубление после изучения следующих уроков

После урока 28 создайте карту основных endpoint без Intruder и без активного сканирования.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `OWASP Test Design for Slider AI`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?

## Примеры вывода

Минимальный эталонный артефакт для сдачи по теме `Занятие 27. Burp Suite база: Proxy, Repeater, Intruder`:

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
