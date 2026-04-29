# Занятие 6: Поиск файлов и работа с текстом

## Теория

Поиск файлов и анализ текста — ежедневные задачи пентестера. Нужно быстро найти конфиги, пароли, ключи, логи.

> **Примечание для macOS (M2, 8GB):** Для запуска Kali Linux на Mac M2 используйте UTM или Parallels Desktop вместо VirtualBox. Выделяйте виртуалке 3-4GB RAM при 8GB на хосте. Установка пакетов: `sudo apt install` (Kali), `brew install` (macOS).

### Поиск файлов (find)

`find` ищет по файловой системе по разным критериям:
- `-name` — по имени
- `-type` — по типу (f файл, d директория, l ссылка)
- `-size` — по размеру
- `-mtime` — по времени изменения
- `-perm` — по правам доступа
- `-user` — по владельцу
- `-exec` — выполнить команду для найденных файлов

### Поиск в тексте (grep)

`grep` ищет паттерны в тексте:
- `-i` — игнорировать регистр
- `-r` — рекурсивно по директориям
- `-n` — показать номера строк
- `-v` — инвертировать (показать то, что НЕ совпадает)
- `-E` — расширенные регулярные выражения

### Обработка текста

| Команда | Назначение |
|---------|-----------|
| `awk` | Мощный процессор текста (по полям) |
| `sed` | Потоковый редактор (замена, удаление) |
| `cut` | Вырезать колонки |
| `sort` | Сортировка строк |
| `uniq` | Удаление дубликатов |
| `wc` | Подсчет строк/слов/символов |

### Архивы

| Команда | Назначение |
|---------|-----------|
| `tar -czf` | Создать .tar.gz |
| `tar -xzf` | Распаковать .tar.gz |
| `gzip` / `gunzip` | Сжать / распаковать .gz |
| `zip` / `unzip` | Работа с .zip |

## Практическое занятие

### Шаг 1: Поиск файлов (find)

```bash
# Найти все файлы с расширением .conf в /etc
find /etc -name "*.conf" 2>/dev/null
```
**Пример вывода:**
```text
/etc/resolv.conf
/etc/hosts.conf
/etc/ld.so.conf
/etc/systemd/system.conf
/etc/ssh/sshd_config
```

```bash
# Найти файлы, измененные за последние 7 дней
find / -mtime -7 2>/dev/null | head -20
```
**Пример вывода:**
```text
/home/user/.bash_history
/home/user/terminal_practice/test.txt
/var/log/syslog
/tmp/test.txt
```

```bash
# Найти файлы больше 100 МБ
find / -size +100M 2>/dev/null
```

```bash
# Найти файлы с SUID-битом
find / -perm -4000 2>/dev/null
```
**Пример вывода:**
```text
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/su
```

```bash
# Найти файлы, доступные на запись всем
find / -perm -002 2>/dev/null | head -10
```

```bash
# Найти и выполнить команду для каждого файла
find /etc -name "*.conf" -exec ls -l {} \;
```
**Пример вывода:**
```text
-rw-r--r-- 1 root root 123 Jan 10 09:00 /etc/hosts.conf
-rw-r--r-- 1 root root 456 Jan 10 09:00 /etc/ld.so.conf
```

### Шаг 2: Поиск в тексте (grep)

```bash
# Поиск паттерна в файле
grep "root" /etc/passwd
```
**Пример вывода:**
```text
root:x:0:0:root:/root:/bin/bash
```

```bash
# Рекурсивный поиск по директории
grep -r "password" /etc/ 2>/dev/null
```

```bash
# Игнорировать регистр
grep -i "error" /var/log/syslog
```
**Пример вывода:**
```text
Jan 10 10:00:00 kali kernel: [    0.000] error: some message
```

```bash
# Показать номера строк
grep -n "bash" /etc/passwd
```
**Пример вывода:**
```text
1:root:x:0:0:root:/root:/bin/bash
7:user:x:1000:1000:user:/home/user:/bin/bash
```

```bash
# Инвертировать поиск (показать строки БЕЗ паттерна)
grep -v "nologin" /etc/passwd
```

```bash
# Регулярные выражения (строки, начинающиеся с root)
grep "^root" /etc/passwd
```

### Шаг 3: Обработка текста (awk, sed)

```bash
# Вывести только первое поле (пользователи) из /etc/passwd
awk -F: '{print $1}' /etc/passwd
```
**Пример вывода:**
```text
root
daemon
bin
user
```

```bash
# Вывести пользователей с UID >= 1000
awk -F: '$3 >= 1000 {print $1, $3}' /etc/passwd
```
**Пример вывода:**
```text
user 1000
```

```bash
# Замена текста через sed (вывод в stdout)
sed 's/root/admin/g' /etc/passwd | head -5
```

```bash
# Замена "на месте" (изменяет файл, -i)
echo "hello world" > test.txt
sed -i 's/world/earth/' test.txt
cat test.txt
```
**Пример вывода `cat test.txt`:**
```text
hello earth
```

```bash
# Удаление строк через sed
sed -i '/^#/d' test.txt  # удалить строки, начинающиеся с #
```

### Шаг 4: Работа с архивами

```bash
# Создать tar.gz архив
tar -czf backup.tar.gz ~/terminal_practice

# Распаковать tar.gz
mkdir extract_test
tar -xzf backup.tar.gz -C extract_test/

# Посмотреть содержимое без распаковки
tar -tzf backup.tar.gz
```
**Пример вывода `tar -tzf backup.tar.gz`:**
```text
home/user/terminal_practice/
home/user/terminal_practice/test.txt
home/user/terminal_practice/dir1/
```

```bash
# Сжать файл gzip
gzip test.txt
ls test.txt.gz
```

```bash
# Распаковать gzip
gunzip test.txt.gz
```

```bash
# Создать zip архив
zip -r backup.zip ~/terminal_practice

# Распаковать zip
unzip backup.zip -d extract_zip/
```

### Шаг 5: Комбинирование инструментов

```bash
# Найти все конфиги, содержащие "password"
find /etc -name "*.conf" -exec grep -l "password" {} \; 2>/dev/null
```

```bash
# Найти всех пользователей и посчитать их количество
awk -F: '{print $1}' /etc/passwd | wc -l
```
**Пример вывода:**
```text
24
```

```bash
# Найти топ-5 самых больших файлов в /var
find /var -type f -exec ls -l {} \; 2>/dev/null | sort -k5 -nr | head -5
```

```bash
# Извлечь все IP-адреса из лог-файла
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' /var/log/auth.log 2>/dev/null | sort | uniq -c | sort -nr
```
**Пример вывода:**
```text
15 192.168.1.105
8 10.10.14.5
3 8.8.8.8
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

1. Найдите все файлы в системе (кроме `/proc` и `/sys`), которые имеют размер 0 байт (пустые файлы). Используйте `find` с параметром `-empty` или `-size 0`. Запишите первые 10 результатов.

2. Найдите в `/var/log/` все строки, содержащие слово "failed" (без учета регистра). Используйте `grep -ri`. Посчитайте количество таких строк с помощью `wc -l`.

3. Создайте файл `data.txt` с 20 строками произвольного текста. Используйте `awk`, чтобы вывести только строки, содержащие более 3 слов. Используйте `sed`, чтобы заменить все вхождения "the" на "THE".

4. Найдите все файлы в домашней директории, которые были изменены за последние 24 часа. Создайте их архив `recent_files.tar.gz` с помощью `tar`.

5. Напишите однострочный скрипт (one-liner), который ищет в `/etc` все файлы, содержащие слово "DNS" (без учета регистра), и выводит только имена этих файлов (без пути). Используйте комбинацию `find`, `grep` и `basename`.

## Частые ошибки

1. **Отсутствие `2>/dev/null` при использовании `find /`.** Поиск от корня выдает много ошибок "Permission denied", которые засоряют вывод.
2. **Забытое `\;` в `-exec`.** Команда `find ... -exec ls -l {} \;` требует завершения точкой с запятой, экранированной обратным слэшем.
3. **Путаница между `grep -r` и `find ... -exec grep`.** `grep -r` рекурсивно ищет внутри файлов, `find` ищет сами файлы по критериям.
4. **Неправильное использование `sed -i`.** Ключ `-i` изменяет файл на месте без создания копии, будьте осторожны с важными файлами.

## Вопросы на понимание

1. Чем отличается `find /etc -name "*.conf"` от `grep -r "conf" /etc`?
2. Как найти файлы, измененные за последние 24 часа, используя `find`?
3. Что делает команда `awk -F: '{print $1}' /etc/passwd`?
4. Зачем нужно перенаправление `2>/dev/null` при поиске файлов от корня?
5. Как распаковать `.tar.gz` архив в конкретную директорию?
