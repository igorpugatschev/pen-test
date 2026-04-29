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

# Инициализация (нужен API ключ)
shodan init YOUR_API_KEY

# Базовый поиск
shodan search "apache"
shodan search "port:22"

# Информация о хосте
shodan host 8.8.8.8

# Сканирование своих IP
shodan scan submit 192.168.1.0/24

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

# Поиск хостов
censys search "services.http.response.status_code: 200"

# Поиск по IP
censys view 8.8.8.8

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

## Задачи для самостоятельного выполнения

1. Зарегистрируйтесь на Shodan (бесплатно). Получите API ключ. Настройте CLI.

2. Найдите через Shodan все серверы Apache в России (country:RU product:"Apache"). Сколько результатов? Попробуйте найти серверы с уязвимой версией 2.4.49.

3. Используя Shodan, найдите открытые MongoDB базы данных (port:27017). Почему это опасно?

4. Настройте Censys CLI. Выполните поиск сертификатов для домена `example.com`. Сколько субдоменов удалось найти через сертификаты?

5. Сравните результаты Shodan и Censys для одного и того же IP-адреса. Какая информация отличается?
