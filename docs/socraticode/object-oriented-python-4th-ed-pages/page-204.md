# Объектно-ориентированный Python, 4-е издание — страница 204

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Управ лен ие объек та м и 203
файла резервной копии. Он про веряет каждый элемент архива, вы полняя ряд
этапов, включая расширение сжатых данных, преобразо вание с помощью метода
tran sfor m( ) и сжатие для записи в выходной файл, а затем очистку временного
файла (и каталогов).
Очевидно, что мы можем выпо лнить все эти этапы в одном методе класса или
даже в одном сложном скрипте, не создавая объект. Но разделение этапов имеет
ряд преимущ еств.
• Удобочит аемость : код для каждого шаг а находится в автономном блоке,
который лег ко читать и понимать. Имя метода описы вает работу метода,
поэтому требуется меньше поясняющей дополн ительной документа ции.
• Расширяемос ть: есл и подкласс захочет испо льзовать сжатые файлы Т AR
вместо файлов ZIP , он может переоп ределить метод copy_a nd_ tran sfor m( ),
повторно испо льзуя все вспом огател ьные методы, пос кольку они применя­
ются к любому файлу, независимо от типа архива.
• Разбиение на разделы: внешний класс может создать экземпляр этого класса
и напрямую при менить методы make_ba cku p() или copy_a nd_ tran sform () ,
минуя менеджер find_a nd_r eplace ( ) .
Эти два метода класса ZipR eplace создают резервную копию и новый файл,
считы вая из резервной копии и записы вая новые элементы после их изменения:
def make _ba ckup ( self) -> tuple [ Path, Pat h] :
inpu t_path = self .a rchi ve_pa th . wit h_s uffix(
f"{ sel f.a rchi ve_path .s uffix} .o ld")
outp ut_ path = self .a rchi ve_path
self . arch iv e_path . ren ame ( inpu t_path )
return inp ut_pat h, outpu t_path
def cop y_and_tran sform (
self, input : zip file .Z ipFile, output : zip file .Z ipFile) -> None :
for item in input . inf olis t( ):
ext racted = Path (i nput . ext ract (i te m) )
if (n ot item .i s_dir( )
and fnmatch . fnmatch( item . filena me , self . pattern )):
print (f" Tran sform {i tem} ")
inp ut_text = extracted . rea d_text ()
outp ut_text = re .s ub( self . find , self . repl ace, inpu t_text )
ext racted . write _text (o ut put_ te xt )
else :
print (f" Ignore {i tem} ")
output .w rite ( ext racte d , item .f ilen ame )
extracted .u nlink ()
for pa rent in extracted .p aren ts :
if pa rent == Path .c wd( ):
break
pa rent .r md ir ()
