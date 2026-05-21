# Объектно-ориентированный Python, 4-е издание — страница 102

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема тическ ое иссле дова ние 10 1
Ниже представлен пример создания класса Sample, котор ый охватывает все
функции ОДНОГО образца:
class Sample :
def _in it_(
self,
sepal _leng th : float ,
sepa l_widt h: float ,
petal_leng th : float ,
peta l_width : float ,
species : Opt iona l[s tr] = None,
- > No ne :
self . sepal _length = sepal _length
self . sepa l_width = sepa l_width
self .p etal _length = peta l_length
self .p etal _width = peta l_width
self . species = species
self .c lassi fica ti on : Opt ion al[s tr] None
def _repr _( self ) -> str :
if self . species is None :
kno wn_u nk nown "Un knownSamp le"
else :
kno wn_unkno wn "K nownSamp le"
if self .c lassi fication is None :
classi fica tion
else :
classi fic ation = f", {s el f.c lass ificat ion }"
return (
f" { kno wn_unkn own } ( "
f" sepal _leng th={ self . sepal _leng th}, "
f" sepal _width ={ self . sepa l_widt h}, "
f" petal _leng th={ self . petal_leng th}, "
f" petal _wid th={ self .p eta l_wid th}, "
f"sp ecies={ self . species !r }"
f"{c lass ifica tion }"
f" )"
Метод _r epr _( ) отражает довольно сложное внутреннее состо яние объекта
Sample. Состояния объекто в, определяемые наличием (или отсутс твием) вида
и наличием (или отсутст вием) классифик ации, приво дят к небольшим изме­
нениям в поведении этих объек тов. До сих пор любые изменения в поведении
ограничивались методом _rе рr _( ), используемым для отображения текущего
состо яния объекта.
Важно то, что изменения сост ояния действите льно приводят к (не значитель­
ному) изменению поведения.
