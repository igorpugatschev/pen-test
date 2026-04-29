# Занятие 16. Практика сети: настройка простой сети в UTM (2 VM)

## Теория

UTM — нативный гипервизор для macOS на чипах Apple Silicon (M1/M2). Для пентестинга часто требуется изолированная сетевая лаборатория.

> **Примечание для macOS M2 (8GB RAM):** VirtualBox официально не поддерживается на M1/M2. Используйте UTM или Parallels Desktop. Выделяйте VM суммарно не более 3.5-4GB RAM при 8GB на хосте.

### Типы сетей в UTM

**NAT (Network Address Translation)**
- VM имеет доступ в интернет через хост
- Внешняя сеть не видит VM
- VM получает IP из диапазона 10.0.2.x
- Простейший вариант, но VM недоступны друг для друга напрямую

**Shared Network (Общая сеть)**
- Группа VM в одной сети
- VM могут общаться друг с другом
- Есть доступ в интернет
- Аналог NAT Network в VirtualBox

**Bridged Adapter (Сетевой мост)**
- VM подключается к физической сети хоста
- VM получает IP из той же сети, что и хост
- VM видна в локальной сети как отдельный хост

**Host-only Adapter**
- Сеть только между хостом и VM
- Нет доступа в интернет
- Полезно для изолированных тестов

**Isolated Network (Внутренняя сеть)**
- Сеть только между VM
- Хост не имеет доступа
- Максимальная изоляция для тестов

### Планирование лаборатории

Для практики настроим:
- **VM1 (Kali Linux)** — атакующая машина (3GB RAM)
- **VM2 (Metasploitable3 или Ubuntu Server)** — целевая машина (512MB RAM)
- **Сеть**: Isolated Network или Host-only для изоляции

> **Важно про 8GB RAM:** Kali (3GB) + Metasploitable (512MB) + macOS ≈ 7.5GB. Не запускайте тяжёлые приложения на хосте во время работы лаборатории.

### Базовая настройка сети в Linux

После создания VM нужно настроить IP-адреса:

```bash
# Просмотр интерфейсов
ip addr show

# Настройка статического IP (временно)
sudo ip addr add 192.168.100.10/24 dev eth0
sudo ip link set eth0 up

# Настройка шлюза (если нужен выход)
sudo ip route add default via 192.168.100.1
```

## Практическое занятие

### Задача 1: Создание виртуальных машин

1. Скачайте образы (выберите ARM-версии для M2):
   - Kali Linux ARM64: https://www.kali.org/get-kali/
   - Metasploitable3 (рекомендуется для M2): https://github.com/rapid7/metasploitable3
   - Альтернатива: Ubuntu Server ARM64

2. Создайте VM в UTM:
   - **VM1**: Kali Linux (3GB RAM, 20+ GB диск)
   - **VM2**: Metasploitable3 (512MB RAM, 8GB диск)

> **Примечание:** Metasploitable2 (x86_64) не запустится нативно на M2. Используйте Metasploitable3 или VulnHub образы с поддержкой ARM.

### Задача 2: Настройка сети

1. Для обеих VM настройте сетевой адаптер:
   - Тип: **Isolated Network** (в UTM) или **Host-only**
   - Имя сети: `pentest-lab` (одинаковое для обеих VM)

2. Запустите VM1 (Kali) и настройте сеть:
```bash
# Проверьте имя интерфейса
ip addr show

# Настройте IP (обычно интерфейс eth0)
sudo ip addr add 192.168.100.10/24 dev eth0
sudo ip link set eth0 up

# Проверьте
ip addr show eth0
```

3. Запустите VM2 (Metasploitable) и настройте сеть:
```bash
# В Metasploitable (логин/пароль зависит от версии)
# Примечание: ifconfig считается устаревшим, используйте ip
sudo ip addr add 192.168.100.20/24 dev eth0
sudo ip link set eth0 up
```

### Задача 3: Проверка связности

1. С Kali пропингуйте Metasploitable:
```bash
ping -c 4 192.168.100.20
```

2. С Metasploitable пропингуйте Kali:
```bash
ping -c 4 192.168.100.10
```

3. Проверьте ARP-таблицы на обеих машинах:
```bash
ip neigh show
```
Примечание: команда `arp -n` считается устаревшей, используйте `ip neigh`.

### Задача 4: Сканирование сети

1. На Kali просканируйте сеть:
```bash
# Обнаружение хостов
nmap -sn 192.168.100.0/24

# Сканирование портов Metasploitable
nmap -sV -p- 192.168.100.20
```

2. Попробуйте подключиться к сервисам:
```bash
# SSH (если запущен)
ssh user@192.168.100.20

# HTTP
curl http://192.168.100.20
```

### Задача 5: Захват трафика

1. На Kali запустите tcpdump:
```bash
sudo tcpdump -i eth0 -w capture.pcap
```

2. На Metasploitable выполните любой сетевой запрос (например, ping до Kali)

3. Остановите tcpdump (Ctrl+C) и проанализируйте файл в Wireshark:
```bash
# Установка Wireshark в Kali:
sudo apt install -y wireshark

# Или на macOS (M2):
# brew install --cask wireshark

wireshark capture.pcap
```

## Примеры вывода

### ping -c 4 192.168.100.20
```
PING 192.168.100.20 (192.168.100.20) 56(84) bytes of data.
64 bytes from 192.168.100.20: icmp_seq=1 ttl=64 time=0.512 ms
64 bytes from 192.168.100.20: icmp_seq=2 ttl=64 time=0.487 ms
64 bytes from 192.168.100.20: icmp_seq=3 ttl=64 time=0.501 ms
64 bytes from 192.168.100.20: icmp_seq=4 ttl=64 time=0.495 ms

--- 192.168.100.20 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3000ms
rtt min/avg/max/mdev = 0.487/0.498/0.512/0.020 ms
```

### nmap -sn 192.168.100.0/24
```
Starting Nmap 7.94 ( https://nmap.org )
Nmap scan report for 192.168.100.1
Host is up (0.00045s latency).
Nmap scan report for 192.168.100.10
Host is up (0.00030s latency).
Nmap scan report for 192.168.100.20
Host is up (0.00028s latency).
Nmap done: 256 IP addresses (3 hosts up) scanned in 2.34 seconds
```

### nmap -sV -p- 192.168.100.20
```
Starting Nmap 7.94 ( https://nmap.org )
Nmap scan report for 192.168.100.20
Host is up (0.00050s latency).
Not shown: 65518 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1
23/tcp   open  telnet      Linux telnetd
25/tcp   open  smtp        Postfix smtpd
53/tcp   open  domain      ISC BIND 9.4.2
80/tcp   open  http        Apache httpd 2.2.8
111/tcp  open  rpcbind     2 (rpc #100000)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X
...
```

### ip neigh show
```
192.168.100.10 dev eth0 lladdr 08:00:27:ab:cd:ef REACHABLE
192.168.100.1 dev eth0 lladdr 52:54:00:12:34:56 REACHABLE
```

## Частые ошибки

1. **Проблема с UTM и 8GB RAM**: На хосте с 8GB RAM запускайте VM суммарно не более 3.5-4GB памяти. Kali требует минимум 2GB, Metasploitable может работать на 512MB.
2. **ifconfig vs ip**: Команда `ifconfig` устарела, используйте `ip addr` и `ip link`. В Metasploitable можете использовать обе, но старайтесь привыкать к `ip`.
3. **Сетевые адаптеры UTM**: Isolated Network изолирует VM от внешнего мира. Если нужен интернет на VM — используйте Shared Network или Bridged.
4. **Не забудьте про SSH**: В Metasploitable SSH часто запущен на порту 22, логин/пароль по умолчанию зависит от версии.
5. **Architecture mismatch**: Metasploitable2 (x86_64) не запустится на M2 (ARM). Используйте Metasploitable3 или VulnHub ARM-образы.

## Вопросы на понимание

1. В чем разница между Isolated Network в UTM и Host-only?
   <details><summary>Ответ</summary>Isolated Network — только между VM, Host-only — между VM и хостом (хост видит VM)</details>
2. Зачем пентестеру изолированная лаборатория?
   <details><summary>Ответ</summary>Для безопасного тестирования уязвимостей без риска атаки на реальные системы или выхода трафика во внешнюю сеть</details>
3. Почему используется Metasploitable3 вместо Metasploitable2 на M2?
   <details><summary>Ответ</summary>Metasploitable2 собран под x86_64 архитектуру и не запустится нативно на ARM (M1/M2). Metasploitable3 имеет поддержку ARM</details>
4. Какую роль выполняет Kali Linux в этой лаборатории?
   <details><summary>Ответ</summary>Kali используется как атакующая машина со встроенными инструментами для пентестинга (nmap, metasploit, wireshark и др.)</details>

## Задачи для самостоятельного выполнения

1. **Настройка статической IP через конфигурационные файлы**: Настройте статические IP-адреса так, чтобы они сохранялись после перезагрузки. Для Kali (если использует NetworkManager) создайте файл `/etc/NetworkManager/system-connections/pentest.nmconnection` или отредактируйте `/etc/network/interfaces`. Для Metasploitable отредактируйте `/etc/network/interfaces`. Перезагрузите VM и проверьте, что адреса применились.

2. **Добавление третьей VM**: Добавьте третью виртуальную машину (например, Ubuntu Desktop или Windows) в ту же Isolated Network. Настройте IP и проверьте связность между всеми тремя машинами. Создайте простую топологию: Kali (192.168.100.10), Target1 (192.168.100.20), Target2 (192.168.100.30).

3. **Настройка маршрутизации между сетями**: Создайте две разные Isolated Network (например, `net1` и `net2`). Настройте одну VM как роутер (с двумя сетевыми адаптерами в разные сети). Настройте маршруты на других VM так, чтобы они могли достигать машин в другой сети через роутер.

4. **Сканирование уязвимостей**: Используя nmap со скриптами NSE, просканируйте Metasploitable на наличие уязвимостей:
```bash
nmap --script vuln 192.168.100.20
```
Найдите минимум 3 уязвимых сервиса и опишите, какие именно уязвимости обнаружены.

5. **Настройка Host-only сети с доступом хоста**: Переключите VM на Host-only Adapter. Настройте сеть так, чтобы хост (ваша основная ОС) мог пинговать VM, а VM могли пинговать друг друга. Исследуйте, какой IP получает хост в этой сети (обычно .1).

6. **Траблшутинг сети**: Намеренно создайте проблему (например, заблокируйте ICMP с помощью iptables на Metasploitable, или уберите маршрут по умолчанию). Используйте инструменты диагностики (ping, traceroute, tcpdump, ss, ip route) для поиска и устранения проблемы. Опишите шаги диагностики.

## Адаптация под macOS (M2, 8GB)

Для пользователей macOS (особенно на чипах M1/M2 с 8GB RAM):

- **Виртуализация**: VirtualBox официально не поддерживается на Apple Silicon. Используйте:
  - **UTM** — нативный для Apple Silicon, бесплатный (рекомендуется)
  - **Parallels** — платный, но быстрый на M-чипах
  
- **Ограничения 8GB RAM**: 
  - Kali Linux: выделяйте 3GB RAM
  - Metasploitable: 512MB RAM
  - Суммарно: ~3.5GB для VM + ~4GB для macOS
  - Не запускайте тяжёлые приложения на хосте во время работы лаборатории

- **Установка инструментов** (на macOS хосте):
  ```bash
  brew install nmap
  brew install --cask wireshark
  brew install tcpdump  # обычно уже установлен
  ```

- **Скачивание образов (ARM64)**:
  - Kali Linux ARM64: https://www.kali.org/get-kali/
  - Metasploitable3: https://github.com/rapid7/metasploitable3
  - Внимание: Metasploitable2 (x86_64) не запустится на M2. Используйте альтернативы для ARM.

- **Настройка сети в UTM**:
  - Isolated Network: в UTM называется "Isolated Network"
  - Host-only: используйте "Shared Network" в UTM
  - Для доступа хоста к VM используйте "Shared Network"

- **Устаревшие команды**: Везде, где в уроке упоминаются `ifconfig`, `netstat`, `arp` — эти команды считаются устаревшими. Используйте современные аналоги:
  - `ifconfig` → `ip addr` / `ip link`
  - `netstat -tunap` → `ss -tunap`
  - `arp -n` → `ip neigh`
  - `route -n` → `ip route`

- **TryHackMe AttackBox (альтернатива локальным VM)**:
  - Если ресурсы 8GB RAM не позволяют комфортно работать с локальными VM, используйте TryHackMe AttackBox:
  - Браузерный доступ к полноценной Kali Linux
  - Не требует ресурсов вашей машины
  - Доступно на сайте tryhackme.com (раздел AttackBox)

- **testssl.sh**: Не устанавливается через brew. Скачайте с GitHub:
  ```bash
  git clone https://github.com/drwetter/testssl.sh.git
  cd testssl.sh
  ./testssl.sh example.com
  ```
