# Black Hat Python. Программирование для хакеров и пентестеров — страница 99

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Использование веб-библиотек   99
аутентификации методом перебора» далее. Для выполнения HTTP-запроса
проделайте следующее:
import requests
url = 'http://boodelyboo.com'
response = requests.get(url) # GET
data = {'user': 'tim', 'passwd': '31337'}
response = requests.post(url, data=data) # POST 
print(response.text) # response.text = string; response.content = bytestring 
Создаем url, request и словарь data с ключами user и passwd. Затем отправ-
ляем запрос методом POST  и выводим атрибут text (строку) . Если вы
предпочитаете работать с байтовыми строками, используйте атрибут content,
возвращенный вместе с ответом. Пример этого будет показан в разделе «Взлом
HTML-формы аутентификации методом перебора».
Пакеты lxml и BeautifulSoup
Для разбора содержимого полученного HTTP-ответа подойдет пакет lxml
или BeautifulSoup. За последние несколько лет эти два пакета стали более
похожими, вы можете применять синтаксический анализатор lxml в сочета-
нии с BeautifulSoup, равно как и синтаксический анализатор BeautifulSoup
в сочетании с lxml. Другие хакеры используют в своем коде и тот, и другой
пакет. У lxml синтаксический анализатор чуть быстрее, а у BeautifulSoup
предусмотрена логика для автоматического обнаружения кодировки задан-
ной HTML-страницы. Здесь мы будем работать с lxml. Оба пакета можно
установить с помощью pip:
pip install lxml
pip install beautifulsoup4
Допустим, вы сохранили HTML-код, возвращенный внутри ответа, в пере-
менную content. С  помощью lxml можете извлечь из него ссылки, как по-
казано далее:
from io import BytesIO 
from lxml import etree
import requests
url = 'https://nostarch.com
r = requests.get(url) # GET 
