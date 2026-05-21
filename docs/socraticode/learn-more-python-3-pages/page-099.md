# Легкий способ выучить Python 3 еще глубже — страница 99

98 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
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
while node:
node = node.next
count += 1
return count
def merge_sort(numbers):
numbers.begin = merge_node(numbers.begin)
# ужасный способ получить конец
node = numbers.begin
while node.next:
node = node.next
numbers.end = node
def merge_node(start):
"""Сортирует список чисел путем сортировки слиянием."""
if start.next == None:
return start
mid = count(start) // 2
# проход до середины
scanner = start
for i in range(0, mid-1):
scanner = scanner.next
# серединный узел сразу после точки прохода
mid_node = scanner.next
# выход в средней точке
scanner.next = None
mid_node.prev = None
merged_left = merge_node(start)
merged_right = merge_node(mid_node)
return merge(merged_left, merged_right)
def merge(left, right):
