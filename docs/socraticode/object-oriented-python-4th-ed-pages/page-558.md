# Объектно-ориентированный Python, 4-е издание — страница 558

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Па тте рн Л егк овес 557
Пр оизойдет серьезная и фата льная ошибка, если приложение будет пы таться
испо льзов ать метод _get item_( ) объекта Messa ge без предвар ительного вы­
полнения set_ fiel ds( ). Мы сделали это очевидным, намеренно вызвав сбой при­
ложе ния. По сле изучения главы 13 вы сможете испо льзовать модульные тесты,
чтобы убедиться, что методы применяются в правильном порядке. До тех пор
мы должны быть уверены в правильности использования метода _g eti tem_ () .
Рассмотрим оставшуюся часть абстрак тного базового класса Messa ge, демон­
стрирующую работу методо в, необхо димых для извлечения изменений из
сообщения:
def get_f ix (s elf) -> Point :
return Point . fr om_by tes (
self . latitu de( ),
self . lat _n_s (),
self . longit ude( ),
sel f. lo n_e_w( )
@abc .a bs tr actmethod
def latitude (s elf) -> byt es :
@abc .a bs tra ctmethod
def la t_n_s (s elf) -> byt es :
@abc .a bs tract method
def longitude (s elf) -> byt es :
@abc . abstr actmethod
def lo n_e_w( self) -> byt es :
Метод get_ fi x( ) делегирует работу четырем отдел ьным методам, каждый из
которых извлекает одно из множества полей сообщения GPS. Также предоставим
подклас сы, подобные следующим:
class GPGLL(M essa ge) :
def latitude (s elf) -> byt es :
return self [1]
def la t_n_s (s elf) - > byt es :
return sel f[2]
def longitu de( self) -> bytes :
return sel f[З]
def lo n_e_w( self) -> byt es :
retur n self [4]
