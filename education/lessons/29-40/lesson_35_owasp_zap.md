# Урок 35: OWASP ZAP — альтернатива Burp Suite

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

# Или через меню: Applications -> 03 - Web Application Analysis -> owasp-zap

# Запуск в headless режиме (без GUI)
zap-cli start
```

### Настройка браузера
1. Запустите ZAP
2. В браузере настройте прокси: `127.0.0.1:8080`
3. Скачайте и установите CA-сертификат ZAP для HTTPS: `Tools -> Options -> Dynamic SSL Certificates -> Save`

### Автоматическое сканирование
```bash
# Через GUI:
# 1. Введите URL в поле "Quick Start"
# 2. Нажмите "Attack"

# Через CLI (zap-cli)
pip install python-owasp-zap

zap-cli open-url http://example.com
zap-cli spider http://example.com
zap-cli active-scan http://example.com
zap-cli alerts -l High
```

### Использование Proxy (ручной режим)
1. Настройте браузер на прокси ZAP (8080)
2. Откройте целевой сайт
3. В ZAP вы увидите весь трафик в History
4. Выберите запрос -> правой кнопкой -> Attack -> Fuzz
5. Подставьте payloads для тестирования

### Fuzzer
1. Откройте History -> выберите запрос
2. Right-click -> Attack -> Fuzz
3. Выделите параметр -> Add -> выберите словарь
4. Start Fuzzer
5. Анализируйте ответы

### Passive и Active Scan
- **Passive Scan** — анализ трафика без отправки атакующих запросов (безопасно)
- **Active Scan** — реальные атаки на уязвимости (может нагрузить сервер)

```bash
# API вызовы
zap-cli passive-scan -r http://example.com
zap-cli active-scan -r http://example.com
```

## Задачи для самостоятельного выполнения

1. Запустите DVWA на уровне Low. Настройте браузер на прокси ZAP. Попробуйте выполнить SQL Injection, перехватывая запросы в ZAP.

2. Используйте Spider (паук) в ZAP для обхода сайта `testphp.vulnweb.com`. Сколько уникальных URL удалось найти?

3. Запустите Active Scan против DVWA. Какие уязвимости обнаружил ZAP? Сравните с результатами ручного тестирования.

4. Используйте Fuzzer ZAP для подбора директорий на `testphp.vulnweb.com/admin/`. Используйте словарь `/usr/share/wordlists/dirb/common.txt`. Какие пути нашлись?

5. Настройте ZAP в headless режиме (через `zap-cli`). Напишите Python-скрипт, который запускает сканирование через `zap-cli` и сохраняет алерты в JSON.
