# Легкий способ выучить Python 3 еще глубже — страница 106

СЛОВАРЬ 105
77 print(slot_node.value)
78 slot_node = slot_node.next
79 bucket node = bucket node.next
Этот код реализует словарь с использованием вашего кода двусвязного спи­
ска. Если вы не полностью понимаете двусвязный список, тогда вы должны
попытаться выполнить процедуру мастер-копии кода. Как только вы будете
уверены, что понимаете двусвязный список, можете ввести этот код и начать
работать с ним. Помните, прежде чем добавлять аннотации, убедитесь, что
это идеальная копия. Худшее, что вы можете сделать, это аннотировать не­
правильно работающую копию моего кода.
Чтобы помочь вам лучше понять этот код, я написал быстрый и неаккуратный
тестовый сценарий:
test dictionary.ру
I from dictionary import Dictionary
2
3 # создать соответствие названий штатов и их аббревиатур
4 states = DictionaryO
5 states.set('Oregon’, ’OR’)
6 states.set('Florida’, ’FL’)
7 states.set(’California’, ’CA’)
8 states.set('New York', ’NY’)
9 states.set(’Michigan’, ’MI’)
10
II # создать базовый набор штатов и некоторых их городов
12 cities = DictionaryO
13 cities.set(’CA’, ’San Francisco’)
14 cities.set(’MI’, ’Detroit’)
15 cities.set('FL’, ’Jacksonville’)
16
17 # добавить еще немного городов
18 cities.set('NY', ’New York’)
19 cities.set(’OR’, ’Portland')
20
21
22 # вывести некоторые города
23 print('-’ * 10)
24 print("NY State has: %s" % cities.get(’NY’))
25 print("0R State has: %s” % cities.get(’OR’))
26
