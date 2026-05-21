# Объектно-ориентированный Python, 4-е издание — страница 575

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

574 ГЛАВА 12 Н овы е па тrерны проек ти рован ия
@abc .a bs tr ac tmethod
def remove (s elf) -> None :
Абстрактн ый класс Node определяет, что каждый узел имеет строку со ссылкой
на родителя. Сохранение родител ьской информации позво ляет анализировать
дерево выше, ближе к корневому узлу. То есть становится возможн ым переме­
щать и удалять файл ы, внося изменения в родител ьскую коллекцию дочерних
фай лов.
В классе Node мы создали метод move () . Он перемеща ет в новое место объекты
Folder или Fil e. Далее следует удаление объекта из его предыдущего местопо­
ложения. Для метода move () целью должна быть существую щая папка, иначе
мы получ им ошибку, поскольку экземпляр File не имеет метода add _c hild () .
Как и во многих примерах из технической литератур ы, обработка ошибок, к со­
жалению, отсутствует. Это сделано для того, чтобы сосред оточить все внима­
ние на рассма триваемых принциriах. Обычной прак тикой является обработка
иск лючения Att ributeE rror путем создания нового исключения Ty peE rror
(см. главу 4).
Теперь мы можем расширить этот класс, чтобы предоста вить уник альные
функции папки , содержащей дочерние элементы, и файла, котор ый является
конечным узлом дерева и не имеет дочер них элементов:
class Fol der( Node ):
def _init_(
self,
name : str,
chil dren : Option al [dic t[s tr, "N od e" ]] = None
-> None :
supe r( ). _ in it_( name )
self .c hildr en = childr en or {}
def _re pr_( self) -> str :
return f" Folder ({s elf . name !r }, {s elf .c hildr en !r })"
def add_ chil d ( self, node : "N ode ") -> "N od e" :
node . pa rent = self
retur n self .c hi ldren . se tdefa ult (n ode . name , node)
def cop y( self, new_fold er : "F older ") -> None :
ta rget = new_fold er . add _child ( Fold er( self .n ame) )
for с in self .c hi ldren :
self . childr en [c] . copy (tar get )
def remove (s elf) - > None :
names = lis t (s elf . childr en )
for с in names :
