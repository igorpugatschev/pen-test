# Объектно-ориентированный Python, 4-е издание — страница 512

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

class Plus (A djus tment ):
def apply (s elf, dice : "D ic e" ) -> None :
dice .m odifier += self .a mount
class Mi nus (A djus tment ):
def apply (s elf, dice : "Dic e") -> None :
dice . mod ifier -= self .a mount
Па ттерн Кома нда 51 1
Эк земпляр класса Roll( ) устанавливает значения игральных костей и атрибут
модифи катора экземпляра Dice. Другие объекты Adjust ment либо удаляют не­
которые кубики, либо изменяют модифи катор. Опе рации зависят от того, какие
кости сортируются . Это позволяет с помощью операций среза легко отбрасы вать
худшее или сохранять лучшее. Поск ольку каждая корректировка является своего
рода командой, в общее состоя ние брош енных костей вносятся коррек тивы.
Недостаю щая часть переводит строковое вы раже ние в после дова тел ьность
объектов Adju stment. Здесь это сделано методом @c lass класса Dice, что по­
зволяет испо льзовать Dice . from_t ext () для создания нового экземпляра Dice.
Он также предоставляет подкласс в качестве перв ого значения параметра, cls,
гарантируя, что каждый подкласс создает надлежащие экземпляры самого себя,
а не родител ьског о класса. Например:
@c las smethod
def fr om_text (c ls, dice _text : str) -> "Dic e" :
dice _pattern = re . co mpi le(
r" ( ?P <n> \ d*)d( ?P<d> \ d+ )( ?P <a> [ dk+-]\ d+ )*")
adju stment _pattern = re . comp il e(r "( [dk + -])( \ d+) ")
adj_ class : dic t[s tr, Type [A dju stment ]] = {
}
"d" : Drop ,
"k" : Кеер ,
"+ ": Pl us,
"-" : Mi nus,
if (d ice _mat ch := dice _patt ern .m at ch(di ce_t ext )) is No ne :
raise Va lueErr or (f"Er ror in {dice _text !r }")
n = in t( di ce_match .g rou p( "n" )) if dice _mat ch . grou p("n") else 1
d = int (d ice _match .g rou p( "d" ))
adju stment _mat ches = adjust ment_ pattern .f indi ter(
dice _matc h. grou p( "a" ) or "")
adju stment s = [
adj_ class [a. grou p(l) ](i nt (a. grou p(2) ))
for а in adj ustme nt_matches
return cls (n, d, *adj us tmen ts)
Сна чала применяется dice_p attern, а результат присваива ется переменной dice_
match. Если результатом является объект None, паттерн не совпал и нельзя сделать
ничего большего, кроме как вызвать исключение ValueErr or. Adjustment_ pattern
