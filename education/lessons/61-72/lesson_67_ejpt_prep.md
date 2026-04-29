# Занятие 67. eJPT подготовка: практические лабы INE

## Теория

### Что такое eJPT (eLearnSecurity Junior Penetration Tester)

eJPT — сертификация от INE (ранее eLearnSecurity), ориентированная на начинающих пентестеров. Это практический сертификат, который проверяет базовые навыки пентеста.

**Особенности eJPT:**
- 100% практический экзамен (без тестов)
- Длительность экзамена: 48 часов (рекомендуется 8-16 часов)
- Стоимость: ~$200-400 (вместе с курсом) или отдельно экзамен
- Не требует продления (пожизненный)
- На английском языке

**Темы eJPT (согласно официальному syllabus):**

1. **Penetration Testing Processes and Methodologies**
   - PTES
   - OWASP
   - Подходы к пентесту

2. **Networking and Networking Protocols**
   - OSI Model
   - TCP/IP
   - Протоколы: HTTP, DNS, FTP, SMB, RDP, SSH, SMTP, POP3, IMAP

3. **Information Gathering**
   - Passive Information Gathering
   - Active Information Gathering
   - Footprinting

4. **Vulnerability Assessment**
   - Vulnerability scanners (Nessus, OpenVAS, Nmap)
   - Manual vulnerability assessment

5. **Host Profiling**
   - OS Fingerprinting
   - Service enumeration

6. **Network Scanning**
   - Port scanning (TCP Connect, SYN, UDP)
   - Nmap (все основные флаги)
   - Service detection

7. **Enumeration**
   - SMB enumeration (smbclient, enum4linux)
   - SNMP enumeration
   - SMTP enumeration
   - DNS enumeration
   - HTTP enumeration (dirb, gobuster)

8. **Vulnerability Assessment of Web Applications**
   - OWASP Top 10 (базовый уровень)
   - SQL Injection (базовый)
   - XSS (базовый)
   - Directory Traversal
   - File Inclusion

9. **Exploitation**
   - Exploit modification
   - Manual exploitation
   - Metasploit framework
   - Buffer overflow (базовый)

10. **Post-Exploitation**
    - Privilege Escalation (Windows/Linux)
    - Pivoting
    - Lateral Movement
    - File transfers
    - Hash dumping

11. **Network Attacks**
    - Man-in-the-Middle (ARP Spoofing)
    - Sniffing
    - DNS spoofing

### Структура курса INE (PTP - Penetration Testing Professional)

Курс PTP (Penetration Testing Professional) готовит к eJPT и включает:
- Видеолекции (40+ часов)
- Лабораторные работы (100+ лаб)
- Практические задания
- Quiz (тесты)

### Подготовка к экзамену eJPT

**Рекомендуемый план подготовки (4-6 недель):**
1. **Неделя 1**: Networking, Information Gathering, Scanning
2. **Неделя 2**: Enumeration, Vulnerability Assessment
3. **Неделя 3**: Exploitation (Metasploit + manual)
4. **Неделя 4**: Post-Exploitation, Pivoting
5. **Неделя 5**: Web Application Attacks (база)
6. **Неделя 6**: Практика в лабах, mock-экзамены

## Практическое занятие

### Настройка лаборатории для подготовки

Для подготовки к eJPT вам понадобятся:

1. **Kali Linux** (основная рабочая станция)
2. **VulnHub VMs** (цели для практики):
   - **Basic Pentesting 1** — отлично для начала
   - **Kioptrix Level 1** — классика
   - **Metasploitable 2/3** — для сканирования и эксплуатации
   - **Mr. Robot** — веб-приложения + привилегии
   - **Stapler** — разнообразные векторы
   - **SickOs 1.2** — веб + привилегии

3. **TryHackMe** (онлайн-платформа):
   - Пройдите комнаты: "Intro to Researching", "Nmap", "Metasploit", "John the Ripper", "Hydra"
   - Изучите "Penetration Testing" learning path

4. **Hack The Box** (Starting Point machines):
   - Meow, Fawn, Dancing, Redeemer, Tier 2 machines

### Практические лабы: Checklist

```markdown
# eJPT Preparation Checklist

## 1. Networking & Reconnaissance
- [ ] Понимать OSI и TCP/IP модели
- [ ] Уметь читать заголовки пакетов (Wireshark)
- [ ] Знать номера портов (20, 21, 22, 23, 25, 53, 80, 443, 445, 3389, 5432, 3306)
- [ ] Nmap: все типы сканирования (TCP Connect, SYN, UDP, FIN, Null, Xmas)
- [ ] Nmap: скрипты (-sC, --script)
- [ ] Nmap: вывод в разных форматах (-oN, -oA)
- [ ] Passive recon: theHarvester, Shodan, Google dorks

## 2. Enumeration
- [ ] SMB: enum4linux, smbclient, smbmap
- [ ] HTTP: dirb, gobuster, nikto, whatweb
- [ ] DNS: nslookup, dig, dnsenum, dnsrecon
- [ ] SNMP: snmpwalk, snmp-check
- [ ] SMTP: smtp-user-enum
- [ ] FTP: анонимный доступ, brute-force
- [ ] NFS: showmount, mount

## 3. Vulnerability Assessment
- [ ] Nessus/OpenVAS: настройка, запуск, анализ
- [ ] SearchSploit: поиск эксплойтов
- [ ] CVE/CVSS: понимание, поиск
- [ ] Умение отличать false positives

## 4. Exploitation
- [ ] Metasploit: msfconsole, search, use, set, exploit
- [ ] Metasploit: msfvenom (генерация payload)
- [ ] Manual exploitation: понимать, как работает эксплойт
- [ ] Buffer Overflow: базовое понимание (пройти модуль в курсе)
- [ ] Web exploits: SQLi (union, boolean), XSS (reflected)

## 5. Post-Exploitation
- [ ] Linux privilege escalation: перечисление (linpeas.sh, linenum.sh)
- [ ] Windows privilege escalation: перечисление (winpeas.exe)
- [ ] SUID/SGID exploits (Linux)
- [ ] Crontab exploits (Linux)
- [ ] Token impersonation (Windows)
- [ ] Dumping hashes: mimikatz, hashdump
- [ ] Cracking hashes: John the Ripper, hashcat

## 6. Pivoting & Lateral Movement
- [ ] Port forwarding: SSH tunneling (local, remote, dynamic)
- [ ] Pivoting через Metasploit (route add, autoroute)
- [ ] Proxychains: настройка, использование
- [ ] RDP: подключение, перенос файлов

## 7. Web Application Basics
- [ ] SQL Injection: понимание, ручная эксплуатация, sqlmap
- [ ] XSS: reflected, stored (базовый уровень)
- [ ] Directory Traversal: чтение /etc/passwd
- [ ] File Upload: загрузка PHP shell
- [ ] LFI/RFI: базовое понимание

## 8. Password Attacks
- [ ] Brute-force: hydra (FTP, SSH, HTTP, SMB)
- [ ] Wordlists: crunch, cewl, rockyou.txt
- [ ] Password spraying
- [ ] John the Ripper: cracking hashes

## 9. Reporting
- [ ] Уметь оформить найденную уязвимость
- [ ] CVSS scoring
- [ ] Remediation recommendations
```

### Рекомендуемые ресурсы

**Бесплатные:**
- TryHackMe (базовые комнаты)
- Hack The Box (Starting Point)
- VulnHub (скачать VM)
- YouTube: каналы "The Cyber Mentor", "John Hammond", "IPPSEC"

**Платные (рекомендуется):**
- INE PTP Course (включает eJPT exam voucher)
- TryHackMe Subscription (для продвинутых комнат)

## Задачи для самостоятельного выполнения

1. **VulnHub Challenge**: Скачайте и взломайте Basic Pentesting 1 (VulnHub). Напишите отчет по методологии PTES: Information Gathering → Exploitation → Privilege Escalation → Post-Exploitation.

2. **Nmap Mastery**: Напишите скрипт на Bash/Python, который автоматизирует сканирование: 1) Пинг-сканирование всей сети, 2) Детальное сканирование живых хостов, 3) Скриптовое сканирование и сохранение всех результатов.

3. **Metasploit Lab**: Используя Metasploitable 2, найдите и проэксплуатируйте минимум 5 уязвимостей через Metasploit (VSFTPD, IRC, Distcc, PHP CGI, Samba). Для каждой получите shell и соберите доказательства.

4. **Privilege Escalation**: На VulnHub VM (например, Kioptrix или Stapler) получите начальный доступ, затем повысьте привилегии до root. Используйте linpeas.sh для перечисления. Опишите найденный вектор.

5. **TryHackMe Path**: Зарегистрируйтесь на TryHackMe и пройдите минимум 10 комнат из раздела "Learning Paths" → "Complete Beginner" или "Offensive Pentesting". Скриншоты результатов приложите к отчету.
