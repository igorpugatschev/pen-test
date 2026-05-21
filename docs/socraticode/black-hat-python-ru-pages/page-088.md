# Black Hat Python. Программирование для хакеров и пентестеров — страница 88

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

88   Глава 4. Захват сети с помощью Scapy
from scapy.all import TCP, rdpcap
import collections
import os
import re
import sys
import zlib
OUTDIR = '/root/Desktop/pictures' 
PCAPS = '/root/Downloads'
Response = collections.namedtuple('Response', ['header', 'payload']) 
def get_header(payload): 
    pass
def extract_content(Response, content_name='image'): 
    pass
class Recapper:
    def __init__(self, fname):
        pass
    def get_responses(self): 
        pass
    def write(self, content_name): 
        pass
if __name__ == '__main__':
    pfile = os.path.join(PCAPS, 'pcap.pcap')
    recapper = Recapper(pfile)
    recapper.get_responses()
    recapper.write('image')
Это каркас основной логики всего скрипта, вспомогательные функции бу-
дут добавлены чуть позже. Мы импортируем нужные модули и указываем
местоположение каталога, в который будут записываться изображения,
а также путь к pcap-файлу , который нужно прочитать . Затем определяем
namedtuple с именем Response и двумя атрибутами: header (заголовок пакета)
и payload (содержимое пакета) . Мы создадим две вспомогательные функ-
ции для получения заголовка пакета  и извлечения содержимого . А также
определим класс Recapper, чтобы воссоздать изображения, присутствующие
в потоке пакетов. Помимо __init__ класс Recapper будет содержать два ме-
тода: get_responses для чтения ответов из pcap-файла  и write для записи
файлов с изображениями, обнаруженных в ответах, в выходной каталог .
Для начала напишем функцию get_header:
def get_header(payload):
    try:
        header_raw = payload[:payload.index(b'\r\n\r\n')+2] 
