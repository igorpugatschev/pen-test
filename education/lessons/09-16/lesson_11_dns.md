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
# macOS: brew install bind
# Linux: sudo apt install dnsutils
brew install bind
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

## Примеры вывода

### dig example.com
```
; <<>> DiG 9.18.12 <<>> example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; QUESTION SECTION:
;example.com.			IN	A

;; ANSWER SECTION:
example.com.		21599	IN	A	93.184.216.34

;; Query time: 45 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Apr 29 12:00:00 2024
;; MSG SIZE  rcvd: 56
```

### dig +short example.com AAAA
```
2606:2800:220:1:248:1893:25c8:1946
```

### dig -x 8.8.8.8
```
8.8.8.8.in-addr.arpa	IN	PTR	dns.google.
```

### host -t mx example.com
```
example.com mail is handled by 0 .
```

## Частые ошибки

1. **Путаница типов записей**: A — для IPv4, AAAA — для IPv6. Часто ищут IPv6 в A-записях.
2. **Забывание про кэш**: DNS-записи кэшируются. После изменений результат может появиться не сразу (смотрите TTL).
3. **dig vs nslookup**: `dig` — предпочтительный инструмент, `nslookup` устарел. Используйте `dig` для профессиональной работы.
4. **Zone transfer на публичных доменах**: Большинство публичных доменов закрыли zone transfer. Если получаете ошибку — это нормально, не ошибка.

## Вопросы на понимание

1. Чем отличается рекурсивный запрос от итеративного?
    <details><summary>Ответ</summary>При рекурсивном резолвер сам идет до корня и возвращает ответ клиенту. При итеративном клиент сам делает запросы к каждому серверу</details>
2. Почему DNS-spoofing возможен и как ему противостоять?
    <details><summary>Ответ</summary>DNS по умолчанию не имеет аутентификации. Защита: DNSSEC, DNS-over-HTTPS (DoH), DNS-over-TLS (DoT)</details>
3. Зачем пентестеру искать поддомены через DNS?
    <details><summary>Ответ</summary>Поддомены могут вести на забытые или тестовые серверы с уязвимостями, что расширяет поверхность атаки</details>
4. Что такое TXT-записи и зачем они нужны?
    <details><summary>Ответ</summary>TXT-записи содержат текстовую информацию: SPF (защита email), DKIM (подпись писем), верификация домена (Google, Microsoft)</details>

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

## Адаптация под macOS (M2, 8GB)

Для пользователей macOS (особенно на чипах M1/M2 и с 8GB RAM):

- **Установка инструментов**: Используйте `brew install` вместо `apt install`:
  ```bash
  brew install bind  # для dig, host, nslookup
  brew install nmap
  brew install gobuster
  brew install dnsrecon
  ```

- **DNS-утилиты на macOS**: `dig` и `host` обычно уже установлены в macOS (входит в состав системы). Если нет: `brew install bind`.

- **Виртуализация**: Вместо VirtualBox (который может быть нестабилен на M2) рекомендуется использовать:
  - **UTM** — нативный для Apple Silicon, бесплатный
  - **Parallels** — платный, но быстрый на M-чипах
  
  На 8GB RAM запускайте VM с 3-4GB памяти.

- **DoH (DNS-over-HTTPS)**: Для тестирования DoH на macOS можно использовать `curl` или установить `dnslookup`:
  ```bash
  brew install dnslookup
  ```

- **Ограничения 8GB RAM**: Не запускайте одновременно много тяжелых VM. Оптимально: 1 Kali (3GB) + 1 Metasploitable (512MB) = 3.5GB + хост ~4GB.

- **Устаревшие команды**: Везде, где в уроке упоминаются `ifconfig`, `netstat`, `arp` — эти команды считаются устаревшими. Используйте современные аналоги:
  - `ifconfig` → `ip addr` / `ip link`
  - `netstat -tunap` → `ss -tunap`
  - `arp -n` → `ip neigh`
  - `route -n` → `ip route`
