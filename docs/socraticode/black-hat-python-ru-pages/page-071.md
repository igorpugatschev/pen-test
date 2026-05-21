# Black Hat Python. Программирование для хакеров и пентестеров — страница 71

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Декодирование ICMP   71
        self.socket = socket.socket(socket.AF_INET,
                                        socket.SOCK_RAW, socket_protocol)
        self.socket.bind((host, 0))
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        if os.name == 'nt':
            self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
def sniff(self): 
    hosts_up = set([f'{str(self.host)} *'])
    try:
        while True:
            # читаем пакет
            raw_buffer = self.socket.recvfrom(65535)[0]
            # создаем IP-заголовок из первых 20 байт
            ip_header = IP(raw_buffer[0:20])
            # нас интересует ICMP
            if ip_header.protocol == "ICMP":
                offset = ip_header.ihl * 4
                buf = raw_buffer[offset:offset + 8]
                icmp_header = ICMP(buf)
                # ищем тип и код 3
                if icmp_header.code == 3 and icmp_header.type == 3:
                    if ipaddress.ip_address(ip_header.src_address) in 
                                      ipaddress.IPv4Network(SUBNET):
                        # проверяем, содержит ли буфер наше волшебное сообщение
                        if raw_buffer[len(raw_buffer) - len(MESSAGE):] == 
                                      bytes(MESSAGE, 'utf8'):
                            tgt = str(ip_header.src_address)
                            if tgt != self.host and tgt not in hosts_up:
                                hosts_up.add(str(ip_header.src_address))
                                print(f'Host Up: {tgt}') 
    # обрабатываем Ctrl+C
    except KeyboardInterrupt: 
            if os.name == 'nt':
                self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            print('\nUser interrupted.')
            if hosts_up:
                print(f'\n\nSummary: Hosts up on {SUBNET}')
            for host in sorted(hosts_up):
                print(f'{host}')
            print('')
            sys.exit()
if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
