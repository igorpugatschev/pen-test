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

# Обновление базы
searchsploit -u

# Путь к базе и эксплойтам
ls /usr/share/exploitdb/
```

### Базовый поиск
```bash
# Поиск по названию
searchsploit apache 2.4
searchsploit vsftpd
searchsploit samba

# Поиск без учета регистра
searchsploit -i mysql

# Только заголовки (игнорировать пути)
searchsploit -t php
```

### Фильтрация по платформе/типу
```bash
# Только для Windows
searchsploit -p windows samba

# Только webapps
searchsploit -t webapps wordpress

# Удаленные эксплойты (Remote)
searchsploit -t remote ftp

# Локальное повышение привилегий (Local)
searchsploit -t local linux kernel
```

### Работа с найденными эксплойтами
```bash
# Посмотреть путь к эксплойту
searchsploit samba 3.0

# Скопировать эксплойт в текущую директорию
searchsploit -m 12345

# Прочитать эксплойт
searchsploit -x 12345

# Открыть URL к эксплойту на exploit-db.com
searchsploit -w 12345
```

### Поиск по конкретной уязвимости (CVE)
```bash
# Поиск по CVE
searchsploit CVE-2017-0144  # EternalBlue

# Поиск по BID (Bugtraq ID)
searchsploit BID-12345

# Поиск по EDB-ID
searchsploit -p 12345
```

## Задачи для самостоятельного выполнения

1. Найдите все эксплойты для vsftpd 2.3.4 (знаменитый backdoor). Сколько их? Скопируйте один в текущую директорию и изучите код.

2. Используя SearchSploit, найдите эксплойты для Samba (любой версии). Какие типы атак доступны (remote, local)?

3. Найдите эксплойт для уязвимости EternalBlue (CVE-2017-0144). Какой EDB-ID у этого эксплойта? Почитайте описание на exploit-db.com.

4. Настройте Metasploitable2. Определите версию Samba. Найдите подходящий эксплойт через SearchSploit. Попробуйте применить его (если уверены).

5. Сравните результаты SearchSploit и поиска на сайте exploit-db.com для "Apache 2.4.49". Есть ли разница?
