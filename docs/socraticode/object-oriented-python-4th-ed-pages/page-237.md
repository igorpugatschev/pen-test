# Объектно-ориентированный Python, 4-е издание — страница 237

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

236 ГЛ АВА 6 Абст рак тны е класс ы и перег рузка оп ерат оров
def _init_(
self,
sour ce: Union [I teraЫe [
tuple [ Com paraЫe, Any] ]
Ba se Mapping,
No ne] = None,
-> None :
so rted_pa irs : Seque nce [tuple [ Compa raЫe, Any] ]
if isinstance( sou rce, Seq uence ):
sor ted_ pairs = sor ted (s ource )
elif isi nstance( source, abc . Mappin g) :
so rted_pa irs sorted (s ource . items ())
else :
sor ted_ pairs []
self . key_l ist = [р[0] for р in sorted _pa irs ]
self . value _l is t, = [p[l] for р in sort ed_pa irs ]
Ме тод _i nit_( ) должен обрабатывать три случая загрузки соп остав ления.
Это означает пос троение значений из последовате льности пар, или пос трое ние
значений из другого объекта соп остав ления, или же создание пустой последо­
вательности значений. Необходимо отделить ключи от значений и поме стить их
в два паралле льных спи ска. Проана лизируем отсорти рованный список ключей,
чтобы найти совпа дение. Отсортиро ванный список значений возв ращается
в качестве результата, когда мы получаем значение ключа из сопо ставления.
Ниже в приме ре представл ен необходимый импорт:
from _f utu re_ impor t ann ot ations
from collections import аЬс
from typing import Pr oto col , Any , ove rload , Union
impor t bisect
from typing import Iterator, IteraЫe, Sequ ence, Mapping
След ующий пример демонстрирует абстрак тные методы, определенные деко­
ратором @abstra ctmeth od. Рассмотрим приводимые реализаци и:
def _len _( self) -> in t :
return len (s elf . ke y_l ist )
def _iter _( self) -> Iterato r[ Compa raЫe ]:
return iter (s elf . key_l ist )
def _con tains _( self, key : object ) -> bool :
index = bisect .b i sect _left (s elf .k ey_l ist, key )
return key == self . key_ list [ in dex ]
def _get item _( self, key : Com paraЫe ) -> Any :
index = bi sect .b i sect _left (s elf .k ey_l is t, key )
if key == self . ke y_l ist [i nde x] :
return self . value _list [ index ]
raise KeyErr or( key )
