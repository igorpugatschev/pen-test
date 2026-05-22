# Урок 38: Shodan и Censys — OSINT разведка

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 38: Shodan и Censys — OSINT разведка`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

**Shodan** — поисковая система для интернет-устройств. Индексирует не веб-страницы, а сервисы (SSH, FTP, HTTP, IoT устройства, камеры, свитчи).

**Censys** — аналогичный сервис, предоставляет детальную информацию о сертификатах, хостах и сетях.

Примеры использования:
- Поиск незащищенных камер, роутеров
- Поиск серверов с уязвимыми версиями ПО
- Сбор информации о целевой организации
- Поиск открытых портов и сервисов

## Guided practice

1. Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.
2. Заполните tool approval card до запуска любой инструментальной проверки.
3. Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.
4. Проведите false-positive review и приложите только sanitized output.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Shodan CLI

```bash
# Установка
pip install shodan

# macOS (M2, Homebrew) — shodan устанавливается через pip
# brew install shodan  # (если доступно)

# Инициализация (нужен API ключ)
shodan init YOUR_API_KEY
# Пример вывода:
# Successfully initialized

# Базовый поиск
shodan search "apache"
# Пример вывода:
# 198.51.100.1:80    Apache httpd 2.4.41
# 203.0.113.5:8080   Apache Tomcat 9.0.31

shodan search "port:22"
# Пример вывода:
# 198.51.100.2:22    SSH OpenSSH 8.2

# Информация о хосте
shodan host 8.8.8.8
# Пример вывода:
# Country:     United States
# Organization: Google LLC
# Open Ports:  53, 443

# Сканирование публичных IP (Shodan сканирует только публичные адреса!)
# ПРИМЕЧАНИЕ: 192.168.x.x — это приватные IP, Shodan их НЕ сканирует
# Для примера используем публичный IP (например, scanme.nmap.org)
shodan scan submit 45.33.32.156  # scanme.nmap.org
# Пример вывода:
# Scan request submitted successfully

# Поиск уязвимостей
shodan search "vuln:CVE-2021-41773"

# Статистика
shodan stats "apache country:RU"
```

### Shodan Web (через браузер)
```
# Поисковые фильтры:
hostname:target.com
port:80,443
org:"Target Organization"
city:"Moscow"
country:"RU"
vuln:CVE-2021-xxxxx
product:"Apache httpd"
version:"2.4.49"
os:"Windows"
```

### Censys

```bash
# Установка CLI
pip install censys

# Инициализация
censys config  # Ввести API ID и Secret
# Пример вывода:
# Successfully authenticated

# Поиск хостов
censys search "services.http.response.status_code: 200"
# Пример вывода:
# 8.8.8.8
# services: 53/dns, 443/https

# Поиск по IP
censys view 8.8.8.8
# Пример вывода:
# ip: 8.8.8.8
# services:
#   - port: 443
#     service_name: HTTPS

# Поиск сертификатов
censys search --index certificates "parsed.subject_dn: target.com"
```

### Полезные запросы Shodan
```
# Камеры (IoT)
webcam
"Server: uc-httpd"

# Промышленные системы (ICS/SCADA)
"SCADA"
port:502

# Базы данных (открытые)
port:27017 MongoDB
port:6379 Redis

# Уязвимые сервисы
"vsftpd 2.3.4"
"ProFTPD 1.3.3c"

# Админки
"admin panel" port:8080
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

1. Зарегистрируйтесь на Shodan (бесплатно). Получите API ключ. Настройте CLI.

2. Найдите через Shodan все серверы Apache в России (country:RU product:"Apache"). Сколько результатов? Попробуйте найти серверы с уязвимой версией 2.4.49.

3. Используя Shodan, найдите открытые MongoDB базы данных (port:27017). Почему это опасно?

4. Настройте Censys CLI. Выполните поиск сертификатов для домена `example.com`. Сколько субдоменов удалось найти через сертификаты?

5. Сравните результаты Shodan и Censys для одного и того же IP-адреса. Какая информация отличается?

## Частые ошибки

1. **Попытка сканировать приватные IP** — Shodan работает только с публичными IP-адресами, 192.168.x.x, 10.x.x.x, 172.16.x.x не будут работать.

2. **Отсутствие API ключа** — большинство функций Shodan требуют регистрации и получения API ключа (бесплатно).

3. **Слишком общие запросы** — используйте фильтры (country:, city:, port:), чтобы сузить поиск.

4. **Забыли про Censys** — Censys часто дает более свежую информацию о сертификатах, чем Shodan.

## Вопросы на понимание

1. Чем Shodan отличается от обычного поисковика (Google, Bing)?

2. Почему Shodan не может сканировать приватные IP-адреса?

3. Как использовать информацию из Shodan для пентеста (легального)?

4. В чем разница между Shodan и Censys по предоставляемой информации?

### Полезные запросы Shodan
```
# Камеры (IoT)
webcam
"Server: uc-httpd"

# Промышленные системы (ICS/SCADA)
"SCADA"
port:502

# Базы данных (открытые)
port:27017 MongoDB
port:6379 Redis

# Уязвимые сервисы
"vsftpd 2.3.4"
"ProFTPD 1.3.3c"

# Админки
"admin panel" port:8080
```

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** OSINT boundaries

### Минимум

Проверьте только публичную информацию о `olddev.slider-ai.ru` в браузере, без запуска internet scan.

### Практика Slider AI

Сохраните найденные публичные metadata и отметьте, что не является доказательством уязвимости.

### Углубление после изучения следующих уроков

После урока 61 добавьте OSINT-границы в RoE.

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
