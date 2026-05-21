# Объектно-ориентированный Python, 4-е издание — страница 265

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

264 ГЛАВА 6 Абстра ктны е класс ы и перегрузка операт оров
список с помощью оператора for и блока опера ций append( ) . В главе 10 эта тема
будет рассмотрена более подробно.
Резул ьтаты предска зать сложно, поскольк у многое зависит от модуля random,
поэтому тестирование в данном случае также излишне сложное. Сп ециалисты
по обработке данных требуют, чтобы данные перета совыва лись, но они также
хотят получить воспроизво димые результа ты. У становив для random. seed ( )
фиксир ованное значение, мы можем создавать случайные, но воспроизво димые
коллекции обра зцов.
Это работает следующим обра зом:
>>> import ran dom
>>> from mo del import Shuffli ngSJmplePa rt it ion
>>> from pprint import ppri nt
>» dJta = [
"s e pи l_J engtll ": i + 0.1 ,
"s epa l_ c'iidth" : i + 0. 2,
"p eta l_length ": i + 0.3 ,
"p etal_ wid th" : i + 0.4 ,
"s pec ies ": f" sample {i }",
for i in range (1 0)
>>> rand om .s eed (42 )
>>> ssp = Shuf fli ngSamp lePar t ition (d ata )
>>> pprint (s sp . test ing )
[T est ingKno wnSam pl e(s e pal_leng th= 0.1 , sepa l_ width=0 .2,
pet al _leng th=0 .3 , peta l_ wid th-0 .4, spec ies= ' sample 0' ,
classi ficat ion=N one, ) ,
Testi ngK nown Samp le ( sepa l_leng th=l .1 , sepи l_w idth= l.2 ,
pet al _lengt h =l .3 , pet al __ wid th=J .4, spe cie s= ' sи11 1ple 1' ,
classi fica tio n=N one , )]
В тесто вом множестве при случай ном начальном значении 42 мы всегда полу­
чаем два одних и тех же образца.
Это позво ляет нам создавать исходный список различными способам и. Напри­
мер, так: в пустой список добавить элементы данных.
ssp = Shuf flin gSam plePar tition (tr ainin g_s ubse t=0 .6 7)
for row in data :
ssp . append ( row )
По дкласс SampleParti ti on сп иска унаследует все методы родительского класса.
То есть перед извлечением подм ножеств обучения и тестирования можно будет
вносить изменения во внутреннее состояние списка. А параметр размера добавлен
только для ключевого слова, чтобы убедиться, что он четко отделен от объекта
списк а, используемого для инициализации списк а.
