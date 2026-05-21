# Объектно-ориентированный Python, 4-е издание — страница 127

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

12 6 ГЛАВА 3 Ко гда об ъе кты оди нак овы
... s. num lef t_ calJ s ,
... s. num r1ght_ cal ls,
... s. num _base_ call s)
1 1 1 2
Заметно, что метод call _m e( ) базовог о класса вызыва ется дважды. Это может
привести к ошиб кам, если метод при этом выпо лняет какие-либо действ ия, на­
пример дважды пополняет банковский счет.
Испо льзуя порядок разрешения методов (M RO, Method Re solution Order),
преобразуем ромб в плос кий линейный кортеж. Результаты этого можно про­
анализирова ть в атрибуте __ mro_ класса. Ли нейная версия данног о ромба
представляет собой последовате льность Subclass, Left Subclass, RightSub Class,
BaseClass, object. Здесь важно то, что Subclass определяет Left Subclass перед
RightSub Class, применяя порядок к классам в ромбе.
При множестве нном насл едо вании нужно помнить, что часто ока зыва ется
необходимо вызы вать след ующий метод в по следовател ьности MR O, и это
не обяза тельно метод родительского класса. Функция super () находит имя
в последовател ьности MR O. Действ ительно, функция super( ) изначально была
создана для того, чтобы сделать возможн ыми сложные формы множеств енного
наследования.
Ниже представлен тот же код, написанный с помощью super () . Мы переиме­
новали некоторые классы, добав ив _s , чтобы было понятно, что эта версия кода
испо льзует функцию super ():
class BaseCl ass :
пu m_base _c alls = 0
def call _me( self) :
priп t(" Call iпg method оп Base Cla ss" )
self .п um_base _calls += 1
class Lef tSubc lass _S( BaseCla ss) :
пum_lef t_c alls = 0
def cal l_me (s elf) -> Nопе:
sup er( ). call _me ()
priпt (" Calliп g met hod оп Lef tSubc lass _S" )
self .п um_lef t_c alls += 1
class RightSu bclass _S( Base Class ):
пu m_ri ght_c alls = 0
def cal l_me (s elf) -> Nопе:
supe r( ). call _me ()
priп t (" Call iпg method оп Ri ght Subclass _S")
self .п um_ri ght_c alls += 1
