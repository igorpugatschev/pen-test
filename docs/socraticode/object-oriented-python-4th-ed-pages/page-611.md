# Объектно-ориентированный Python, 4-е издание — страница 611

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

61 О ГЛАВА 1 З Тести рова ние об ъек тно - ориен тирова нных пр о гр а мм
Размер загол овка показан в виде четырехбайтног о фрагмента, но размер, ука­
занный здесь, может ввести в заблуждение. Заго ловок форма льно и официально
опре деляется строкой форма та, испо льзуемой модулем struct вида "> L". В мо­
дуле struct имеется функция calcsize( ), позволяющая вычислить фактичес кую
длину из строки форма та. Вме сто испо льзования литерала 4, полученного из
размера форма та "> L", код будет получать размер, size _by tes, из строки формата
размера, size _fo rmat. Испо льзование одного подходящего источника si ze _fo r­
mat для обеих частей информации соответствует принципу проектирования
«Н е повтор яйс я�.
Ниже приводится буфер примера со встро енным в него сообщением от модуля
ведения журнала log ging. Перва я строка - заго ловок с размером полезног о
информационн ого наполнения в виде четырехбайтного значения. Сле дующие
строки представляют собой данные, отобр анные для сообщения журнала:
b' \x00\ x0 0\x02d ' b' } q\x0 0(X \ x0 4\x00\x00\x00nam eq\x 01 X\x03\x 00\x00\
x00appq \x02X\x 03\x 00\x00\x0 0msgq \x03X\x0b \x 00 \x00\x0 0Fac tor 1al
\x19 X\n\x 00\x00\x0 0Ma inThr eadq \x laX\x0b \x00\ x00 \x00pr ocessN ameq \xlb X\
x0b\x 00\x00\ x00Ma inPro cessq \xlcX\x 07\ x00\x00\ x00 p ro cessq\x ldMcQ u .'
Чтобы прочитать эти сообщ ения, сначала нужно получить байты размера полез­
ной нагрузки. За тем становится возможн ым потреблять следующую полезную
нагрузку. Сокет-сервер, читающий заголовки и полезные данные и записыва­
ющий их в файл, имеет следующий вид:
from �f utu re� import ann otat ions
impor t js on
fr om pathlib import Path
import socke tser ver
from typing import TextIO
import pickle
import struct
class LogD ataCat cher( socke tser ver .B ase RequestHandl er) :
lo g_file : Text IO
count : int = 0
siz e_format = "> L"
si ze_byt es = struct .c alcsiz e( siz e_fo rmat )
def hand le( self ) -> None :
siz e_header _byt es = self . request .r ecv ( LogDa taCa tcher .s ize _by tes )
while size _header _bytes :
payload _s ize = struct .u npack(
LogD ataCa tcher .s i ze_fo rmat , si ze_header _bytes )
payl oad_byt es = self . request .r ecv( paylo ad_s ize [0] )
payload = pickle . loa ds( payload _bytes )
