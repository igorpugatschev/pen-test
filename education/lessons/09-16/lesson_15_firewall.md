# Занятие 15. Firewall: основы iptables, правила INPUT/OUTPUT/FORWARD

## Теория

Firewall (брандмауэр, межсетевой экран) — система контроля и фильтрации сетевого трафика на основе заданных правил.

### iptables

iptables — утилита командной строки для настройки таблиц фильтрации пакетов в ядре Linux (netfilter).

### Структура iptables

**Таблицы (tables):**
- **filter** — основная таблица фильтрации (по умолчанию)
- **nat** — трансляция адресов (NAT)
- **mangle** — изменение заголовков пакетов
- **raw** — исключение из отслеживания соединений
- **security** — правила для MAC (SELinux)

**Цепочки (chains):**
- **INPUT** — входящий трафик к локальному хосту
- **OUTPUT** — исходящий трафик от локального хоста
- **FORWARD** — транзитный трафик (если хост выступает роутером)
- **PREROUTING** (в nat) — до маршрутизации
- **POSTROUTING** (в nat) — после маршрутизации

### Логика обработки пакета

1. Пакет поступает на интерфейс
2. PREROUTING (nat) — изменение адреса назначения (DNAT)
3. Routing decision — решение о маршрутизации
4. INPUT (filter) — если пакет для локального хоста
5. FORWARD (filter) — если пакет транзитный
6. OUTPUT (filter) — для локально созданных пакетов
7. POSTROUTING (nat) — изменение адреса источника (SNAT/MASQUERADE)

### Действия (targets)

- **ACCEPT** — разрешить пакет
- **DROP** — отбросить пакет (без ответа)
- **REJECT** — отбросить с отправкой ошибки
- **LOG** — записать в лог (не прерывает обработку)
- **DNAT** — изменить адрес назначения (перенаправление)
- **SNAT/MASQUERADE** — изменить адрес источника (NAT)

### Синтаксис iptables

```bash
iptables [-t table] <command> <chain> <parameters> -j <target>
```

**Команды:**
- `-A` — добавить правило в конец цепочки
- `-I` — вставить правило в начало (или позицию)
- `-D` — удалить правило
- `-R` — заменить правило
- `-L` — список правил
- `-F` — очистить цепочку
- `-P` — установить политику по умолчанию

**Параметры:**
- `-s` — исходный IP/сеть
- `-d` — IP назначения
- `-p` — протокол (tcp, udp, icmp)
- `--sport` — исходный порт
- `--dport` — порт назначения
- `-i` — входной интерфейс
- `-o` — выходной интерфейс
- `-m state --state` — состояние (NEW, ESTABLISHED, RELATED)

## Практическое занятие

### Задача 1: Просмотр текущих правил

1. Просмотрите текущие правила iptables:
```bash
sudo iptables -L -v -n
```

2. Просмотрите правила с номерами строк:
```bash
sudo iptables -L --line-numbers
```

3. Просмотрите таблицу nat:
```bash
sudo iptables -t nat -L -v -n
```

### Задача 2: Базовые правила фильтрации

1. Заблокируйте входящие соединения на порт 23 (Telnet):
```bash
sudo iptables -A INPUT -p tcp --dport 23 -j DROP
```

2. Разрешите входящие SSH-соединения:
```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

3. Заблокируйте конкретный IP-адрес:
```bash
sudo iptables -A INPUT -s 192.168.1.100 -j DROP
```

4. Разрешите трафик на loopback:
```bash
sudo iptables -A INPUT -i lo -j ACCEPT
```

### Задача 3: Политики по умолчанию

1. Установите политику DROP для входящего трафика (ОСТОРОЖНО — может отрезать доступ!):
```bash
# Сначала убедитесь, что SSH разрешен
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -P INPUT DROP
```

2. Разрешите уже установленные соединения:
```bash
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

3. Верните политику ACCEPT для безопасности:
```bash
sudo iptables -P INPUT ACCEPT
```

### Задача 4: NAT и перенаправление

1. Настройте SNAT (используя ваш внешний интерфейс):
```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

2. Перенаправьте порт (DNAT) — пример: трафик на порт 8080 перенаправить на 80:
```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 127.0.0.1:80
```

3. Включите IP forwarding:
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

## Примеры вывода

### sudo iptables -L -v -n
```
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:22
    0     0 DROP       tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:23
    0     0 ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
```

### sudo iptables -t nat -L -v -n
```
Chain PREROUTING (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain POSTROUTING (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 MASQUERADE  all  --  *      eth0    0.0.0.0/0            0.0.0.0/0
```

### sudo iptables -L --line-numbers
```
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination
1    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh
2    DROP       tcp  --  anywhere             anywhere             tcp dpt:telnet
3    ACCEPT     all  --  anywhere             anywhere
```

## Частые ошибки

1. **Блокировка SSH**: При установке политики INPUT DROP всегда сначала разрешайте SSH (`-p tcp --dport 22 -j ACCEPT`), иначе потеряете доступ.
2. **Порядок правил важен**: iptables проверяет правила по порядку. Более специфичные правила ставьте выше, политику по умолчанию — в конце.
3. **Правила не сохраняются**: `iptables-save` и `iptables-restore` нужны для сохранения правил после перезагрузки. Или используйте `iptables-persistent` на Debian/Ubuntu.
4. **DROP vs REJECT**: DROP просто отбрасывает пакет (отправитель ждет таймаута), REJECT отправляет ошибку (ICMP port unreachable). REJECT быстрее показывает, что порт закрыт.

## Вопросы на понимание

1. В чем разница между цепочками INPUT, OUTPUT и FORWARD?
    <details><summary>Ответ</summary>INPUT — входящий трафик к локальному хосту, OUTPUT — исходящий от хоста, FORWARD — транзитный трафик (когда хост выступает роутером)</details>
2. Что делает политика по умолчанию (policy)?
    <details><summary>Ответ</summary>Определяет действие для пакетов, которые не подошли ни под одно правило в цепочке (обычно ACCEPT или DROP)</details>
3. Зачем пентестеру знать iptables?
    <details><summary>Ответ</summary>Для понимания, как обойти файрвол, какие порты могут быть открыты/закрыты, как настроить pivot-хост при атаке</details>
4. Что такое stateful firewall?
    <details><summary>Ответ</summary>Файрвол, отслеживающий состояние соединений (NEW, ESTABLISHED, RELATED). Разрешает ответные пакеты без явного правила</details>

## Задачи для самостоятельного выполнения

1. **Создание базового файрвола**: Напишите скрипт (bash), который настраивает минимальный файрвол со следующими правилами:
   - Политика по умолчанию: INPUT DROP, FORWARD DROP, OUTPUT ACCEPT
   - Разрешить loopback
   - Разрешить SSH (порт 22)
   - Разрешить HTTP (80) и HTTPS (443)
   - Разрешить DNS (53) для исходящих
   - Разрешить уже установленные соединения
   - Заблокировать ping (ICMP echo-request) извне
   
   Протестируйте скрипт в безопасной среде (виртуалка).

2. **Логирование пакетов**: Добавьте правило iptables, которое логирует отброшенные пакеты в системный лог:
```bash
sudo iptables -A INPUT -j LOG --log-prefix "IPTABLES_DROPPED: "
```
Проверьте логи: `sudo dmesg | grep IPTABLES_DROPPED` или `sudo tail -f /var/log/kern.log`. Объясните, зачем нужно логирование в файрволе.

3. **Защита от сканирования портов**: Настройте правило, которое блокирует IP, пытающийся сканировать порты (много новых соединений за короткое время). Исследуйте модуль `recent` в iptables. Пример:
```bash
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 10 -j DROP
```

4. **Анализ существующих правил**: Если у вас есть доступ к серверу с настроенным iptables, проанализируйте его правила. Определите, какие порты открыты, есть ли правила для защиты от атак, используется ли NAT. Напишите отчет.

5. **Сравнение с nftables**: Изучите, чем nftables отличается от iptables. Напишите эквивалентное правило iptables в синтаксисе nftables. Попробуйте выполнить его (если nftables установлен).

6. **Обход файрвола**: Используя nmap, просканируйте хост с включенным файрволом (настройте простые правила для теста). Попробуйте различные типы сканирования (-sS, -sT, -sA, -sN) и объясните, какие из них могут обойти простые правила файрвола и почему.

## Адаптация под macOS (M2, 8GB)

Для пользователей macOS (особенно на чипах M1/M2 и с 8GB RAM):

- **Установка инструментов**: Используйте `brew install` вместо `apt install`:
  ```bash
  brew install nmap
  brew install iptables  # не установится, iptables только для Linux
  ```

- **Firewall на macOS**: В macOS используется **PF (Packet Filter)** вместо iptables:
  - Просмотр правил: `sudo pfctl -sr`
  - Включение: `sudo pfctl -E`
  - Отключение: `sudo pfctl -d`
  - Файл конфигурации: `/etc/pf.conf`
  
  Пример правила PF (блокировка порта 23):
  ```bash
  echo "block drop in on en0 proto tcp from any to any port 23" | sudo pfctl -ef -
  ```

- **Виртуализация**: Вместо VirtualBox (который может быть нестабилен на M2) рекомендуется использовать:
  - **UTM** — нативный для Apple Silicon, бесплатный
  - **Parallels** — платный, но быстрый на M-чипах
  
  На 8GB RAM запускайте VM с 3-4GB памяти.

- **Устаревшие команды**: Везде, где в уроке упоминаются `ifconfig`, `netstat`, `arp` — эти команды считаются устаревшими. Используйте современные аналоги:
  - `ifconfig` → `ip addr` / `ip link` (или установите iproute2mac: `brew install iproute2mac`)
  - `netstat -tunap` → `ss -tunap` (или `netstat -an` на macOS)
  - `arp -n` → `ip neigh`
  - `route -n` → `ip route` (или `netstat -rn` на macOS)

- **Ограничения 8GB RAM**: Не запускайте одновременно много тяжелых VM. Оптимально: 1 Kali (3GB) + 1 Metasploitable (512MB) = 3.5GB + хост ~4GB.

- **PF vs iptables**: Разница в синтаксисе. PF проще в настройке, но iptables мощнее. Для обучения пентестингу лучше использовать Linux VM.
