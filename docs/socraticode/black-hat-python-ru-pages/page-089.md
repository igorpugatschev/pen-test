# Black Hat Python. Программирование для хакеров и пентестеров — страница 89

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Анализ данных в формате pcap   89
    except ValueError:
        sys.stdout.write('-')
        sys.stdout.flush()
        return None 
    header = dict(re.findall(r'(?P<name>.*?): (?P<value>.*?)\r\n',
             header_raw.decode())) 
    if 'Content-Type' not in header: 
        return None
    return header
Функция get_header  принимает необработанный HTTP-трафик и выдает
заголовки. Чтобы извлечь заголовок, переходим в самое начало содержимого
и ищем две пары символов — возврата каретки и перевода строки . Если
ничего не удается найти, мы получим исключение ValueError, в этом слу-
чае просто выведем в консоль дефис (-) и завершим работу . Если поиск
окажется успешным, мы создадим словарь (header), разбив декодированное
содержимое на части, так чтобы ключ находился перед двоеточием, а значе-
ние — после него . Если заголовок не содержит ключа Content-Type, воз-
вращаем None, сигнализируя об отсутствии данных, которые нужно извлечь .
Т еперь давайте напишем функцию для извлечения содержимого из ответа:
def extract_content(Response, content_name='image'):
    content, content_type = None, None
    if content_name in Response.header['Content-Type']: 
        content_type = Response.header['Content-Type'].split('/')[1] 
         content = Response.payload[Response.payload.index(b'\r\n\r\n')+4:] 
        if 'Content-Encoding' in Response.header: 
            if Response.header['Content-Encoding'] == "gzip":
               content = zlib.decompress(Response.payload, zlib.MAX_WBITS | 32)
            elif Response.header['Content-Encoding'] == "deflate":
               content = zlib.decompress(Response.payload)
    return content, content_type 
Функция extract_content принимает HTTP-ответ и тип содержимого, ко-
торое мы хотим извлечь. Как вы помните, Response — это namedtuple с двумя
атрибутами, header и payload.
Если содержимое было закодировано  с помощью такого инструмента как
gzip или deflate, мы его распаковываем, используя модуль zlib. Если ответ
содержит изображение, в атрибуте Content-Type  его заголовка будет на-
ходиться подстрока image (например, image/png или image/jpg) . В таком
случае мы создаем переменную с именем content_type и присваиваем ей тип
