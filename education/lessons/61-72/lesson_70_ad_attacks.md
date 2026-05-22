# Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

Active Directory (AD) — служба каталогов от Microsoft, используемая в большинстве корпоративных сетей Windows. Это главная цель атакующих при компрометации корпоративной сети.

### Архитектура Active Directory (кратко)

- **Domain Controller (DC)** — сервер, управляющий AD
- **Domain** — логическая группа объектов (компьютеры, пользователи)
- **Forest** — коллекция доменов
- **OU (Organizational Unit)** — контейнер для организации объектов
- **GPO (Group Policy Object)** — политики, применяемые к объектам
- **Kerberos** — протокол аутентификации в AD

### Основные векторы атак на AD

1. **Kerberoasting** — атака на сервисные аккаунты (SPN)
2. **ASREPRoasting** — атака на пользователей без Kerberos pre-authentication
3. **DCSync** — имитация контроллера домена для репликации данных
4. **Pass the Hash (PtH)** — использование хешей паролей без их расшифровки
5. **Pass the Ticket (PtT)** — использование билетов Kerberos
6. **Golden Ticket** — подделка билета Kerberos с использованием krbtgt хеша
7. **Silver Ticket** — подделка сервисного билета
8. **BloodHound** — графовый анализ прав и привилегий в AD
9. **LLMNR/NBT-NS Poisoning** — отравление локальных протоколов разрешения имен
10. **Group Policy Preferences (GPP)** — извлечение паролей из GPO

### Kerberoasting

**Суть атаки:**
Атакующий запрашивает билет Kerberos (TGS) для сервисного аккаунта (SPN). Билет зашифрован с использованием хеша пароля сервисного аккаунта. Затем хеш можно подвергнуть оффлайн-брутфорсу.

**Кто уязвим:**
Сервисные аккаунты (Service Accounts), у которых настроен SPN (Service Principal Name) и имеют слабые пароли.

**Процесс риска на уровне понимания:**
1. У атакующего уже есть легитимная доменная учетная запись в учебной AD-lab.
2. Он ищет сервисные аккаунты с SPN.
3. Он получает Kerberos service ticket и анализирует, можно ли подобрать слабый пароль оффлайн.
4. Для Product Security QA важен не запуск атаки на продукт, а checklist защиты: длинные случайные пароли service accounts, gMSA, monitoring, rotation и least privilege.

**Инструменты:**
- Impacket: `GetUserSPNs.py`
- PowerShell: `Invoke-Kerberoast.ps1`
- Rubeus: `Rubeus.exe kerberoast`

### ASREPRoasting

**Суть атаки:**
Некоторые пользователи в AD могут иметь установленным флаг "Do not require Kerberos preauthentication". Это позволяет атакующему запросить AS_REQ (Authentication Service Request) от имени пользователя и получить ответ (AS_REP), который зашифрован с использованием хеша пароля пользователя. Хеш затем брутфорсится оффлайн.

**Кто уязвим:**
Пользователи с флагом `DONT_REQ_PREAUTH` (UserAccountControl = 4194304).

**Процесс риска на уровне понимания:**
1. Найти учетные записи без Kerberos pre-authentication в учебной AD-lab.
2. Понять, почему ответ AS_REP может стать материалом для offline guessing.
3. Для Product Security QA зафиксировать defensive expectation: pre-authentication включен, слабые пароли запрещены, события аномалий мониторятся.

**Инструменты:**
- Impacket: `GetNPUsers.py`
- Rubeus: `Rubeus.exe asreproast`

### DCSync

**Суть атаки:**
Атакующий, имеющий достаточные привилегии (чаще всего Domain Admin или DS-Replication-Get-Changes права), может имитировать контроллер домена и запросить репликацию данных, включая хеши паролей всех пользователей.

**Кто может выполнить:**
- Domain Admins
- Enterprise Admins
- Аккаунты с правами DS-Replication-Get-Changes и DS-Replication-Get-Changes-All

**Процесс риска на уровне понимания:**
1. Компрометация аккаунта с правами репликации.
2. Попытка имитировать контроллер домена и запросить репликацию секретов.
3. Для Product Security QA это не практическая команда, а high-risk scenario для вопросов владельцам AD/SSO: кто имеет replication rights, как это мониторится, как выполняется incident response.

**Инструменты:**
- Impacket: `secretsdump.py`
- Mimikatz: `lsadump::dcsync /domain:DOMAIN /user:krbtgt`
- BloodHound (для поиска путей к DCSync правам)

### CrackMapExec (CME)

CrackMapExec — инструмент для автоматизации атак на Active Directory, позволяющий выполнять различные действия (брутфорс, сбор данных, выполнение команд) на множестве хостов.

**Установка:**
```bash
pip3 install crackmapexec
```

**Основные возможности:**
- Брутфорс учетных данных SMB, WinRM, MSSQL
- Сбор информации о хостах (OS, версия, домен)
- Выполнение команд на скомпрометированных хостах
- Сбор данных для BloodHound (через модули)

**Пример lab-only awareness, не запускать вне разрешенной AD-lab:**
```bash
# Anti-example для Product QA:
# crackmapexec smb <lab-subnet> -u <lab-user> -p <lab-password>
#
# В курсе по Slider AI это оформляется как forbidden/approval-required action,
# а не как команда для рабочего стенда.
```

### BloodHound

BloodHound — инструмент для визуализации и анализа прав в Active Directory с использованием графовой базы данных (Neo4j).

**Возможности:**
- Поиск путей к Domain Admin
- Анализ привилегий пользователей
- Поиск уязвимостей (Kerberoastable, ASREPRoastable users)
- Анализ групповых политик
- Поиск латеральных путей

**Установка:**
- **macOS (M2):** `brew install --cask bloodhound` (нативно) или через Docker: `docker run -p 7474:7474 -p 7687:7687 -v $HOME/neo4j/data:/data -v $HOME/neo4j/logs:/logs neo4j:latest`
- **Linux:** `sudo apt install bloodhound` или через Docker
- **Windows:** Скачать с официального сайта или через Docker

**Сбор данных: SharpHound**
SharpHound — инструмент для сбора данных о AD в BloodHound. Запускается на скомпрометированной Windows-машине:
```powershell
SharpHound.exe -c All --zipfilename data.zip
```
Или использовать bloodhound-python на Kali:
```bash
pip3 install bloodhound
bloodhound-python -u user -p password -d DOMAIN.local -dc dc01.domain.local -c all
```

**Использование:**
1. Запустить Neo4j: `neo4j start`
2. Запустить BloodHound: `bloodhound`
3. Импорт JSON-файлов в BloodHound
4. Запуск встроенных запросов (queries)

### Адаптация для macOS (M2, 8GB RAM)

**Важно:** Запуск Active Directory лабораторий (Windows Server) локально на Mac с 8GB RAM невозможен из-за нехватки памяти. Используйте облачные альтернативы:
- HackTheBox Academy — AD Path
- TryHackMe — AD Rooms (Attacktive Directory, Silver Platter)
- Oracle Cloud Free Tier — бесплатные ARM инстансы (Always Free)

BloodHound работает на M2 natively через `brew install --cask bloodhound` или Docker.

## Guided practice

1. Выберите финальный артефакт урока: RoE, checklist, finding, score, backlog, retest или appendix.
2. Заполните шаблон процесса на безопасном Slider AI-примере без секретов.
3. Свяжите результат с продуктовым риском, owner action и проверкой исправления.
4. Добавьте артефакт в итоговый assessment package и отметьте limitations.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Настройка лаборатории AD

**Варианты:**
1. **GOAD (Game of Active Directory)** — готовая лаборатория с уязвимостями
   - GitHub: https://github.com/Orange-Cyberdefense/GOAD
   - Требует VirtualBox/Vagrant или Proxmox и не подходит как локальный базовый путь для MacBook Air M2 8GB
   - 5+ машин, реалистичная структура

2. **DetectionLab** — лаборатория для тестирования защиты
   - GitHub: https://github.com/clong/DetectionLab
   - Требует значительных ресурсов; для M2 8GB предпочтительнее cloud lab

3. **Простая лаба (ручная настройка):**
   - 1x Windows Server 2019 (Domain Controller)
   - 1x Windows 10 (клиент домена)
   - Kali Linux (атакующий)
   
   Настройте DC, создайте несколько пользователей, настройте SPN для одного пользователя, установите слабый пароль.

Для MacBook Air M2 (8GB) основной путь этого урока — HackTheBox Academy AD Path или TryHackMe AD Rooms. Локальные AD-лаборатории из нескольких Windows VM считать углублением вне базовой конфигурации.

### Lab-only awareness: как читать write-up, не превращая его в действие по продукту

Этот раздел не является обязательным hands-on путем для MacBook Air M2 8GB и не применяется к Slider AI. Используйте его только для разбора write-up в HTB/THM/INE AD lab, где такие техники явно разрешены.

#### Kerberoasting risk flow

```bash
# LAB-ONLY PSEUDOCODE:
# 1. Identify service accounts with SPN in the authorized AD lab.
# 2. Request a service ticket in the lab.
# 3. Record defensive evidence: weak service-account policy, missing monitoring, excessive privileges.
# 4. Do not run this flow against Slider AI or any real AD without written RoE.
```

#### ASREPRoasting risk flow

```bash
# LAB-ONLY PSEUDOCODE:
# 1. In an authorized AD lab, identify accounts without pre-authentication.
# 2. Document why this creates offline guessing risk.
# 3. Convert the result into a defensive checklist: enable pre-auth, monitor events, enforce password policy.
```

#### DCSync risk flow

```bash
# LAB-ONLY PSEUDOCODE:
# 1. In an authorized AD lab, review which accounts have replication rights.
# 2. Explain why replication rights can expose domain secrets.
# 3. Do not collect or print hashes in course artifacts.
# 4. Document defensive controls: least privilege, alerting, Event ID review, krbtgt rotation procedure.
```

### BloodHound сбор данных и анализ

```bash
# На Windows-цели (скомпрометированная машина):
# Скачать SharpHound: https://github.com/BloodHoundAD/SharpHound
SharpHound.exe -c All

# Или использовать bloodhound-python с Kali:
pip3 install bloodhound
bloodhound-python -u user -p password -d CORP.local -dc dc01.corp.local -c all

# Запустить Neo4j и BloodHound
neo4j start
bloodhound

# Загрузить .json файлы через интерфейс BloodHound
# Запустить встроенные запросы:
# - Find all Domain Admins
# - Find Shortest Paths to Domain Admins
# - List all Kerberoastable users
# - List all ASREPRoastable users
```



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

1. **Kerberoasting defensive lab**: В HTB/THM/INE AD lab разберите готовый write-up или выполните разрешенную lab-задачу. В отчете не публикуйте хеши/пароли; опишите риск, признаки detection и remediation.

2. **ASREPRoasting defensive lab**: Опишите, почему `DONT_REQ_PREAUTH` опасен, какие политики должны быть включены и какие события мониторить. Hands-on только в cloud lab с явным разрешением.

3. **BloodHound Analysis**: Установите BloodHound, соберите данные из тестового домена (или GOAD). Найдите 3 пути к Domain Admin. Сделайте скриншоты графов.

4. **Mitigation Research**: Напишите рекомендации по защите от Kerberoasting, ASREPRoasting и DCSync. Что должны делать администраторы? Какие политики настроить? Какие инструменты мониторинга использовать?

5. **DCSync detection**: Изучите, какие права и события связаны с DCSync. Напишите detection/remediation checklist, не описывая пошаговое получение хешей и не публикуя секреты.

## Частые ошибки

1. **Неправильная настройка SharpHound** — запуск без прав администратора домена может привести к неполным данным.
2. **Игнорирование латерального движения** — компрометация одной машины не означает доступ к AD. Нужно искать пути к Domain Admin.
3. **Плохой подбор паролей** — для Kerberoasting и ASREPRoasting используйте актуальные словари (rockyou.txt, сгенерированные cewl).
4. **Неправильное использование CrackMapExec** — запуск без указания правильных протоколов может привести к пропуску уязвимых хостов.

## Вопросы на понимание

1. В чем разница между Kerberoasting и ASREPRoasting?
2. Что такое DCSync и какие права нужны для его выполнения?
3. Как собрать данные для BloodHound с помощью SharpHound?
4. Почему на Mac с 8GB RAM нельзя запускать локальные AD лабы?
5. Как установить CrackMapExec и для чего он используется?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** AD attacks as theory for QA

### Минимум

Не применять AD-атаки к Slider AI; определить, есть ли SSO/AD как область вопросов к владельцам.

### Практика Slider AI

Составьте defensive checklist: MFA, service accounts, logs, least privilege, owner.

### Углубление после изучения следующих уроков

После отдельного AD scope используйте только лабораторные техники, не продуктовый стенд.

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
