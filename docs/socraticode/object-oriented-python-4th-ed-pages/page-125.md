# Объектно-ориентированный Python, 4-е издание — страница 125

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

12 4 ГЛАВА З Ко гда об ъе кты оди нак овы
Базовый класс следует вызывать только один раз. Но когда именно? Какой должна
быть очередность: вызывать класс Friend, затем класс Contact, затем Object, а затем
Addres sHolder? Или Friend, затем Contact, затем AddressHolder, а затем Object?
Чтобы разъяснить эту проблему в деталях, рассмо трим еще один пример. Им е­
ется базо вый класс BaseC lass, содержащ ий метод call _me ( ) . Два подкласса,
Left Subclass и RightSu bclass, расширяют класс BaseCla ss, и каждый из них
переоп ределяет метод call _m e( ) в разных реализациях.
Затем друzой подкласс расшир яет оба этих класса, испо льзуя множеств енное
наследование, с четвертой, отдельной реализацией метода call _me ( ). Такая
ситуация в ООП называ ется ромбовидным наследованием (рис. 3.2).
BaseClass
+call_me()
LeftSubc lass Righ tSu bclass
+call_me( ) +call_me( )
SubC lass
+call_me( )
Рис. 3.2. Ромбов ид ное наследован ие
Пре образуем эту диаграмму в код:
class BaseCl ass :
num_ba se_c alls = 0
def cal l_me (s elf) -> None :
print (" Cal lin g method on BaseCl ass ")
self . num_base _c alls += 1
class Lef tSubclas s(B aseClass ):
num_l eft_c alls = 0
