# Объектно-ориентированный Python, 4-е издание — страница 330

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

>>> class Custo mSe quen ce:
def _iп it_ (s elf , ar g s) :
self ._ list = args
def _len_ (s el f) :
ret tJrn 5
def _get i te 111 ( sc 1 f, i ndcx ) :
re turn f"x{ index }"
>>> class Funk yBac kwa rds( lis t) :
dcf reversed (s el f) :
ret urn "B AC KWARDS 1"
Встрое нные фун кции Python 329
Давайте проверим эту функцию на трех списк ах различных видов:
»> ge neric = [1, 2, 3, 4, 5]
>» cu stom = CtJs tomSeq ueп ce ([ G, 7, 8, 9, 10] )
»> fuпkadelic = Ft1nk yBackwar ds( [l l, 12, 13, 14, 15] )
>>> for secitJeпce iп gPner 'ic , CLJ<;to1 11, fun kadeJ ic :
pr·int (f"{s eqt1P nce . class . _nam e_} : end =" ")
for it e1 11 in reve rsed (s equcnc e) ·
print (f"{ ttP 11 1} , ", епd =" ")
pr· int ()
list : 5, 4, З, 2, 1,
Custo 111 Seq uence : х4, хЗ, х2 , xl, хо ,
Funk yB ack war ds : В, А, С, К, W, А, R, D, S, 1
Циклы for в конце вы водят обра тные версии сп иска generic, а также экзем­
пляров класса Custo mSequence и класса FunkyBackwards. Вывод показыв ает, что
функция reve rsed работает со всеми тремя объект ами, но воз вращает очень
разные результаты.
Когда мы инвертируем объект CustomSequence, для каждого элемента вызы вается
метод _g et i te m_ () , который просто вставляет х перед индексом. Для объекта
FunkyBackwards мeтoд _reve rsed_( ) возвращает строку, каждый символ которой
выводится отдел ьно в цикле for.
о Кла сс Cus tomSequenc e яв ляе тся неполным. В нем ме тод ite r () долж ­
ным о бразом не определ ен, поэто му цик л for с прямым ег о перебором
ни ког да не завершится . Этому посвящена глава 1 О.
Функ ци я enumer ate()
Ин огда, например при переборе элементов в контейнере с помощью оператора
for, оказы вается нужен доступ к индексу (п озиции в контейнере) текущег о об­
рабатываемого элемента. Оператор for не предоставляет индексов, а вот функция
enumerate () создает последовательность кортеж ей, где первый объект в каждом
кортеже - индекс, а второй - исходный элемент.
