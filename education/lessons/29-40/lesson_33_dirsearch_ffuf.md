# Урок 33: Dirsearch и ffuf — поиск скрытых директорий

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

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Content discovery

### Минимум

Не запускайте словари по Slider AI; составьте список публичных путей, уже видимых из навигации.

### Практика Slider AI

Проверьте вручную 3-5 видимых URL на корректные статусы и отсутствие directory listing.

### Углубление после изучения следующих уроков

После отдельного разрешения запланируйте small wordlist run с 1 rps и stop conditions.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.
