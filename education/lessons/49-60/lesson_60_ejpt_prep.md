# Занятие 60. Подготовка к eJPT: курс на INE

## Теория

**eJPT (eLearnSecurity Junior Penetration Tester)** — сертификация для начинающих пентестеров. Признана в индустрии как качественный entry-level сертификат.

**Отличия eJPT от других:**
- **Практический экзамен** — реальная сеть с машинами (без вопросов с выбором ответа)
- **Доступно для новичков** — не требует глубоких знаний
- **Доступна по цене** — дешевле CEH, OSCP

**INE (eLearnSecurity)** — платформа, предоставляющая курс "Penetration Testing Student" для подготовки к eJPT.

**Темы экзамена eJPT:**
1. **Assessment Methodologies** — методологии оценки
2. **Host Discovery** — обнаружение хостов (ping, nmap)
3. **Port Scanning** — сканирование портов
4. **OS Fingerprinting** — определение ОС
5. **Service Enumeration** — перечисление сервисов
6. **Vulnerability Assessment** — оценка уязвимостей
7. **Exploitation** — эксплуатация (Metasploit, ручная)
8. **Post-Exploitation** — повышение привилегий, lateral movement
9. **Active Directory** — базовые атаки на AD
10. **Report Writing** — написание отчетов

## Практическое занятие

### Подготовка через INE (или альтернативы)

**Если есть доступ к INE:**
1. Зарегистрируйтесь на ine.com
2. Пройдите курс "Penetration Testing Student" (PTS)
3. Выполните все лабораторные работы

**Альтернатива (бесплатная):**
- TryHackMe: пройдите треки "Complete Beginner", "Jr Penetration Tester", "Offensive Pentesting"
- HackTheBox: Starting Point + 10-15 Easy машин
- YouTube: каналы "The Cyber Mentor", "John Hammond" (eJPT prep)

### Симуляция экзамена eJPT

**Формат экзамена:**
- 48 часов на выполнение (можно сдать и за 8-12)
- Доступ к VPN-лаборатории
- 8-12 машин в сети
- Задачи: сканирование, эксплуатация, повышение привилегий, чтение флагов
- Написание отчета (обязательно!)

**Практическая симуляция (лаборатория):**

1. **Сканирование сети:**
```bash
nmap -sn 192.168.1.0/24  # Host discovery
nmap -sV -sC -p- 192.168.1.0/24  # Full scan
```

2. **Эксплуатация (пример):**
```bash
msfconsole
search exploit/windows/smb/ms17_010_eternalblue
use <exploit>
set RHOSTS <target>
exploit
```

3. **Повышение привилегий (Linux):**
```bash
sudo -l
find / -perm -4000 2>/dev/null
```

4. **Lateral Movement (AD):**
```bash
crackmapexec smb 192.168.1.0/24 -u user -p password
```

5. **Сбор флагов:**
- `user.txt` — в домашних директориях
- `root.txt` / `admin.txt` — после повышения привилегий

### Чек-лист готовности к eJPT

- [ ] Уверенное владение Nmap (все основные типы сканирования)
- [ ] Работа с Metasploit (search, use, set, exploit)
- [ ] Ручная эксплуатация SQLi, XSS, LFI
- [ ] Повышение привилегий Linux (sudo, SUID, cron)
- [ ] Повышение привилегий Windows (kernel exploits, service exploits)
- [ ] Базовые атаки на AD (Kerberoasting, LLMNR poisoning)
- [ ] Написание отчета (Executive Summary, Findings, Remediation)
- [ ] Работа с Burp Suite (Proxy, Repeater)
- [ ] Брутфорс (Hydra, John the Ripper)


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

1. **Пройти 3 машины HTB Easy за один день** — тренировка скорости (на экзамене время ограничено)
2. **Написать полный отчет** по пройденной сети (как для реального заказчика)
3. **Изучить материалы:** "eJPT Cheat Sheet" (найти на GitHub) — соберите свою шпаргалку

> **Финальный совет:** eJPT — отличная первая сертификация. После неё можно двигаться к OSCP (Offensive Security) или PNPT (Practical Network Penetration Tester). Главное — практика, практика, практика!
