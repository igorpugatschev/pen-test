# Легкий способ выучить Python 3 еще глубже — страница 105

104 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
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
63
64
65
66
67
68
69
70
71
72
73
74
75
76
return bucket, node
else:
node = node.next
i += 1
# не охватывается конструкциями if и while выше
return bucket, None
def get (self, key, default=None):
'"’"Получает значение в корзине для данного
ключа, или значение по умолчанию.”'”’
bucket, node = self.get_slot(key, default «default)
return node and node.value[1] or node
def set (self, key, value):
’’’’’’Присваивает ключ значению, заменяя любое
существующее значение.”””
bucket, slot = self.get_slot(key)
if slot:
# ключ существует, заменить его
slot.value = (key, value)
else:
# ключ не существует, присоединить, создав
bucket.push((key, value))
def delete(self, key):
»»»»»'Удаляет заданный ключ с карты.”””
bucket = self.get_bucket(key)
node = bucket.begin
while node:
k, v = node.value
if key = k:
bucket.detach_node(node)
break
def list (self):
’’’’’’Выводит то, что есть на карте.”””
bucket_node = self.map.begin
while bucket_node:
slot_node = bucket_node.value.begin
while slot node:
