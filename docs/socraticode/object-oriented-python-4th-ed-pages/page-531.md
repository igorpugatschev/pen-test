# Объектно-ориентированный Python, 4-е издание — страница 531

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

530 ГЛАВА 11 О бщие патте рны про екти рова ния
Диаграмма фокуси руется на нескольких классах.
• Экземпляр класса Hyperpa rameter имеет ссылку на класс Distance. Такое
использование паттерна проектирования Стратегия позво ляет создавать
любое количество подклассов Distance с любым найденным алгоритмом.
• Экзем пляр класса Distance вычис ляет расстоя ние между двумя обра зцами.
Исс ледователи разработали 54 реализации. Мы оста новимс я на нескольких
более простых, описанных в главе 3:
при вычислении расстоя ния Чебышева испо льзуется функция max ( ) для
уменьшения четырех расстояний по каждому измерению до единственного
наибольшег о значения;
при вычислении евклидова расстояния используется функция math. hypot () ;
манхэттенское расст ояние - это сумма всех расстоя ний по четырем из­
мерениям.
• Экземпляр класса Hyperparameter будет иметь ссылку на функцию классифи­
катора k-ближай ших соседе й. При таком использовании паттерна проектиро­
вания Стратегия можно задейство вать любое количество оптим изированных
алгоритмов классифи катора.
• Объект TrainingData содержит исходные объекты Sample, совм естно исполь­
зуемые объектами Hyperpa ramet er.
Ниже приведен пример определения класса Distance, представля ющего общий
протокол для вычисления расстоя ния и реализацию Eucli dean:
from typing import Pr otoc ol
fr om math import hypot
class Dis tance ( Pr ot ocol ):
def dista nce(
self,
sl : Traini ngKno wnSamp le,
s2 : AnySample
-> float :
class Eucli dean ( Distance ):
def dis tance ( self, sl : Tr ainin gK nownSamp le, s2 : AnySamp le) ->
float :
return hypot (
(s l. samp le . sample . sepal _length - s2 . sample . sepal _leng th) **2,
(s l. samp le . sample . sepa l_width - s2 . sample . sepa l_wid th )* *2,
(sl. sample .s ample . peta l_l ength - s2 . sample . petal_leng th) **2,
(sl. sample .s ample . peta l_width - s2 . samp le . peta l_wid th )** 2,
