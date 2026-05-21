# Объектно-ориентированный Python, 4-е издание — страница 210

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Управ лен ие об ъек та м и 209
Решать проблему начнем с использования наслед ования. Во -первых, преоб­
разуем исходн ый класс ZipR eplace в суперк ласс для обработки ZIР -файлов
различными спо соба ми:
from аЬс import АВС , abstract method
class Zi pProce ssor(A BC ):
def �init �( self, archi ve : Path) -> None :
self .a rchi ve_path = archi ve
se lf._ pattern : str
def proces s_fi les ( self, pattern : str) -> No ne :
self ._ pattern = pattern
inp ut_pat h, outpu t_path = self . make _back up( )
with zip file .Z ipFile (o ut put_ path, "w" ) as output :
with zip file .Z ipFil e ( inpu t_pat h) as input :
self . cop y_and_transf orm (in put, output )
def make_backup( self) -> tuple [ Path, Pat h] :
inp ut_path = self .a rchi ve_path . with_suf fix(
f"{s elf .a rchiv e_path .s uffix} .o ld")
outp ut_ path = self .a rchi ve_path
sel f.a rchi ve_pa th . ren ame (i np ut_pat h)
return inp ut_pat h, outpu t_path
def cop y_and_transf orm (
self, input : zip file .Z ipFile, output : zip file .Z ipFile) -> None :
for item in in put . inf olis t( ):
extracted = Path (i nput . extr act ( ite m) )
if self . mat ches (i te m) :
print (f" Tran sform {i tem} ")
self . tran sform ( extracted )
else :
print (f" Ignore {i tem} ")
output .w rite ( extracted , item .f ilen ame )
self . remove _u nder _cwd (e xtracted )
def mat ches (s elf, item : zip file . Zipln fo ) -> bool :
return (
not ite m. is_ di r( )
and fnma tch . fnmatch ( item . fi lename , self ._ pattern ))
def remove _u nder _cwd (s elf, ext racted : Path) -> None :
extracted .u nlin k( )
for pa rent in ext racte d .p ar ents :
if pa rent == Path .c wd( ):
break
pa rent . rmdir( )
