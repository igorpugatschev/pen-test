# Занятие 11. DNS: как работает, записи A, AAAA, CNAME, MX, TXT

## Теория

DNS (Domain Name System) — система доменных имен, преобразующая человекочитаемые имена (например, example.com) в IP-адреса.

### Как работает DNS

1. Пользователь вводит домен в браузере
2. Запрос идет к DNS-резолверу (обычно провайдера или 8.8.8.8)
3. Резолвер проверяет кэш
4. Если нет — запрашивает корневые DNS-серверы (.)
5. Получает адреса серверов TLD (.com, .ru и т.д.)
6. Запрашивает TLD-серверы, получает NS-серверы домена
7. Запрашивает авторитетный NS-сервер и получает IP-адрес
8. Возвращает IP браузеру

### Типы DNS-записей

**A (Address)** — связывает домен с IPv4-адресом
```
example.com.  IN  A  93.184.216.34
```

**AAAA** — связывает домен с IPv6-адресом
```
example.com.  IN  AAAA  2606:2800:220:1:248:1893:25c8:1946
```

**CNAME (Canonical Name)** — псевдоним домена
```
www.example.com.  IN  CNAME  example.com.
```

**MX (Mail Exchange)** — серверы электронной почты
```
example.com.  IN  MX  10 mail.example.com.
```

**TXT** — текстовые записи (используется для SPF, DKIM, верификации домена)
```
example.com.  IN  TXT  "v=spf1 include:_spf.google.com ~all"
```

**NS (Name Server)** — авторитетные DNS-серверы для домена
```
example.com.  IN  NS  ns1.example.com.
```

**SOA (Start of Authority)** — информация об авторитете зоны

**PTR (Pointer)** — обратный DNS (IP -> домен)

### DNS для пентестера

- **DNS-reconnaissance**: сбор информации о цели через DNS
- **DNS-zone-transfer**: попытка получить копию всей DNS-зоны
- **DNS-spoofing**: подмена DNS-ответов
- **Subdomain enumeration**: поиск поддоменов через DNS
- **DNS-tunneling**: передача данных через DNS-запросы

## Практическое занятие

### Задача 1: Базовые DNS-запросы через dig

1. Установите dig (если нет):
```bash
sudo apt install dnsutils
```

2. Простой A-запрос:
```bash
dig example.com
```

3. Запрос конкретного типа записи:
```bash
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com TXT
dig example.com NS
```

4. Краткий вывод:
```bash
dig +short example.com A
```

### Задача 2: Обратный DNS-запрос (PTR)

1. Выполните обратный запрос для известного IP:
```bash
dig -x 8.8.8.8
```

2. Попробуйте для своего публичного IP (узнайте его через `curl ifconfig.me`)

### Задача 3: Поиск поддоменов через DNS

1. Используйте host для перечисления записей:
```bash
host -t ns example.com
host -t mx example.com
```

2. Попробуйте zone transfer (часто закрыто, но стоит проверить):
```bash
dig axfr example.com @ns1.example.com
```

### Задача 4: Использование nmap для DNS-разведки

1. Скрипт nmap для DNS-bruteforce:
```bash
nmap --script dns-brute example.com
```

2. Скрипт для проверки zone transfer:
```bash
nmap --script dns-zone-transfer -p 53 example.com
```

## Задачи для самостоятельного выполнения

1. **Анализ DNS-записей целевого домена**: Выберите любой публичный домен (например, yandex.ru или google.com) и выполните полный анализ: получите все типы записей (A, AAAA, MX, TXT, NS, CNAME). Составьте схему, показывающую, какие поддомены существуют и какие сервисы на них указывают.

2. **Настройка альтернативного DNS**: Временно измените DNS-сервер в системе (через `/etc/resolv.conf` или `nmcli`) на 1.1.1.1 (Cloudflare) и 8.8.8.8 (Google). Сравните скорость разрешения имен с помощью `dig +stats domain.com` для каждого сервера.

3. **DNS-over-HTTPS (DoH)**: Исследуйте, как работает DoH. Установите `dnslookup` или используйте curl для запроса через DoH:
```bash
curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=example.com&type=A'
```
Опишите, чем это отличается от обычного DNS с точки зрения безопасности и пентестера.

4. **Subdomain enumeration**: Используя словарь (можно взять из репозитория SecLists) и инструмент `dnsrecon` или `gobuster`, найдите минимум 5 существующих поддоменов для выбранного домена:
```bash
gobuster dns -d example.com -w /path/to/wordlist.txt
```

5. **Анализ TXT-записей**: Найдите домены, использующие SPF, DKIM и DMARC записи. Объясните, зачем они нужны и как их отсутствие может быть использовано для email-spoofing атак.
