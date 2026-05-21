# Объектно-ориентированный Python, 4-е издание — страница 115

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

114 ГЛ АВА З Ко гда об ъек ты одинак ов ы
в класс Contact добав ить метод поиск а, но на самом деле он уже принадлежит
самому списку.
В примере ниже показано, как организуется поиск с использованием наследова­
ния от встроенного типа. Здесь применяется тип lis t. С помощью синтаксиса
lis t [ "Contact "] укажем туру, что список состоит только из экземпляров класса
Contact. Чтобы этот синтаксис работал в Python 3.9, необходимо импо ртирова ть
модуль annotations из пакета _fut ure_, как показано ниже:
fr om _f utu re_ import ann ot ations
class Contact list (l is t[" Contac t"] ):
def sear ch( self, name : str) -> list [ "C ontac t"] :
mat ching _con tacts : lis t[" Contact "] = []
for contact in self :
if name in contact .n ame :
mat chi ng_c ontac ts . append (c onta ct)
return mat chi ng_con tacts
class Cont act :
all _cont acts = Contac tl is t()
def _init _( self, name : str, email : str) -> None :
self . name = name
self . email = email
Contact .a ll _co ntac ts . append (s elf)
def _re pr_( self) -> str :
return (
f"{ sel f ._ class _._ name_} ( "
f"{s elf . name !r }, {s elf . email !r }" f" )"
Вме сто создания универсального списка в качестве переменной класса мы соз­
даем новый класс Contact l ist, который расшир яет встроенный тип данных lis t.
Затем создадим этот подкласс как список all _con tacts. Про тестируем новую
функцию поиска следующим обра зом:
>» cl = Contact (" J ohn А" , "jo hna @e xamp le. ne t")
>» с2 = Contact (" John В", "j ohnb @slo op .n et ")
»> сЗ = Con tact (" J enna С", "c utty@s ar k.i o" )
>>> [c. na me for с in Contact .a ll _c ontac ts . search ('J oh n')]
[ 'J ohn А' , 'J ohn В' ]
Итак, уже имеется два спо соба создания универсальных объектов списка. А с ис­
пользованием подсказок типов можем прийти еще к одному способу, отличному
от создания реальных экземпляров спи ска.
