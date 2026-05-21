# Легкий способ выучить Python 3 еще глубже — страница 191

190 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
Это приводит к классу Parameters, который содержит каждое из выраже­
ний, составляющих параметры для функции. Parameters . analyze просто
проходит через свой список выражений, которых у нас два:
ех34а.ру
1 class Expr(Production): pass
2
3 class IntExpr(Expr):
4 def __init__(self, integer):
5 self.integer = integer
6
7 def analyze(self, world):
8 print(">>>> IntExpr: ", self.integer)
9
10 class AddExpr(Expr):
11 def __init__(self, left, right):
12 self.left = left
13 self.right = right
14
15 def analyze(self, world):
16 print(”>>> AddExpr: ")
17 self.left.analyze(world)
18 self.right.analyze(world)
В этом примере я прибавляю только два числа. Для этого я создаю базовый
класс Expr, а затем классы IntExpr и AddExpr. У каждого из них просто
есть методы analyze (), которые выводят их содержимое.
Таким образом, у нас есть классы для наших синтаксических деревьев, и мы
можем провести определенный анализ. Первое, что нам нужно, - это мир
(world), который может отслеживать определения переменных, функции
и другие данные, которые нужны нашим методам Production. analyze ().
ех34а.ру
1 class PunyPyWorld(object):
2
3 def __init__(self, variables):
4 self.variables = variables
5 self.functions = {}
