# Объектно-ориентированный Python, 4-е издание — страница 200

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

@property
Управ л ение пове де нием об ъе кто в класса 19 9
def content (s elf) -> byt es :
if self ._ content is None :
print (" Ret rieving New Page ... ")
with ur lopen (s elf .u rl ) as res pon se :
self . _content = response .r ead()
return self ._ content
Здесь считы вается содер жимое сайта только один раз, когда self ._ content
имеет начальное значение None. После этого возвращается пос леднее считан­
ное значение для сайта. Тес тирование кода покажет, что страница извлека ется
только ОДИН раз:
import ti me
webpage = WebPag e("h ttp :/ /ccp hillips .n et/ ")
now = ti me . pe rf_count er( )
contentl = webpage .c ontent
fir st _fet ch = ti me . pe rf_counte r( ) - now
now = ti me . pe rf_counte r()
content2 = webpage .c ontent
second _fet ch = ti me . pe rf_c oun te r() - now
as ser t content2 == content l , "P roЫem : Pages were di fferent "
print (f" Initial Request {fir st _fetch :. Sf} ")
print (f" Subse quent Requests {s ec ond_fet ch : .S f} ")
Что в результате?
% python src/c olors .p y
Ret r1ev1ng New Page ...
In1t1al Request 1. 3883G
Subse quent Requests 0. 00001
Получение стр аницы с веб-у зла ccp hilips . net заняло около 1, 388 секунды.
Вторая вы борка - из опера тивной памяти ноутбука - занимает 0,0 1 миллисе­
кунды, то есть 10 микросекунд. Поск ольку это пос ледняя цифра, предположи ­
тельно необходи мо выпо лнить округление, и время может быть вдвое меньше,
возможно всего 5 микросекунд.
По льзовательские геттеры также полезны для атрибуто в, котор ые необходимо
вычислять сразу на основе других атрибутов объекта. Допусти м, нужно вычис­
лить среднее значение для списк а целых чисел:
class Average list (L ist [i nt] ):
@property
def average (s elf ) -> float :
return su m( self) / len ( self)
