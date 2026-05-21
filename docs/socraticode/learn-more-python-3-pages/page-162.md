# Легкий способ выучить Python 3 еще глубже — страница 162

КОНЕЧНЫЕ АВТОМАТЫ 161
32 return READING
33 elif event == "write":
34 return WRITING(event)
35 elif event == "close":
36 return CLOSED
37 else:
38 return ERROR
39
40 def WRITING(event):
41 if event == "read":
42 return READING(event)
43 elif event == "write":
44 return WRITING
45 elif event == "close":
46 return CLOSED
47 else:
48 return ERROR
49
50 def CLOSED(event):
51 return LISTENING(event)
52
53 def ERROR(event):
54 return ERROR
Вот также крошечный тест, который показывает вам, как запустить этот модуль:
test fsm.py
1 import fsm
2
3 def test_basic_connection():
4 state = fsm.START()
5 script = ["connect”, "accept", "read",
6 "write", "close", "connect"]
7
8 for event in script:
9 print(event, ">>>", state)
10 state = state (event)
Ваша задача в данном упражнении - превратить этот пробный модуль в более
надежный и обобщенный класс FSM. Используйте это как набор подсказок
