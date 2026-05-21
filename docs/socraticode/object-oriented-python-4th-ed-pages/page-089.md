# Объектно-ориентированный Python, 4-е издание — страница 89

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

88 ГЛАВА 2 Об ъе кты в Python
Класс Point (и функцию main()) можно испо льзовать повторно. Со держи мое
этого модуля импортируется без како й-либо сложной обработ ки. Однако когда
мы запус каем его как основную прог рамму, он выпо лняет функцию main () .
Это действительно работает, так как каждый модуль имеет спе циальную пере­
менную _na me_ (помни те, Python испо льзует двойное подче ркивание для
специа льных переменных, таких как метод _in it_ класса) , котора я опреде­
ляет имя модуля при его импо рте. Когда модуль выпо лняется непосредств енно
с помощью команды pyt hon module . ру, он не импо ртируется, поэтому _na me_
в обяза тельном порядке устанавливается в строку "_ main_".
о Дел ай те так, что бы все ваши скри пты зак лючались в тест if _n ame _ ==
"_ma in _ ", на тот случ ай, если вы пишете функци ю, кот ор ую, возможно,
зах отите в будущем импор ти роват ь в друго й код .
Итак, пакеты содержат модул и, которые, в свою очередь, содер жат классы, ко­
торые содержа т методы. Это наконец-то все?
Вообще-то, нет. Таков типичный порядок в программе Python, но не единствен­
ная возможная схема. Классы могут быть определены в любом месте прог раммы.
Обычно это прои сходит на уровне модуля, но также классы мог ут быть опреде­
лены внутри функции или метода, например:
fr om typing import Opt io nal
class For matter :
def format (s elf, string : str) -> str :
pass
def format_st ring ( string : str, format ter : Optio nal [F ormatt er] No ne)
-> str :
For mat а string using the form atter obj ect, which
is expected to have а format () method that ac cepts
а string .
class Defa ultFor mat ter( For matter ):
"""For mat а string in title case . '""'
def fo rmat (s elf, string : st r) -> st r:
return str( strin g) . titl e()
if not forma tter :
forma tter = Defa ultF ormat te r()
return formatte r. format (s tring)
