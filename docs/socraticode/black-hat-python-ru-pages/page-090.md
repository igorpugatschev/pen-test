# Black Hat Python. Программирование для хакеров и пентестеров — страница 90

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

90   Глава 4. Захват сети с помощью Scapy
содержимого, указанный в заголовке . Для хранения самого содержимого
(всего, что идет после заголовка) используем еще одну переменную . В конце
возвращаем кортеж с content и content_type .
Итак, две вспомогательные функции готовы. Добавим методы в класс Recapper:
class Recapper:
    def __init__(self, fname): 
        pcap = rdpcap(fname)
        self.sessions = pcap.sessions() 
        self.responses = list() 
Сначала мы инициализируем объект, передавая ему имя pcap-файла, который
нужно прочитать . Мы пользуемся прекрасными возможностями библио-
теки Scapy , позволяющей разбивать TCP-поток на отдельные сеансы  и со-
хранять их в виде словаря. В конце создаем пустой список с именем responses,
который позже будет наполнен ответами из pcap-файла .
В методе get_responses мы пройдемся по потоку пакетов в поиске каждого
отдельного ответа и добавим найденное в список responses:
def get_responses(self):
    for session in self.sessions: 
        payload = b''
        for packet in self.sessions[session]: 
            try:
                if packet[TCP].dport == 80 or packet[TCP].sport == 80: 
                    payload += bytes(packet[TCP].payload)
            except IndexError:
                sys.stdout.write('x') 
                sys.stdout.flush()
    if payload:
        header = get_header(payload) 
        if header is None:
            continue
        self.responses.append(Response(header=header, payload=payload)) 
В методе get_responses мы перебираем сначала словарь сеансов sessions ,
а затем пакеты, принадлежащие каждому сеансу . Фильтруем трафик, что-
бы получить только пакеты, которые были приняты или отправлены через
порт 80 . Затем объединяем все полезное содержимое в буфер с именем
payload . Это фактически то же самое, что щелкнуть в Wireshark правой
кнопкой мыши на пакете и выбрать пункт меню Follow TCP Stream (Отследить
TCP-поток). Если не получится добавить содержимое в переменную payload
