# Объектно-ориентированный Python, 4-е издание — страница 532

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема тическ ое исследо ва ние 531
Мы определ или протокол Distance, чтобы такие инструменты , как туру, могли
распозна вать класс, выпо лняющий вычисление расстоя ния. Тело функции
Distance () представляет собой токен Python .... В действите льности это три
точки. В книге это не заполнитель, а токен, использу емый для обозначения тел
абстрак тных методо в, как мы уже делали в главе 6.
Расстоя ния манхэттенское и Чебышева похожи. Ма нхэттенское расстоя ние -
это сумма изменений, а расст ояние Чебышева - наибольшее изменение:
class Manhat tan (D istan ce) :
de f dista nce( self, sl : Tra ini ngKno wnSamp le, s2 : AnySamp le) ->
float :
return sum(
ab s(s l. sample .s ample . sepal _length -
s2 . sample . sepa l_l eng th ),
ab s(sl. sample .s ample . sepa l_width -
s2 . sample . sepa l_wid th ),
abs (sl. sample .s ample . peta l_l ength -
s2 . sa mple . peta l_l eng th ),
abs (sl. sample .s ample . peta l_width -
s2 . sample . peta l_wid th ),
]
class Chebyshev (Distanc e) :
def distance( self, sl : Traini ngKno wnSam ple, s2 : AnySamp le) ->
float :
return max (
ab s(s l. sa mple .s ample . sepa l_l ength -
s2 . sample . sepal _leng th ),
ab s(sl. sample .s ample . sepa l_width -
s2 . sa mple . sepal _wid th ),
ab s(sl. sample .s ample . peta l_length -
s2 . samp le . peta l_l eng th ),
ab s(sl. sample .s ample . petal _width -
s2 . sample . peta l_wid th ),
]
Точно так же классифик ация k-ближ ай ших соседей может быть опре делена
как иерархия с альтернати вными страт егиями реализации. Уже упомина лось
в главе 10, что существует несколько способов выпо лнения данного алгоритма.
Мы можем испо льзова ть простой подход с отсортиро ванным спис ком или
более слож ный подход, когда строится очередь кучи или модуль Ьise ct, чтобы
сократить трудозатраты на создание большой коллекции. Сейча с мы не станем
повт орять определения из главы 10 . Все они представляют собой функци и, и это
