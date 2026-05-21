# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 23

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Введение 23
ходимо выполнить в коде, и передавая эту задачу хорошо определенному
объекту или функции. Мы называем этот объект или функцию абстракцией.
Взгляните на следующие два фрагмента кода:
Выполнить поиск с помощью urllib
import json
from urllib.request import urlopen
from urllib.parse import urlencode
params = dict(q='Sausages', format='json')
handle = urlopen('http://api.duckduckgo.com' + '?' + urlencode(params))
raw_text = handle.read().decode('utf8')
parsed = json.loads(raw_text)
results = parsed['RelatedTopics']
for r in results:
 if 'Text' in r:
 print(r['FirstURL'] + ' - ' + r['Text'])
Выполнить поиск с помощью requests
import requests
params = dict(q='Sausages', format='json')
parsed = requests.get('http://api.duckduckgo.com/', params=params).json()
results = parsed['RelatedTopics']
for r in results:
 if 'Text' in r:
 print(r['FirstURL'] + ' - ' + r['Text'])
Оба листинга делают одно и то же: отправляют значения, закодированные
в форме, на URL-адрес, чтобы воспользоваться API поисковой машины. Но
второй код воспринимается легче, потому что работает на более высоком
уровне абстракции.
Мы можем пойти еще дальше, определив и назвав задачу , которую должен
выполнять код. Чтобы сделать ее более явной, мы используем еще более
высокоуровневую абстракцию.
Выполнить поиск с помощью модуля duckduckgo
import duckduckgo
for r in duckduckgo.query('Sausages').results:
 print(r.url + ' - ' + r.text)
