# Объектно-ориентированный Python, 4-е издание — страница 687

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

686 ГЛАВА 14 Ко нк ур ентна я обрабо тка да нных
import ran dom
import time
import sys
from typing import IteraЫe
logger = log ging . get logg er(f" app_{os . get pi d()}")
class Sorter (a bc .A BC) :
def _init _( self) -> None :
id = os .g etpid ()
self . logge r = log ging . get logge r(
f" app _{i d} .{ self ._ class _._ name_} ")
@abc .a bs tract method
def sor t (s elf, data : list [f loa t] ) -> list [f loa t] :
За тем опре деляется конкретная реализация абстрактного класса Sorter:
class BogoSort (S orter ):
@stat icm ethod
def is _ordered (d ata : tuple [ float , ... ]) -> bool :
pairs : IteraЫe [T uple [f loat , floa t] ] zip( data, dat a[ l:])
return all (a <= Ь for а, Ь in pairs )
def sort (s elf, data : list [f loat ]) -> list [f loa t] :
self . logger .i nfo( "S or ting %d ", len ( data ))
star t = ti me . perf _counter ()
ordering : Tuple [f loat , ... ] = tuple ( dat a[ :])
per mute _it er = pe rmut ation s(d ata )
steps = 0
while not BogoSort .i s_o rdered (o rderin g) :
ordering next ( permute _it er)
steps += 1
du ration = 1000 * (t ime . per f_count er( ) - star t )
self . logger . in fo (
"S orted %d items in %d ste ps, %.З f ms ",
len ( data ), ste ps, du ration )
return list ( ordering)
Ме тод is _o rde red () класса BogoSort проверяет, правильно ли отсортирова н
сп исок объекто в. Метод sor t () генерирует все пере становки данных в целях
поиска расстан овки, которая бы удовлетворяла ограничению, определяемому
методом is _o rdered () .
Следует заметить, что набор из п значений имеет п! пере становок, что говорит
о вопиющей неэффекти вности данного алгоритма сортиров ки. Из 13 значений
