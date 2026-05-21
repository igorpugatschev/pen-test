# Объектно-ориентированный Python, 4-е издание — страница 651

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

650 ГЛАВА 14 Ко н куре нтн а я обрабо тка да нных
Теорети чески разработч ик вполне способен управлять всеми этими переклю­
чениями между разными действиями в рамках самой создав аемой программы,
но сделать это долж ным образом практически нереально. Лучше положиться
на возможности языка Python и опера ционной сист емы, которые берут на себя
самую сложную часть переключений, оставляя на долю программистов создание
объектов, которые как бы действуют одновременно, но независимо друг от друга.
Именно такие объекты и назыв аются потоками. Рассмо трим простой пример,
начиная, как показано в следующем классе, с основного определения потоковой
обработки данных:
class Che f(T hr ead ):
def �init�( self, name : str) -> None :
supe r() .� ini t�(na me=name )
self . to tal = 0
def get_o rder( self) -> None :
self . order = TH E_ORDE RS . pop (0)
def prepare (s elf ) -> None :
'""' Si mulate doing а lot of work with а BIG comp utation """
star t = time . mono toni c()
ta rget = star t + 1 + ra ndom .r ando m( )
for i in range ( 1_000_000_000 ):
self . to tal += math . factori al(i)
if ti me . monoto ni c() >= ta rget :
break
print (
f" {ti me .m ono tonic (): .З f} {s elf . name} made {s elf . orde r}" )
def run ( self) -> None :
while True :
tr y :
self . get_ord er( )
self . prepa re ( )
excep t IndexErr or :
break # No more orders
По ток в выпо лняемом прил ожении должен расширить класс Thread и реали­
зовать метод run. Любой код, выпо лняемый методом run, является отдельным
потоком обработки данных, прохо дящим независимую диспе тчеризацию. Опи­
санный в коде поток ссылается на совместно используемый объект - глобальную
переменную THE_ORDERS:
impor t math
impor t ran dom
fr om th reading import Thread , Lock
impor t ti me
THE_ ORD ERS =
"R euben ",
"H am and Cheese ",
