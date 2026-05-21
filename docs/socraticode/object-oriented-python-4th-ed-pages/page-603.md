# Объектно-ориентированный Python, 4-е издание — страница 603

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

602 ГЛАВА 13 Тести ро вание об ъе ктно - ориен тир ов анн ы х пр о гр а мм
кода подгото вки и очистки. Пр едполагает ся, что методы setup _ class () и te ar­
down_ class () будут методами класса, принимающими один аргум ент, кото рый
представляет данный класс (а ргумента sel f нет, поскольку нет экземпляра;
вместо этого предоставляется класс). Эти методы запускаются средством pytest
не при каждом тестовом прогоне, а при запуске класса.
И наконец, в нашем распоряж ении имеются функции setup _mo dul e( ) и tear ­
down_modul e(), запуска емые pyt est непосредс твенно до и после выпо лнения
всех тестов (в функциях или классах) в данном модуле. Они могут пригодиться
для одноразовой настройки, например для создания сок ета или подключения
к базе данных, которые будут испо льзоваться всеми тестами в модуле. Но здесь
нужно проявить осмотр ительность, пос кольку можно случай но спрово цировать
зависи мость тестов друг от друга, если какое-то из состо яний объекта не будет
должным образом очищено между запуск ами тесто в.
По данному краткому описанию трудно составить представ ление о том, когда
именно вызы ваются эти методы. По этому рассмотрим пример, который четко
иллюстрирует нужные моменты:
from _f utu re_ impor t annotat ions
from typing import Any , CallaЫe
def setu p_mod ule (m od ule : Any ) -> None :
print (f" sett ing up MODU LE {m odule . _na me_} ")
def tea rdow n_module (m od ule : Any ) -> None :
print (f"t earing down MODU LE {mo dule . _nam e_} ")
def tes t_a_fu nctio n() -> None :
prin t(" RUNNING TEST FU NCТION ")
class Base Test :
@c las smethod
def setup _class (c ls : type (" Ba seTest "]) -> None :
print (f" se tt ing up CL ASS {cls ._ name_} ")
@c las smethod
def tea rdo wn_class (c ls : type [" BaseTes t" ]) -> None :
prin t (f" tearing do wn CL ASS {cls ._ name_} \n" )
def setu p_method (s elf, method : CallaЫ e( [], Non e] ) -> None :
print (f" se tt ing up ME THOD {m ethod . _na me_} ")
def tea rd own_method (s elf, met hod : CallaЫ e[ [], Non e] ) -> None :
print (f" tearing down ME THOD {method . _na me_} ")
class TestCla ssl( BaseTest ):
def test _met hod_l (s elf) -> None :
prin t(" RUNNING ME THOD 1-1" )
