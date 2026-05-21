# Легкий способ выучить Python 3 еще глубже — страница 85

84 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
5 self.next = nxt
6 self.prev = prev
7
8 def __repr__(self) :
9 nval = self.next and self.next.value or None
10 pval = self.prev and self.prev.value or None
11 return f” [ {self.value}, {repr(nval)}, {repr(pval)}]"
Добавилась лишь строка кода self.prev = prev и, соответственно, из­
менилась функция__repr__ . Класс DoubleLinkedList использует те же
самые операции, что и класс SingleLinkedList, лишь для конца списка
добавилась еще одна переменная:
dllist.ру
1 class DoubleLinkedList(object):
2
3 def _init__(self):
4 self.begin = None
5 self.end = None
Введение в инвариантные условия
Мы осуществляем все те же операции, что и прежде, но теперь добавляем не­
сколько новых соображений:
dllist.ру
1 def push(self, obj):
2 ’’’’’’Присоединяет новое значение к концу списка.’””’
3
4 def pop(self):
5 ’’’’’’Удаляет последний элемент и возвращает его.”””
6
7 def shift(self, obj):
8 ’””’На самом деле, то же, что push.”””
9
10 def unshift(self):
11 "’’’’Удаляет первый элемент (с начала) и возвращает его.'””’
