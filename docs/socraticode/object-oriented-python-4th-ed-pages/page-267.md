# Объектно-ориентированный Python, 4-е издание — страница 267

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

266 ГЛАВА 6 Абст рактн ые класс ы и перегрузка операто ров
Теперь приш ло время расширить это, чтобы создать конкре тный подкласс,
оберты вающий две внутренние коллекции. Разобьем код на две части : сначала
созда дим коллек ции, а затем созда дим свойс тва для отображе ния значений
коллекций:
class Counti ngDea lin gPartition (D eali ngPartition ):
def _init_(
self,
items : Opt io nal [ IteraЫe [ SampleDict ]],
* '
trainin g_s ubse t : Tuple [i nt , int ] = (8, 10 },
-> None :
self .t rain ing _s ubse t = traini ng_subse t
self . counter = 0
self ._ trainin g : List [T rainin gK nownSamp le ] = []
self ._ testing : List [ Testi ngK nown Sam ple] []
if items :
self . extend ( items )
def extend (s elf, items : Iter aЫe[ SampleDict ]) -> No ne :
for item in items :
self . append ( item )
def append (s elf, item : SampleDi ct ) -> None :
n, d = self .t rainin g_s ubse t
if self .c ounter % d < n:
self ._ training .a ppend ( Tr aini ngKno wnSample (**i te m) )
else :
self ._ testing .a ppend (T esti ngKno wnSample (* *i te m) )
self .c ounter += 1
Здесь опре деляется инициализатор, устанавл ивающий начальное состоя ние
двух пустых коллекций. Затем создаются коллекции из исходного итерируемог о
объекта с применением метода ext end ( ) .
Метод extend () использует append () для включения экземпляра SampleDict
либо в тесто вое, либо в обучающее подмножество. На самом деле всю работу
выполняет метод append () . Он подсчитыва ет элементы и принимает решение
на основе некоторой арифметики деления по модулю.
Учебное подмно жество описы вается как дробь. Выше уже говорилось, что под­
множество определ ено как кортеж (8, 1 О) с комме нтарием, предпо лагающим,
что это означает 8/ 10 , или 80 %, обучения, а остальное для тестирован ия. Для
заданного значения счетчика с, если с< 8 (mod 10) , мы отнесем это к обучению,
а если с� 8 (тоd 10) - к тести рованию.
Рассмотрим остав шие ся два метода, служащие для предоставл ения значений
двух внутренних объектов сп иска:
@property
def training (s elf } -> List [ Trainin gKno wnSample ]:
ret urn self ._ tr aining
