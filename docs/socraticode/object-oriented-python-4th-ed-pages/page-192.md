# Объектно-ориентированный Python, 4-е издание — страница 192

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Управ ле ние пове де нием объе кто в класса 19 1
self ._ rgb_ value = rgb_ value
self ._ name = name
def set_name (s elf, name : str) -> None :
self ._ name = name
def get_name (s elf) -> str :
return self ._ name
def se t_rgb _va lue ( self, rgb_ value : int) -> None :
self ._ rgb_ value = rgb_ value
def get_rgb _va lue ( self ) -> int :
return self ._ rgb _value
Пе ред пере менными экземпляра ставится сим вол подчерки вания, чтобы при
взгляде на код можно было сразу предположить, что они являются приватными
(в других язык ах переменные экзем пляра обязател ьно должны быть прива тны­
ми). Затем методы get и se t обеспечи вают доступ к каждой пере менной:
»> с = Col or( 0x ff0000 , "b right re d")
» > с. get_name ()
'b righ t red '
»> с. se t_name ( "r ed")
» > с. get_name ()
'r ed '
При веденный выше пример не так удобочитаем, как версия с прямым дост упом,
а именно она принята в языке Python в типичном случае:
class Color _Py :
def �in it�( self, rgb_ value : int , name : st r) -> None :
self .r gb_va lue rgb _value
self . name = name
Данный класс работает следу ющим обра зом:
Итак, чем же так хорош синтаксис, основанный на методах? Почему так настаи­
вают на собл юдении его принципов?
Идея использования сеттеров и геттеров кажется полезной для инкапсуляции опре­
делений классов. Некоторые инструменты на основе J ava могут автоматически ге­
нерировать все геттеры и сеттеры, делая их почти невидимыми. Автоматизировать
