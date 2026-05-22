# Урок 31: Amass — разведка поддоменов

## Учебная рамка

**Входные требования:** Умение работать в терминале, понимать IP/порт, scope и базовые юридические ограничения.

**Результат занятия:** Студент запускает инструмент только по разрешенной цели, читает ключевые строки вывода и оформляет результат как находку или наблюдение.

**Наследуемая SDET-компетенция:** tool governance, false-positive triage, безопасный запуск инструментов и оформление результата.

**Security QA-компетенция:** контролируемое применение security-инструментов, scope/rate-limit/stop conditions.

**Связь с книгами:** OWASP/WSTG/PTES как методология инструментов; «PyCharm. Профессиональная работа на Python 2024» — Git, Markdown, отчетность и артефакты.

**Основной источник:** «PyCharm. Профессиональная работа на Python 2024» и «Паттерны разработки на Python».

**Дополнительные источники:** `Black Hat Python` только для понимания lab-only техник и defensive boundaries.

**Что берем из источника:** tool governance, false-positive review, structured output, границы ручного/passive/low-rate режима.

**Как это превращается в SDET/Security QA навык:** превратить инструменты в управляемый QA-процесс с approval, stop conditions и evidence policy.

**Что нельзя переносить на Slider AI без отдельного разрешения:** не запускать aggressive scan, brute force, wordlists или intrusive templates по Slider AI без отдельного письменного разрешения.


**Процессный артефакт:** `TOOLING_POLICY.md` и finding/observation по шаблону.

**Безопасная цель:** Только `192.168.100.20`, `target.local`, Metasploitable/VulnHub/THM/HTB/PortSwigger в рамках их правил. Не использовать домашний роутер как цель атаки.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Запустить безопасный минимальный режим инструмента, сохранить команду и объяснить 2-3 ключевых параметра.

**Углубление:** Сравнить два режима инструмента, добавить ограничение скорости/потоков и оформить краткий риск-анализ.

**Минимальная проверка успеха:** Команда выполнена по учебной цели, вывод сохранен, студент отличает обнаружение от подтвержденной уязвимости.

**Эталонный вывод:** В отчете есть target, команда, сокращенный вывод, интерпретация и пометка `разрешенная учебная цель`.

**Критерии сдачи:** Зачет: корректный запуск и интерпретация. Отлично: добавлены ограничения безопасности, rate limit или проверка false positive.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 31: Amass — разведка поддоменов`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/pycharm-professional-python-2024-pages/`
- `docs/socraticode/architecture-patterns-python-pages/`

Конкретные страницы для этого блока: `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md`; `architecture-patterns-python-pages/page-038.md`-`page-069.md`.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: tool governance, false-positive review, structured output, границы ручного/passive/low-rate режима. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: не запускать aggressive scan, brute force, wordlists или intrusive templates по Slider AI без отдельного письменного разрешения. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

## Теория

Amass (Automated Attack Surface Mapping) — мощный инструмент для внешней разведки, разработанный OWASP. Использует пассивные и активные методы для обнаружения поддоменов, связей и инфраструктуры цели.

Основные режимы работы:
- **Passive** — сбор данных из публичных источников (без прямого контакта с целью)
- **Active** — DNS-запросы к цели для подтверждения поддоменов
- **Intel** — сбор общей информации об организации
- **Enum** — полное перечисление поддоменов

## Guided practice

1. Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.
2. Заполните tool approval card до запуска любой инструментальной проверки.
3. Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.
4. Проведите false-positive review и приложите только sanitized output.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Установка
```bash
# Kali Linux
sudo apt update && sudo apt install amass

# macOS (M2, Homebrew)
brew install amass

# Или через Go
go install -v github.com/owasp-amass/amass/v3/...@master

# Проверка
amass --version
# Пример вывода:
# OWASP Amass v3.23.2
```

### Пассивный сбор
```bash
# Пассивный поиск поддоменов (не касается цели напрямую)
amass enum -passive -d example.test
# Пример вывода:
# www.example.test
# mail.example.test
# ftp.example.test

# С выводом IP-адресов
amass enum -passive -d example.test -ip
# Пример вывода:
# www.example.test 93.184.216.34
# mail.example.test 93.184.216.34

# Сохранение в файл
amass enum -passive -d example.test -o results.txt
```

### Активное перечисление
```bash
# Активный режим (DNS-запросы к цели)
# requires approval: amass enum -active -d example.test

# С брутфорсом поддоменов
# lab-only/approval: amass enum -brute -d example.test

# Использование словаря
# Kali Linux, lab-only/approval
# amass enum -brute -w /usr/share/wordlists/dirb/common.txt -d example.test
# macOS (M2, Homebrew), lab-only/approval
# amass enum -brute -w /opt/homebrew/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -d example.test
```

### Intel режим (сбор информации об организации)
```bash
# Поиск доменов, связанных с организацией
amass intel -org "Target Organization"
# Пример вывода:
# example.test
# example.net
# example.org

# Поиск по ASN
amass intel -asn 1337

# Поиск по диапазону IP
amass intel -addr 192.168.1.0/24
```

### Визуализация
```bash
# Сохранение в формате GraphML для визуализации
amass enum -d example.test -graphml graph.graphml

# Использование OWASP Amass Netmap (если установлен)
amass viz -d3graph -o3 graph.html
```


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



## Адаптация под macOS (M2, 8GB)

- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`; для явно помеченной Kali/Linux-среды допустим `apt`.
- Kali/Linux VM запускайте только как углубление и выделяйте не более 3-4GB RAM на MacBook Air M2 (8GB)
- Если нужна Kali/Linux VM на Apple Silicon, используйте ARM64-образ в UTM/VMware Fusion/Parallels; не используйте x86/x64 VM как базовый путь.
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. Подготовьте passive-only команду Amass для домена из согласованного scope. Если scope содержит только `olddev.slider-ai.ru`, зафиксируйте `not applicable` для расширения доменов.

2. Не запускайте brute force. Заполните approval card: домен, словарь, rate limit, stop conditions и причина, почему это не входит в обязательный путь новичка.

3. Сравните passive и active режимы теоретически: какие запросы отправляются, какие риски для scope и почему active требует approval.

4. Установите `sublist3r` в lab/cloud среде или опишите, почему он не нужен для текущего Slider AI scope.

5. Если есть расширенный scope, используйте `-ip` только для разрешенных доменов. Иначе оформите `requires approval`.

## Частые ошибки

1. **Путаница между passive и active режимами** — passive не отправляет запросы к цели, active делает DNS-запросы напрямую.

2. **Отсутствие словарей для брутфорса** — убедитесь, что путь к словарю указан верно (`/opt/homebrew/share/seclists/` в macOS).

3. **Долгое выполнение активного режима** — amass enum -active может работать долго, используйте -timeout для ограничения времени.

4. **Игнорирование вывода IP-адресов** — флаг `-ip` помогает понять, какие поддомены реально работают.

## Вопросы на понимание

1. В чем главное отличие между passive и active режимами Amass?

2. Какой режим Amass является более "скрытным" и почему?

3. Что делает режим `intel` и когда его стоит использовать?

4. Как Amass отличается от Subfinder по методам сбора информации?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Passive subdomain discovery

### Минимум

Не запускайте active enumeration; подготовьте список разрешенных доменов из scope.

### Практика Slider AI

Если scope разрешает только `olddev.slider-ai.ru`, зафиксируйте, что расширение доменов не выполняется.

### Углубление после изучения следующих уроков

После письменного расширения scope выполните passive-only сбор и отметьте источники.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `Tool Governance Report`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
