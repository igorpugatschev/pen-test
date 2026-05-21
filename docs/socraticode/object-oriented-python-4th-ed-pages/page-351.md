# Объектно-ориентированный Python, 4-е издание — страница 351

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

350 ГЛАВА 8 ОО П и фу нк ци она ль ное пр о гр амм и рован ие
Метод repeat ( ) возвращает задачу для тех дейс твий, которые способны повто­
ряться. Он вычисляет новое время для задачи, предоставляет ссы лку на исходный
объект функци и, а также задает после дующую задержку, delay, и измененный
предел, li mi t. Измененный предел будет считать количество повторений вплоть
до нуля, что дает разработчикам определенный верхний предел обработк и; всегда
приятно быть уверенными, что итерация завершится .
Комментарии # type : ignore [misc] здесь потому, что существует определенная
деталь, приво дящая туру в недоумение.
Когда мы испо льзуем код типа self . callback или someTask . cal lba ck( ), он
выглядит как обычный метод. Однако в коде класса Scheduler он не будет ис­
пользова ться в качестве обычно го метода; его будут испо льзова ть как ссылку
на отдельную функцию, опре деленную совершенно вне класса. У Python есть
следующее предположен ие: атрибут Cal laЫe должен быть методом, а это значит,
чтп у мРтn.п:::� .пn тт"о/р� 6r.:!Th нt:vt.:м:спная sel f. В этом случае вызы ваемый объек т
будет являться отдельной функцией. Самый простой способ опрове ргнуть это
предположе ние - заглушить проверку туру этой строки кода. Альтернативный
вариант - присвои ть sel f. callback другой пере менной, не являющейся sel f,
чтобы создать 1ш� ч:от ттрние. что это внешняя функция.
Вот общий класс планиров щика Scheduler, который использует объекты Task
и связанные с ними функции обратного вызова:
class Schedul er :
def �init �( self) -> No ne :
sel f.t asks : List [Task] = []
def ent er(
self,
aft er : in t,
ta sk: Callback,
delay : int 0,
li mit : int = 1,
-> No ne :
new_task = Ta sk( after, task, delay, li mit )
heapq .h eapp ush( self .t asks, new_task)
def run ( self) -> None :
curr ent_ time = 0
while sel f.t asks :
nex t_task = heapq . heapp op (s elf .t asks )
if (d elay := nex t_task . sc heduled - cu rr ent_ time ) > 0:
ti me .s leep ( nex t_task . sc heduled - cu rre nt_ti me )
curr ent _t ime = nex t_task . sc heduled
next_t ask . callba ck(c u rr ent_ ti me ) # type : ignore [mi sc]
if again := next_ task . repeat (c urr ent_ ti me ):
heap q .h eapp ush ( self .t asks, again)
