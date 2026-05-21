# Объектно-ориентированный Python, 4-е издание — страница 505

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

50 4 ГЛ АВА 11 О бщие па ттерны про екти ро ва ния
Рассмотрим нашу первую конкретную стратегию. Это полный алгоритм, который
отобра жает изображения в виде мозаики:
class Ti ledStrateg y( Fill Algorith m) :
def make_bac kground (
self,
img_file : Path,
des ktop _s ize : Size
-> Image :
in_img = Image .o pen ( img_file)
out_img = Image .n ew (" RGB ", desk top _size)
num_tiles = [
о // i + 1 for о , i in zip( out_img .s ize, in_img. siz e)]
for х in range (nu m_tiles [0 ]):
for у in range (nu m_tiles [l ]):
out_img .p aste(
in_img,
(
) ,
return out_img
in_img .s iz e[0] * х,
in_img. siz e[l] * у ,
in_img .s iz e[0] * (х + 1),
in_img .s ize [l ] * ( у + 1),
Это работает путем деления высоты и ширины резул ьтирующ его изобра­
жения на вы соту и ширину входного изобра жения . Пос ледова тел ьность
num_ tiles - способ вы полнения одних и тех же вычислений для ширины
и высоты. Здесь мы задействовали два кортежа, вычис ляемые с помощью
пр едста вления спис ка, чтобы быть уверен ными, что ширина и вы сота об­
рабатываются одинаково.
Ниже приведен алгоритм, котор ый центрирует изображение без его повторног о
масшта бирован ия:
class Cente redSt rat egy (F ill Alg orith m) :
def make _ba ck ground (
self,
img_file : Path,
des ktop _siz e : Size
-> Image :
in_img = Image .o pen ( img_file)
out _img = Image .n ew ( "R GB", des ktop _size)
le ft = (o ut_img .s ize [0] - in_img. siz e[0] ) // 2
top = (o ut_img .s iz e[l] - in_img. siz e[l] ) // 2
out_img .p aste(
in_img ,
(l eft , top, le ft + in_img. siz e[0] , top + in_im g. siz e[l] ),
return out_img
