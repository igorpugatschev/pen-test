# Легкий способ выучить Python 3 еще глубже — страница 192

СЕМАНТИЧЕСКИЕ АНАЛИЗАТОРЫ 191
Когда вызывается какой-либо метод Production. analyze (), ему пере­
дается объект PunyPyWorld, поэтому метод analysis () знает состояние
world. Он может обновлять переменные, искать функции и проводить анализ
везде в world.
Затем нам нужен PunyPyAnalyzer, который может принять дерево разбора
и world и выполнить все грамматические продукции:
ех34а.ру
1 class PunyPyAnalyzer(object):
2 def __init__(self, parse_tree, world):
3 self.parse_tree = parse_tree
4 self.world = world
5
6 def analyze(self):
7 for node in self.parse_tree:
8 node.analyze(self.world)
Это достаточно просто, чтобы настроить простой вызов функции hello
(10 + 20):
ех34а.ру
1 variables = {}
2 world = PunyPyWorld(variables)
3 # смоделировать hello (10 + 20)
4 script = [FuncCall (’’hello" ,
5 Parameters(
6 [AddExpr(IntExpr(10), IntExpr (20))])
7 )]
8 analyzer = PunyPyAnalyzer(script, world)
9 analyzer.analyze()
Убедитесь, что вы понимаете, как я структурировал эту переменную script.
Обратите внимание, что в первую очередь там используется список.
