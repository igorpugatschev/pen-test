# Урок 33: Dirsearch и ffuf — поиск скрытых директорий

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 33: Dirsearch и ffuf — поиск скрытых директорий`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

Поиск скрытых директорий и файлов — критический этап пентеста веб-приложений. Многие администраторы прячут админки, бэкапы, конфиги в неочевидных путях.

**Dirsearch** — классический инструмент на Python для брутфорса директорий.
**ffuf** (Fuzz Faster U Fool) — быстрый инструмент на Go, работает в разы быстрее.

Оба инструмента используют словари (wordlists) для перебора возможных путей.

## Guided practice

1. Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.
2. Заполните tool approval card до запуска любой инструментальной проверки.
3. Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.
4. Проведите false-positive review и приложите только sanitized output.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Dirsearch

```bash
# Установка
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip install -r requirements.txt

# macOS (M2) — также можно через pip
pip3 install dirsearch

# Базовый запуск
python3 dirsearch.py -u http://127.0.0.1:8080
# Пример вывода:
# Target: http://127.0.0.1:8080
# [20:30:15] Starting: 
# [20:30:16] 200 -    12KB - /index.html
# [20:30:17] 403 -    1KB - /admin/

# Указание словаря
python3 dirsearch.py -u http://127.0.0.1:8080 -w /usr/share/wordlists/dirb/common.txt
# macOS (M2, Homebrew)
python3 dirsearch.py -u http://127.0.0.1:8080 -w /opt/homebrew/share/seclists/Discovery/Web-Content/common.txt

# Расширения файлов
python3 dirsearch.py -u http://127.0.0.1:8080 -e php,html,txt,bak

# Рекурсивный поиск
python3 dirsearch.py -u http://127.0.0.1:8080 -r

# Сохранение результатов
python3 dirsearch.py -u http://127.0.0.1:8080 -o results.txt
```

### ffuf

```bash
# Установка (Kali Linux)
sudo apt install ffuf

# macOS (M2, Homebrew)
brew install ffuf

# Через Go
go install github.com/ffuf/ffuf@latest

# Базовый запуск
ffuf -u http://127.0.0.1:8080/FUZZ -w /usr/share/wordlists/dirb/common.txt
# Пример вывода:
# :: Method       : GET
# :: URL          : http://127.0.0.1:8080/FUZZ
# :: Wordlist     : FUZZ: /usr/share/wordlists/dirb/common.txt
# :: Status codes : 200,204,301,302,307,403,404,500
# [Status: 200] [Size: 1234] [Words: 100] [Lines: 50] /index.html

# Поиск файлов с расширениями
ffuf -u http://127.0.0.1:8080/FUZZ -w wordlist.txt -e .php,.html,.txt

# Фильтрация результатов (игнорировать 404)
ffuf -u http://127.0.0.1:8080/FUZZ -w wordlist.txt -fc 404

# Поиск по конкретным статус-кодам
ffuf -u http://127.0.0.1:8080/FUZZ -w wordlist.txt -mc 200,204,301,302,403
# Пример вывода:
# [Status: 301] [Size: 234] [Words: 14] [Lines: 8] /admin

# Рекурсивный (через скрипт или вручную)
```

### Полезные словари
```bash
# В Kali Linux уже есть словари
ls /usr/share/wordlists/

# Dirb (базовый)
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirb/big.txt

# SecLists (огромная коллекция)
/usr/share/wordlists/seclists/Discovery/Web-Content/

# macOS (M2, Homebrew)
brew install seclists
ls /opt/homebrew/share/seclists/Discovery/Web-Content/

# Скачать SecLists
git clone https://github.com/danielmiessler/SecLists.git /usr/share/wordlists/seclists
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

1. Запустите DVWA или bWAPP. Используйте dirsearch для поиска скрытых директорий. Какие интересные пути удалось найти?

2. Сравните скорость работы dirsearch и ffuf на одном и том же целевом сайте с одинаковым словарем. Какой инструмент быстрее?

3. Найдите файлы бэкапов (.bak, .old, .backup) на тестовом веб-сервере, используя расширения в ffuf.

4. Используя dirsearch с флагом `-e` (расширения), найдите все PHP-файлы в директории `/admin` тестового сайта.

5. Настройте рекурсивный поиск. Найдите вложенные директории глубиной 3 уровня на `локальный DVWA/bWAPP или PortSwigger lab`.

## Частые ошибки

1. **Неправильный путь к словарям в macOS** — в macOS с Homebrew словари SecLists находятся в `/opt/homebrew/share/seclists/`, а не в `/usr/share/wordlists/`.

2. **Отсутствие расширений файлов** — при поиске директорий часто забывают указать `-e` для поиска файлов с расширениями.

3. **Слишком агрессивный ffuf** — большое количество потоков может вызвать блокировку IP, используйте `-rate` для ограничения.

4. **Dirsearch требует Python 3** — убедитесь, что используете `python3`, а не `python`.

## Вопросы на понимание

1. В чем главное преимущество ffuf перед dirsearch?

2. Как интерпретировать статус-коды ответов при поиске директорий (200, 301, 403, 404)?

3. Зачем нужен флаг `-e` в dirsearch и аналог `-e` в ffuf?

4. Какой словарь лучше использовать для глубокого аудита: common.txt или big.txt?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Content discovery

### Минимум

Не запускайте словари по Slider AI; составьте список публичных путей, уже видимых из навигации.

### Практика Slider AI

Проверьте вручную 3-5 видимых URL на корректные статусы и отсутствие directory listing.

### Углубление после изучения следующих уроков

После отдельного разрешения запланируйте small wordlist run с 1 rps и stop conditions.

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
