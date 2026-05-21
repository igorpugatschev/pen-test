# Объектно-ориентированный Python, 4-е издание — страница 474

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти ческ ое исследование 473
2. Функция вычисляет итоговый результат с количеством правильных значений
из длинной последовательности фактических классифицирова нных образцов.
Это редуц ирующая часть map-reduce.
Для операций соп оставл ения и сокращения Python пре доставляет высоко­
уровневые функци и. Это позво ляет сосре доточиться на деталях сопос тавления
и игнориро вать стандартную часть перебора элементов данных.
В следующем разделе прове дем рефакт оринг класса Hyperpa rameter, чтобы от­
делить от алгоритма классифи катора автономную функцию. Сделаем функцию
классифи катора стратеmей, которую мы предоставляем при создании экземпля­
ра класса Hyperpa rameter . Так будет легче эксперимен тирова ть с некоторыми
альтернативными вариантами. Приступим к рассмотрению трех разных подходов
к рефак торингу класса.
Разберем одно оп реде ление, основанное на внешней функ ции-к лассифика­
торе:
Classi fier = CallaЫe [
[i nt , Distanc eFunc, Tr aininglist, AnySam pl e] , str]
class Hype rpa rame ter( NamedTu pl e) :
k: int
dis tance _fun ction : DistanceFunc
traini ng_d ata : Traininglist
clas sifier : Clas sifier
def classi fy ( self, unkn own : AnySamp le) -> str :
classi fier = self . classi fier
return clas sifier (
sel f.k , self .d is tance _funct ion ,
self . trainin g_data,
unkn own
def test ( self, testing : Test inglis t ) -> int :
classi fier = self . clas sifier
te st_r esults = (
Class ifiedKno wnSamp le(
t. sample,
classi fi er(
) ,
self .k , self .d is tance _function,
self .tr ainin g_da ta, t. sample
for t in testing
pass _fa il = map(
lambda t: (
