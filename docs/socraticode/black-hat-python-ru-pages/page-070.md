# Black Hat Python. Программирование для хакеров и пентестеров — страница 70

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

70   Глава 3. Написание анализатора трафика
Если быстро проверить этот код с помощью стандартной команды ping, вывод
должен немного измениться:
Protocol: ICMP 74.125.226.78 -> 192.168.0.190
ICMP -> Type: 0 Code: 0
Это говорит о том, что ответы на ping (ICMP Echo) принимаются и декоди-
руются корректно. Т еперь все готово для реализации последней части логики
для отправки UDP-датаграмм и интерпретации ответов.
Воспользуемся модулем ipaddress, чтобы сканирование сетевых узлов могло
охватить целую подсеть. Сохраните свой скрипт sniffer_with_icmp.py под
именем scanner.py и добавьте в него следующий код:
import ipaddress
import os
import socket
import struct
import sys
import threading
import time
# сканируемая подсеть
SUBNET = '192.168.1.0/24'
# волшебная строка, которую мы будем искать в ICMP-ответах
MESSAGE = 'PYTHONRULES!' 
class IP:
--пропущено--
class ICMP:
--пропущено--
# эта функция добавляет в UDP-датаграммы наше волшебное сообщение
def udp_sender(): 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        for ip in ipaddress.ip_network(SUBNET).hosts():
            sender.sendto(bytes(MESSAGE, 'utf8'), (str(ip), 65212))
class Scanner: 
    def __init__(self, host):
        self.host = host
        if os.name == 'nt':
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP
