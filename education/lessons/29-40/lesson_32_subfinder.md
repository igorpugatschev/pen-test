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

# Через Go
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder

# Проверка
subfinder -version
```

### Базовое использование
```bash
# Простой поиск поддоменов
subfinder -d example.com

# Сохранение в файл
subfinder -d example.com -o results.txt

# Вывод в формате JSON
subfinder -d example.com -o results.json -oJ
```

### Настройка источников
```bash
# Показать все доступные источники
subfinder -ls

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

## Задачи для самостоятельного выполнения

1. Сравните скорость работы Subfinder и Amass (passive) для домена `scanme.nmap.org`. Какой инструмент быстрее и почему?

2. Настройте хотя бы один API ключ (например, VirusTotal бесплатный). Запустите Subfinder с этим ключом. Изменилось ли количество найденных поддоменов?

3. Выполните рекурсивный поиск для домена `example.com`. Сколько уровней поддоменов удалось обнаружить?

4. Объедините результаты Subfinder и Amass в один файл, удалите дубликаты (`sort -u`). Сколько уникальных поддоменов получилось?

5. Используйте связку `subfinder | httpx` для проверки живых веб-серверов. Сколько хостов отвечают на порту 80/443?
