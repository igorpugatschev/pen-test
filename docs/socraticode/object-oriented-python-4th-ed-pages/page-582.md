# Объектно-ориентированный Python, 4-е издание — страница 582

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

self . resul ts : list [t uple [ str, ... ] ]
self .q uer y : str
self .h eader : lis t [s tr]
def connect (s elf) -> None :
Па п ерн Ш аб ло нн ы й ме тод 581
self . conn = sqli teЗ . connect (s elf .d b_name )
def constru ct _quer y( self) -> None :
raise Not imple mented Er ror ("c on struct _quer y not implemented ")
def do_ quer y (s elf) -> None :
results = self .c onn . execute (s elf .q uer y)
self . results = results . fetchall ()
def outp ut_c ontext (s elf) -> Cont extMa nag er[T extI O] :
self .t ar get_ file = sys . stdout
return cast ( Contex tMa nag er[ TextI O] , contex tlib .n ullc ontext ())
def outp ut_r esul ts( self ) -> None :
writer = csv . writer (s elf . ta rget_ file)
writ er . writer ow( self . heade r)
writ er . write rows (s elf . resul ts)
def proces s_format (s elf) -> None :
self . connect ( )
self . construct _query ()
self . do_ quer y ( )
with self . outp ut_c ontext ():
self . outp ut_re sul ts ()
Это своего рода абстрак тный класс. В данном случае не испо льзуется формаль­
ный абстрак тный базо вый класс. Вместо него два метода, которые необходи мо
обновить, демонстрир уют два разных подхода к предоставле нию абстракт ного
опре деления.
• Ме тод construct _q uer y () должен быть переоп ределе н. Ба зовый класс
оп реде ления метода вызы вает исключение Not imple mentedError. Такова
альтернатива созданию абстрактного интерфейса в Python. Вызов Notimple­
mentedError помог ает разработч ику понять, что класс предназначен для под­
класса и что эти методы переоп ределены. По добные вык ладки могут быть
опис аны как �о бход действующих правил в абстрак тном базовом классе без
явного указания» в определении класса и без использования декораторов
@abc .a bstracm ethod.
• Ме тод outpu t_c ont ext () может быть переоп реде лен. Существует реа­
лизация по умолчан ию, которая устанавли вает переменную экзем пляра
sel f. ta rget_ file и возвращает значение контекста. По умолчанию в качестве
выходного файла используется sys . stdout и менеджер нулевого контекста.
