# Объектно-ориентированный Python, 4-е издание — страница 573

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

572 ГЛАВА 12 Н ов ы е пап ерн ы про екти рова ния
П ример реал иза ци и папер на Ко м понов щик
Патгерн Компоновщик необходимо применять к древовидным структурам, таким
как, скажем, файлы и папки файловой системы. Независимо от того, является ли
узел в дереве обычным файлом данных или папкой, он по- прежнему подвергается
таким операциям, как перемещен ие, копирование или удаление узла. Мы можем
создать компонентный интерфейс, поддер живающий эти операции, а затем ис­
пользова ть составной объект для предста вления папок и конечные узлы - для
представления файлов данных.
Конечно, для неявного предоста вления интерфейса в Python мы снова можем
восполь зоваться утиной типи зацией, для этого необходимо создать только два
класса. Сн ачала определим эти интерфейсы в следующем коде:
class Fold er :
def _init_(
self,
name : str,
childr en : Opt iona l[ dic t[s tr, "N od e" ]] None
-> None :
self .n ame = name
self . chi ldren = childr en or {}
self . pa rent : Option al ["F older "] None
def _repr _( self) -> st r:
return f" Folder ({s elf . name !r }, {s elf .c hildr en !r })"
def add _child( self, node : "N od e" ) -> "N od e" :
node . pa rent = self
return self .c hildr en . setde fa ult (n ode . name , node )
def move (s elf, new_folder : "F olde r" ) -> None :
pass
def cop y( self, new_folder : "F older ") -> None :
pass
def remove (s elf) -> None :
pass
class File :
def _i nit _( self, name : str) -> None :
self .n ame = name
self . pa rent : Opt io nal [ Folde r] = None
def _repr _( self) -> str :
return f"Fil e({s elf . name!r })"
def move (s elf, new_path) :
pass
