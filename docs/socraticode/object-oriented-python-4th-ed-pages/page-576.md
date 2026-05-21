# Объектно-ориентированный Python, 4-е издание — страница 576

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

self . chil dr en[c] . remove ()
if self . pa rent :
del self . pa rent .c hildr en [s elf . name ]
class File(N od e) :
def �re pr�( self) -> st r:
ret urn f"Fil e({s elf . name!r })"
Па п ерн Ком понов щи к 575
def cop y( self, new_fold er : "F olde r" ) -> None :
new_fo ld er . add_ child (F ile( self .n ame) )
def remove (s elf) -> None :
if self .p ar ent :
del self . pa rent . chil dr en [s elf . name ]
При добавлении дочернего элемента в Folder происходит следующее. Во-пе рвых,
мы указы ваем ему, кто его новый родитель. Это гарантирует, что у каждого Node
(к роме экземпляра Folder) будет родител ь. Во-в торых, новый Node помеща ется
в коллекцию дочерних элементов папки, если он еще не существует.
При копировании объектов Folder нам необхо димо убедиться, что при этом
копир уются все его дочерние объек ты. Ведь каждый дочерний элемент, в свою
очередь, может быть еще одним объектом Folder, содерж ащим дочерние эле­
менты. Такой реку рсивный обход элементов подразу мевает делегиров ание
операции сор у () каждой подпапке внутри экземп ляра Folder. С другой сторо ны,
реал изация объекта File гораздо проще.
Рекур сивный дизайн для удаления аналогичен рекур сивному копирован ию.
Эк земп ляр Folder должен сначала удалить все дочерние элементы. Это вклю­
чает удаление экземпляров подпапок. С другой стор оны, объект Fil e можно
удалить напрямую.
Итак, пока все до статоч но легко. Пр оанализируем, правильно ли работает
описан ная состав ная файло вая иерархия, обратимся для этого к следующему
фрагменту кода:
>» tr 'cc - F older '("T r· c c" )
>» tr ·cc .i нlcl chil d(Folc k r(" src" ))
FoJder( 's r'c ', {})
»> tr ee.c hiJd re n[ "sr c" ] .a dc1 chil d( File( "exl .p y" ))
Fil e( 'e x l.p y' )
> » tr ·ee . ac ld c�1i ld( Fo 1 сlсг ( "sr c"))
Folc1Pr '( 'sr· c', {'e xl .p y' : Fi l c ( ' exl . p y' ) } )
>» tr ee .c hi ldre n["s rc" J .a dd _c hil d (Fi le( "testl .p y" ))
F i lc' ( 't cs t 1. ру ')
>» tr ec
Folde r( 'T re e' , {'s rc ' : Foldc r( 's rc ', {' e xl .p y' : Fi le ( 'e x l.p y'), 't estl .
ру ' : Fi le( 't es tl .p y' )})})
