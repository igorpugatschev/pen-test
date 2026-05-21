# Объектно-ориентированный Python, 4-е издание — страница 153

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

15 2 ГЛАВА /+ Ожидаемы е нео жиданн ости
По сле запуска этой функции на выполнение становится понятно, что первый вы­
зов print () выполняется, а затем возникает исключение. Второй вызов функции
print() никогда не выпо лняется, так же как и оператор return:
>>> ncver _re turns ()
I am about to raise an exception
Traceba ck (m ost rec ent call las t) :
File "<in pu t>", line 1, in <m odtJlc>
Fil e "< in pu t>", linc 6 , lП never rctc1r r1 s
Excep ti on : Tl1is is a1w ays r·ai secJ
Кроме того, если имеется функция, котора я вызы вает другую функцию, гене­
рирующую исключение, в первой функции ничего не выпо лняется после точки,
в которой было возбуждено исключение второй функции. Вызов исключения
останавл ивает все вып олнение вплоть до стека вызовов функц ий, до тех пор
пока исключение не будет обработано либо пока оно не застав ит интерпретатор
завершить прог рам му. Для ясности добав им вторую функцию, вызы вающую
never _re tur ns( ):
def call _exc eptor () - > None :
prin t( "ca ll _exceptor starts here ... ")
never _re turns ()
prin t( "an exception was rai sed ... ")
print (" ... so these lines don 't ru n" )
При вызове данной функции выпо лняется первый оператор print, а также пер­
вая строка функции never _ret urns () . Но как только возникает исключение, код
опять же прек ращает выпо лнение:
>>> call _exce ptor ()
call _exccptor starts here . ..
I am about to raise an exception
Traceb ack (m ost reccnt call las t) :
Fi le "< inpu t>", li ne 1, in <m odule>
Fil e "< inpu t>", line 3, in call cxceptor·
Fil e "< inpu t>", line 6 , in nev(•r ' гct c1гns
Exc ept ion : This is al ways rai sed
Об ратите внимание: туру не распозна л, что именно never _re turns ( ) делает
с обработкой в call _e xcep tor( ). Анализируя предыдущие примеры, можно
сделать такой выво д: call _e xcep tor( ) лучше описы вать как функцию NoRe tur n.
В результате мы получаем предупрежде ние от туру. Оказывается, возможности
инструмента туру довольно ограниченны. Инс трумент исследует определения
относительно изолированных функций и методо в. Он не способен установить,
что never _ret ur ns() вызы вает исключение.
