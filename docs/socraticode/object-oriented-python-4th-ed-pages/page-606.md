# Объектно-ориентированный Python, 4-е издание — страница 606

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Пр ове де ние м одул ьно го те сти р ов ани я с по м о щью pytest 605
def mean (s elf) -> float :
cl ean = list (f ilter (N one , sel f) )
return su m( cl ean ) / len (cl ean )
def medi an( self) -> float :
cl ean = list (f ilt er(N one, sel f) )
if len (cl ean ) % 2:
return cl ean [l en (cl ean ) // 2)
else :
idx = len (c lean ) // 2
return (c lean [ idx) + cl ean [i dx - 1) ) / 2
def mode (s elf) -> list [ floa t] :
fre qs : Def aultD ict [ float , int ] collectio ns . defa ultdict (i nt )
for item in filt er(N one, sel f) :
fre qs [ item ] += 1
mode _freq = max ( freqs .v alue s( ))
modes = [i tem
for item, value in fre qs . items ()
if value == mode_ freq ]
return modes
Данный класс расшир яет встроенный класс lis t путем добавления трех методов
статистической сводки: mean() , median () и mode() . Каждому методу нужен не­
который набор дост упных для использования данных; конфиг урация Statsl ist
с известными данными и будет тестируемой фик стурой.
Для испо льзования фи кстуры с целью создания предварительного условия
GIVEN в тестовую функцию в качестве параметра добавляется имя фи кстуры.
При запуске теста имена параме тров тестовой функции будут расп олагаться
в колле кции фи кстур, и эти функции создания фи кстур будут выпо лняться
в автоматическом режиме.
Например, чтобы пр отестирова ть класс Sta tsLis t, требуется мног ократное
предоставл ение списка допусти мых целых чисел. Соответств ующие тесты можно
написать следующим обра зом:
import pytest
fr om stats import Sta ts list
@pyt est .f ixture
def val id_sta ts () -> Sta tsl ist :
return Sta ts list ([ l, 2, 2, З, З, 4) )
def test _mean (v ali d_s ta ts : Sta tslist) -> None :
as ser t valid _sta ts .m ea n() == 2.5
def test _med ian (v al id_sta ts : Sta tslist) -> None :
as ser t val id_ stats .m edian () 2.5
val id_sta ts . append (4)
as ser t val id_sta ts .m edian () З
