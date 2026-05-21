# Объектно-ориентированный Python, 4-е издание — страница 107

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

10 6 ГЛ АВА 2 Об ъе кты в Python
Создадим зависи мость от источ ника данных. Его свойс тва описаны подска зкой
типа IteraЫe [dict [s tr, st r] ]. IteraЫe утвер ждает, что результаты метода
могут использова ться оператором for или функцией lis t. Это справе дливо для
таких колле кций, как списки и файл ы, а также верно для функци й-гене рато ров,
котор ым посвящена глава 10 .
Результатом работы итератора долж ны быть слова ри, отображ ающие строки
в строках. Такова общая структура, она позво ляет нам запросить слова рь, ко­
торый выг лядит так:
{
}
"s epal _leng th" : 5.1 ,
"s epal _wid th" : 3.5 ,
"p etal_leng th" : 1.4 ,
"p eta l_wid th" : 0.2 ,
"sp ecies ": "I ris-set osa "
Эта требуема я структура кажется достато чно гибко й, чтобы мы могли создать
некий объект, который будет ее произво дить . Более подробно эту тему рассмо­
трим в главе 9.
Ос тальные методы делегируют большую часть своей работы классу Hyper ­
parameter. Вместо того чтобы выпо лнять работу по классифик ации, этот класс
обращается к другому клас су, не посредств енно вы полняющему эту работу:
def test (
self,
pa ramete r: Hyperpa ramete r) - > None :
"' "'Test this Hyperpa rameter value . '""'
pa ramet er .t es t()
self .t uning . append (p ar ameter)
self . tested = datet ime .d atetime . now( tz=d atet ime .t imezone .u tc )
def classi fy (
self,
pa ramete r: Hyperpa rameter,
sample : Sam ple} -> Sample :
'"" 'Classi fy this Samp le . """
classi fication = pa rameter .c lassi fy (s ample}
sample .c lassi fy(cl ass ification )
retur n sample
В обоих случаях в качестве параметра пре доставляется кон кретн ый объект
Hyperpa rameter. Это име ет смыс л для тестирования, так как каждый тест должен
име ть отдел ьное значение. Однако для класс ификации следует испо льзовать
<�лучший» объект - Hyperpa rameter.
