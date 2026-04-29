# Занятие 23. Broken Authentication: Слабые пароли, Session Fixation

## Теория

**Broken Authentication** — это уязвимости в механизмах аутентификации и управления сессиями, позволяющие атакующему скомпрометировать учетные данные или сессии пользователей.

### Основные типы атак

1. **Credential Stuffing**: использование утекших баз паролей для входа (многие используют одинаковые пароли на разных сайтах)
2. **Brute Force**: перебор паролей (обычно коротких или простых)
3. **Weak Passwords**: использование паролей типа "123456", "password", "admin"
4. **Session Fixation**: атакующий заставляет жертву использовать сессию, известную атакующему
5. **Session Hijacking**: перехват или кража идентификатора сессии

### Session Fixation — механизм атаки

1. Атакующий получает валидный Session ID от сервера (например, `JSESSIONID=ABC123`)
2. Атакующий создает ссылку: `http://site.com/login?JSESSIONID=ABC123`
3. Жертва переходит по ссылке и авторизуется
4. Теперь атакующий с ID `ABC123` имеет доступ к аккаунту жертвы

### Признаки уязвимой аутентификации

- Отсутствие блокировки после N неудачных попыток (брутфорс)
- Сессия не меняется после входа (session fixation)
- Слабые пароли разрешены
- Session ID передается через URL (вместо cookie)
- Отсутствие HTTPS (перехват cookie)
- Длинные сессии без таймаута

### Session Management

Правильная реализация:
- Генерация новой сессии после входа
- Использование `HttpOnly` и `Secure` флагов для cookie
- Короткий таймаут неактивности
- Защита от фиксации сессии

---

## Практическое занятие

### Настройка DVWA

1. Откройте http://192.168.0.x (DVWA)
2. Установите уровень **Low**
3. Перейдите в **Brute Force**

### Практика: Brute Force на DVWA (Low)

**Шаг 1: Ручная проверка**
Попробуйте войти с:
- Login: `admin`, Password: `password` — успех
- Login: `admin`, Password: `123456` — может сработать

**Шаг 2: Брутфорс через Burp Suite Intruder**
1. Включите прокси Burp (127.0.0.1:8080)
2. В DVWA попробуйте войти с `admin` / `test`
3. В Burp (Proxy → HTTP history) найдите запрос логина
4. Отправьте запрос в Intruder (ПКМ → Send to Intruder)
5. В Intruder → Positions:
   - Clear §
   - Поставьте § вокруг значения пароля: `password=§test§`
6. В Intruder → Payloads → Load:
   - Загрузите словарь паролей (например, `/usr/share/wordlists/rockyou.txt` или маленький список: `password,123456,admin,letmein,qwerty`)
7. Нажмите Start Attack
8. Ищите ответ с другой длиной (Length) — это успешный вход

**Шаг 3: Session Fixation в bWAPP**
1. Откройте bWAPP: http://192.168.0.x
2. Проверьте, передается ли PHPSESSID через URL
3. Войдите как `bee` / `bug`
4. Посмотрите в DevTools → Application → Cookies — есть ли флаг HttpOnly?

### Практика: Анализ сессий

**Проверка смены сессии после входа:**
1. Откройте DevTools → Network
2. Войдите в DVWA, посмотрите заголовки ответа (Response Headers)
3. Ищите `Set-Cookie: PHPSESSID=...` — создается ли новая сессия?

На уровне Low в DVWA сессия обычно НЕ меняется — это уязвимость.

### Скриншоты для отчета

1. **Скриншот 1**: Burp Intruder — атака завершена, найден правильный пароль
2. **Скриншот 2**: DVWA — успешный вход после брутфорса
3. **Скриншот 3**: DevTools — Cookie с флагами (HttpOnly, Secure)

### Примеры вывода

**Burp Intruder — результат брутфорса:**
```
Payload 1: password
Payload 2: 123456
Payload 3: admin
Payload 4: letmein
...
Payload 7: password  [Status: 302, Length: 0] ← Успех!
```

**Cookie в DevTools:**
```
PHPSESSID: abc123def456
  Domain: localhost
  Path: /
  Expires: Session
  HttpOnly: ✓ (установлен)
  Secure: ✗ (отсутствует, небезопасно)
  SameSite: Lax
```

**Session Fixation — проверка:**
```bash
# Передача сессии через URL
http://192.168.0.x/portal.php?PHPSESSID=attacker_session
# Если сессия не меняется после входа — уязвимость
```

### Частые ошибки

1. **Забыть про флаг HttpOnly** — cookie доступна через `document.cookie`
2. **Сессия не меняется после входа** — классическая Session Fixation
3. **Отсутствие задержки при брутфорсе** — приложение не блокирует попытки
4. **Передача Session ID через URL** — сессия видна в логах, реферах

### Вопросы на понимание

1. Почему отсутствие флага HttpOnly — это проблема Broken Authentication?
2. В чем разница между Session Fixation и Session Hijacking?
3. Как флаг SameSite защищает от CSRF и почему это не Broken Authentication?
4. Почему передача Session ID через URL опасна?

### Адаптация под macOS (M2)

```bash
# Установка Burp Suite (если еще не установлен)
brew install --cask burp-suite

# Создание простого словаря паролей на macOS
cat > /tmp/passwords.txt << EOF
password
123456
admin
letmein
qwerty
EOF

# Брутфорс через curl (проверка идеи)
for pass in $(cat /tmp/passwords.txt); do
  curl -s -o /dev/null -w "%{http_code}" \
    -d "username=admin&password=$pass&Login=Login" \
    http://192.168.0.x/login.php
  echo " -> $pass"
done
```

---


## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. **Брутфорс пароля admin**: Используя Burp Suite Intruder, подберите пароль для пользователя `admin` в DVWA (уровень Low). Используйте небольшой словарь (10-20 паролей). Укажите в отчете: какой пароль был подобран, сколько попыток потребовалось, как вы определили успешную попытку (длина ответа, код ответа).

2. **Проверка других пользователей**: В DVWA (Low) попробуйте подобрать пароли для пользователей `gordonb`, `1337`, `pablo`. Используйте тот же метод с Burp Intruder. Сколько пользователей удалось взломать? Укажите их пароли.

3. **Session Fixation в bWAPP**: В bWAPP выберите уязвимость **Session Management** → **Session Fixation**. Изучите, как приложение обрабатывает сессии. Попробуйте передать PHPSESSID через URL: `http://192.168.0.x/portal.php?PHPSESSID=12345`. Создается ли новая сессия или используется переданная? Сделайте скриншот.

4. **Анализ уровня Medium**: Переключите DVWA на уровень **Medium** в Brute Force. Попробуйте ту же атаку через Burp Intruder. Что изменилось? Появилась ли защита от брутфорса (задержка, блокировка)? Опишите разницу.

5. **Парольная политика**: Напишите список требований к паролю, которые должны применяться в безопасном веб-приложении (минимум 5 требований). Приведите примеры инструментов для проверки сложности паролей (например, zxcvbn).
