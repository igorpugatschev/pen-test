# Занятие 17e. OWASP A08: Software and Data Integrity Failures — Нарушение целостности ПО и данных

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

Пример вывода команд будет добавлен индивидуально для каждого урока.



## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
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
