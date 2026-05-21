# Объектно-ориентированный Python, 4-е издание — страница 353

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

352 ГЛА ВА 8 ОО П и фу нкци о наль ное про гра мм и рова ние
Важно отметить строки, которые касаются функций обратного вызова. Функция
передается как любой другой объект: классы планировщика Scheduler и задачи
Task никогда не знают и не заботятся о том, как изначально называлась функция
или где она была определена. Когда прих одит время вызва ть функцию, пла­
нировщик просто вычис ляет ее с помощью new_ task . callb ack( cur rent_t ime).
Вот набор функций обратного вызова, которые тестируют класс Scheduler:
impor t datet ime
def format_ ti me (m es sage : str) -> None :
now = datet ime . datet ime .n ow ( )
print (f" {n ow:% I:% M:% S} : {messag e}" )
def one (t imer : float ) -> None :
format_ ti me ( "Call ed Опе" )
def two(ti mer : float ) -> None :
format_ ti me ("C al led Two" )
def thr ee (ti mer : float ) -> None :
forma t_t ime (" Cal led Three ")
class Repea ter :
def �in it�( self) -> None :
self . count = 0
def fo ur( self, tim er : float ) - > None :
self . count += 1
forma t_t ime (f"C al led Fo ur : {s elf . coun t}" )
Все эти функции соответствуют опре делению подсказки типа Callback, по­
этому они хорошо подойдут. В определении класса Repeat er есть метод four () ,
который соответствует этому определению. То есть экземпляр класса Repeat er
также может быть испо льзован .
Для написания обычных сообщен ий была определена удобная служебная функ­
ция format_ ti me( ). Она исполь зует форматирование строк при добавл ении
текущего времени в сообщ ение. Три небольшие функции обратного вызова вы­
водят текущее время и короткое сообщение о том, какой из обр атных вызовов
был вып олнен.
Вот пример создан ия планировщика и загрузки его функ циями обратного
вызова:
s = Sch eduler ()
s. enter (l, опе)
s. ent er(2, опе)
s. enter (2, two )
