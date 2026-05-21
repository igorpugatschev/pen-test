# Объектно-ориентированный Python, 4-е издание — страница 664

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

М н ог опр о цесс н а я обр а бо тк а да нных 663
Основ ная часть приложения создает соответс твующий пул рабоч их процессов
и их очереди. Воспользуемся шаблоном проектирования Фасад (для получения
дополните льной информации см. главу 12 «Но вые паттер ны проектирова ния»).
Идея заключается в том, чтобы для объединения очередей и пула рабо чих про­
цессов в один объект определить класс DirectorySea rch.
По лучаемый в результате объект будет спо собен выстраивать очереди и рабочие
процесс ы, после чего приложение сможет взаимодействова ть с ними, отправляя
запрос и получая ответы .
from �f utu re� import ann ot ations
from fnmat ch impor t fnmat ch
impor t os
class Dir ector ySea rch :
def �init �( self ) -> Ndne :
self .q ue ry_queues : Lis t [Q ue ry_Q]
self . res ul ts _queue : Resu lt _Q
self . search _worke rs : List [ Pro ce ss]
def setup _sea rch(
self, paths : List [P at h] , cpus : Opt iona l[i nt ] No ne ) -> None :
if cpus is No ne :
cpus = cp u_count ()
worker _paths = [p aths [i: :c pu s] for 1 in rang e( cpus )]
self .q uer y_queues = (Queue () for р in rang e( cpus )]
self . results _queue = Queue ()
self . search _workers = [
Proces s(
tar get=sear ch, args= (p at hs, q, self . results _queue ))
for paths, q in zip(w orker _pa ths, self .q uer y_queu es)
for proc in self . search _worke rs :
proc .s tar t()
def tea rdo wn_s ea rch( self) -> None :
# Signal proc ess termination
for q in self .q uer y_queue s:
q. put (N one )
for pr oc in self .s earch _workers :
proc . join ()
def sear ch{ self, ta rget : str) -> Iter ator [s tr] :
for q in self .q uer y_queues :
q. put ( ta rget )
for i in range (l en(s elf . quer y_queues )):
for mat ch in self . results _queue .g et( ):
yield match
