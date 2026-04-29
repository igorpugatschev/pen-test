# Урок 33: Dirsearch и ffuf — поиск скрытых директорий

## Теория

Поиск скрытых директорий и файлов — критический этап пентеста веб-приложений. Многие администраторы прячут админки, бэкапы, конфиги в неочевидных путях.

**Dirsearch** — классический инструмент на Python для брутфорса директорий.
**ffuf** (Fuzz Faster U Fool) — быстрый инструмент на Go, работает в разы быстрее.

Оба инструмента используют словари (wordlists) для перебора возможных путей.

## Практическое занятие

### Dirsearch

```bash
# Установка
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip install -r requirements.txt

# macOS (M2) — также можно через pip
pip3 install dirsearch

# Базовый запуск
python3 dirsearch.py -u http://example.com
# Пример вывода:
# Target: http://example.com
# [20:30:15] Starting: 
# [20:30:16] 200 -    12KB - /index.html
# [20:30:17] 403 -    1KB - /admin/

# Указание словаря
python3 dirsearch.py -u http://example.com -w /usr/share/wordlists/dirb/common.txt
# macOS (M2, Homebrew)
python3 dirsearch.py -u http://example.com -w /opt/homebrew/share/seclists/Discovery/Web-Content/common.txt

# Расширения файлов
python3 dirsearch.py -u http://example.com -e php,html,txt,bak

# Рекурсивный поиск
python3 dirsearch.py -u http://example.com -r

# Сохранение результатов
python3 dirsearch.py -u http://example.com -o results.txt
```

### ffuf

```bash
# Установка (Kali Linux)
sudo apt install ffuf

# macOS (M2, Homebrew)
brew install ffuf

# Через Go
go install github.com/ffuf/ffuf@latest

# Базовый запуск
ffuf -u http://example.com/FUZZ -w /usr/share/wordlists/dirb/common.txt
# Пример вывода:
# :: Method       : GET
# :: URL          : http://example.com/FUZZ
# :: Wordlist     : FUZZ: /usr/share/wordlists/dirb/common.txt
# :: Status codes : 200,204,301,302,307,403,404,500
# [Status: 200] [Size: 1234] [Words: 100] [Lines: 50] /index.html

# Поиск файлов с расширениями
ffuf -u http://example.com/FUZZ -w wordlist.txt -e .php,.html,.txt

# Фильтрация результатов (игнорировать 404)
ffuf -u http://example.com/FUZZ -w wordlist.txt -fc 404

# Поиск по конкретным статус-кодам
ffuf -u http://example.com/FUZZ -w wordlist.txt -mc 200,204,301,302,403
# Пример вывода:
# [Status: 301] [Size: 234] [Words: 14] [Lines: 8] /admin

# Рекурсивный (через скрипт или вручную)
```

### Полезные словари
```bash
# В Kali Linux уже есть словари
ls /usr/share/wordlists/

# Dirb (базовый)
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirb/big.txt

# SecLists (огромная коллекция)
/usr/share/wordlists/seclists/Discovery/Web-Content/

# macOS (M2, Homebrew)
brew install seclists
ls /opt/homebrew/share/seclists/Discovery/Web-Content/

# Скачать SecLists
git clone https://github.com/danielmiessler/SecLists.git /usr/share/wordlists/seclists
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

1. Запустите DVWA или bWAPP. Используйте dirsearch для поиска скрытых директорий. Какие интересные пути удалось найти?

2. Сравните скорость работы dirsearch и ffuf на одном и том же целевом сайте с одинаковым словарем. Какой инструмент быстрее?

3. Найдите файлы бэкапов (.bak, .old, .backup) на тестовом веб-сервере, используя расширения в ffuf.

4. Используя dirsearch с флагом `-e` (расширения), найдите все PHP-файлы в директории `/admin` тестового сайта.

5. Настройте рекурсивный поиск. Найдите вложенные директории глубиной 3 уровня на `testphp.vulnweb.com`.

## Частые ошибки

1. **Неправильный путь к словарям в macOS** — в macOS с Homebrew словари SecLists находятся в `/opt/homebrew/share/seclists/`, а не в `/usr/share/wordlists/`.

2. **Отсутствие расширений файлов** — при поиске директорий часто забывают указать `-e` для поиска файлов с расширениями.

3. **Слишком агрессивный ffuf** — большое количество потоков может вызвать блокировку IP, используйте `-rate` для ограничения.

4. **Dirsearch требует Python 3** — убедитесь, что используете `python3`, а не `python`.

## Вопросы на понимание

1. В чем главное преимущество ffuf перед dirsearch?

2. Как интерпретировать статус-коды ответов при поиске директорий (200, 301, 403, 404)?

3. Зачем нужен флаг `-e` в dirsearch и аналог `-e` в ffuf?

4. Какой словарь лучше использовать для глубокого аудита: common.txt или big.txt?
