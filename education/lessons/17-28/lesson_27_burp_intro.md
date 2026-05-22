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

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: разделение lab payload и product-safe marker, HTTP evidence, перевод риска OWASP в security test case. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: учебные payloads выполнять только в DVWA/WebGoat/PortSwigger; на Slider AI использовать безопасные маркеры и passive evidence. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

## Теория

**Burp Suite** — это интегрированная платформа для тестирования безопасности веб-приложений. Состоит из нескольких инструментов (табов).

### Основные инструменты

1. **Proxy**: Перехватывает трафик между браузером и сервером
2. **Repeater**: Позволяет повторять и изменять запросы вручную
3. **Intruder**: Автоматизированная подстановка значений; в этом курсе только lab-only или после отдельного approval
4. **Decoder**: Кодирование/декодирование данных
5. **Comparer**: Сравнение двух данных (запросов, ответов)
6. **Scanner** (Pro): Автоматическое сканирование уязвимостей
7. **Sequencer**: Анализ случайности токенов/сессий
8. **Extender**: Плагины (BApp Store)

### Как работает Proxy

1. Браузер настроен на использование прокси 127.0.0.1:8080
2. Весь трафик идет через Burp
3. Burp может:
   - Просто пропускать (Forward)
   - Остановить для анализа (Intercept on/off)
   - Изменить запрос перед отправкой

### Repeater — назначение

Используется для:
- Изучения ответов сервера на модифицированные запросы
- Тестирования SQL Injection, XSS вручную
- Проверки граничных случаев

### Intruder — назначение

Используется для:
- учебной демонстрации подстановки значений в lab;
- проверки rate limit только после отдельного approval;
- fuzzing параметров в специально разрешенной среде;
- анализа различий ответов без применения к Slider AI по умолчанию.

### Типы атак Intruder

1. **Sniper**: Одна позиция, один словарь
2. **Battering ram**: Одно значение подставляется во все позиции
3. **Pitchfork**: Уникальные значения из нескольких словарей (параллельно)
4. **Cluster bomb**: Все комбинации из нескольких словарей

---

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
