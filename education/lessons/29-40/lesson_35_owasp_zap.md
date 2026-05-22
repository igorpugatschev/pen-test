# Урок 35: OWASP ZAP — альтернатива Burp Suite

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 35: OWASP ZAP — альтернатива Burp Suite`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

OWASP ZAP (Zed Attack Proxy) — бесплатный инструмент для тестирования веб-приложений на проникновение. Альтернатива Burp Suite Community/Pro. Полностью open-source.

Основные возможности:
- Перехват и изменение трафика (Proxy)
- Автоматическое сканирование (Spider, Ajax Spider)
- Fuzzer для параметров
- Поиск уязвимостей (Passive + Active Scan)
- REST API для автоматизации
- Поддержка скриптов (Zest)

## Guided practice

1. Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.
2. Заполните tool approval card до запуска любой инструментальной проверки.
3. Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.
4. Проведите false-positive review и приложите только sanitized output.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Установка и запуск
```bash
# Kali Linux (уже установлен)
zaproxy &

# macOS (M2, Homebrew)
brew install --cask owasp-zap

# Или через меню: Applications -> 03 - Web Application Analysis -> owasp-zap

# Запуск в headless режиме (без GUI)
zap-cli start
```

### Настройка браузера
1. Запустите ZAP
2. В браузере настройте прокси: `127.0.0.1:8080`
3. Скачайте и установите CA-сертификат ZAP для HTTPS: `Tools -> Options -> Dynamic SSL Certificates -> Save`

Пример успешной настройки прокси:
```
Browser: Firefox
Settings -> Network Settings -> Manual proxy configuration:
HTTP Proxy: 127.0.0.1  Port: 8080
SSL Proxy: 127.0.0.1  Port: 8080
```

### Автоматическое сканирование
```bash
# Через GUI:
# 1. Введите URL в поле "Quick Start"
# 2. Нажмите "Attack"

# Через CLI (zap-cli)
pip install zapcli

# Или через Docker:
docker run -t owasp/zap2docker-stable zap-cli status

# Использование zap-cli
zap-cli open-url http://127.0.0.1:8080
# Пример вывода:
# Opened URL: http://127.0.0.1:8080

zap-cli spider http://127.0.0.1:8080
# Пример вывода:
# Spider started at: http://127.0.0.1:8080
# Spider progress: 100%
# Spider completed

# lab-only/approval: zap-cli active-scan http://127.0.0.1:8080
# Пример вывода:
# Active scan started for: http://127.0.0.1:8080
# Scan progress: 100%
# Scan completed

zap-cli alerts -l High
# Пример вывода:
# [{'id': '10003', 'name': 'X-Frame-Options header scanner', ...}]
```

### Использование Proxy (ручной/passive режим)
1. Настройте браузер на прокси ZAP (8080)
2. Откройте целевой сайт
3. В ZAP вы увидите весь трафик в History
4. Для обязательного пути используйте только History и Passive Scan.
5. Fuzz/Active Scan выполняются только в DVWA/PortSwigger/local lab или после отдельного approval.

Пример увиденного трафика в ZAP:
```
History tab:
GET http://127.0.0.1:8080/ 200 OK 1234 bytes
POST http://127.0.0.1:8080/login 200 OK 456 bytes
```

### Fuzzer (lab-only/approval)
1. Откройте History -> выберите запрос
2. Right-click -> Attack -> Fuzz
3. Выделите параметр -> Add -> выберите словарь
4. Start Fuzzer только в lab или после approval.
5. Анализируйте ответы как candidate evidence; не считайте scanner output подтвержденной уязвимостью.

Пример результатов Fuzzer:
```
URL: http://127.0.0.1:8080/login
Parameter: username
Payload: admin -> Response: 200 OK (Login successful)
Payload: test -> Response: 401 Unauthorized
```

### Passive и Active Scan
- **Passive Scan** — анализ трафика без отправки атакующих запросов (безопасно)
- **Active Scan** — реальные атаки на уязвимости (может нагрузить сервер)

```bash
# API вызовы
zap-cli passive-scan -r http://127.0.0.1:8080
# Пример вывода:
# Passive scan completed for: http://127.0.0.1:8080

# lab-only/approval: zap-cli active-scan -r http://127.0.0.1:8080
# Пример вывода:
# Active scan progress: 100%
# Scan completed
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

1. Запустите DVWA на уровне Low. Настройте браузер на прокси ZAP. Попробуйте выполнить SQL Injection, перехватывая запросы в ZAP.

2. Используйте Spider (паук) в ZAP для обхода сайта `локальный DVWA/bWAPP или PortSwigger lab`. Сколько уникальных URL удалось найти?

3. Запустите Active Scan только против DVWA/PortSwigger/local lab. Какие candidate findings обнаружил ZAP? Сравните с результатами ручного тестирования и отметьте false positives.

4. Используйте Fuzzer ZAP для подбора директорий на `локальный DVWA/bWAPP или PortSwigger lab/admin/`. Используйте словарь `/usr/share/wordlists/dirb/common.txt`. Какие пути нашлись?

5. Настройте ZAP в headless режиме (через `zap-cli`). Напишите Python-скрипт, который запускает сканирование через `zap-cli` и сохраняет алерты в JSON.

## Частые ошибки

1. **Проблемы с HTTPS (SSL/TLS)** — обязательно установите CA-сертификат ZAP, иначе браузер будет ругаться на "незащищенное соединение".

2. **ZAP не видит трафик** — проверьте, что прокси в браузере настроен правильно (127.0.0.1:8080) и ZAP запущен.

3. **Active Scan на "боевых" серверах** — активное сканирование может нагрузить сервер или вызвать подозрение, используйте только на разрешенных целях.

4. **Docker-версия ZAP требует проброса портов** — при запуске через `docker run` убедитесь, что порт 8080 проброшен (`-p 8080:8080`).

## Вопросы на понимание

1. В чем разница между Passive и Active сканированием в ZAP?

2. Зачем нужна установка CA-сертификата ZAP в браузере?

3. Как использовать ZAP для тестирования мобильных приложений (Android/iOS)?

4. Чем ZAP отличается от Burp Suite Community Edition?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** ZAP passive

### Минимум

Откройте Slider AI через ZAP proxy и включите только passive scan.

### Практика Slider AI

Соберите alerts passive scan, удалите cookies/tokens и классифицируйте informational vs finding.

### Углубление после изучения следующих уроков

После урока 40 экспортируйте отчет ZAP и добавьте ручную валидацию.

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
