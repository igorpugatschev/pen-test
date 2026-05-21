# Объектно-ориентированный Python, 4-е издание — страница 188

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

self .x = х
self .y = у
def distance( self, other : "P oin t" ) -> float :
Рабо та с объек та м и 18 7
return hypot (s el f.x - oth er .x , self .y - ot her .y)
class Polygon :
def �init �( self) -> None :
self . ver tices : List [P oint ] = []
def ad d_po int (s elf, point : Point ) -> None :
self . ver tices .a ppend (( poin t))
def perim eter( self) -> float :
pairs = zip(
self . ver tices, self . ver tices [l :] + self . ver tices [: l] )
return su m(p l . dis tan ce(p 2) for pl, р2 in pairs )
Кажется, полу чивши йся код почти в два раза больше, чем в предыдущей
верс ии, хотя очевидно, что метод add_po int совсем не обяза телен. Да, можно
применять _ve rt ices, чтобы не испо льзова ть доступ к атрибуту, но знак под­
черкивани я _ в именах переменных, кажется, не решает проб лему.
Теперь, чтобы немного лучше понять различия между двумя классам и, сравним
два испо льзуемых API. Пр оанализируем, как можно вычислить пери метр ква­
драта с помощью объек тно-ори ентированного кода:
>>> squar e = Polygon ()
>>> squar e . add _p oint (P oint (l, 1))
>>> squar e . ad d_p oin t (P oint (l,2) )
>>> squar e . ad d_p oin t(P oin t(2, 2) )
>>> squar e . add _p oint ( Point (2 ,1))
>>> squar e . perim et er( )
4.0
На ваш взгляд, это слишк ом просто? Но давайте срав ним его с кодом, основан­
ным на функциях:
»> square = [( 1,1), (1, 2), (2, 2) , (2 ,1)] '
>>> per 1met er (s quar e )
4.0
А теперь задумаемся: может быть, объек тно-ориентирован ный API не такой уж
комп актный! Пер вая переработанная версия кода, без подска зок и определений
классов, является самой коротк ой. Но! Отк уда при работе с ней мы узнаем, что
должен представлять собой список корте жей? Вспомним ли мы в нужное вре­
мя, какой объект должны передать в функцию per imeter? Выво д: необходима
документация, объясняющая, как именно следует использова ть первый набор
функций.
