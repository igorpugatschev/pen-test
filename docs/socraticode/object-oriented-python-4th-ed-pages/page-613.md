# Объектно-ориентированный Python, 4-е издание — страница 613

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

61 2 ГЛ АВА 13 Тести рова ние об ъе ктн о- ориен тиров анн ы х про грамм
Здесь предоставляются IР -адрес хоста, номер порта и файл, в котор ый следует
записыва ть все сообщен ия. В реальной работе для передачи этих значений
прилож ению можно было бы рассмо треть возможность использования модуля
argparse и словаря os . environ. Но в этой реализации они задаются конкретными
значениями.
При ложение remote_logg ing_a pp. ру, передающее журнальные записи на сервер,
отслежи вающий журнальные фай лы, имеет следующий вид:
from _f utu re_ import annotations
impor t logging
import logging .h andlers
import ti me
import sys
from math import factorial
logger = logg ing .g etL ogger (" app" )
def work (i: int ) -> int :
logg er. inf o(" Fac torial %d ", i)
f = factorial (i)
logg er . inf o( " Factor ial (% d) = %d ", i, f)
return f
if _n ame_ _ma in_" ·
HOST, PORT = "l oca lhost ", 188 42
soc ket_ handler = log ging .h andlers . Soc ketHa ndler (H OS T, PORT)
st ream_handler = log ging . Stream Handler (s ys . std err)
log ging .b as icC onfig (
handler s= [ soc ket_ handler, st ream_handler ],
level= log ging .I NFO)
for i in rang e(1 0) :
work (i)
log ging .s hu tdo wn()
В прилож ении создаются два обработч ика журналов. Экземпляр SocketHandler
откр ыва ет сокет и порт с конкретным номером на заданном сервере и начина­
ет запись байт ов. Байты включают заголовки и поле зные данные. Экземпляр
StreamHandler ведет запись в окно терминала; это исходный обработч ик журнала,
который был бы достаточ ен, если бы не создава лись никакие специа льные об­
работчики. Регистратор настраивается с обоими обработч иками, позволяющими
отправлять каждое сообщен ие журнала как на консоль, так и на поток овый
сервер, собирающий сообщен ия. А в чем заключается реальная работа? В мате­
матических расчетах факториа ла числа. При каждом запуске приложения им
должно вы водиться 20 сообщений журнала.
