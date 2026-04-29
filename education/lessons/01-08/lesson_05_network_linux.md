# Занятие 5: Сеть в Linux для пентестера

## Теория

Сетевые инструменты Linux — основа разведки и эксплуатации в пентесте. Умение быстро узнать свои IP, проверить связность и просканировать порты критично.

> **Примечание для macOS (M2, 8GB):** Для запуска Kali Linux на Mac M2 используйте UTM или Parallels Desktop вместо VirtualBox. Выделяйте виртуалке 3-4GB RAM при 8GB на хосте. Установка пакетов: `sudo apt install` (Kali), `brew install` (macOS).

### Сетевые интерфейсы

- `lo` — loopback (127.0.0.1), локальная петля
- `eth0`, `ens33` — проводные интерфейсы
- `wlan0` — беспроводные интерфейсы
- `tun0` — VPN-интерфейсы (часто в HTB, TryHackMe)

### Основные команды

| Команда | Назначение |
|---------|-----------|
| `ip addr` | Показать IP-адреса интерфейсов |
| `ip route` | Таблица маршрутизации |
| `ifconfig` | Устаревшая, но всё ещё используемая команда |
| `ping` | Проверка связности (ICMP) |
| `netstat` | Сетевая статистика (устаревшая) |
| `ss` | Современная замена netstat |
| `arp` | Таблица ARP (соседи по сети) |
| `route` | Таблица маршрутизации (устаревшая) |

### Порты и соединения

- **Listening** — порт открыт и ждет подключений
- **Established** — активное соединение
- **TCP** — надежный, с установлением соединения
- **UDP** — без установления соединения

### DNS

- `/etc/resolv.conf` — DNS-серверы
- `/etc/hosts` — локальные записи имён
- `dig`, `nslookup` — запросы DNS

## Практическое занятие

### Шаг 1: Просмотр сетевых интерфейсов

```bash
# Современный способ (iproute2)
ip addr show
```
**Пример вывода `ip addr show`:**
```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:ab:cd:ef brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.105/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 86300sec preferred_lft 86300sec
```

```bash
# Кратко — только IP адреса
ip -br addr
```
**Пример вывода `ip -br addr`:**
```text
lo               UNKNOWN        127.0.0.1/8
eth0             UP             192.168.1.105/24
tun0             UNKNOWN        10.10.14.5/23
```

```bash
# Устаревший способ
ifconfig

# Показать только активные интерфейсы
ip link show up
```

### Шаг 2: Маршрутизация и шлюз

```bash
# Посмотреть таблицу маршрутизации
ip route
```
**Пример вывода `ip route`:**
```text
default via 192.168.1.1 dev eth0 proto dhcp src 192.168.1.105 metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.105
10.10.14.0/23 dev tun0 proto kernel scope link src 10.10.14.5
```

```bash
# Добавить маршрут (пример)
sudo ip route add 10.0.0.0/8 via 192.168.1.1

# Удалить маршрут
sudo ip route del 10.0.0.0/8

# Посмотреть ARP-таблицу (соседи)
ip neigh
```
**Пример вывода `ip neigh`:**
```text
192.168.1.1 dev eth0 lladdr 00:11:22:33:44:55 REACHABLE
192.168.1.50 dev eth0 lladdr aa:bb:cc:dd:ee:ff STALE
```

### Шаг 3: Проверка связности

```bash
# Ping (Ctrl+C для остановки)
ping -c 4 8.8.8.8
```
**Пример вывода `ping -c 4 8.8.8.8`:**
```text
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=15.2 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=14.8 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=118 time=15.0 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=118 time=14.9 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 14.800/14.975/15.200/0.150 ms
```

```bash
# Ping по имени
ping -c 4 google.com

# TTL и размер пакета
ping -c 3 -s 1024 8.8.8.8

# Traceroute — путь до хоста
traceroute google.com

# Если нет traceroute, установить:
sudo apt install -y traceroute
# Для macOS: brew install traceroute
```

### Шаг 4: Просмотр портов и соединений (ss / netstat)

```bash
# Все слушающие TCP порты
ss -tlnp
```
**Пример вывода `ss -tlnp`:**
```text
State     Recv-Q    Send-Q    Local Address:Port    Peer Address:Port    Process
LISTEN    0         128       0.0.0.0:22            0.0.0.0:*           users:(("sshd",pid=123,fd=3))
LISTEN    0         128       127.0.0.1:631         0.0.0.0:*           users:(("cupsd",pid=456,fd=7))
LISTEN    0         80        0.0.0.0:3306          0.0.0.0:*           users:(("mysqld",pid=789,fd=29))
```

```bash
# Все активные соединения
ss -tunap

# Только UDP
ss -ulnp

# С резолвом имён (медленно)
ss -tlnp --resolve

# Устаревший netstat (если доступен)
netstat -tlnp
netstat -tunap
```

### Шаг 5: DNS и хосты

```bash
# Посмотреть DNS-серверы
cat /etc/resolv.conf
```
**Пример вывода `cat /etc/resolv.conf`:**
```text
nameserver 192.168.1.1
nameserver 8.8.8.8
```

```bash
# Добавить запись в hosts
echo "10.10.10.10 target.htb" | sudo tee -a /etc/hosts

# Проверить запись
cat /etc/hosts
ping target.htb

# DNS-запрос
dig google.com
```
**Пример вывода `dig google.com` (фрагмент):**
```text
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		300	IN	A	142.250.74.46
```

```bash
# Короткий ответ
dig +short google.com

# Обратный DNS (PTR)
dig -x 8.8.8.8
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

1. Определите свой внешний IP-адрес, используя команду `curl ifconfig.me` или `curl ipinfo.io/ip`. Сравните с внутренним IP (из `ip addr`). Объясните разницу. *Примечание: на Mac M2 с 8GB RAM при запуске HTB-лабораторий выделяйте ВМ не более 3-4GB.*

2. Найдите все открытые порты на локальной машине, которые слушают на всех интерфейсах (0.0.0.0). Используйте `ss -tlnp`. Запишите список портов и соответствующих служб.

3. Добавьте в `/etc/hosts` запись для вымышленной машины: `10.10.10.100 hackthebox.htb`. Проверьте, что `ping hackthebox.htb` пытается пинговать указанный IP. Удалите запись после проверки.

4. Используя `ping` и `traceroute`, исследуйте маршрут до `1.1.1.1` (Cloudflare DNS). Сколько хопов (промежуточных узлов) до цели? Запишите результаты.

5. *Перенесено в Урок 7: Bash-скрипты.*
   *Справка:* Написание скриптов на bash изучается в Уроке 7. Кратко: скрипт сохраняется в файл с shebang `#!/bin/bash`, делается исполняемым через `chmod +x` и запускается как `./script.sh`.

## Частые ошибки

1. **Путаница между `ss` и `netstat`.** `ss` — современная утилита, `netstat` считается устаревшей, но работает похоже. Предпочитайте `ss`.
2. **Забытое `sudo` при изменении `/etc/hosts`.** Файл принадлежит root, для редактирования нужны права суперпользователя.
3. **Игнорирование `tun0` интерфейса.** В HTB VPN-интерфейс `tun0` — основной для доступа к целевым машинам, не путайте его с `eth0`.
4. **Неправильное чтение вывода `ss -tlnp`.** `0.0.0.0:22` означает, что порт слушает на всех интерфейсах, `127.0.0.1:631` — только на локальной петле.

## Вопросы на понимание

1. Чем отличается `ip addr show` от устаревшего `ifconfig`?
2. Что означает состояние порта "Listening"?
3. Зачем нужен файл `/etc/hosts` и чем он отличается от DNS-сервера?
4. Как узнать, какой процесс слушает конкретный порт (например, 22)?
5. Почему в пентесте важно знать свой внутренний и внешний IP-адреса?
