# Объектно-ориентированный Python, 4-е издание — страница 608

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

П ро ве дение м одул ьн ог о те стирова ни я с по м ощью pytest 607
import tar file
from pathlib impor t Path
import hashlib
def checksum( sour ce: Path, checksu m_pat h: Path) -> None :
if checks um_path .e xists ():
backup = checks um_path . with _ste m(f" (o ld ) {c hecksu m_path . stem} ")
backup . write _text (c hecksu m_pat h. read _text ())
checksum = hashlib . sha256 ( source . rea d_byt es ())
checks um_pat h. write _text (f"{s ource . name} {c hecksu m . hexdigest ()} \n" )
Есть два возможн ых сценария.
• Исходн ый файл действит ельно существует, и в каталог добавля ется новая
контрольная сумма.
• Существует как исходный файл, так и файл контрольной суммы. В данном
случае делается резервная копия старой контрольной суммы и записыва ется
новая контрольна я сумма.
Не станем здесь тестировать оба сценария, пок ажем , как фикс тура может соз­
давать, а затем удалять файл ы, необходимые для тестовой после довател ьности.
Сос редото чимся на втором сценарии, поск ольку он сложнее первого. Разобьем
тестирование на две части и начнем с фик стуры:
from �fut ure � import ann otat ions
import checksu m_writer
import pyt est
from pathlib import Path
from typing impor t Iterator
import sys
@pyte st . fixture
def wo rki ng_dir ector y ( tmp_pat h: Path) -> Iterator [tuple [ Path, Pat h] ]:
wo rking = tmp_path / "s ome_dir ectory"
wo rking .m kd ir ()
source = working / "d ata . txt "
sour ce . write _byte s( b"H ello, world ! \ n")
checksum = wo rking / "c hecksu m . txt "
ch ecksum . write _text (" data . txt Old_ Chec ksu m" )
yield sou rce, chec ksum
checksu m. unlink ()
source . unlink( )
Работа этого кода основана на применении инструкции yield. Фактически
фи кстура является генератором, выдающим один результат и ожидающим сле­
дующего запроса значения. Первым результатом становится выполнение целого
ряда шагов: создание рабочего каталога, создание в нем исходного файла, а затем
создание старого файла контрольной суммы. Ин струкция yield предоставляет
