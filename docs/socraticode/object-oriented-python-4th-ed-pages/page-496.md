# Объектно-ориентированный Python, 4-е издание — страница 496

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

П ап ер н Де коратор 495
раз. Теперь в другом месте прило жения никакие изменения больше не требуют­
ся. Ин огда улучшение от этого небольш ого нюанса может быть значительным.
Конечно, можно точно настроить размер кэша на основе данных и количества
выполняемых вычис лений.
Испо льзование подобных параметризован ных декораторов похоже на топтание
на одном месте. Сна чала мы настраиваем декоратор с парамет ром, затем приме­
няем этот настроенный декора тор к определению функци и. Эти два отдельных
ша га аналоги чны действ иям, когда вызываемые объекты инициализиру ются
с помощью мeтoдa _i nit_( ) и могут быть вызваны в качестве функции с по­
мощью метода _c all _( ).
Рассмотрим пример настраиваемого декоратора логирования NamedLogger:
class Named logg er :
de f _i nit _( self, lo gger _name : str) -> None :
self . logger = loggi ng . get logge r( logge r_name )
def _c all _(
self,
function : CallaЫe [ ... , Any ]
-> CallaЫe [ ... , Any] :
@wraps (f unct ion )
def wrap ped_fu nct ion (* ar gs : Any , **k wargs : Any ) -> Any :
star t = ti me . pe rf_c oun te r( )
tr y:
result = funct ion (* ar gs , **k wargs )
µs = (t ime . pe rf_c oun ter( ) - star t ) * 1_000_000
self . logger .i nfo (
f" {funct ion ._ name_} , { µs :. lf}µ s")
return result
excep t Exce ption as ех :
µs = (t ime . pe rf_c oun te r( ) - star t ) * 1_000_000
self .l ogg er . err or(
f" {e x}, {funct ion ._ name_} , { µs :. lf}µ s")
raise
return wrapp ed_function
Ме тод _i nit_( ) гарантирует, что для создания декоратора мы можем напи­
сать код вроде NamedLogger( "l og4" ). Этот декоратор позаботится о том, чтобы
следующая функция испо льзовала определенный регистратор.
Метод _с аll _( ) следует уже известному паттерну. Опр еделяем новую функ­
цию wrap_fu nction(), которая делает всю работу, и возвращаем новую функцию:
>» (a1Named logg er( "l og 4" )
.. . def test4 (m ed1an fl oat , sample : fl oat ) -> float :
. . . re turn abs ( sam ple-m ed 1an )
