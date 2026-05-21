# Объектно-ориентированный Python, 4-е издание — страница 424

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Се ри ал иза ция объ екто в 423
консервирова ть эти объек ты. Состо яние устройства и опе рационной системы
будет бессмыс ленным, когда программа попытается перезагрузить объект позже.
Нельзя же просто притворяться, что исходный поток или соединение соке та
существует, когда прои сходит переза грузка! Необходи мо особ ым обра зом на­
страива ть выгрузку и загрузку таких перехо дных и динамических данных.
Рассмотрим пример класса, который загружает содержимое неб-страницы каждый
час, чтобы обеспечить ее актуальность. Он испо льзует класс thr eading . Timer
для планирования следующего обновления:
from thr eading impor t Timer
import datet ime
from urllib . request import ur lopen
class URLP ol ling :
def _init _( self, url : str) -> None :
self .u rl = url
self . contents = ""
self .l ast _u pdated : datet ime . da tetime
self .t imer : Timer
self . upda te( )
def update (s elf) -> None :
self . contents = url open (s el f. url ) .r ead()
self .l ast _u pdated = datetim e .d atetime .n ow ()
self .s chedul e()
def sch edule (s elf) -> None :
self .t imer = Tim er( 3600 , self .u pdate )
self .t imer . se tDa emon (T rue )
self . ti mer .s tar t()
Такие объек ты, как url, content и la st_u pdated, можно консервирова ть, но если
поп ытаться выбрать экземпляр этого класса, в экземпляре sel f. timer все пой дет
немного не так, как ожидалось:
>>> import pickle
»> poll = URLP ol lin g( "h ttp :/ /du sty .p hilli ps . cod es ")
>>> pickle . dumps (p o ll)
Traceback (m ost recent call las t) :
F ile "<d octest ur l_poll . _ test_ . te st_ broken [2] >", lin e 1, in
<m odule>
pickle . dumps (p ol l)
Type Err or : can not pickle ' thr ead .l ock ' object
Это не очень инфор мативная ошибка, но, похоже, мы пы таемся консервирова ть
то, что не должны, а именно экзем пляр Timer. Ссылка на sel f. ti mer хранится
в методе sch edule ( ), и этот атрибут не может быть сериализован.
