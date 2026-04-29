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

# Предположим, IP = 192.168.1.101
TARGET=192.168.1.101
```

### Шаг 2: Сканирование портов (Nmap)
```bash
# Полное сканирование
sudo nmap -A -p- -oA nmap_full $TARGET

# Результат: порты 21, 22, 23, 25, 53, 80, 111, 139, 445, 512, 513, 514, 1099, 1524, 2049, 2121, 3306, 5432, 5900, 6000, 6667, 8009, 8180
```

### Шаг 3: Поиск веб-директорий
```bash
# Поиск на порту 80
ffuf -u http://$TARGET/FUZZ -w /usr/share/wordlists/dirb/common.txt -e .txt,.php,.bak

# Результат: /dvwa, /phpMyAdmin, /mutillidae, /cgi-bin/
```

### Шаг 4: Поиск уязвимостей (Nuclei)
```bash
# Сканирование на уязвимости
nuclei -u http://$TARGET -severity critical,high

# Nmap NSE
nmap --script vuln -p 21,22,23,80,445 $TARGET
```

### Шаг 5: Поиск эксплойтов (SearchSploit)
```bash
# Для vsftpd 2.3.4
searchsploit vsftpd 2.3.4

# Для Samba
searchsploit samba 3.0
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
ffuf -u http://$TARGET/FUZZ -w /usr/share/wordlists/dirb/common.txt -o dirs_$TARGET.json -of json

echo "[3] Nuclei vulnerability scan..."
nuclei -u http://$TARGET -o nuclei_$TARGET.txt

echo "[4] SearchSploit..."
nmap -sV -p- $TARGET -oX nmap_$TARGET.xml
searchsploit --nmap nmap_$TARGET.xml

echo "[*] Scan complete!"
```

## Задачи для самостоятельного выполнения

1. Разверните Metasploitable2. Выполните полный пентест по шагам выше. Составьте список найденных уязвимостей.

2. Напишите скрипт на Python, который связывает Subfinder → httpx → Nuclei. Скрипт должен принимать домен и выдавать найденные уязвимости.

3. Используя Shodan, найдите 5 интересных хостов (с уязвимыми сервисами). Попробуйте подключиться к ним (только те, которые вам принадлежат или имеют разрешение!).

4. Настройте связку: Amass → Subfinder → ffuf → Nuclei. Результат сохраните в Markdown-отчет.

5. Изучите логи Metasploitable во время вашего сканирования. Какие инструменты вызвали подозрение? Как можно скрыть сканирование (stealth)?
