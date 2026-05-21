# Black Hat Python. Программирование для хакеров и пентестеров — страница 69

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Декодирование ICMP   69
        self.type = header[0]
        self.code = header[1]
        self.sum = header[2]
        self.id = header[3]
        self.seq = header[4]
def sniff(host):
--пропущено--
            ip_header = IP(raw_buffer[0:20])
            # нас интересует ICMP
            if ip_header.protocol == "ICMP": 
                print('Protocol: %s %s -> %s' % (ip_header.protocol,
                        ip_header.src_address, ip_header.dst_address))
                print(f'Version: {ip_header.ver}')
                print(f'Header Length: {ip_header.ihl} TTL:
                      {ip_header.ttl}')
                # определяем, где начинается ICMP-пакет
                offset = ip_header.ihl * 4 
                buf = raw_buffer[offset:offset + 8]
                # создаем структуру ICMP
                icmp_header = ICMP(buf) 
                print('ICMP -> Type: %s Code: %s\n' %
                     (icmp_header.type, icmp_header.code))
        except KeyboardInterrupt:
            if os.name == 'nt':
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            sys.exit()
if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = '192.168.1.203'
    sniff(host)
Этот простой фрагмент кода создает структуру ICMP  внутри нашей струк-
туры IP. Когда главный цикл для приема пакетов обнаруживает, что мы полу-
чили ICMP-пакет , определяем, насколько его тело смещено относительно
исходного пакета , затем создаем буфер  и выводим поля type и code.
Величина смещения зависит от поля IP-заголовка ihl, которое показывает,
сколько 32-битных слов (4-байтных блоков) содержится в этом заголовке.
Таким образом, умножив это поле на 4, мы получаем размер IP-заголовка
и тем самым определяем, где начинается следующий уровень (в данном
случае ICMP).
