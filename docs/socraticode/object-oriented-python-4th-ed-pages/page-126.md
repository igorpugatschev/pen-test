# Объектно-ориентированный Python, 4-е издание — страница 126

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

М ножестве нн ое нас ле дова ние 12 5
def call _me (s elf) -> None :
BaseCla ss .c all _me (s elf)
print (" Calling method on Lef tSubc la ss" )
self .n um_l eft_c alls += 1
class RightSubc la ss( BaseClas s) :
num_ri ght _c alls = 0
def call _me (s elf) -> None :
BaseCla ss . call _me (s elf)
prin t(" Call ing met hod on Righ tSubc lass ")
self . num_ri ght_c alls += 1
class Subcl ass ( Lef tSub class, RightS ubcl ass) :
num_s ub_c alls = 0
def cal l_me (s elf) -> None :
Lef tSubc lass . call _me (s elf)
RightSubc lass . call _me (s elf)
print (" Calling met hod on Subcla ss" )
self .n um_sub _c alls += 1
В приме ре показано, что каждый переопре деленный метод call _m e() напрямую
вызы вает родите льский метод с тем же именем и сообщает, когда вызыва ется
этот метод, отображая информацию на экране. Метод также создает отдельную
переменную экзем пляра, чтобы показать, сколько раз он был вызван.
Строка self.пum_base _ca lls += 1 тре бует не бол ьшого пояснения . Фак ­
тически это self.пum_b ase _ca lls = self.пum_base _ca lls + 1 . Ког да Pythoп
о бра батывае т фор мулу, он начи нае т распоряжаться self.пum_ba se_ca lls
справа от знак а =,сначала и щет перемен ную экз емпляра, а затем пере-
мен ную класса. М ы предоста ви ли переменную класса со значением по
умо лчан ию, ра вным нулю. По сле вычис ления +1 оператор присваив ания
создаст нов ую перемен н ую экзем пляра. Он не будет о бновля ть пере­
менн ую ур овня класса. Каждый раз после первог о вызова будет на йдена
переменная экземпляр а. Это неплохо для кла сса - предоста влять зна че­
ния по умо лчанию для переменных экз емпляр а .
Если мы создадим экземп ляр одного объекта Subclass и вызовем для него метод
call _me () один раз, то получим следующий вывод:
>>> 5 = Subclas s()
>>> s. call _m e( )
Calling method on Base Class
Call ing method on Lef tSubc lass
Calling method on Base Class
Calli ng method on RightS ubclass
Callin g method on Subc lass
»> prin t (
... s. nu m_ sub _ calls,
