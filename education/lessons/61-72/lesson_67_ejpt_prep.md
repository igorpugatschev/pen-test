# Занятие 67. eJPT подготовка: практические лабы INE

## Учебная рамка

**Входные требования:** Понимание полного цикла пентеста, базовые навыки отчетности и опыт работы с учебными лабораториями.

**Результат занятия:** Студент применяет методологию, оформляет артефакт профессионального уровня и отделяет факты от предположений.

**Наследуемая SDET-компетенция:** security ownership: стратегия, RoE, risk scoring, remediation, retest и коммуникация с командой.

**Security QA-компетенция:** планирование и сопровождение полного security assessment: findings, risk, remediation, retest.

**Связь с книгами:** PTES, OWASP Testing Guide, CVSS и «PyCharm. Профессиональная работа на Python 2024» для reporting, Git/VCS, Markdown evidence и процесса.

**Основной источник:** «PyCharm. Профессиональная работа на Python 2024» и «Паттерны разработки на Python».

**Дополнительные источники:** Все книги курса как справочник для финального Security QA assessment и automation appendix.

**Что берем из источника:** strategy, RoE, evidence policy, triage, remediation, retest, security regression и ownership.

**Как это превращается в SDET/Security QA навык:** собрать полный безопасный assessment package для Slider AI olddev.

**Что нельзя переносить на Slider AI без отдельного разрешения:** финальный проект остается в рамках `education/slider_ai_scope.md`; любые intrusive checks требуют отдельного approval.


**Процессный артефакт:** `REMEDIATION_BACKLOG.md` или `RETEST_PLAN.md`: приоритизация, владелец, retest evidence.

**Безопасная цель:** Учебный scope, подписанный RoE, собственная лаборатория или платформа с явным разрешением. Реальные организации только с письменным согласием.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Заполнить шаблон документа/чек-листа по учебному кейсу и связать каждую находку с доказательством.

**Углубление:** Добавить приоритизацию рисков, executive summary, ограничения тестирования и план повторной проверки.

**Минимальная проверка успеха:** Документ содержит scope, методологию, доказательства, ограничения и понятные рекомендации.

**Эталонный вывод:** Сданный артефакт: отчет, чек-лист, RoE, матрица рисков или презентация с проверяемыми доказательствами.

**Критерии сдачи:** Зачет: полный артефакт по шаблону. Отлично: ясная бизнес-интерпретация, приоритизация и план remediation.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 67. eJPT подготовка: практические лабы INE`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/pycharm-professional-python-2024-pages/`
- `docs/socraticode/architecture-patterns-python-pages/`

Конкретные страницы для этого блока: `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md`; `page-437.md`-`page-466.md`; `architecture-patterns-python-pages/page-038.md`-`page-129.md`.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: strategy, RoE, evidence policy, triage, remediation, retest, security regression и ownership. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: финальный проект остается в рамках `education/slider_ai_scope.md`; любые intrusive checks требуют отдельного approval. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

## Теория

### Что такое eJPT (eLearnSecurity Junior Penetration Tester)

eJPT (eJPTv2 — текущая версия) — сертификация от INE, ориентированная на начинающих пентестеров. Это практический сертификат, который проверяет базовые навыки пентеста.

**Особенности eJPTv2:**
- 100% практический экзамен (без тестов)
- Длительность экзамена: 48 часов (рекомендуется 8-16 часов)
- Стоимость: ~$249 (отдельно экзамен) или включен в курсы INE
- Не требует продления (пожизненный)
- На английском языке
- **Бесплатная альтернатива:** TryHackMe Jr. Penetration Tester path (бесплатно, покрывает базовые темы eJPT)

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

## Guided practice

1. Выберите финальный артефакт урока: RoE, checklist, finding, score, backlog, retest или appendix.
2. Заполните шаблон процесса на безопасном Slider AI-примере без секретов.
3. Свяжите результат с продуктовым риском, owner action и проверкой исправления.
4. Добавьте артефакт в итоговый assessment package и отметьте limitations.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Настройка лаборатории для подготовки

Для подготовки к eJPT вам понадобятся:

1. **MacBook Air M2 как рабочая станция**: заметки, браузер, VPN-клиент, Burp/ZAP, `nmap`, Python, Git.
   - Kali Linux ARM64 VM используется как углубление, если нужен Kali-специфичный инструмент.
   - TryHackMe AttackBox/HTB/Pwnbox предпочтительны для тяжелых лабораторий и Metasploit.
2. **Cloud/готовые лаборатории** (предпочтительно для 8GB RAM):
   - TryHackMe Jr Penetration Tester rooms
   - Hack The Box Starting Point / Academy
   - PortSwigger Academy для web-блока

3. **VulnHub VMs** (цели для практики, только если есть подходящая ARM64/легкая конфигурация):
   - **Basic Pentesting 1** — отлично для начала
   - **Kioptrix Level 1** — классика
   - **Metasploitable 2/3** — для сканирования и эксплуатации
   - **Mr. Robot** — веб-приложения + привилегии
   - **Stapler** — разнообразные векторы
   - **SickOs 1.2** — веб + привилегии

4. **TryHackMe** (онлайн-платформа):
   - Пройдите комнаты: "Intro to Researching", "Nmap", "Metasploit", "John the Ripper", "Hydra"
   - Все комнаты с Hydra/Metasploit/John выполнять только внутри правил THM/HTB/INE, не переносить техники на Slider AI и реальные сервисы.
   - Изучите "Penetration Testing" learning path

5. **Hack The Box** (Starting Point machines):
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

## 5. Post-Exploitation (понимание и reporting)
- [ ] Linux privilege escalation: перечисление (linpeas.sh, linenum.sh)
- [ ] Windows privilege escalation: перечисление (winpeas.exe)
- [ ] SUID/SGID exploits (Linux)
- [ ] Crontab exploits (Linux)
- [ ] Token impersonation (Windows)
- [ ] Dumping hashes: mimikatz, hashdump — только как лабораторная/экзаменационная тема; для рабочего QA-стенда формулировать риск и detection evidence, не выполнять
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
- [ ] Brute-force: hydra (FTP, SSH, HTTP, SMB) — только THM/HTB/INE lab с лимитами
- [ ] Wordlists: crunch, cewl, rockyou.txt; на Kali путь обычно `/usr/share/wordlists`, на macOS используйте локальный файл или `/opt/homebrew/share`
- [ ] Password spraying — знать как риск и анти-паттерн; не выполнять без отдельного письменного разрешения
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



## Примеры вывода

Минимальный эталонный артефакт для сдачи:

```markdown
Environment: macOS native / Kali ARM64 VM / cloud lab / Slider AI olddev
Target: <разрешенная учебная цель или https://olddev.slider-ai.ru>
Action: <выполненная безопасная команда или ручной шаг>
Evidence: <санитизированный фрагмент вывода, скриншота или HTTP history>
Result status: finding / observation / not reproducible / not applicable / requires approval
Next step: <retest, remediation, approval request или lab-only follow-up>
```

В отчете студент указывает среду выполнения, безопасную цель, команду или ручные шаги и коротко объясняет, какая строка подтверждает результат.




## Адаптация под macOS (M2, 8GB)

- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`; для явно помеченной Kali/Linux-среды допустим `apt`.
- Kali/Linux VM запускайте только как углубление и выделяйте не более 3-4GB RAM на MacBook Air M2 (8GB)
- Если нужна Kali/Linux VM на Apple Silicon, используйте ARM64-образ в UTM/VMware Fusion/Parallels; не используйте x86/x64 VM как базовый путь.
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты


## Задачи для самостоятельного выполнения

1. **Cloud-first Challenge**: пройдите одну комнату TryHackMe/HTB из разрешенного learning path и напишите отчет по PTES: Information Gathering → Exploitation → Privilege Escalation → Post-Exploitation.

2. **Nmap Mastery**: Напишите скрипт на Bash/Python, который автоматизирует сканирование только allowlist-целей: 1) пинг-сканирование лабораторной сети, 2) ограниченное сканирование живых хостов, 3) сохранение результатов. Добавьте rate limit и отказ от запуска вне lab/cloud.

3. **Metasploit Lab**: используйте TryHackMe AttackBox/HTB/Pwnbox или Kali ARM64 VM с разрешенной целью. Найдите и подтвердите 1-2 учебные уязвимости, не требуя локального Metasploitable2 на MacBook.

4. **Privilege Escalation**: выполните privesc только в cloud lab или легкой локальной ARM64 VM. Используйте linpeas.sh для перечисления и опишите найденный вектор.

5. **TryHackMe Path**: Зарегистрируйтесь на TryHackMe и пройдите минимум 10 комнат из раздела "Learning Paths" → "Complete Beginner" или "Offensive Pentesting". Скриншоты результатов приложите к отчету.

## Частые ошибки

1. **Недооценка времени** — 48 часов кажутся долгими, но новички часто тратят 16+ часов.
2. **Игнорирование базы** — eJPT проверяет базовые навыки, не пытайтесь учить сложные эксплойты.
3. **Плохая подготовка к pivoting** — многие заваливают латеральное движение, так как не практиковались.
4. **Незнание бесплатных альтернатив** — TryHackMe Jr. Penetration Tester path покрывает большинство тем eJPT бесплатно.

## Вопросы на понимание

1. Чем eJPTv2 отличается от предыдущих версий?
2. Какова стоимость экзамена eJPTv2?
3. Какая бесплатная альтернатива eJPT существует?
4. Сколько времени рекомендуется готовиться к eJPT?
5. Какие темы покрывает eJPT?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** eJPT readiness for QA

### Минимум

Отметьте, какие eJPT-навыки уже применялись в Slider AI-практике.

### Практика Slider AI

Составьте личный план добора навыков без расширения scope стенда.

### Углубление после изучения следующих уроков

После экзамена обновите курс: какие навыки реально помогли в QA.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `Final Security QA Assessment`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
