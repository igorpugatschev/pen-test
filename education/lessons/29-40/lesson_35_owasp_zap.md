# Урок 35: OWASP ZAP — альтернатива Burp Suite

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

OWASP ZAP (Zed Attack Proxy) — бесплатный инструмент для тестирования веб-приложений на проникновение. Альтернатива Burp Suite Community/Pro. Полностью open-source.

Основные возможности:
- Перехват и изменение трафика (Proxy)
- Автоматическое сканирование (Spider, Ajax Spider)
- Fuzzer для параметров
- Поиск уязвимостей (Passive + Active Scan)
- REST API для автоматизации
- Поддержка скриптов (Zest)

## Практическое занятие

### Установка и запуск
```bash
# Kali Linux (уже установлен)
zaproxy &

# macOS (M2, Homebrew)
brew install --cask owasp-zap

# Или через меню: Applications -> 03 - Web Application Analysis -> owasp-zap

# Запуск в headless режиме (без GUI)
zap-cli start
```

### Настройка браузера
1. Запустите ZAP
2. В браузере настройте прокси: `127.0.0.1:8080`
3. Скачайте и установите CA-сертификат ZAP для HTTPS: `Tools -> Options -> Dynamic SSL Certificates -> Save`

Пример успешной настройки прокси:
```
Browser: Firefox
Settings -> Network Settings -> Manual proxy configuration:
HTTP Proxy: 127.0.0.1  Port: 8080
SSL Proxy: 127.0.0.1  Port: 8080
```

### Автоматическое сканирование
```bash
# Через GUI:
# 1. Введите URL в поле "Quick Start"
# 2. Нажмите "Attack"

# Через CLI (zap-cli)
pip install zapcli

# Или через Docker:
docker run -t owasp/zap2docker-stable zap-cli status

# Использование zap-cli
zap-cli open-url http://example.com
# Пример вывода:
# Opened URL: http://example.com

zap-cli spider http://example.com
# Пример вывода:
# Spider started at: http://example.com
# Spider progress: 100%
# Spider completed

zap-cli active-scan http://example.com
# Пример вывода:
# Active scan started for: http://example.com
# Scan progress: 100%
# Scan completed

zap-cli alerts -l High
# Пример вывода:
# [{'id': '10003', 'name': 'X-Frame-Options header scanner', ...}]
```

### Использование Proxy (ручной режим)
1. Настройте браузер на прокси ZAP (8080)
2. Откройте целевой сайт
3. В ZAP вы увидите весь трафик в History
4. Выберите запрос -> правой кнопкой -> Attack -> Fuzz
5. Подставьте payloads для тестирования

Пример увиденного трафика в ZAP:
```
History tab:
GET http://example.com/ 200 OK 1234 bytes
POST http://example.com/login 200 OK 456 bytes
```

### Fuzzer
1. Откройте History -> выберите запрос
2. Right-click -> Attack -> Fuzz
3. Выделите параметр -> Add -> выберите словарь
4. Start Fuzzer
5. Анализируйте ответы

Пример результатов Fuzzer:
```
URL: http://example.com/login
Parameter: username
Payload: admin -> Response: 200 OK (Login successful)
Payload: test -> Response: 401 Unauthorized
```

### Passive и Active Scan
- **Passive Scan** — анализ трафика без отправки атакующих запросов (безопасно)
- **Active Scan** — реальные атаки на уязвимости (может нагрузить сервер)

```bash
# API вызовы
zap-cli passive-scan -r http://example.com
# Пример вывода:
# Passive scan completed for: http://example.com

zap-cli active-scan -r http://example.com
# Пример вывода:
# Active scan progress: 100%
# Scan completed
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

1. Запустите DVWA на уровне Low. Настройте браузер на прокси ZAP. Попробуйте выполнить SQL Injection, перехватывая запросы в ZAP.

2. Используйте Spider (паук) в ZAP для обхода сайта `testphp.vulnweb.com`. Сколько уникальных URL удалось найти?

3. Запустите Active Scan против DVWA. Какие уязвимости обнаружил ZAP? Сравните с результатами ручного тестирования.

4. Используйте Fuzzer ZAP для подбора директорий на `testphp.vulnweb.com/admin/`. Используйте словарь `/usr/share/wordlists/dirb/common.txt`. Какие пути нашлись?

5. Настройте ZAP в headless режиме (через `zap-cli`). Напишите Python-скрипт, который запускает сканирование через `zap-cli` и сохраняет алерты в JSON.

## Частые ошибки

1. **Проблемы с HTTPS (SSL/TLS)** — обязательно установите CA-сертификат ZAP, иначе браузер будет ругаться на "незащищенное соединение".

2. **ZAP не видит трафик** — проверьте, что прокси в браузере настроен правильно (127.0.0.1:8080) и ZAP запущен.

3. **Active Scan на "боевых" серверах** — активное сканирование может нагрузить сервер или вызвать подозрение, используйте только на разрешенных целях.

4. **Docker-версия ZAP требует проброса портов** — при запуске через `docker run` убедитесь, что порт 8080 проброшен (`-p 8080:8080`).

## Вопросы на понимание

1. В чем разница между Passive и Active сканированием в ZAP?

2. Зачем нужна установка CA-сертификата ZAP в браузере?

3. Как использовать ZAP для тестирования мобильных приложений (Android/iOS)?

4. Чем ZAP отличается от Burp Suite Community Edition?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** ZAP passive

### Минимум

Откройте Slider AI через ZAP proxy и включите только passive scan.

### Практика Slider AI

Соберите alerts passive scan, удалите cookies/tokens и классифицируйте informational vs finding.

### Углубление после изучения следующих уроков

После урока 40 экспортируйте отчет ZAP и добавьте ручную валидацию.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.
