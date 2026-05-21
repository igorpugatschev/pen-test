# Объектно-ориентированный Python, 4-е издание — страница 458

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

wh ile line and "W ARN" not in lin e :
line = self . inseque nce . read line ()
if not line :
raise Stoplte rat ion
else :
ret urn tuple(
cast (M atch [s t r] ,
self . pattern . mat ch (l ine)
) . groups ()
def extr act _and_parse _2 (
Функ ции - ге не рато ры 457
ful l_log _pat h: Path, warni ng_log_pat h: Path
-> None :
with warning _log_pa th .o pen(" w" ) as ta rget :
writer = csv . wri ter(tar get , del imite r=" \t" )
with ful l_log_pa th . ope n() as sour ce :
filter _reformat = Wa rni ngR eformat (s our ce)
for li ne_groups in filter _reformat :
writ er . writer ow( line _groups )
Здесь оп реде лен форма льный итератор Warni ngReforma t, кот орый вы дает
три кортежа из даты, предупреж дения и сообщ ения. Мы испо льзовали под­
ск азку типа tuple [s tr, ... ], так как она соотве тствует вы ходн ым данным
выр ажения sel f. pattern . match ( line ) . groups (): это неограниченная последо­
вател ьность строк. Итера тор инициализир уется объектом Text IO, имеющим
метод read line () .
Метод _ne xt_ () считы вает информацию из файла, отбрасы вая любые строки,
которые не являются строками WARNIN G. При обнаруж ении строки WARNIN G мы
анализируем ее и возвращаем три кортежа строк.
В опер аторе for функция Extra ct _a nd_ parse _2 () заде йствует экземпляр
класса WarningR efo rmat, что мног ократно будет оцени вать метод _next _( )
для обработки последующей строки WARNING. Когда все строки найдены, класс
WarningReformat вызы вает исключение Stopiteration, чтобы сообщить опера­
тору функции о завершен ии итераци и. По сравнению с другими при мерами
данный код выг лядит довольно некрасиво, но мощно. Теперь, когда у нас есть
класс, можем делать с ним все, что захоти м.
Например, проанализирова ть настоящие генераторы в действ ии.
След ующий пример делает то же самое, что и предыд ущий: он создает объект
с помощью метода _next _( ), который при отсутс твии входных данных вы­
зывает исключение Stopiteration:
from �f utu re� import ann ot ations
import cs v
impor t re
