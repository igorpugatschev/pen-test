# Урок 32: Subfinder — быстрая разведка поддоменов

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 32: Subfinder — быстрая разведка поддоменов`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

Subfinder — быстрый и простой инструмент для пассивного поиска поддоменов, разработанный проектом ProjectDiscovery (теми же, что сделали Nuclei). Работает быстрее Amass, но использует только пассивные источники.

Преимущества:
- Высокая скорость работы
- Поддержка множества источников (VirusTotal, Censys, Chaos, Shodan и др.)
- Простота использования
- Интеграция с другими инструментами ProjectDiscovery

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
sudo apt update && sudo apt install subfinder

# macOS (M2, Homebrew)
brew install subfinder

# Через Go
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder

# Проверка
subfinder -version
# Пример вывода:
# subfinder: v2.6.3
```

### Настройка источников
```bash
# Проверить конфигурацию (файл создается автоматически при первом запуске)
subfinder -config
# Пример вывода:
# Configuration file: /Users/username/.config/subfinder/config.yaml
# (откроется редактор для настройки API ключей)

# Посмотреть содержимое конфига
cat ~/.config/subfinder/config.yaml
# Пример вывода:
# provider-config:
#   virustotal:
#     - apikey: ""
#   censys:
#     - api_id: ""
#       api_secret: ""
```

### Базовое использование
```bash
# Простой поиск поддоменов
subfinder -d example.test
# Пример вывода:
# www.example.test
# mail.example.test
# ftp.example.test
# admin.example.test

# Сохранение в файл
subfinder -d example.test -o results.txt

# Вывод в формате JSON
subfinder -d example.test -o results.json -oJ
# Пример вывода (JSON):
# {"host":"www.example.test","source":"Virustotal"}
# {"host":"mail.example.test","source":"Censys"}
```

### Настройка источников
```bash
# Использовать только конкретные источники
subfinder -d example.test -sources virustotal,censys

# Исключить источники
subfinder -d example.test -exclude virustotal

# Рекурсивный поиск (искать поддомены у найденных поддоменов)
subfinder -d example.test -recursive
```

### Интеграция с другими инструментами
```bash
# Передать результаты в httpx (проверка живых хостов)
# approval-required active validation: subfinder -d example.test | httpx -o live_hosts.txt

# Передать в Nuclei для поиска уязвимостей
# requires approval: subfinder -d example.test | httpx | nuclei -t vulnerabilities/

# Комбинация с Amass
amass enum -passive -d example.test | subfinder -d example.test | sort -u > all_subdomains.txt
# Пример вывода (результат в файле):
# admin.example.test
# api.example.test
# www.example.test
```

### Конфигурация API ключей
```bash
# При первом запуске subfinder автоматически создает конфиг:
# ~/.config/subfinder/config.yaml
# Можно открыть его для редактирования вручную:
nano ~/.config/subfinder/config.yaml

# Пример конфига с API ключами:
# provider-config:
#   virustotal:
#     - apikey: "ваш_ключ"
#   censys:
#     - api_id: "ваш_id"
#       api_secret: "ваш_секрет"
```

### Конфигурация API ключей
```bash
# Создать конфиг (редактировать ~/.config/subfinder/config.yaml)
subfinder -config

# Пример конфига с API ключами:
# virustotal:
#   - apikey: "ваш_ключ"
# censys:
#   - api_id: "ваш_id"
#   - api_secret: "ваш_секрет"
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

1. Сравните Subfinder и Amass на уровне режима работы: какие источники использует passive mode, какие API-ключи нужны, какие запросы не отправляются к целевому приложению.

2. Настройте хотя бы один API ключ в локальном конфиге, но не сохраняйте его в evidence. Если нет разрешенного домена, сдайте sanitized конфиг и approval note.

3. Не выполняйте recursive search без расширенного scope. Подготовьте команду и объясните, почему recursive mode может выйти за границы `olddev.slider-ai.ru`.

4. Объедините только заранее подготовленные lab-файлы Subfinder и Amass, удалите дубликаты (`sort -u`) и оформите output как учебный artifact.

5. Для связки `subfinder | httpx` заполните approval card. Без расширенного scope не запускайте active validation.

## Частые ошибки

1. **Флаг `-ls` больше не работает** — в новых версиях Subfinder этот флаг удален, для просмотра источников используйте конфиг или документацию.

2. **Отсутствие конфигурационного файла** — файл `~/.config/subfinder/config.yaml` создается автоматически при первом запуске subfinder, не нужно создавать его вручную.

3. **Неправильный путь к конфигу в macOS** — в macOS путь будет `/Users/username/.config/subfinder/config.yaml`, а не `/root/.config/...`.

4. **Запуск без API ключей** — многие источники (VirusTotal, Censys) требуют API ключи, без них поддоменов будет меньше.

## Вопросы на понимание

1. В чем разница между Subfinder и Amass по методам сбора информации?

2. Зачем нужен рекурсивный поиск (`-recursive`) и когда его стоит использовать?

3. Как настроить API ключи в Subfinder и почему они важны?

4. Почему вывод Subfinder может отличаться при запуске с одного и того же домена в разные дни?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Subfinder passive

### Минимум

Проверьте, применим ли subfinder к текущему scope; если нет, оформите `not applicable`.

### Практика Slider AI

Не добавляйте найденные поддомены в тестирование без явного включения в scope.

### Углубление после изучения следующих уроков

После урока 61 предложите процедуру согласования новых доменов в RoE.

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
