# Объектно-ориентированный Python, 4-е издание — страница 447

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

446 ГЛАВА 10 Па тте рн Ите рато р
Рассмотрим следу ющий очень подро бный пример такой реализаци и. В нем
по казаны итерация и два протокола. Позже в этой главе мы разберем несколько
еще более понятных примеров получения подобного результата:
fr om typing import IteraЫe, Iter ator
class Capitalltera Ыe( IteraЫe [s tr] ):
def �init �( self, string : str) -> None :
self .s tring = string
def �iter �( self ) -> Iterator [s tr] :
return Capital lterator (s elf . string)
class Capital lterat or( Iterator [s tr] ):
def �init �( self, string : str) -> None :
self .w ords [w. capitalize () for w in strin g. spli t()]
self . index = 0
def �next �( self) -> st r:
if self . index == len ( self .w or ds) :
raise Stoplteration ()
word = self .w or ds [s elf . index ]
self .i ndex += 1
return word
В при мере опре деляется класс Capita ll teraЫe, задачей которого является
циклический перебор каждого слова в строке и вы вод их с заглавной первой
буквы. Чтобы определить намерение, мы формализовали это, испо льзуя в каче­
стве суперк ласса подсказку типа IteraЫe [ st r]. Больша я часть работы данного
итерируемог о класса делегирована реализации класса Capi tal!ter ator. Один из
способов взаимодействия с итератором выглядит следующим обра зом:
>>> iteraЬle � Capitali teraЫe (' t he quick br own fox ju mps over the lazy dog ' )
>>> iter ator � iter ( iteraЫe )
> » while True :
The
Qu ick
Br own
Fox
Ju mps
Ov er
The
Lazy
Dog
tr y:
print (n ext ( iterator ))
exc ept Stop iter ation :
break
