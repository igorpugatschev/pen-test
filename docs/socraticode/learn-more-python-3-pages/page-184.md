# Легкий способ выучить Python 3 еще глубже — страница 184

СИНТАКСИЧЕСКИЕ АНАЛИЗАТОРЫ 183
63 if peek(tokens) == ’PLUS':
64 return plus(tokens, number)
65 else:
66 return number
67 else:
68 assert False, "Syntax error %r" % start
69
70 def plus(tokens, left):
71 """plus = expression PLUS expression"""
72 match(tokens, ’PLUS')
73 right = expression(tokens)
74 return {'type': 'PLUS', 'left': left, 'right': right}
75
76
77 def main(tokens):
78 results = []
79 while tokens:
80 results.append(root(tokens))
81 return results
82
83 parsed = main(scan(code))
84 pprint(parsed)
Обратите внимание, что я использую написанный мной модуль scanner,
который содержит функции match, peek, skip и scan. Я использую from
scanner import * только для того, чтобы сделать этот пример более по­
нятным. Вы должны использовать свой класс Scanner.
Также заметьте, что внутри этого маленького синтаксического анализатора я
поместил РБНФ в комментарии внутри каждой функции. Это помогло мне пи­
сать код, и позже я смогу использовать это для отчетов об ошибках. Прежде
чем переходить к разделу «Задача упражнения», вы должны изучить этот ана­
лизатор, возможно даже с использованием метода мастер-копии.
Задача упражнения
Ваша следующая задача состоит в том, чтобы объединить свой класс Scan­
ner с недавно написанным классом Parser, в котором вы можете выделить
подкласс. Также его можно повторно реализовать с помощью моего простого
