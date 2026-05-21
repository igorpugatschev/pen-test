# Объектно-ориентированный Python, 4-е издание — страница 548

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

from _f utu re_ import ann otat ions
import re
from pathlib import Path
from typing import Iter ator , Tuple
class FindU ML :
def _init _( self, base : Path) -> None :
self .b ase = base
Па ттерн Фасад 547
self .s tar t_pat tern = re . compi le (r "@startuml *( .* )")
def uml_ file _i ter( self) -> Ite rator [t uple [ Path, Pat h] ]:
for source in self .b ase . glo b( "* */* .u ml" ):
if any(n. star ts wit h(" ." ) for n in sour ce . parts ):
cont inue
body = sour ce . read _text ()
for outp ut_name in self .s tar t_pattern .f indal l(b od y) :
if out put_name :
ta rget sour ce . parent / outp ut_n ame
else :
ta rget sour ce . with _suffix (".p ng" )
yield (
sour ce . relative _to (s el f.b as e),
ta rget . relati ve_to (s elf . base )
Для класса FindUML необходим базо вый каталог. Метод uml_ file _ite r( ) про­
ходит 110 всему дереву каталогов, испо льзуя метод Path . glob () . При поиске
11 ропус каются все каталоги, имена которых начинаются с . , так как к ним часто
обращаются в своей работе инструменты tox, туру или git. Оста льные файлы
будут содержать cтpoки @sta rtuml, а некоторые и строку с именами нескольких
вых одных фай лов.
Большинс тво файлов UML не создают нескольких файл ов. Рег улярное выра­
жение sel f. sta rt_ pattern опре деляет имя, если оно указано, а итератор выдает
кортежи с двумя путями.
Име ется класс, который в качестве подпроцесса запус кает прикладную програм­
му Plant U ML. Когда Python работает, все это является процессом опера ционной
систем ы. Оп ираясь на модуль subpr ocess, можно запус кать дочерние проце ссы,
которые, в свою очередь, запус кают другие бинарные приложения или сценарии
обо лочки. Напри мер, так:
impor t sub proc ess
class Plan tUML :
conda _env_name = "Ca seStudy "
base _env = Path . home () / "m inic ondaЗ" / "e nvs " / cond a_env_name
def _in it_(
self,
