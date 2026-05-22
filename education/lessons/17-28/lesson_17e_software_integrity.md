# Занятие 17e. OWASP A08: Software and Data Integrity Failures — Нарушение целостности ПО и данных

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 17e. OWASP A08: Software and Data Integrity Failures — Нарушение целостности ПО и данных`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

**A08:2021 – Software and Data Integrity Failures** — уязвимости, связанные с небезопасным обновлением ПО, десериализацией данных и доверием к данным из ненадежных источников.

### Основные типы атак

1. **Insecure Deserialization** — манипуляция сериализованными объектами для выполнения кода
2. **Unsafe Software Updates** — обновление без проверки подписи/хеша
3. **Dependency Confusion** — подмена внутренних пакетов на публичные
4. **Unauthorized Code/Data Modification** — изменение критических данных без проверки целостности

### Insecure Deserialization

Приложение десериализует данные, полученные от пользователя, без проверки.

**Пример уязвимого кода (PHP):**
```php
$data = unserialize($_COOKIE['user_data']);
```
Атакующий создает сериализованный объект с вредоносным кодом.

**Пример (Java):**
```java
ObjectInputStream in = new ObjectInputStream(request.getInputStream());
Object obj = in.readObject(); // Может выполнить произвольный код
```

### Небезопасное обновление

Приложение скачивает обновление по HTTP (без HTTPS) или не проверяет подпись:
```
GET http://example.com/update.zip
→ Установка файла без проверки хеша
```
Атакующий через MITM подменяет файл обновления на вредоносный.

---

## Guided practice

1. Сформулируйте риск урока как abuse case и как проверяемое ожидание защиты.
2. Отработайте опасную технику только в lab, если урок этого требует.
3. Для Slider AI выполните safe-marker или passive observation без извлечения данных и без destructive payload.
4. Классифицируйте результат: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Поиск проблем целостности в WebGoat

**Шаг 1: Insecure Deserialization в WebGoat**
1. Откройте WebGoat: http://192.168.0.x80/WebGoat
2. Перейдите в **Insecure Deserialization**
3. Изучите задание

Пример сериализованных данных (Java):
```
rO0ABxoljlIxNjI1NjM4MjYzNDAyODNmMS4wLjQuMlRo
```
Это Base64-encoded сериализованный объект.

**Шаг 2: Модификация данных**
Используя Burp Suite, перехватите запрос с сериализованными данными:

```
POST /WebGoat/InsecureDeserialization/task HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded

token=rO0ABxoljlIxNjI1NjM4MjYzNDAyODNmMS4wLjQuMlRo
```

Попробуйте изменить данные (десериализация может привести к выполнению кода).

**Шаг 3: Проверка отсутствия проверки целостности**
В DVWA откройте Burp → Repeater, отправьте запрос с измененным cookie:

```
GET /vulnerabilities/sqli/?id=1 HTTP/1.1
Host: localhost
Cookie: PHPSESSID=../../etc/passwd
```

Если приложение не проверяет формат сессии — это проблема целостности.

**Шаг 4: Dependency Confusion (теория + практика в браузере)**
Откройте DVWA и посмотрите, откуда подгружаются ресурсы:

```html
<script src="http://192.168.0.x/vulnerabilities/xss_r/source/jquery.js"></script>
```

Если src ведет на внешний CDN (например, cdnjs.cloudflare.com), и CDN взломан — код заменен.

---

## Частые ошибки

1. **Использовать unserialize на данных пользователя** — классическая уязвимость десериализации
2. **Не проверять подпись обновлений** — установка файлов с неизвестного источника
3. **Доверять данным из localStorage/cookie** без проверки целостности (HMAC)
4. **Использовать CDN без Subresource Integrity (SRI)** — подмена JS-библиотек

---

## Вопросы на понимание

1. Почему десериализация данных пользователя опасна?
2. Что такое Subresource Integrity (SRI) и как оно защищает от подмены CDN?
3. Как проверить, что обновление ПО не было скомпрометировано?
4. Приведите пример атаки через Dependency Confusion.

---

## Адаптация под macOS (M2)

```bash
# Проверка целостности файлов через shasum (работает на M2)
shasum -a 256 downloaded_file.zip
# Сравните с ожидаемым хешем

# Генерация HMAC для проверки целостности данных
echo -n "data" | openssl dgst -sha256 -hmac "secret_key"

# Проверка подписи файла (если есть .sig файл)
curl -s https://example.com/update.tar.gz -o update.tar.gz
curl -s https://example.com/update.tar.gz.sig -o update.tar.gz.sig
gpg --verify update.tar.gz.sig update.tar.gz
```

---


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

1. **Insecure Deserialization в WebGoat**: Пройдите задания в разделе **Insecure Deserialization** (минимум 2). Сделайте скриншот выполненных заданий. Опишите, в чем была уязвимость.

2. **Поиск отсутствия SRI**: Откройте исходный код DVWA или bWAPP. Найдите подключенные внешние скрипты. Проверьте, используется ли атрибут `integrity` для проверки целостности (SRI). Пример правильного подключения:
   ```html
   <script src="https://cdn.example.com/jquery.js" 
           integrity="sha384-xxx" 
           crossorigin="anonymous"></script>
   ```

3. **Проверка cookie на целостность**: В DVWA посмотрите значение PHPSESSID в DevTools. Попробуйте изменить один символ в cookie и отправить запрос. Что произойдет? Проверяет ли сервер целостность сессии?

4. **Dependency Confusion лаба**: Изучите концепцию Dependency Confusion. Напишите пример: как атакующий может подменить внутренний пакет `company-lib` на публичный в npm/pip, если названия совпадают.

5. **Анализ целостности**: Выберите любой загружаемый файл в DVWA/bWAPP (например, аватар). Если бы этот файл загружался с сервера обновлений, какие проверки должны быть выполнены перед использованием?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Integrity checks

### Минимум

Проверьте, загружаются ли внешние скрипты/ресурсы и есть ли SRI там, где это применимо.

### Практика Slider AI

Зафиксируйте URL публичных ресурсов, не скачивая закрытый код и не меняя запросы.

### Углубление после изучения следующих уроков

После урока 42 автоматизируйте проверку SRI/внешних доменов для одной страницы.

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
