# Занятие 69. OSCP база: чтение PWK syllabus

## Теория

### Что такое OSCP (Offensive Security Certified Professional)

OSCP — самая известная и уважаемая сертификация в области пентестинга, выдаваемая компанией Offensive Security.

**Особенности OSCP:**
- 100% практический экзамен
- Экзамен: 24 часа активной работы + 24 часа на написание отчета (итого 48 часов)
- Включает Active Directory (AD) сеты — обязательная часть экзамена
- Требует создания полноценного отчета (как в реальном пентесте)
- Стоимость: $1499 (90 дней лаб) или $1999 (1 год лаб + экзамен)
- Срок действия: пожизненный (не требует продления)
- Один из самых сложных сертификатов начального-среднего уровня
- OffSec Proving Grounds (Practice Labs) — официальные лаборатории для подготовки

### PWK (Penetration Testing with Kali Linux)

PWK — официальный курс от Offensive Security, готовящий к OSCP.

**Структура курса:**
1. PDF-учебник (850+ страниц)
2. Видеолекции (18+ часов)
3. Доступ к лаборатории (разное количество дней в зависимости от пакета)
4. VPN-доступ к изолированной сети с целями
5. Exercises (упражнения в конце каждой главы)

### PWK Syllabus (темы курса)

**Модуль 1: Обзор курса и методологии**
- Введение в пентест
- Методология Offensive Security
- Настройка Kali Linux
- Правила лаборатории

**Модуль 2: Фундаментальные инструменты**
- Bash scripting
- Netcat, Socat, Powershell
- Wireshark, TCPDump
- Nmap (углубленно)

**Модуль 3: Информационный сбор (Information Gathering)**
- Passive recon
- Active recon
- OSINT
- Google hacking
- DNS enumeration
- Перечисление поддоменов

**Модуль 4: Сканирование (Scanning)**
- TCP/IP фундаментально
- Типы сканирования Nmap
- Сканирование UDP
- SMB enumeration
- SNMP enumeration
- NFS enumeration

**Модуль 5: Эксплуатация (Exploitation)**
- Поиск эксплойтов (Exploit-DB, GitHub, Google)
- Кастомизация эксплойтов
- Обработка ошибок компиляции
- Stack Buffer Overflow (введение)
- Написание эксплойтов на Python

**Модуль 6: Web Application Attacks**
- OWASP Top 10
- SQL Injection (расширенно)
- XSS (все типы)
- Command Injection
- File Inclusion (LFI/RFI)
- File Upload
- CSRF
- XXE
- SSRF
- Использование Burp Suite

**Модуль 7: Privilege Escalation (Linux)**
- Kernel exploits
- SUID/SGID binaries
- Sudo misconfigurations
- Cron jobs
- Capabilities
- Linpeas, Linenum
- /etc/passwd, /etc/shadow

**Модуль 8: Privilege Escalation (Windows)**
- Kernel exploits
- Service misconfigurations
- Registry
- AlwaysInstallElevated
- Token Impersonation
- Winpeas, PowerUp
- Credentials in memory (Mimikatz)

**Модуль 9: Transferring Files**
- HTTP server (Python)
- SMB transfer
- FTP
- Powershell
- Certutil, VBS, debug.exe

**Модуль 10: Pivoting и Lateral Movement**
- SSH tunneling
- Proxychains
- Metasploit pivoting
- Port forwarding
- Chisel
- Ligolo-ng

**Модуль 11: Active Directory Attacks (база)**
- Основы AD
- Kerberoasting
- ASREPRoasting
- LLMNR/NBT-NS poisoning
- Pass the Hash
- BloodHound

**Модуль 12: Client-Side Attacks**
- Phishing
- Malicious documents
- Hta attacks
- Payload generation (msfvenom)

**Модуль 13: Antivirus Evasion**
- Obfuscation
- Encoding
- Veil framework
- Custom payloads

**Модуль 14: Writing Reports**
- Структура отчета OSCP
- Template
- Оформление доказательств
- Executive Summary
- Technical Details

### Отличия eJPT от OSCP

| Характеристика | eJPT | OSCP |
|----------------|------|------|
| Сложность | Начинающий | Средний |
| Длительность экзамена | 48 часов | 24 часа (актив) + 24 (отчет) |
| Количество целей | 3-5 | 5 (3 standalone + AD set) |
| Active Directory | Нет (база) | Да (обязательно) |
| Buffer Overflow | Базовый (1) | Обязательный (1 машина) |
| Отчет | Нет (ответы в форме) | Да (полный отчет) |
| Стоимость | ~$200-400 | $1499+ |
| Подготовка | 1-2 месяца | 6-12 месяцев |

### Структура экзамена OSCP

**Экзамен (24 часа активной работы):**
- 1. Буферная переполнение (BOF) — 25 баллов (автоматический скрипт)
- 2. 3 Standalone машины — 20, 20, 10 баллов
- 3. Active Directory set (3 машины в сети) — 40 баллов
- **Всего: 115 баллов**
- **Проходной: 70 баллов** (можно сдать без BOF, но нужно все AD + пару машин)

**После экзамена (24 часа на отчет):**
- Написание полного отчета (как в реальном пентесте)
- Отчет должен включать: Executive Summary, пошаговый эксплойт каждой машины, скриншоты, листинги кода

**Подготовка через OffSec Proving Grounds:**
- PG Practice — платные лаборатории от Offensive Security
- PG Play — бесплатные машины для начинающих
- Машин подобранный по сложности к экзамену OSCP
- Рекомендуется пройти 30+ машин перед экзаменом

## Практическое занятие

### Анализ PWK Syllabus

Скачайте официальный syllabus с сайта offensive-security.com и заполните таблицу самооценки:

```markdown
# PWK/OSCP Self-Assessment

Оцените свои знания по шкале:
1 = Не знаю вообще
2 = Слышал, но не пробовал
3 = Пробовал, нужна практика
4 = Хорошо знаю
5 = Эксперт

## Модули PWK

| Тема | Оценка (1-5) | План изучения |
|------|-------------|---------------|
| Bash scripting |  |  |
| Netcat/Socat |  |  |
| Nmap (продвинутый) |  |  |
| Information Gathering |  |  |
| Enumeration (SMB, SNMP, NFS) |  |  |
| Поиск и модификация эксплойтов |  |  |
| Stack Buffer Overflow |  |  |
| SQL Injection |  |  |
| XSS, CSRF, XXE, SSRF |  |  |
| Burp Suite |  |  |
| Linux Privilege Escalation |  |  |
| Windows Privilege Escalation |  |  |
| File Transfer |  |  |
| Pivoting (SSH, Proxychains) |  |  |
| Active Directory (Kerberoasting, etc.) |  |  |
| Client-Side Attacks |  |  |
| Antivirus Evasion |  |  |
| Report Writing |  |  |

## Итого
Средняя оценка: ___ / 5
Темы со оценкой 1-2: [перечислите]
Темы со оценкой 3: [перечислите]
Темы со оценкой 4-5: [перечислите]
```

### План подготовки к OSCP

На основе самооценки составьте план:

```
Месяц 1: Фундамент
- Неделя 1: Linux, Bash, Netcat
- Неделя 2: Nmap, Enumeration
- Неделя 3: Web Attacks (OWASP Top 10)
- Неделя 4: Buffer Overflow (база)

Месяц 2: Эксплуатация и PrivEsc
- Неделя 1: Linux Privilege Escalation
- Неделя 2: Windows Privilege Escalation
- Неделя 3: Pivoting и Lateral Movement
- Неделя 4: Практика на VulnHub (5 VMs)

Месяц 3: Active Directory
- Неделя 1: Теория AD, настройка лабы
- Неделя 2: Kerberoasting, ASREPRoasting
- Неделя 3: BloodHound, Pass the Hash
- Неделя 4: Практика (GOAD, Pro Lab)

Месяц 4: Подготовка к экзамену
- Неделя 1: Hack The Box (10 machines)
- Неделя 2: PWK Exercises (если купили курс)
- Неделя 3: Proctored practice exams
- Неделя 4: Написание отчетов, финальная подготовка
```

### Полезные ресуры для подготовки

**Бесплатные:**
- [TJ Null's OSCP List](https://docs.google.com/spreadsheets/u/0/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBmcUjvM7rU/htmlview) — список Hack The Box машин для подготовки
- TryHackMe: "Offensive Pentesting" path
- YouTube: "The Cyber Mentor", "ippsec"

**Платные:**
- PWK Course (Offensive Security)
- Hack The Box: VIP подписка (для доступа к retired машинам)
- PG Practice (Proving Grounds) — от Offensive Security



## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.




## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты


## Задачи для самостоятельного выполнения

1. **PWK Syllabus Deep Dive**: Прочитайте детальный outline курса PWK на offensive-security.com. Напишите краткое резюме каждого модуля (по 3-5 предложений).

2. **HTB Machines (OSCP-like)**: Пройдите 5 машин с TJ Null's списка (например: Lame, Blue, Devel, Legacy, Optimum). Напишите краткий отчет для каждой (Recon → Exploit → PrivEsc).

3. **Buffer Overflow Practice**: Пройдите курс "Practical Buffer Overflow" (бесплатно на YouTube или TryHackMe "Buffer Overflow Prep"). Напишите свой Python-скрипт для эксплуатации BO (используя pattern_create, pattern_offset).

4. **Active Directory Lab**: Настройте лабораторию Active Directory (можно использовать GOAD - Game of Active Directory). Попробуйте выполнить Kerberoasting атаку (GetUserSPNs.py, crack hashes с помощью hashcat).

5. **OSCP Report Template**: Найдите в интернете примеры OSCP-отчетов (GitHub, Reddit). Создайте свой шаблон в Markdown, который будет включать: Cover Page, Executive Summary, Methodology, Targets (IP, hostname), Vulnerabilities (с CVSS, PoC, remediation), Appendices.

## Частые ошибки

1. **Недооценка AD сета** — многие фокусируются на standalone машинах и не готовятся к AD. AD сет дает 40 баллов из 115 — это стратегически важная часть.
2. **Плохой отчет** — даже если сдали все машины, плохой отчет может привести к провалу. Скриншоты должны быть четкими, с видимым IP и доказательством (proof.txt).
3. **Игнорирование BOF** — Buffer Overflow дает 25 баллов "автоматом", но требует практики. Не надейтесь "понять на экзамене".
4. **Неправильный тайм-менеджмент** — 24 часа проходят быстро. Рекомендуется: BOF (1-2 часа), AD (8-10 часов), Standalone (по 3-4 часа на каждую).
5. **Попытка использовать Metasploit на всех машинах** — на экзамене Metasploit разрешен только на одной машине (не включая BOF).
6. **Отсутствие бэкапов** — делайте скриншоты и сохраняйте вывод команд постоянно. Потеря сессии = потеря времени.

## Вопросы на понимание

1. Сколько баллов нужно набрать для прохождения OSCP?
2. Какую часть экзамена составляет Active Directory?
3. Сколько времени дается на написание отчета?
4. Можно ли использовать Metasploit на всех машинах экзамена?
5. Что такое OffSec Proving Grounds и чем они отличаются от обычных лаб PWK?
6. Почему при подготовке на Mac с 8GB RAM не рекомендуется запускать локальные AD лабы?
