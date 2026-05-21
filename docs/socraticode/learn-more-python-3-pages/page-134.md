# Легкий способ выучить Python 3 еще глубже — страница 134

ТРОИЧНЫЕ ДЕРЕВЬЯ ПОИСКА 133
1
2
3
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
tstree.ру
class TSTreeNode(object):
def _init__(self, key, value, low, eq, high):
self.key = key
self.low = low
self.eq = eq
self.high = high
self.value = value
class TSTree(object):
def __init__(self) :
self.root = None
def _get(self, node, keys):
key = keys[0]
if key < node.key:
return self._get(node.low, keys)
elif key == node.key:
if len(keys) > 1:
return self._get(node.eq, keys[l:J)
else:
return node.value
else:
return self._get(node.high, keys)
def get(self, key):
keys = [x for x in key]
return self._get(self.root, keys)
def _set(self, node, keys, value):
next_key = keys[0]
if not node:
# что случится, если вы добавите значение сюда?
node = TSTreeNode(next_key, None, None,
None, None)
if next—key < node.key:
node.low = self._set(node.low, keys, value)
elif next—key == node.key:
