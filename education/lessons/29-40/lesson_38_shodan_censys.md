# Урок 38: Shodan и Censys — OSINT разведка

## Теория

**Shodan** — поисковая система для интернет-устройств. Индексирует не веб-страницы, а сервисы (SSH, FTP, HTTP, IoT устройства, камеры, свитчи).

**Censys** — аналогичный сервис, предоставляет детальную информацию о сертификатах, хостах и сетях.

Примеры использования:
- Поиск незащищенных камер, роутеров
- Поиск серверов с уязвимыми версиями ПО
- Сбор информации о целевой организации
- Поиск открытых портов и сервисов

## Практическое занятие

### Shodan CLI

```bash
# Установка
pip install shodan

# macOS (M2, Homebrew) — shodan устанавливается через pip
# brew install shodan  # (если доступно)

# Инициализация (нужен API ключ)
shodan init YOUR_API_KEY
# Пример вывода:
# Successfully initialized

# Базовый поиск
shodan search "apache"
# Пример вывода:
# 198.51.100.1:80    Apache httpd 2.4.41
# 203.0.113.5:8080   Apache Tomcat 9.0.31

shodan search "port:22"
# Пример вывода:
# 198.51.100.2:22    SSH OpenSSH 8.2

# Информация о хосте
shodan host 8.8.8.8
# Пример вывода:
# Country:     United States
# Organization: Google LLC
# Open Ports:  53, 443

# Сканирование публичных IP (Shodan сканирует только публичные адреса!)
# ПРИМЕЧАНИЕ: 192.168.x.x — это приватные IP, Shodan их НЕ сканирует
# Для примера используем публичный IP (например, scanme.nmap.org)
shodan scan submit 45.33.32.156  # scanme.nmap.org
# Пример вывода:
# Scan request submitted successfully

# Поиск уязвимостей
shodan search "vuln:CVE-2021-41773"

# Статистика
shodan stats "apache country:RU"
```

### Shodan Web (через браузер)
```
# Поисковые фильтры:
hostname:target.com
port:80,443
org:"Target Organization"
city:"Moscow"
country:"RU"
vuln:CVE-2021-xxxxx
product:"Apache httpd"
version:"2.4.49"
os:"Windows"
```

### Censys

```bash
# Установка CLI
pip install censys

# Инициализация
censys config  # Ввести API ID и Secret
# Пример вывода:
# Successfully authenticated

# Поиск хостов
censys search "services.http.response.status_code: 200"
# Пример вывода:
# 8.8.8.8
# services: 53/dns, 443/https

# Поиск по IP
censys view 8.8.8.8
# Пример вывода:
# ip: 8.8.8.8
# services:
#   - port: 443
#     service_name: HTTPS

# Поиск сертификатов
censys search --index certificates "parsed.subject_dn: target.com"
```

### Полезные запросы Shodan
```
# Камеры (IoT)
webcam
"Server: uc-httpd"

# Промышленные системы (ICS/SCADA)
"SCADA"
port:502

# Базы данных (открытые)
port:27017 MongoDB
port:6379 Redis

# Уязвимые сервисы
"vsftpd 2.3.4"
"ProFTPD 1.3.3c"

# Админки
"admin panel" port:8080
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

1. Зарегистрируйтесь на Shodan (бесплатно). Получите API ключ. Настройте CLI.

2. Найдите через Shodan все серверы Apache в России (country:RU product:"Apache"). Сколько результатов? Попробуйте найти серверы с уязвимой версией 2.4.49.

3. Используя Shodan, найдите открытые MongoDB базы данных (port:27017). Почему это опасно?

4. Настройте Censys CLI. Выполните поиск сертификатов для домена `example.com`. Сколько субдоменов удалось найти через сертификаты?

5. Сравните результаты Shodan и Censys для одного и того же IP-адреса. Какая информация отличается?

## Частые ошибки

1. **Попытка сканировать приватные IP** — Shodan работает только с публичными IP-адресами, 192.168.x.x, 10.x.x.x, 172.16.x.x не будут работать.

2. **Отсутствие API ключа** — большинство функций Shodan требуют регистрации и получения API ключа (бесплатно).

3. **Слишком общие запросы** — используйте фильтры (country:, city:, port:), чтобы сузить поиск.

4. **Забыли про Censys** — Censys часто дает более свежую информацию о сертификатах, чем Shodan.

## Вопросы на понимание

1. Чем Shodan отличается от обычного поисковика (Google, Bing)?

2. Почему Shodan не может сканировать приватные IP-адреса?

3. Как использовать информацию из Shodan для пентеста (легального)?

4. В чем разница между Shodan и Censys по предоставляемой информации?

### Полезные запросы Shodan
```
# Камеры (IoT)
webcam
"Server: uc-httpd"

# Промышленные системы (ICS/SCADA)
"SCADA"
port:502

# Базы данных (открытые)
port:27017 MongoDB
port:6379 Redis

# Уязвимые сервисы
"vsftpd 2.3.4"
"ProFTPD 1.3.3c"

# Админки
"admin panel" port:8080
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

1. Зарегистрируйтесь на Shodan (бесплатно). Получите API ключ. Настройте CLI.

2. Найдите через Shodan все серверы Apache в России (country:RU product:"Apache"). Сколько результатов? Попробуйте найти серверы с уязвимой версией 2.4.49.

3. Используя Shodan, найдите открытые MongoDB базы данных (port:27017). Почему это опасно?

4. Настройте Censys CLI. Выполните поиск сертификатов для домена `example.com`. Сколько субдоменов удалось найти через сертификаты?

5. Сравните результаты Shodan и Censys для одного и того же IP-адреса. Какая информация отличается?
