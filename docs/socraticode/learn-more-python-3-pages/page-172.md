# Легкий способ выучить Python 3 еще глубже — страница 172

ЛЕКСИЧЕСКИЕ АНАЛИЗАТОРЫ 171
14 (re.compile (r"A\)") , "RPAREN") ,
15 (re.compile(r"A\+"), "PLUS"),
16 (re.compile(r" A : ") , "COLON") ,
17 (re.compile(r"A,"), "COMMA") ,
18 (re.compile(r"A\s+"), "INDENT"),
19 ]
20
21 def match(i, line):
22 start « line[i:]
23 for regex, token in TOKENS:
24 match » regex.match(start)
25 if match:
26 begin, end = match.span()
27 return token, start[:end],end
28 return None, start, None
29
30 script = []
31
32 for line in code:
33 i = 0
34 while i < len(line):
35 token, string, end = match(i, line)
36 assert token, "Failed to match line %s" % string
37 if token:
38 i += end
39 script.append((token, string, i, end))
40
41 print(script)
Когда вы запускаете этот сценарий, вы получаете список кортежей, в которых
находятся ТОКЕНЫ, соответствие в строке, начало и конец, следующим об­
разом:
('PLUS', ' + ', 13, 1), ('INDENT', ' ', 14, 1), ('NAME', 'у', 15, 1),
[('DEF', 'def, 3, 3), (’'INDENT', ' ', 4, 1) , ( 'NAME', 'hello', 9, 5)
('LPAREN',’ ( ’ z 10, 1), ('NAME', 'x', 11, 1), ('COMMA', ',', 12, 1)
('INDENT',’ 13, 1), ('NAME', 'y', 14, 1), (: 'RPAREN', ')', 15, 1)
('COLON', 16, 1), (’'INDENT', ' ', 4, 4), ( 'NAME', 'print', 9, 5)
('LPAREN',’ (’, 10, 1), ('NAME', 'x', 11, 1), ('INDENT', ' ',12,1)
('RPAREN', ')', 16, 1), ('NAME', 'hello', 5, 5), ('LPAREN', '(', 6, 1) ,
