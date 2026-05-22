# Занятие 57. OSINT практика: сбор информации о домене

## Учебная рамка

**Входные требования:** Пройдены базовые Linux, сети, web и инструменты; студент понимает правила scope учебных платформ.

**Результат занятия:** Студент проходит учебную комнату/машину, ведет заметки и превращает действия в воспроизводимый write-up без публикации секретных флагов.

**Наследуемая SDET-компетенция:** перенос lab-навыков в продуктовый QA без выхода за scope, write-up discipline и hypothesis tracking.

**Security QA-компетенция:** осознанный перенос CTF/academy-навыков в продуктовый контекст и фиксация запретов.

**Связь с книгами:** PortSwigger/THM/HTB как lab-transfer; «Black Hat Python» только для понимания lab-техник, boundaries и defensive interpretation.

**Основной источник:** `Black Hat Python` только lab-only, «PyCharm. Профессиональная работа на Python 2024» для write-ups и evidence discipline.

**Дополнительные источники:** «Паттерны разработки на Python» для переноса lab-навыков в поддерживаемые process artifacts.

**Что берем из источника:** lab-to-product transfer, structured notes, boundaries, write-up discipline, отделение exploitation от product QA.

**Как это превращается в SDET/Security QA навык:** переносить из THM/HTB/PortSwigger только безопасные QA-аналогии и артефакты.

**Что нельзя переносить на Slider AI без отдельного разрешения:** не переносить exploitation, privesc, bypass и aggressive enumeration на Slider AI без расширенного scope.


**Процессный артефакт:** `VULNERABILITY_TRIAGE.md`: lab-to-product transfer matrix и ограничения scope.

**Безопасная цель:** TryHackMe, Hack The Box, PortSwigger Academy и другие платформы только в рамках их правил и активной учебной машины.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Пройти указанную комнату или ее часть, записать команды, ошибки и выводы без копирования чужого решения.

**Углубление:** После самостоятельной попытки разобрать официальный write-up, сравнить подходы и улучшить собственные заметки.

**Минимальная проверка успеха:** Есть подтверждение прохождения этапа, список команд, выводы и пометка, что работа велась внутри учебной платформы.

**Эталонный вывод:** Отчет содержит название комнаты, цель, основные шаги, фрагменты вывода и выводы без раскрытия приватных флагов.

**Критерии сдачи:** Зачет: завершен обязательный этап и оформлены заметки. Отлично: добавлена ретроспектива ошибок и альтернативный путь решения.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 57. OSINT практика: сбор информации о домене`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/black-hat-python-ru-pages/` только lab-only/defensive
- `docs/socraticode/pycharm-professional-python-2024-pages/`

Конкретные страницы для этого блока: `black-hat-python-ru-pages/page-060.md`-`page-178.md` только lab-only; `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md`.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: lab-to-product transfer, structured notes, boundaries, write-up discipline, отделение exploitation от product QA. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: не переносить exploitation, privesc, bypass и aggressive enumeration на Slider AI без расширенного scope. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

## Теория

**OSINT (Open Source Intelligence)** — сбор информации из открытых источников. В пентесте OSINT — это первый этап (Information Gathering).

**Источники информации:**
- Поисковые системы (Google, Bing, DuckDuckGo)
- Социальные сети (LinkedIn, Facebook, Twitter)
- Специализированные сервисы (Shodan, Censys, VirusTotal)
- Публичные базы данных (WHOIS, DNS, Certificate Transparency)
- Кодовые репозитории (GitHub, GitLab)

**Google Dorks** — специальные запросы для поиска уязвимой информации:
- `site:example.com filetype:pdf` — документы на сайте
- `site:example.com intitle:"index of"` — открытые директории
- `site:example.com inurl:admin` — админ-панели
- `"example.com" "password"` — утечки паролей

**Shodan** — поисковик для устройств (IoT, серверов):
- Поиск по IP, порту, сервису, геолокации
- Пример: `port:22 country:"RU"` — SSH-серверы в России

## Guided practice

1. После lab выпишите навык, который был отработан, и его безопасный QA-аналог.
2. Укажите, какие действия остаются только в lab и почему.
3. Сделайте одну безопасную Slider AI-проверку или оформите `not applicable`/`requires approval`.
4. Добавьте transfer card в матрицу подготовки к финальному assessment.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Сбор информации о целевом домене (на примере вымышленного example.com)

**Шаг 1. WHOIS информация**
```bash
whois example.com
```
Получаем: регистратора, даты регистрации, контактные данные, NS-серверы.

**Шаг 2. DNS enumeration**
```bash
# A-записи
dig example.com A

# MX-записи (почтовые серверы)
dig example.com MX

# NS-записи (DNS-серверы)
dig example.com NS

# Все записи
dig example.com ANY
```

**Шаг 3. Поддомены (Subdomain enumeration)**
```bash
# Через sublist3r
sublist3r -d example.com

# Через amass
amass enum -d example.com

# Через gobuster
gobuster dns -d example.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

**Шаг 4. Google Dorks**
В браузере выполняем:
```
site:example.com filetype:pdf
site:example.com intitle:"index of" 
site:example.com inurl:php?id=
site:example.com "confidential"
```

**Шаг 5. Shodan**
1. Регистрируемся на shodan.io
2. Ищем: `hostname:example.com`
3. Анализируем: открытые порты, баннеры сервисов, уязвимости (CVE)

**Шаг 6. Email harvesting**
```bash
theharvester -d example.com -b google,linkedin
```
Собираем email-адреса сотрудников для будущих фишинговых атак.

**Шаг 7. GitHub разведка**
Ищем в GitHub: `example.com password`, `example.com api_key`
Разработчики часто случайно публикуют секреты в репозиториях.


## Примеры вывода

Минимальный эталонный артефакт для сдачи:

```markdown
Environment: macOS native / Kali ARM64 VM / cloud lab / Slider AI olddev
Target: <разрешенная учебная цель или https://olddev.slider-ai.ru>
Action: <выполненная безопасная команда или ручной шаг>
Evidence: <санитизированный фрагмент вывода, скриншота или HTTP history>
Result status: finding / observation / not reproducible / not applicable / requires approval
Next step: <retest, remediation, approval request или lab-only follow-up>
```

В отчете студент указывает среду выполнения, безопасную цель, команду или ручные шаги и коротко объясняет, какая строка подтверждает результат.



## Частые ошибки

1. **Ошибка 1**: Типичная ошибка новичков в этом уроке.
2. **Ошибка 2**: Еще одна распространенная проблема.
3. **Ошибка 3**: Важный момент, который часто упускают.

## Вопросы на понимание

1. Вопрос 1 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 1</details>
2. Вопрос 2 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 2</details>
3. Вопрос 3 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 3</details>

## Форматы флагов

- **TryHackMe**: `THM{...}`
- **HackTheBox**: `HTB{...}`
- **PortSwigger**: "Lab solved!" (без флагов)



## Адаптация под macOS (M2, 8GB)

- Для VPN используйте **Tunnelblick** (бесплатный OpenVPN клиент для macOS): скачайте .ovpn файл и откройте через Tunnelblick
- Виртуалки: используйте только при необходимости; для Apple Silicon выбирайте ARM64-образы в **UTM**, **VMware Fusion** или **Parallels**, а тяжелые лабы выносите в cloud lab
- "На 8GB RAM выделяйте VM не более 3-4GB"
- Docker работает нативно на M2: `docker pull <image>`
- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`; для явно помеченной Kali/Linux-среды допустим `apt`.
- Если требуется Python: `pip3 install <package>`


## Задачи для самостоятельного выполнения

1. **OSINT на реальную компанию** (по выбору) — соберите: домены, поддомены, IP-диапазоны, сотрудников, технологии
2. **Комната "OSINT"** на THM — пройдите все задания, изучите инструменты (Sherlock, Maltego)
3. **Поиск утечек:** Используйте haveibeenpwned.com для проверки email на утечки паролей

> **Важно:** OSINT — легальный этап пентеста, включенный в scope. Но не используйте найденные пароли без разрешения заказчика.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** OSINT for own product

### Минимум

Соберите только публичные сведения о разрешенном домене и не проверяйте найденные внешние активы.

### Практика Slider AI

Классифицируйте сведения: полезно для QA, требует scope, не относится к тесту.

### Углубление после изучения следующих уроков

После урока 61 предложите обновление scope на основе OSINT-наблюдений.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `Lab-to-Product Transfer`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
