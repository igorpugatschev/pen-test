# Урок 32: Subfinder — быстрая разведка поддоменов

## Теория

Subfinder — быстрый и простой инструмент для пассивного поиска поддоменов, разработанный проектом ProjectDiscovery (теми же, что сделали Nuclei). Работает быстрее Amass, но использует только пассивные источники.

Преимущества:
- Высокая скорость работы
- Поддержка множества источников (VirusTotal, Censys, Chaos, Shodan и др.)
- Простота использования
- Интеграция с другими инструментами ProjectDiscovery

## Практическое занятие

### Установка
```bash
# Kali Linux
sudo apt update && sudo apt install subfinder

# macOS (M2, Homebrew)
brew install subfinder

# Через Go
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder

# Проверка
subfinder -version
# Пример вывода:
# subfinder: v2.6.3
```

### Настройка источников
```bash
# Проверить конфигурацию (файл создается автоматически при первом запуске)
subfinder -config
# Пример вывода:
# Configuration file: /Users/username/.config/subfinder/config.yaml
# (откроется редактор для настройки API ключей)

# Посмотреть содержимое конфига
cat ~/.config/subfinder/config.yaml
# Пример вывода:
# provider-config:
#   virustotal:
#     - apikey: ""
#   censys:
#     - api_id: ""
#       api_secret: ""
```

### Базовое использование
```bash
# Простой поиск поддоменов
subfinder -d example.com
# Пример вывода:
# www.example.com
# mail.example.com
# ftp.example.com
# admin.example.com

# Сохранение в файл
subfinder -d example.com -o results.txt

# Вывод в формате JSON
subfinder -d example.com -o results.json -oJ
# Пример вывода (JSON):
# {"host":"www.example.com","source":"Virustotal"}
# {"host":"mail.example.com","source":"Censys"}
```

### Настройка источников
```bash
# Использовать только конкретные источники
subfinder -d example.com -sources virustotal,censys

# Исключить источники
subfinder -d example.com -exclude virustotal

# Рекурсивный поиск (искать поддомены у найденных поддоменов)
subfinder -d example.com -recursive
```

### Интеграция с другими инструментами
```bash
# Передать результаты в httpx (проверка живых хостов)
subfinder -d example.com | httpx -o live_hosts.txt

# Передать в Nuclei для поиска уязвимостей
subfinder -d example.com | httpx | nuclei -t vulnerabilities/

# Комбинация с Amass
amass enum -passive -d example.com | subfinder -d example.com | sort -u > all_subdomains.txt
# Пример вывода (результат в файле):
# admin.example.com
# api.example.com
# www.example.com
```

### Конфигурация API ключей
```bash
# При первом запуске subfinder автоматически создает конфиг:
# ~/.config/subfinder/config.yaml
# Можно открыть его для редактирования вручную:
nano ~/.config/subfinder/config.yaml

# Пример конфига с API ключами:
# provider-config:
#   virustotal:
#     - apikey: "ваш_ключ"
#   censys:
#     - api_id: "ваш_id"
#       api_secret: "ваш_секрет"
```

### Конфигурация API ключей
```bash
# Создать конфиг (редактировать ~/.config/subfinder/config.yaml)
subfinder -config

# Пример конфига с API ключами:
# virustotal:
#   - apikey: "ваш_ключ"
# censys:
#   - api_id: "ваш_id"
#   - api_secret: "ваш_секрет"
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

1. Сравните скорость работы Subfinder и Amass (passive) для домена `scanme.nmap.org`. Какой инструмент быстрее и почему?

2. Настройте хотя бы один API ключ (например, VirusTotal бесплатный). Запустите Subfinder с этим ключом. Изменилось ли количество найденных поддоменов?

3. Выполните рекурсивный поиск для домена `example.com`. Сколько уровней поддоменов удалось обнаружить?

4. Объедините результаты Subfinder и Amass в один файл, удалите дубликаты (`sort -u`). Сколько уникальных поддоменов получилось?

5. Используйте связку `subfinder | httpx` для проверки живых веб-серверов. Сколько хостов отвечают на порту 80/443?

## Частые ошибки

1. **Флаг `-ls` больше не работает** — в новых версиях Subfinder этот флаг удален, для просмотра источников используйте конфиг или документацию.

2. **Отсутствие конфигурационного файла** — файл `~/.config/subfinder/config.yaml` создается автоматически при первом запуске subfinder, не нужно создавать его вручную.

3. **Неправильный путь к конфигу в macOS** — в macOS путь будет `/Users/username/.config/subfinder/config.yaml`, а не `/root/.config/...`.

4. **Запуск без API ключей** — многие источники (VirusTotal, Censys) требуют API ключи, без них поддоменов будет меньше.

## Вопросы на понимание

1. В чем разница между Subfinder и Amass по методам сбора информации?

2. Зачем нужен рекурсивный поиск (`-recursive`) и когда его стоит использовать?

3. Как настроить API ключи в Subfinder и почему они важны?

4. Почему вывод Subfinder может отличаться при запуске с одного и того же домена в разные дни?
