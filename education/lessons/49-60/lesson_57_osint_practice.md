# Занятие 57. OSINT практика: сбор информации о домене

## Теория

**OSINT (Open Source Intelligence)** — сбор информации из открытых источников. В пентесте OSINT — это первый этап (Information Gathering).

**Источники информации:**
- Поисковые системы (Google, Bing, DuckDuckGo)
- Социальные сети (LinkedIn, Facebook, Twitter)
- Специализированные сервисы (Shodan, Censys, VirusTotal)
- Публичные базы данных (WHOIS, DNS, Certificate Transparency)
- Кодовые репозитории (GitHub, GitLab)

**Google Dorks** — специальные запросы для поиска уязвимой информации:
- `site:example.com filetype:pdf` — документы на сайте
- `site:example.com intitle:"index of"` — открытые директории
- `site:example.com inurl:admin` — админ-панели
- `"example.com" "password"` — утечки паролей

**Shodan** — поисковик для устройств (IoT, серверов):
- Поиск по IP, порту, сервису, геолокации
- Пример: `port:22 country:"RU"` — SSH-серверы в России

## Практическое занятие

### Сбор информации о целевом домене (на примере вымышленного example.com)

**Шаг 1. WHOIS информация**
```bash
whois example.com
```
Получаем: регистратора, даты регистрации, контактные данные, NS-серверы.

**Шаг 2. DNS enumeration**
```bash
# A-записи
dig example.com A

# MX-записи (почтовые серверы)
dig example.com MX

# NS-записи (DNS-серверы)
dig example.com NS

# Все записи
dig example.com ANY
```

**Шаг 3. Поддомены (Subdomain enumeration)**
```bash
# Через sublist3r
sublist3r -d example.com

# Через amass
amass enum -d example.com

# Через gobuster
gobuster dns -d example.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

**Шаг 4. Google Dorks**
В браузере выполняем:
```
site:example.com filetype:pdf
site:example.com intitle:"index of" 
site:example.com inurl:php?id=
site:example.com "confidential"
```

**Шаг 5. Shodan**
1. Регистрируемся на shodan.io
2. Ищем: `hostname:example.com`
3. Анализируем: открытые порты, баннеры сервисов, уязвимости (CVE)

**Шаг 6. Email harvesting**
```bash
theharvester -d example.com -b google,linkedin
```
Собираем email-адреса сотрудников для будущих фишинговых атак.

**Шаг 7. GitHub разведка**
Ищем в GitHub: `example.com password`, `example.com api_key`
Разработчики часто случайно публикуют секреты в репозиториях.

## Задачи для самостоятельного выполнения

1. **OSINT на реальную компанию** (по выбору) — соберите: домены, поддомены, IP-диапазоны, сотрудников, технологии
2. **Комната "OSINT"** на THM — пройдите все задания, изучите инструменты (Sherlock, Maltego)
3. **Поиск утечек:** Используйте haveibeenpwned.com для проверки email на утечки паролей

> **Важно:** OSINT — легальный этап пентеста, включенный в scope. Но не используйте найденные пароли без разрешения заказчика.
