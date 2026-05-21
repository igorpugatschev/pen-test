# Легкий способ выучить Python 3 еще глубже — страница 183

182 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
II П II
funcdef = DEF name LPAREN params RPAREN COLON body
Я игнорирую тело, поскольку это слишком сложно.
В смысле, можете сами в этом разобраться,
и и и
skip(tokens) # отбрасываем def
name = match(tokens, 'NAME')
match(tokens, ’LPAREN’)
params = parameters(tokens)
match(tokens, 'RPAREN')
match(tokens, 'COLON')
return {'type': 'FUNCDEF', 'name': name, 'params': params}
def parameters(tokens):
"'"'params = expression * (COMMA expression)"""
params = []
start = peek(tokens)
while start != 'RPAREN':
params.append(expression(tokens))
start = peek(tokens)
if start ?= 'RPAREN':
assert match(tokens, 'COMMA')
return params
def function_call(tokens, name):
"""funccall = name LPAREN params RPAREN"""
match(tokens, 'LPAREN')
params = parameters(tokens)
match(tokens, 'RPAREN')
return {'type': 'FUNCCALL', 'name': name, 'params': params}
def expression(tokens):
"""expression = name / plus / integer"""
start = peek(tokens)
if start == 'NAME':
name = match(tokens, 'NAME')
if peek(tokens) == 'PLUS':
return plus(tokens, name)
else:
return name
elif start == 'INTEGER':
number = match(tokens, 'INTEGER')
