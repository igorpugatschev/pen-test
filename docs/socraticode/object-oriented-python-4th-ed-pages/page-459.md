# Объектно-ориентированный Python, 4-е издание — страница 459

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

458 ГЛАВА 10 Па тте рн Ите рат ор
from pathlib import Path
fr om typing import Match, cast, Iterat or, IteraЫe
def warnin gs_fi lt er(
sour ce : IteraЫe [s tr]
-> Iterat or [ tuple [s tr, ... ] ] :
pattern = re . com pile (
r" ( \w\w\w \d \ d, \d \ d \ d \ d \d \d: \d \ d: \ d \ d) ( \w+ ) ( .* ) " )
for line in so urce :
if "W ARN " in line :
yield tuple (
cast (M atch [s tr] , pattern .m at ch( lin e) ). grou ps ())
def extr act _and_parse _З (
ful l_log_pat h: Path, warni ng_l og_path : Path
-> None :
with warning _log_pa th . ope n(" w" ) as ta rget :
writer = csv . write r(t ar get , delimi ter= " \t")
with ful l_log _pa th . ope n() as inf ile :
filter = warni ngs_ filter (i nfile )
for li ne_groups in filter :
writ er . writero w( line _grou ps)
Оп ератор yield функции warni ng_ filte rs () является ключом к генерато рам.
Когда Python в функции обнаруживает оператор yield, он берет эту функцию
и оборач ивает ее в объект, следующий за протоколом Iterator, мало чем отлича­
ющимся от класса, определенного в предыдущем примере. Можно предположить,
что оператор yield - это оператор return, который также возвра щает строку.
Однако, в отличие от реакции на return, функция только приос танавлива ется
(п ере водится в состоя ние ожидан ия). При повторном вызове (по средством
next()) функция начинает выпо лняться с того места, на котором остановилась
(со строки после оператора yield), а не с начала. В этом примере после опе ра­
тора yield нет стро ки, поэтому выпо лняется пере ход к следу ющей итерации
оператора for. Поск ольку оператор yield находится внутри оп ератора if, он
выдает только те стро ки, которые содержат WARNIN G.
Хотя это выглядит как функция, перебира ющая строки, в действ ительности она
создает объект сп ециального типа, объект-генератор:
>>> print (w arnin gs_ filter ([]))
<g enerator object wa rni ngs_ filter at 0 хЫ28сбЬс >
Все, что делает функция, - создает и возвр ащает объект -генератор. В примере
выше был предоставл ен пустой список и создан генератор. Об ъект- генератор
имеет методы _i tеr _( ) и _next_( ), точно такие же, как в предыдущем при­
мере (ис пользование встроенной функции dir( ) продемонстрирует, что еще
