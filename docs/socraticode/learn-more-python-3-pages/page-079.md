# Легкий способ выучить Python 3 еще глубже — страница 79

78 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
Тест
Я предоставлю тест, который вы должны пройти, реализовывая этот класс. Вы
увидите, что я прошелся по каждой операции и постарался учесть большин­
ство пограничных случаев, но когда дело дойдет до проверки, окажется, что
часть из них из них я пропустил. Люди иногда забывают выполнить тест для
случаев «ноль элементов» или «один элемент».
test_sllist.ру
1 from sllist import *
2
3 def test_push():
4 colors = SingleLinkedList()
5 colors .push (’’Pthalo Blue")
6 assert colors.count() == 1
7 colors.push("Ultramarine Blue")
8 assert colors.count() == 2
9
10 def test_pop():
11 colors = SingleLinkedList()
12 colors.push("Magenta")
13 colors.push("Alizarin")
14 assert colors.pop() == "Alizarin"
15 assert colors.pop() == "Magenta"
16 assert colors.pop() == None
17
18 def test_unshift():
19 colors = SingleLinkedList()
20 colors.push("Viridian")
21 colors.push("Sap Green")
22 colors.push("Van Dyke")
23 assert colors.unshift() == "Viridian"
24 assert colors.unshift() == "Sap Green"
25 assert colors.unshift() == "Van Dyke"
26 assert colors.unshift() == None
27
28 def test_shift():
29 colors = SingleLinkedList()
30 colors.shift("Cadmium Orange")
31 assert colors.count() == 1
32
33 colors.shift("Carbazole Violet")
