# Объектно-ориентированный Python, 4-е издание — страница 518

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Па ттерн Состоя ние 51 7
о Для стор онник ов класси че ских взглядов имя класса пок ажется не соот ­
ветствую щим тре бов аниям РЕР-8. Слож но вк лю чат ь аббревиат уры или
акр онимы и сохра ни ть прав ильное назв ание в вер блю жьем регис тре .
Кажется , имя клас са Nm eaS tate не очен ь понятно. Более подходя щим
именем класса ста не т NM EAState, но ко нф лик т ме жду аббревиат ур ами
и именем класса мо жет сил ьно запутат ь. Примен ител ьно к да нн ому слу­
чаю процитир уем фра зу «Буквал ьное следова ние инс трукци и ни к чему
хорошему не приведет». По дде ржа ние вн утр енней сог лас ованнос ти
иерархии классов важнее , чем полн ая сог лас ова нн ость и соотв етствие
ка нонам РЕР-8 .
Объект Messag e является оболочкой двух структур bytearr ay, в которых нака­
пливается содержимое сообщ ения:
class Me ss age :
def �init �( self) -> None :
self .b ody = bytearray (8 0)
self .c hec ks um_source = bytearray (2)
self . body _len = 0
self . chec ks um_len = 0
self .c hecksu m_computed 0
def rese t (s elf) -> None :
self . body_l en = 0
self .c hecksu m_len = 0
self .c heck su m_computed 0
def body _app end ( self, inp ut : int ) -> in t :
self .b ody [s elf . body_l en ] = in put
self . body _l en += 1
self .c hecksu m_computed л= input
return self .b ody_l en
def checks um_append (s elf, in put : in t) -> int :
self .c hec ksum _sou rce [s el f.c hecksu m_len ] in put
self .c hecksu m_len += 1
return self .c hecksu m_len
@property
def valid (s elf ) -> bool :
return (
self . checksu m_len == 2
and int ( self .c hecks um_sou rce, 16 ) self .c hecksu m_comp uted
Опр еделение класса Mess age инкапсулирует многое из того, что важно в каж­
дом предложении, поступающем от GРS-у стройства. Для накопления байтов
в теле сообщения и накопления контрол ьной суммы этих байтов опре делен
метод body _a ppend () .
