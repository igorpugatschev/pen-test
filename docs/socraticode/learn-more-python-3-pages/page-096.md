# Легкий способ выучить Python 3 еще глубже — страница 96

ПУЗЫРЬКОВАЯ И БЫСТРАЯ СОРТИРОВКА, СОРТИРОВКА СЛИЯНИЕМ 95
Изучаем пузырьковую сортировку
Теперь уделите время изучению этого переведенного мной кода Python. Что­
бы получить об этом более глубокое представление, посмотрите видео, где
я осуществляю перевод в реальном времени. Также схематически изобрази­
те такую сортировку списков различных типов (уже отсортированных, с эле­
ментами в случайном порядке, дубликатов и так далее). Когда у вас появится
понимание того, как я это сделал, изучите фреймворк pytest и алгоритм
сортировки слиянием:
test sorting.ру
1 import sorting
2 from dllist import DoubleLinkedList
3 from random import randint
4
5 max numbers = 30
6
7 def random_list(count):
8 numbers = DoubleLinkedList()
9 for i in range(count, 0, -1):
10 numbers.shift(randint(0, 10000))
11 return numbers
12
13
14 def is_sorted(numbers):
15 node = numbers.begin
16 while node and node.next:
17 if node.value > node.next.value:
18 return False
19 else:
20 node = node.next
21
22 return True
23
24
25 def test_bubble_sort():
26 numbers = random_list(max_numbers)
27
28 sorting.bubble_sort(numbers)
29
30 assert is_sorted(numbers)
31
