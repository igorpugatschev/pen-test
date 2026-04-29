# Урок 39: Итоговая практика с инструментами

## Теория

Комплексный пентест требует умения связывать разные инструменты в цепочки (chains). Один инструмент находит поддомены, другой проверяет живые хосты, третий ищет уязвимости.

Типичный workflow пентеста внешнего периметра:
1. **Разведка** (Amass, Subfinder, Shodan) → список поддоменов
2. **Проверка живых хостов** (httpx, httprobe) → активные веб-сервера
3. **Сканирование портов** (Nmap) → открытые сервисы
4. **Поиск директорий** (ffuf, dirsearch) → скрытые пути
5. **Поиск уязвимостей** (Nuclei, Nmap NSE) → известные баги
6. **Эксплуатация** (SearchSploit, ручной анализ)

## Практическое занятие

### Цель: Metasploitable2

Разверните Metasploitable2 в VM (логин/пароль: msfadmin/msfadmin).

### Шаг 1: Разведка
```bash
# Определите IP Metasploitable
sudo nmap -sn 192.168.1.0/24  # Поиск хоста в сети
# Пример вывода:
# Nmap scan report for 192.168.1.101
# Host is up (0.00047s latency).

# Предположим, IP = 192.168.1.101
TARGET=192.168.1.101
```

### Шаг 2: Сканирование портов (Nmap)
```bash
# Полное сканирование
sudo nmap -A -p- -oA nmap_full $TARGET
# Пример вывода:
# PORT     STATE SERVICE    VERSION
# 21/tcp   open  ftp        vsftpd 2.3.4
# 22/tcp   open  ssh        OpenSSH 4.7p1 Debian
# 23/tcp   open  telnet     Linux telnetd
# 80/tcp   open  http       Apache httpd 2.2.8

# Результат: порты 21, 22, 23, 25, 53, 80, 111, 139, 445, 512, 513, 514, 1099, 1524, 2049, 2121, 3306, 5432, 5900, 6000, 6667, 8009, 8180
```

### Шаг 3: Поиск веб-директорий
```bash
# Поиск на порту 80
ffuf -u http://$TARGET/FUZZ -w /opt/homebrew/share/seclists/Discovery/Web-Content/common.txt -e .txt,.php,.bak
# Пример вывода:
# [Status: 200] [Size: 1234] /index.php
# [Status: 302] [Size: 0] /dvwa
# [Status: 200] /phpMyAdmin

# Результат: /dvwa, /phpMyAdmin, /mutillidae, /cgi-bin/
```

### Шаг 4: Поиск уязвимостей (Nuclei)
```bash
# Сканирование на уязвимости
nuclei -u http://$TARGET -severity critical,high
# Пример вывода:
# [CRITICAL] [http://$TARGET] [cves/2021/CVE-2021-41773] [...]

# Nmap NSE
nmap --script vuln -p 21,22,23,80,445 $TARGET
# Пример вывода:
# |_  smb-vuln-ms08-067: ERROR: Script execution failed
# |  ftp-vsftpd-backdoor: VULNERABLE: vsftpd 2.3.4 backdoor
```

### Шаг 5: Поиск эксплойтов (SearchSploit)
```bash
# Для vsftpd 2.3.4
searchsploit vsftpd 2.3.4
# Пример вывода:
# Exploits: 3
#   |  /usr/share/exploitdb/exploits/unix/remote/17491.rb

# Для Samba
searchsploit samba 3.0
# Пример вывода:
# Exploits: 5
#   |  /usr/share/exploitdb/exploits/linux/remote/10.c
```

### Шаг 6: Автоматизация (Bash скрипт)
Создайте скрипт `auto_scan.sh`:
```bash
#!/bin/bash
TARGET=$1

echo "[*] Starting full scan for $TARGET"

echo "[1] Nmap full scan..."
nmap -A -p- -oN nmap_$TARGET.txt $TARGET

echo "[2] Directory bruteforce (port 80)..."
ffuf -u http://$TARGET/FUZZ -w /opt/homebrew/share/seclists/Discovery/Web-Content/common.txt -o dirs_$TARGET.json -of json

echo "[3] Nuclei vulnerability scan..."
nuclei -u http://$TARGET -o nuclei_$TARGET.txt

echo "[4] SearchSploit..."
nmap -sV -p- $TARGET -oX nmap_$TARGET.xml
searchsploit --nmap nmap_$TARGET.xml

echo "[*] Scan complete!"
```


## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.



## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. Разверните Metasploitable2. Выполните полный пентест по шагам выше. Составьте список найденных уязвимостей.

2. Напишите скрипт на Python, который связывает Subfinder → httpx → Nuclei. Скрипт должен принимать домен и выдавать найденные уязвимости.

3. Используя Shodan, найдите 5 интересных хостов (с уязвимыми сервисами). Попробуйте подключиться к ним (только те, которые вам принадлежат или имеют разрешение!).

4. Настройте связку: Amass → Subfinder → ffuf → Nuclei. Результат сохраните в Markdown-отчет.

5. Изучите логи Metasploitable во время вашего сканирования. Какие инструменты вызвали подозрение? Как можно скрыть сканирование (stealth)?

## Частые ошибки

1. **Отсутствие прав для SYN-сканирования** — nmap -sS требует sudo, иначе будет использоваться TCP connect.

2. **Слишком агрессивное сканирование** — запуск всех инструментов одновременно может вызвать блокировку или обнаружение.

3. **Неправильный путь к словарям в macOS** — проверьте, что `/opt/homebrew/share/seclists/` или `/usr/share/wordlists/` доступны.

4. **Забыли про проверку живых хостов** — перед сканированием убедитесь, что цель доступна (ping, nmap -sn).

## Вопросы на понимание

1. В каком порядке нужно запускать инструменты для минимизации шума?

2. Какой инструмент дает наиболее полную картину уязвимостей: Nmap NSE, Nuclei или SearchSploit?

3. Почему важно связывать результаты разных инструментов (например, поддомены → живые хосты → уязвимости)?

4. Как автоматизировать весь процесс пентеста одним скриптом?


