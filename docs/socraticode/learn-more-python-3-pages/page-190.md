# Легкий способ выучить Python 3 еще глубже — страница 190

СЕМАНТИЧЕСКИЕ АНАЛИЗАТОРЫ 189
2 def analyze(self, world):
3 ’"’’’Реализуйте свой анализатор здесь.”’’’’
Здесь мой первоначальный метод analyze (), и мы берем PunyPyWorld,
который будем использовать позже. Первая продукция грамматики - продук­
ция FuncCall:
ех34а.ру
1 class FuncCall(Production):
2
3 def __init (self, name, params):
4 self.name = name
5 self.params = params
6
7 def analyze(self, world):
8 print("> FuncCall: ”, self.name)
9 self.params.analyze(world)
Вызовы функций содержат имя (name) и params - класс продукции Param­
eters для параметров вызова функции. Взгляните на метод analyze (),
и вы увидите первую функцию Посетителя. Когда вы дойдете до PunyPy-
Analyzer, вы увидите, как она выполняется, но обратите внимание, что эта
функция затем вызывает param, analyze (world) для каждого из параме­
тров этой функции:
ех34а.ру
1 class Parameters(Production):
2
3 def _init__(self, expressions):
4 self.expressions = expressions
5
6 def analyze(self, world):
7 print(”» Parameters: ")
8 for expr in self.expressions:
9 expr.analyze(world)
