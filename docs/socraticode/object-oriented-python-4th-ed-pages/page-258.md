# Объектно-ориентированный Python, 4-е издание — страница 258

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Мета класс ы 257
метод _рrераrе _ (). Метод _new_ () для построения конечного объекта класса
будет испо льзова ть аЬс .A BCMeta ._new_() . Класс ABCMeta решит, является ли
объект конкретным или остается абстрак тным, поскольку функция roll ()
не была опре делена:
import log ging
fr om functools import wraps
from typing import Ту ре, Any
class Di eMeta( abc . ABCMeta ):
def _new _(
met ac lass : Type [t ype ],
name : str,
bases : tuple [t ype, ... ],
namesp ace : di ct [s tr, Any] ,
**k wargs : Any,
-> "Die Meta" :
if "r oll" in namespace and not getatt r(
namespace [" rol l"], "_ isabs tra ctmethod _" , False
) :
namesp ace . setde fa ult (" logg er" , log ging . get logg er( name) )
origina l_met hod = namespace ["r ol l"]
@wra ps( original _met hod )
def lo gged_r oll (s elf : "D ielo g" ) -> None :
original _met hod (s elf)
self . logg er . inf o(f" Rolled {s elf . face} ")
namespace ["r ol l"] = logged_ro ll
new_object = cast (
"D ieMeta ", abc . ABCMe ta . _new _(
meta class, name, bases , namespace)
return new_object
Метод _nеw_ () получает большое количество значений аргументов, они пере­
числены ниже.
• Па раметр metaclass является ссылкой на выпо лняющий работу метак ласс.
Python обычно не создает и не испо льзует экземпляры метакла ссов. Напро­
тив, сам метакласс передается в качестве параметра каждому методу. Немного
по хоже на предоставляемое объе кту значение sel f, но все-т аки это класс,
а не экземп ляр класса.
• Па раметр name - имя целевого класса, взятое из исходного оператора класса.
• Параметр bases - это список базовых классов. Как правило, сюда включаются
миксины, отсор тированные в порядке разрешения методов. В примере будет
определен супе ркласс, использующий метакласс DieLog.
