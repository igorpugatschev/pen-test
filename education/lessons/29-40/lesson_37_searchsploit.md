# Урок 37: SearchSploit — поиск эксплойтов

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 37: SearchSploit — поиск эксплойтов`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

SearchSploit — инструмент командной строки для поиска эксплойтов в базе Exploit-DB (Exploit Database). Позволяет быстро находить готовые эксплойты для известных уязвимостей без использования браузера.

Основные возможности:
- Поиск по названию ПО/сервиса
- Копирование эксплойта в текущую директорию
- Поиск по конкретным платформам (Windows, Linux, PHP, etc.)
- Поиск по типам (remote, dos, local, webapps)

## Guided practice

1. Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.
2. Заполните tool approval card до запуска любой инструментальной проверки.
3. Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.
4. Проведите false-positive review и приложите только sanitized output.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Установка и обновление
```bash
# Kali Linux (уже установлен)
searchsploit --version

# macOS (M2, Homebrew)
brew install exploitdb

# Обновление базы
searchsploit -u
# Пример вывода:
# Updating via apt
# [*] Updating exploit database...
# [*] Updating exploitdb_cache...

# Путь к базе и эксплойтам
ls /usr/share/exploitdb/
# Пример вывода (macOS):
# /opt/homebrew/share/exploitdb/
```

### Базовый поиск
```bash
# Поиск по названию
searchsploit apache 2.4
# Пример вывода:
# Exploits: No Results
# Shellcodes: No Results

searchsploit vsftpd
# Пример вывода:
# Exploits: 3
#   |  Path
#   |  /usr/share/exploitdb/exploits/linux/remote/17491.rb

searchsploit samba
# Пример вывода:
# Exploits: 45
#   |  Path
#   |  /usr/share/exploitdb/exploits/linux/remote/10.c

# Поиск без учета регистра
searchsploit -i mysql

# Только заголовки (игнорировать пути)
searchsploit -t php
```

### Фильтрация по платформе/типу
```bash
# Только для Windows
searchsploit --platform windows samba
# Пример вывода:
# Exploits: 12
#   |  Path
#   |  /usr/share/exploitdb/exploits/windows/remote/...

# Только webapps
searchsploit -t webapps wordpress
# Пример вывода:
# Exploits: 850
#   |  Path
#   |  /usr/share/exploitdb/exploits/php/webapps/...

# Удаленные эксплойты (Remote)
searchsploit -t remote ftp

# Локальное повышение привилегий (Local)
searchsploit -t local linux kernel
```

### Работа с найденными эксплойтами
```bash
# Посмотреть путь к эксплойту
searchsploit samba 3.0
# Пример вывода:
# Exploits: 5
#   |  Path
#   |  /usr/share/exploitdb/exploits/linux/remote/10.c

# Скопировать эксплойт в текущую директорию
searchsploit -m 12345
# Пример вывода:
#  Copied to: /current/dir/12345.rb

# Прочитать эксплойт
searchsploit -x 12345

# Открыть URL к эксплойту на exploit-db.com
searchsploit -w 12345
# Пример вывода:
#  URL: https://www.exploit-db.com/exploits/12345
```

### Поиск по конкретной уязвимости (CVE)
```bash
# Поиск по CVE
searchsploit CVE-2017-0144  # EternalBlue
# Пример вывода:
# Exploits: 5
#   |  Path
#   |  /usr/share/exploitdb/exploits/windows/remote/42315.py

# Поиск по BID (Bugtraq ID)
searchsploit BID-12345

# Поиск по EDB-ID
searchsploit -p 12345
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

1. Найдите все эксплойты для vsftpd 2.3.4 (знаменитый backdoor). Сколько их? Скопируйте один в текущую директорию и изучите код.

2. Используя SearchSploit, найдите эксплойты для Samba (любой версии). Какие типы атак доступны (remote, local)?

3. Найдите эксплойт для уязвимости EternalBlue (CVE-2017-0144). Какой EDB-ID у этого эксплойта? Почитайте описание на exploit-db.com.

4. Настройте Metasploitable2. Определите версию Samba. Найдите подходящий эксплойт через SearchSploit. Попробуйте применить его (если уверены).

5. Сравните результаты SearchSploit и поиска на сайте exploit-db.com для "Apache 2.4.49". Есть ли разница?

## Частые ошибки

1. **Использование флага `-p` вместо `--platform`** — в новых версиях SearchSploit флаг `-p` используется для поиска по EDB-ID, а фильтрация по платформе делается через `--platform`.

2. **Забыли обновить базу** — команда `searchsploit -u` должна выполняться регулярно, иначе будут отсутствовать новые эксплойты.

3. **Путаница с путями** — в macOS путь к базе exploitdb может отличаться (`/opt/homebrew/share/exploitdb/` вместо `/usr/share/exploitdb/`).

4. **Копирование эксплойта без проверки** — всегда изучайте код эксплойта перед запуском, чтобы не нанести вред системе.

## Вопросы на понимание

1. Чем отличается поиск по CVE и по названию ПО в SearchSploit?

2. Как определить, подходит ли найденный эксплойт для вашей цели (учитывая архитектуру, версию ОС)?

3. Почему флаг `--platform` важен при поиске эксплойтов?

4. Что делает флаг `-m` и в чем разница между `-m` и `-x`?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Exploit-DB research

### Минимум

Используйте SearchSploit только для изучения публичных версий компонентов, если версии раскрыты.

### Практика Slider AI

Не применяйте эксплойты; оформите observation о риске раскрытия версии или `not enough data`.

### Углубление после изучения следующих уроков

После урока 47 сопоставьте наблюдение с CVE и рекомендацией обновления.

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
