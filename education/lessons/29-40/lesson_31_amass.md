# Урок 31: Amass — разведка поддоменов

## Теория

Amass (Automated Attack Surface Mapping) — мощный инструмент для внешней разведки, разработанный OWASP. Использует пассивные и активные методы для обнаружения поддоменов, связей и инфраструктуры цели.

Основные режимы работы:
- **Passive** — сбор данных из публичных источников (без прямого контакта с целью)
- **Active** — DNS-запросы к цели для подтверждения поддоменов
- **Intel** — сбор общей информации об организации
- **Enum** — полное перечисление поддоменов

## Практическое занятие

### Установка
```bash
# Kali Linux
sudo apt update && sudo apt install amass

# Или через Go
go install -v github.com/owasp-amass/amass/v3/...@master

# Проверка
amass --version
```

### Пассивный сбор
```bash
# Пассивный поиск поддоменов (не касается цели напрямую)
amass enum -passive -d example.com

# С выводом IP-адресов
amass enum -passive -d example.com -ip

# Сохранение в файл
amass enum -passive -d example.com -o results.txt
```

### Активное перечисление
```bash
# Активный режим (DNS-запросы к цели)
amass enum -active -d example.com

# С брутфорсом поддоменов
amass enum -brute -d example.com

# Использование словаря
amass enum -brute -w /usr/share/wordlists/dirb/common.txt -d example.com
```

### Intel режим (сбор информации об организации)
```bash
# Поиск доменов, связанных с организацией
amass intel -org "Target Organization"

# Поиск по ASN
amass intel -asn 1337

# Поиск по диапазону IP
amass intel -addr 192.168.1.0/24
```

### Визуализация
```bash
# Сохранение в формате GraphML для визуализации
amass enum -d example.com -graphml graph.graphml

# Использование OWASP Amass Netmap (если установлен)
amass viz -d3graph -o3 graph.html
```

## Задачи для самостоятельного выполнения

1. Выполните пассивный сбор поддоменов для домена `scanme.nmap.org`. Сколько поддоменов удалось найти?

2. Используйте Amass с брутфорсом для домена `example.com`. Какой словарь используется по умолчанию? Укажите путь к словарю.

3. Сравните результаты пассивного и активного режимов для одного и того же домена. Что общего, чем отличаются?

4. Установите `sublist3r` (`pip install sublist3r`) и сравните результаты с Amass для одного домена. Какой инструмент нашел больше?

5. Используя флаг `-ip`, получите IP-адреса найденных поддоменов для `google.com`. Определите, какие поддомены используют IPv6 (AAAA записи).
