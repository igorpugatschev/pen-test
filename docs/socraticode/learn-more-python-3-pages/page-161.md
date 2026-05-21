# Легкий способ выучить Python 3 еще глубже — страница 161

160 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
Задача упражнения
Я создал модуль конечного автомата, который обрабатывает несколько про­
стых событий для обработки соединений с веб-сервером. Этот воображаемый
конечный автомат служит примером для того, как самому быстро написать
его на Python. Это только каркас обрабатывающих соединений, которые счи­
тывают и записывают из сокета, и ему не хватает нескольких важных вещей.
Но это всего лишь небольшой пример, которым вы можете пользоваться.
fsm.py
1 def START():
2 return LISTENING
3
4 def LISTENING(event):
5 if event == "connect":
6 return CONNECTED
7 elif event == ’’error”:
8 return LISTENING
9 else:
10 return ERROR
11
12 def CONNECTED(event):
13 if event = ’’accept”:
14 return ACCEPTED
15 elif event == ’’close”:
16 return CLOSED
17 else:
18 return ERROR
19
20 def ACCEPTED(event):
21 if event == ’’close”:
22 return CLOSED
23 elif event = "read”:
24 return READING(event)
25 elif event = "write":
26 return WRITING(event)
27 else:
28 return ERROR
29
30 def READING(event) :
31 if event == "read”:
