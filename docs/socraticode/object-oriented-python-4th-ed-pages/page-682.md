# Объектно-ориентированный Python, 4-е издание — страница 682

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Б иб лио те ка Asyn clO 681
Применение глобальной переменной LIN E_COUNТ у кого-то может выз вать удив­
ление. Напомним, что в предыдущих разделах уже приводились страш илки о по­
следс твиях одновременного обновления совме стно испо льзуемой переменной
сразу несколькими потокам и. С as yncio вытес нение потоков отсутствует. И по­
скольку каждая сопр ограмма для передачи управления другим сопрог раммам
через цикл обработки событий испо льзует явные запросы ожидания, значение
этой переменной можно обновить в сопр ограмме log_ writer( ) , зная, что изме­
нение состояния в среде всех сопрограмм будет фактически атомарным, то есть
иметь характер ни с кем не разделяемог о обновления.
Чтобы придать примеру завершенный вид, приведем код блока импортирования:
fr om �f utu re� import ann ot ations
impor t asyncio
import asyncio . exceptions
import js on
fr om pathlib import Path
fr om typing import Text IO
import pickle
impor t si gnal
import struct
import sys
А вот так выг лядит код высокоур овневог о диспе тчера, запус кающего данный
сервис:
serv er : asy nci o . AbstractServer
async def main{ host : str, port : in t) -> None :
global server
ser ver = awa it async io . sta rt_s erve r(
lo g_c atcher,
host=host ,
port= port ,
if sys . pl atform != "win3 2" :
loop = async io . get_ running _loop ()
loop . add _s ignal _han dler (si gnal . SIG TER M, server .c lose )
if server .s ocke ts :
addr = ser ver .s ocke ts[0] . get sock name ()
print (f" Serving on {addr} ")
else :
raise Va lueErr or {" Fai led to cr eate ser ver ")
async with serv er :
await ser ver .s er ve_foreve r()
