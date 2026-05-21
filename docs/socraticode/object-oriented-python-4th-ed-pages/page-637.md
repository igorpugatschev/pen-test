# Объектно-ориентированный Python, 4-е издание — страница 637

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

636 ГЛАВА 13 Тести рован и е о бъе ктно - ор и е нти ров анн ых п ро гра мм
unkno wn_row = {
"s epal _leng th" : 7.9 ,
"s epal _wid th" : 3.2 ,
"p etal _leng th" : 4.7 ,
"p eta l_wid th" : 1. 4,
}
u Unk nown Sam pl e{* *unkn own_row )
return k, u
Здесь созданы объекты Traini ngKnownSample и UnknownSample, котор ыми можно
воспо льзова ться в последу ющих тестах. Это определение фи кстуры зависит от
ряда важных подсказок и опре делений:
Fr om �f uture � import anno tations
import pytest
fr om mod el import Trainin gKno wnSam ple, Unkn ownSample
fr om model import CD, ED, MD, SD
fr om typing import Tuple, Type dDict
Kno wn_Unk nown = Tuple [T raini ngKnow nSam ple, Unk nown Samp le ]
class Ro w(T ypedD ic t) :
species : str
sepa l_leng th : float
sepa l_widt h: float
peta l_l eng th : float
peta l_widt h: float
Вычисление расстоя ния может быть предоста влено шагу WHEN, а окончательное
срав нение в инструкции as ser t - шаг у THEN. Для сравнения нужно прибегнуть
к объекту approx, поскольку работа ведется со значениями с плавающей точкой,
а слишком точные сравнения редко бы вают удачными.
В рассма триваемом пр иложении количество знаков после запятой в тестовом
сценарии представляется чрезмер ным. Все цифры оста влены на своих местах,
чтобы значения соответствовали значениям по умолчан ию, испо льзуемым
approx. Это приводит к относительной погрешно сти 1 х 1 О-6, или в обозначениях
Python le -6. Остальна я часть тестового сценария имеет следующий вид:
def test _ed (k nown_u nkno wn_example _l S: Kno wn_Unk nown ) -> None :
k, u = kno wn_unkno wn_example _l S
as ser t ED (). dis tan ce{k, u) == pytest .a pp rox (4. 501110 97 )
При влекает то, что все выг лядит кратко и по существу. При задании двух об­
разцов результат измерения расстоя ния должен соответствовать вычисленному
вручную или же с помощью sympy.
В тесто вом сценарии нуждается каждый из классов расстоя ний. Вот два других
вычисления расстоя ний. Ожида емые результаты получены, как это и делалось
ранее, при проверке формулы и подстановке конкретных значений:
