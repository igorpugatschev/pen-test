# Урок 37: SearchSploit — поиск эксплойтов

## Теория

SearchSploit — инструмент командной строки для поиска эксплойтов в базе Exploit-DB (Exploit Database). Позволяет быстро находить готовые эксплойты для известных уязвимостей без использования браузера.

Основные возможности:
- Поиск по названию ПО/сервиса
- Копирование эксплойта в текущую директорию
- Поиск по конкретным платформам (Windows, Linux, PHP, etc.)
- Поиск по типам (remote, dos, local, webapps)

## Практическое занятие

### Установка и обновление
```bash
# Kali Linux (уже установлен)
searchsploit --version

# macOS (M2, Homebrew)
brew install exploitdb

# Обновление базы
searchsploit -u
# Пример вывода:
# Updating via apt
# [*] Updating exploit database...
# [*] Updating exploitdb_cache...

# Путь к базе и эксплойтам
ls /usr/share/exploitdb/
# Пример вывода (macOS):
# /opt/homebrew/share/exploitdb/
```

### Базовый поиск
```bash
# Поиск по названию
searchsploit apache 2.4
# Пример вывода:
# Exploits: No Results
# Shellcodes: No Results

searchsploit vsftpd
# Пример вывода:
# Exploits: 3
#   |  Path
#   |  /usr/share/exploitdb/exploits/linux/remote/17491.rb

searchsploit samba
# Пример вывода:
# Exploits: 45
#   |  Path
#   |  /usr/share/exploitdb/exploits/linux/remote/10.c

# Поиск без учета регистра
searchsploit -i mysql

# Только заголовки (игнорировать пути)
searchsploit -t php
```

### Фильтрация по платформе/типу
```bash
# Только для Windows
searchsploit --platform windows samba
# Пример вывода:
# Exploits: 12
#   |  Path
#   |  /usr/share/exploitdb/exploits/windows/remote/...

# Только webapps
searchsploit -t webapps wordpress
# Пример вывода:
# Exploits: 850
#   |  Path
#   |  /usr/share/exploitdb/exploits/php/webapps/...

# Удаленные эксплойты (Remote)
searchsploit -t remote ftp

# Локальное повышение привилегий (Local)
searchsploit -t local linux kernel
```

### Работа с найденными эксплойтами
```bash
# Посмотреть путь к эксплойту
searchsploit samba 3.0
# Пример вывода:
# Exploits: 5
#   |  Path
#   |  /usr/share/exploitdb/exploits/linux/remote/10.c

# Скопировать эксплойт в текущую директорию
searchsploit -m 12345
# Пример вывода:
#  Copied to: /current/dir/12345.rb

# Прочитать эксплойт
searchsploit -x 12345

# Открыть URL к эксплойту на exploit-db.com
searchsploit -w 12345
# Пример вывода:
#  URL: https://www.exploit-db.com/exploits/12345
```

### Поиск по конкретной уязвимости (CVE)
```bash
# Поиск по CVE
searchsploit CVE-2017-0144  # EternalBlue
# Пример вывода:
# Exploits: 5
#   |  Path
#   |  /usr/share/exploitdb/exploits/windows/remote/42315.py

# Поиск по BID (Bugtraq ID)
searchsploit BID-12345

# Поиск по EDB-ID
searchsploit -p 12345
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

1. Найдите все эксплойты для vsftpd 2.3.4 (знаменитый backdoor). Сколько их? Скопируйте один в текущую директорию и изучите код.

2. Используя SearchSploit, найдите эксплойты для Samba (любой версии). Какие типы атак доступны (remote, local)?

3. Найдите эксплойт для уязвимости EternalBlue (CVE-2017-0144). Какой EDB-ID у этого эксплойта? Почитайте описание на exploit-db.com.

4. Настройте Metasploitable2. Определите версию Samba. Найдите подходящий эксплойт через SearchSploit. Попробуйте применить его (если уверены).

5. Сравните результаты SearchSploit и поиска на сайте exploit-db.com для "Apache 2.4.49". Есть ли разница?

## Частые ошибки

1. **Использование флага `-p` вместо `--platform`** — в новых версиях SearchSploit флаг `-p` используется для поиска по EDB-ID, а фильтрация по платформе делается через `--platform`.

2. **Забыли обновить базу** — команда `searchsploit -u` должна выполняться регулярно, иначе будут отсутствовать новые эксплойты.

3. **Путаница с путями** — в macOS путь к базе exploitdb может отличаться (`/opt/homebrew/share/exploitdb/` вместо `/usr/share/exploitdb/`).

4. **Копирование эксплойта без проверки** — всегда изучайте код эксплойта перед запуском, чтобы не нанести вред системе.

## Вопросы на понимание

1. Чем отличается поиск по CVE и по названию ПО в SearchSploit?

2. Как определить, подходит ли найденный эксплойт для вашей цели (учитывая архитектуру, версию ОС)?

3. Почему флаг `--platform` важен при поиске эксплойтов?

4. Что делает флаг `-m` и в чем разница между `-m` и `-x`?
