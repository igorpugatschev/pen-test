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

# Базовый запуск
python3 dirsearch.py -u http://example.com

# Указание словаря
python3 dirsearch.py -u http://example.com -w /usr/share/wordlists/dirb/common.txt

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

# Через Go
go install github.com/ffuf/ffuf@latest

# Базовый запуск
ffuf -u http://example.com/FUZZ -w /usr/share/wordlists/dirb/common.txt

# Поиск файлов с расширениями
ffuf -u http://example.com/FUZZ -w wordlist.txt -e .php,.html,.txt

# Фильтрация результатов (игнорировать 404)
ffuf -u http://example.com/FUZZ -w wordlist.txt -fc 404

# Поиск по конкретным статус-кодам
ffuf -u http://example.com/FUZZ -w wordlist.txt -mc 200,204,301,302,403

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

# Скачать SecLists
git clone https://github.com/danielmiessler/SecLists.git /usr/share/wordlists/seclists
```

## Задачи для самостоятельного выполнения

1. Запустите DVWA или bWAPP. Используйте dirsearch для поиска скрытых директорий. Какие интересные пути удалось найти?

2. Сравните скорость работы dirsearch и ffuf на одном и том же целевом сайте с одинаковым словарем. Какой инструмент быстрее?

3. Найдите файлы бэкапов (.bak, .old, .backup) на тестовом веб-сервере, используя расширения в ffuf.

4. Используя dirsearch с флагом `-e` (расширения), найдите все PHP-файлы в директории `/admin` тестового сайта.

5. Настройте рекурсивный поиск. Найдите вложенные директории глубиной 3 уровня на `testphp.vulnweb.com`.
