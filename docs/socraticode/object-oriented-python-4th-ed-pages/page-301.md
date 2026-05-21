# Объектно-ориентированный Python, 4-е издание — страница 301

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

300 ГЛА ВА 7 Струк туры да нн ых Python
и он будет работа ть. Так что модульное тес тирование необходи мо даже при
тщател ьно прора ботанных подс казках для типов.
Сле дующий вывод пок азыва ет этот класс в действии при сортировке:
>» mi_0 = Mu ltiite m( "L oc al" , 160728052 2. 6801 2, None , "S ome Fi le" ,
"etc . 0" )
»> mi_l Mu lti ite m( " Remo te" , No ne, "2 02 0-12-0 6Т13 :4 7:5 2.8 49 15 J",
"Ano ther Fil e", "e tc . 1")
>» mi 2 = Mu ltiite m("L ocal ", 15793732 92 . 45299 3, No ne, "Tl 1is Fi le" ,
"e tc . 2" )
»> mi_З = MLJltilte m( " Remo te" , No ne, "2 020 01- 18T13 :4 8:1 2.4 52'J 93" ,
"T hat File" , "e tc . 3")
>» file _l ist = [m i_0 , mi_l , mi_2 , mi_З J
>>> fi le_l ist .s or t()
>>> fr om pprint im port pprint
>>> pprint ( file _ lis t)
[M ultil tem ( data_ source= 'L ocal ', tim estam p=l5793732 92 . 452993 ,
cr eatioп dat e=None , name= 'Тl1 is Fil e', own er _e tc= 'e tc . 2' ),
Mult ii tem( data_ source= 'R emot e ', ti mestamp=N one, cr eati on_ da te= ' 2020 -
01 - 18Тl3 :4 8:1 2.4 52993 ', name= 'T hat Fil e', owne r_e tc= 'e tc . 3'),
Multiite m(d a ta_sourc e= ' Rem ot e ', ti me stamp=N one , cr cat ion _date =' 2020 -
12-0 6T13 :4 7:5 2.8 49 153 ', name= ' Anot her Fil e', owne r_e tc= 'e tc . 1· ),
Mu ltii tem( data_source= 'L ocal ', ti mest amp=l60728 0522 . 68 012,
cr eat ion_ date=N one , name= ' Some Fil e', ow ner et c= 'e tc . 0' )]
Правила сравнения применялись к различным подтипам, которые были объ­
единены в одно определение класса. Однако, если правила будут более сложные,
такие записи могут стать довольно гром оздкими.
Чтобы обеспечить возможность сортир овки, необходимо реализова ть только
метод _1 t_( ). Для полноты класс может также реализовать аналогичные ме­
тоды _g t_( ), _e q_ ( ), _ne_ ( ), _ge_ ( ) и _le_( ). Это гарантирует, что все
операторы <, >, ==, ! =, >= и< = также будут работать правильно. Python позволяет
нам получить все это даро м, реализовав только методы _lt _( ) и _eq _( )
и применив затем декрратор клacca @total _ ordering для того, чтобы обеспечить
работу всег о остального:
from functools impor t to tal _ordering
from dat aclass es impor t da taclass
from typing import Option al, cast
import datet ime
@tot al_ ordering
@d ata class ( frozen=Tr ue)
class Multi ltem :
data _sou rce : str
ti mestamp : Optiona l[f loat ]
