# Объектно-ориентированный Python, 4-е издание — страница 180

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

class Tr ainin gData :
def �init �( self, name : str) -> None :
self . name = name
self . uplo aded : datetime . datet ime
se lf . tested : datetime .d atetime
Темат ическ ое иссл едован ие 17 9
self .t raining : list [T rainin gKno wnSamp le] = []
self . testing : list [T esti ngKnownSamp le] []
self .t uning : list [H yperpa rame ter] = []
def load (s elf, raw_d ata_iter : IteraЫe [d ict [s tr, str] ]) -> None :
for n, row in enu mera te( raw_d at a_iter) :
tr y:
if n % 5 == 0:
test = Test ing KnownSam ple . fr om_dict ( row )
self .t esting . ap pend (t est )
else :
train = Traini ngKno wnSam ple . fr om_dic t ( row )
self .tr aining . append (tr ain )
excep t Inval idSam pleErr or as ех :
print ( f" Row {n +l}: {е х}")
return
self . up loaded = datet ime .d atetime . now(t z=d atetime .t imezone .u tc)
Ме тод load () разбива ет образ цы на тесто вые и обуч ающие подмно жества.
Он ожидает итерируемый источник объектов dict [ str, st r], которые создаются
объектом csv . DictReader.
Реа лизованный в приме ре пользова тельский интерфейс заключа ется в том,
чтобы сообщить о первом сбое и возврате. Это может привести к следующему
сообще нию об ошибке:
text Row 2: inval1d spec1es in {' sepa l_length ': 7.9 , 's e pa l_ w1d th ':
3.2 , 'p etal_leng th ' · 4.7 , 'p eta l_ w1d th ': 1.4 , 's pec1es ': 'B ut tercup '}
В данном сообщ ении содержится вся необходи мая информация, но оно может
оказаться не таким поле зным, как ожидалось. Мы, например, надеемся увидеть
сооб щение обо всех сбоях, а не только о перв ом. Метод load () можно реструк­
турирова ть следующим обра зом:
def load (s elf, raw_d ata _iter : IteraЬle [d ict [s tr, str] ]) -> None :
bad_ count = 0
for n, row in en umera te( raw_dat a_iter) :
tr y :
if n % 5 == 0:
test = TestingK nownSam ple .f rom_dic t ( row )
self .t esting . append (t est )
else :
train = Traini ngKno wnSam ple . fr om_dict ( row )
self .tr aining . append (tr ain )
excep t Inval idSam pleE rror as ех :
