# Объектно-ориентированный Python, 4-е издание — страница 542

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Па ттерн Адап тер 541
Пр еимущ ество такой схемы заключается в том, что весь код, отображ ающий
сопо ставл яемый ожида емый и фактический интерф ейсы, находится в одном
месте - в классе Adapter. В качестве альтернативы можно было бы поме стить
код в клиента, допо лняя его не относя щимися к делу деталя ми реализа ции.
В такой редакции кода при наличии нескольких типов клиентов пришлось бы
в нескольких местах выпо лнять сложную обработку load_ data () всякий раз, ко­
гда какому-то из этих клиентов потребовался бы доступ к классу Imple mentation.
П риме р ре ал иза ци и паттерна Ада птер
Пр едставьте, что уже существует класс, который прини мает временные метки
строк в форма те ННММSS и вычисляет полезные интервалы с плавающей запятой:
class Тime Since :
""" Expects ti me as six digi ts, по punctuation ." ""
def parse _t ime (s elf, ti me : str) -> tuple [ float , float , floa t] :
return (
float (t ime[ 0:2 ]),
float (ti me[2:4 ] ),
float (ti me [ 4: ]),
def �init �( self, starting _t ime : str) -> None :
self .h r, self .m in, self .s ec = self .p arse _tim e(s tar ti ng_ti me )
self . star t_seconds = ((s el f.h r * 60 ) + self .m in) * 60 + self .s ec
def interv al( self, lo g_ti me : st r) -> float :
lo g_h r, log_ min, lo g_s ec = self . parse _t ime ( log _ti me )
lo g_seconds = (( lo g_h r * 60) + lo g_min ) * 60 + lo g_s ec
return log_ seconds - self . star t_seconds
Этот класс выпо лняет преобра зование строки во временной интервал и уже
прису тствует в прилож ении, имеет модульные тесты и прекрасно работает.
Если вы забудете импо ртиро вать аннотации from _f ut ure _, при попы тке
испо льзова ть tuple [ float , float , float ] в качестве подска зки типа получите
сообщение об ошибке. Не забудьте включить модул ь аннотаций в качестве
первой строки кода. Например, так:
>» ts = TimeS1 nc e( "0 00123 ") # Log star ted at 00 :0 1:2 3
»> ts . 1nter va l( "0 2030 4" )
7301 . 0
>» ts . 1n terva l( "0 304 05" )
10962 . 0
