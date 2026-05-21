# Легкий способ выучить Python 3 еще глубже — страница 104

СЛОВАРЬ 103
управлять производительностью. А сейчас реализуйте эту простую
версию, чтобы понять основы структуры данных.
Скопируйте код
Сначала взглянем на код словаря, копию которого вы будете создавать:
dictionary.ру
1 from dllist import DoubleLinkedList
2
3 class Dictionary(object):
4 def __init__(self, num_buckets=256):
5 """Инициализирует карту (Map) с заданным количеством
6 корзин (buckets).'’'’”
7 self.map = DoubleLinkedList()
8 for i in range (0, num_buckets):
9 self.map.push(DoubleLinkedList())
10
11 def hash_key(self, key):
12 С данным ключом это создаст число
13 и преобразует его в индекс корзин на карте.’’"’’
14 return hash(key) % self.map.count()
15
16 def get—bucket(self, key):
17 "”"C данным ключом найти соответствующую корзину.’”’’’
18 bucket—id = self.hash_key(key)
19 return self.map.get(bucket_id)
20
21 def get—slot(self, key, default=None):
22 " ” ”
23 Возвращает либо корзину и узел для слота, либо
24 None, None
25
26 bucket = self.get_bucket(key)
27
28 if bucket:
29 node = bucket.begin
30 i = 0
31
32 while node:
33 if key == node.value[0]:
