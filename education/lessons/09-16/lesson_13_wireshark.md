# Занятие 13. Wireshark: захват трафика, фильтры, анализ HTTP-запросов

## Теория

Wireshark — мощный анализатор сетевого трафика (сниффер), позволяющий захватывать и анализировать пакеты в реальном времени.

### Интерфейсы захвата

- **eth0, eth1** — проводные сетевые интерфейсы
- **wlan0, wlan1** — беспроводные интерфейсы
- **lo** — loopback (локальный трафик)
- **any** — все интерфейсы (Linux)

### Режимы работы сетевых карт

- **Unicast mode** — карта принимает только пакеты для своего MAC
- **Promiscuous mode** — карта принимает все пакеты в сегменте сети
- **Monitor mode** (для Wi-Fi) — перехват всех беспроводных пакетов

### Фильтры в Wireshark

**Capture filters** (фильтры захвата) — применяются ДО захвата, используют синтаксис BPF (Berkeley Packet Filter):
- `host 192.168.1.1` — только трафик с/на этот IP
- `net 192.168.1.0/24` — трафик подсети
- `port 80` — трафик на порту 80
- `tcp port 443` — TCP трафик на 443
- `icmp` — только ICMP
- `arp` — только ARP

**Display filters** (фильтры отображения) — применяются ПОСЛЕ захвата:
- `ip.addr == 192.168.1.1` — IP-адрес
- `tcp.port == 80` — порт TCP
- `http` — только HTTP-трафик
- `http.request.method == "GET"` — GET-запросы
- `dns` — DNS-трафик
- `tcp.flags.syn == 1 && tcp.flags.ack == 0` — SYN-пакеты (начало соединения)
- `ip.src == 192.168.1.100 && ip.dst == 8.8.8.8` — исходящий трафик

### Структура окна Wireshark

1. **Packet List** — список пакетов
2. **Packet Details** — детали выбранного пакета (по уровням)
3. **Packet Bytes** — сырые данные пакета (hex + ASCII)

### Анализ TCP-соединения

- **SYN** — инициация соединения
- **SYN-ACK** — подтверждение
- **ACK** — завершение handshake
- **FIN** — корректное закрытие
- **RST** — сброс соединения

### Follow TCP Stream

Функция "Follow TCP Stream" позволяет собрать все пакеты TCP-сессии и увидеть переданные данные как единый поток (полезно для HTTP, FTP и др.).

## Практическое занятие

### Задача 1: Базовый захват и навигация

1. Установите Wireshark:
```bash
# macOS: brew install wireshark
# Linux: sudo apt install wireshark
brew install wireshark
```

2. Запустите Wireshark с правами root или через `sudo wireshark`
2. Выберите интерфейс (обычно тот, через который идет интернет)
3. Начните захват (красная кнопка или Ctrl+E)
4. В другом терминале выполните:
```bash
ping -c 5 8.8.8.8
```
5. Остановите захват и найдите ICMP-пакеты, используя фильтр отображения:
```
icmp
```

### Задача 2: Анализ HTTP-трафика

1. Начните новый захват
2. В терминале выполните HTTP-запрос (не HTTPS):
```bash
curl http://example.com
```
3. В Wireshark используйте фильтр:
```
http
```
4. Выберите пакет с HTTP GET-запросом
5. В Packet Details раскройте:
   - Frame — информация об уровне захвата
   - Ethernet II — MAC-адреса
   - Internet Protocol — IP-адреса
   - Transmission Control Protocol — порты и флаги
   - Hypertext Transfer Protocol — метод, путь, версия, заголовки

### Задача 3: Follow TCP Stream

1. Найдите HTTP-запрос в списке пакетов
2. Правый клик -> Follow -> TCP Stream
3. Увидите весь диалог клиент-сервер в виде текста
4. Нажмите "Close" и попробуйте фильтр:
```
tcp.stream == 0
```
(замените 0 на номер потока)

### Задача 4: Фильтрация и поиск

1. Используйте фильтр для поиска GET-запросов:
```
http.request.method == "GET"
```

2. Поиск по содержимому (Ctrl+F):
   - Выберите "Packet bytes" или "Packet details"
   - Введите строку поиска (например, "User-Agent")

3. Фильтр для поиска пакетов с ошибками:
```
tcp.flags.reset == 1
```

## Примеры вывода

### Фильтр: icmp (ping 8.8.8.8)
```
No.  Time        Source          Destination     Protocol Length Info
1    0.000000    192.168.1.100  8.8.8.8        ICMP     98     Echo (ping) request  id=0x1234, seq=1/256
2    0.023456    8.8.8.8        192.168.1.100   ICMP     98     Echo (ping) reply    id=0x1234, seq=1/256
```

### Фильтр: http.request.method == "GET"
```
No.  Time        Source          Destination     Protocol Length Info
15   2.123456    192.168.1.100  93.184.216.34   HTTP     456    GET / HTTP/1.1
```

### Фильтр: tcp.flags.syn == 1 && tcp.flags.ack == 0 (SYN-пакеты)
```
No.  Time        Source          Destination     Protocol Length Info
10   1.000000    192.168.1.100  93.184.216.34   TCP      66     52341 -> 80 [SYN] Seq=0 Win=64240 Len=0
```

### Follow TCP Stream (HTTP-диалог)
```
GET / HTTP/1.1
Host: example.com
User-Agent: curl/7.88.1
Accept: */*

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1256

<!doctype html>
<html>
...
```

## Частые ошибки

1. **Promiscuous mode vs Monitor mode**: Promiscuous — для проводных сетей (видит весь трафик в сегменте), Monitor — для Wi-Fi (видит все беспроводные пакеты). Не путайте их.
2. **Capture filter vs Display filter**: Capture filter (BPF) применяется ДО захвата, Display filter — ПОСЛЕ. Синтаксис разный! `tcp port 80` (capture) vs `tcp.port == 80` (display).
3. **Забыли sudo**: Wireshark и tcpdump требуют прав root для захвата пакетов. Используйте `sudo wireshark` или запускайте от root.
4. **Не видят трафик в свитче**: В коммутируемых сетях (через switch) вы видите только broadcast и свой трафик. Нужен ARP-spoofing для MITM.

## Вопросы на понимание

1. Чем отличается Capture filter от Display filter?
    <details><summary>Ответ</summary>Capture filter фильтрует ДО захвата (синтаксис BPF), Display filter — ПОСЛЕ (синтаксис Wireshark)</details>
2. Что делает функция "Follow TCP Stream"?
    <details><summary>Ответ</summary>Собирает все пакеты TCP-сессии и показывает переданные данные как единый текстовый поток</details>
3. Почему в свитчевой сети не виден чужой трафик?
    <details><summary>Ответ</summary>Коммутатор отправляет пакеты только на порт получателя (по MAC-таблице), в отличие от хаба, который шлет на все порты</details>
4. Как найти пароль в HTTP-трафике в Wireshark?
    <details><summary>Ответ</summary>Используйте Follow TCP Stream или фильтр http.request.method == "POST", смотрите тело запроса</details>

## Задачи для самостоятельного выполнения

1. **Захват DNS-запросов**: Начните захват трафика, выполните несколько DNS-запросов (через `dig` или браузер). Используйте фильтр `dns` и проанализируйте структуру DNS-пакета: найдите вопрос (query), ответ (answer), тип записи. Сколько времени занял запрос?

2. **Анализ TCP-handshake**: Захватите трафик при подключении к любому сайту по HTTP. Найдите три пакета 3-way handshake (SYN, SYN-ACK, ACK). Используйте фильтр `tcp.flags.syn == 1 || tcp.flags.ack == 1`. Опишите значения полей Sequence Number и Acknowledgment Number.

3. **Поиск чувствительной информации**: Если у вас есть доступ к тестовой среде (например, DVWA или Juice Shop), захватите трафик при вводе логина/пароля через HTTP (не HTTPS). Используйте "Follow TCP Stream" и найдите переданные учетные данные в открытом виде. Объясните, почему HTTPS важен.

4. **Анализ ARP-трафика**: Используйте фильтр `arp` и проанализируйте ARP-запросы и ответы в сети. Очистите ARP-таблицу (`sudo arp -d <ip>`) и снова захватите трафик при ping — увидите процесс ARP-resolution. Опишите структуру ARP-пакета.

5. **Экспорт объектов**: Зайдите на сайт с изображениями при включенном Wireshark. Используйте File -> Export Objects -> HTTP и сохраните изображения, переданные через HTTP. Объясните, почему это возможно только для незашифрованного трафика.

## Адаптация под macOS (M2, 8GB)

Для пользователей macOS (особенно на чипах M1/M2 и с 8GB RAM):

- **Установка инструментов**: Используйте `brew install` вместо `apt install`:
  ```bash
  brew install wireshark
  brew install nmap
  brew install tcpdump  # обычно уже установлен в macOS
  ```

- **Wireshark на macOS**: Устанавливается через `brew install wireshark`. Для захвата трафика может потребоваться дать права в Security & Privacy. Интерфейсы могут называться иначе (en0, en1 вместо eth0).

- **VirtualBox на M2**: Вместо VirtualBox рекомендуется использовать:
  - **UTM** — нативный для Apple Silicon, бесплатный
  - **Parallels** — платный, но быстрый на M-чипах
  
  На 8GB RAM запускайте VM с 3-4GB памяти.

- **Устаревшие команды**: Везде, где в уроке упоминаются `ifconfig`, `netstat`, `arp` — эти команды считаются устаревшими. Используйте современные аналоги:
  - `ifconfig` → `ip addr` / `ip link` (или установите iproute2mac: `brew install iproute2mac`)
  - `netstat -tunap` → `ss -tunap`
  - `arp -n` → `ip neigh`
  - `route -n` → `ip route`

- **Ограничения 8GB RAM**: Wireshark потребляет много памяти при захвате трафика. Ограничивайте размер захвата или используйте tcpdump для записи в файл, затем анализируйте в Wireshark.

- **Установка tcpdump на macOS**: Обычно уже установлен. Если нет: `brew install tcpdump`
