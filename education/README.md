# Education Materials

Учебные материалы для курса по пентесту (72 урока).

## Структура

```
education/
├── lessons/           # Уроки по блокам (01-08, 09-16, 17-28, 29-40, 41-48, 49-60, 61-72)
├── tools/             # Вспомогательные скрипты проверки и исправления
└── pentest_learning_program.md  # Полная программа курса
```

## Блоки уроков

### 01-08: Linux основы (8 уроков)
- Урок 01: Введение в Linux и Kali Linux
- Урок 02: Терминал и основные команды
- Урок 03: Права доступа и файловая система
- Урок 04: Процессы и управление ими
- Урок 05: Сетевые настройки в Linux
- Урок 06: Поиск файлов и текста
- Урок 07: Bash-скрипты для пентестера
- Урок 08: Итоговое задание по Linux

### 09-16: Сетевые технологии (8 уроков)
- Урок 09: Модель OSI и TCP/IP
- Урок 10: Протоколы TCP/IP
- Урок 11: DNS - как это работает
- Урок 12: HTTP и HTTPS
- Урок 13: Wireshark - анализ трафика
- Урок 14: Маршрутизация и трассировка
- Урок 15: Фаерволы и правила фильтрации
- Урок 16: Практика: сетевой анализ

### 17-28: OWASP Top 10 (12 уроков + 5 доп.)
- Урок 17: Введение в OWASP Top 10
- Урок 17b: A04 - Insecure Design
- Урок 17c: A05 - Security Misconfiguration
- Урок 17d: A06 - Vulnerable and Outdated Components
- Урок 17e: A08 - Software and Data Integrity Failures
- Урок 17f: A09 - Security Logging and Monitoring Failures
- Урок 18: A03 - SQL Injection
- Урок 19: SQLMap - автоматизация SQLi
- Урок 20: A07 - Cross-Site Scripting (XSS)
- Урок 21: DOM-based XSS
- Урок 22: A08 - Cross-Site Request Forgery (CSRF)
- Урок 23: A07 - Broken Authentication
- Урок 24: A02 - Cryptographic Failures (Sensitive Data)
- Урок 25: A05 - XML External Entities (XXE)
- Урок 26: A10 - Server-Side Request Forgery (SSRF)
- Урок 27: Введение в Burp Suite
- Урок 28: Практика с Burp Suite

### 29-40: Инструменты пентеста (12 уроков)
- Урок 29: Nmap - основы сканирования
- Урок 30: Nmap NSE скрипты
- Урок 31: Amass - разведка поддоменов
- Урок 32: Subfinder и другие инструменты
- Урок 33: Dirsearch и FFuf
- Урок 34: Nuclei - автоматизация
- Урок 35: OWASP ZAP
- Урок 36: Hydra и Patator
- Урок 37: Searchsploit и Exploit-DB
- Урок 38: Shodan и Censys
- Урок 39: Практика с инструментами
- Урок 40: Создание отчетов

### 41-48: Python для пентеста (8 уроков)
- Урок 41: Сокеты в Python
- Урок 42: Библиотека Requests
- Урок 43: Создание PoC эксплойтов
- Урок 44: Автоматизация Nmap
- Урок 45: Парсинг поддоменов
- Урок 46: Brute force директорий
- Урок 47: Парсер CVE
- Урок 48: Итоговый проект на Python

### 49-60: Практика на площадках (12 уроков)
- Урок 49: Введение в TryHackMe
- Урок 50: TryHackMe Jr. Penetration Tester
- Урок 51: HackTheBox - старт
- Урок 52: HackTheBox - easy машины
- Урок 53: HackTheBox - Active Directory
- Урок 54: PortSwigger Web Security Academy
- Урок 55: Linux Privilege Escalation
- Урок 56: Отчеты в практике
- Урок 57: OSINT практика
- Урок 58: WAF обход
- Урок 59: Полный пентест (симуляция)
- Урок 60: Подготовка к EJPT

### 61-72: Методология и сертификация (12 уроков)
- Урок 61: PTES - стандарт пентеста
- Урок 62: OWASP Testing Guide
- Урок 63: Написание отчетов
- Урок 64: CVSS v3.1 scoring
- Урок 65: Коммерческие сканеры
- Урок 66: Qualys и Rapid7
- Урок 67: Подготовка к EJPT
- Урок 68: Экзамен EJPT
- Урок 69: Основы OSCP
- Урок 70: Атаки на Active Directory
- Урок 71: Post-Exploitation
- Урок 72: Финальный проект

## Проверка уроков

Используйте скрипты в папке `tools/`:
```bash
cd tools
bash check_lessons.sh        # Проверка структуры
python3 final_fix_all.py     # Исправление ошибок
```

## Адаптация под macOS (M2, 8GB)

Каждый урок содержит раздел "Адаптация под macOS" с:
- Использованием `brew install` вместо `apt install`
- Рекомендациями по выделению RAM для VM (3-4GB)
- Ссылками на облачные альтернативы (AttackBox, Tunnelblick)

## Полная программа

См. файл `pentest_learning_program.md` для детального описания всех уроков.
