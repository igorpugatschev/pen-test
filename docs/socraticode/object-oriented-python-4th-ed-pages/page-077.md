# Объектно-ориентированный Python, 4-е издание — страница 77

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

76 ГЛАВА 2 О бъекты в Python
и подтвердить правильно сть приве денных примеров. Все примеры в книге про­
верены с помощью инструмента doctest.
Ис пользование строк документации мы рассмотрим на примере задокум енти­
рованного класса Point:
class Point :
Represents а point in two-dimensi onal geomet ric coord inates
>>> р_0 = Point ()
>>> p_l = Point (З, 4)
>>> p_0. calc ul ate_ dis tance (p _l )
5.0
def �init �( self, х: float = 0, у: float = 0) -> None :
Initialize the posit ion of а new point . The х and у
coord inates сап Ье spec ified . If the y are not , the
point def aults to the orig in .
:p ar am х: float x-coordinate
:p ar am у: float x-coordinate
self . move (x, у)
def move (s elf, х: flo at, у: float ) -> None :
Move the point to а new location in 2D space .
:p ar am х: float x-coordinate
:p ar am у: float x-coord in ate
self .x = х
self .y = у
def reset (s elf) -> None :
Rese t the point back to the geom etric origin : 0, 0
self . move (0, 0)
def calcula te_distance( self, oth er : "P oin t") -> float :
Calcu late the Eucli dean di stance fr om this point
to а second point pas sed as а pa rameter .
:p aram ot her : Point instance
:r eturn : float distance
return math . hypo t(s elf .x - other .x , self .y - ot her .y)
