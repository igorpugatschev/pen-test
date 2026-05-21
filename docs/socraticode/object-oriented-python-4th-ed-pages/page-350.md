# Объектно-ориентированный Python, 4-е издание — страница 350

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

fr om future impor t ann ot ations
import heapq
import ti me
Функ ции - это тоже объек ты 349
fr om typing import CallaЫe, Any , List, Optional
from da taclasses import dat acla ss, field
Callback = CallaЫ e[ [i nt], No ne]
@d ata cla ss( fro zen=True, order=Tr ue)
class Task :
sc heduled : int
callb ac k: Callback = field ( compare= False)
delay : int = field ( defa ult=0, compare= False)
li mit : int = field ( def aul t= l, compare= False)
def repeat (s elf, curr ent_ ti me : int ) -> Optional [" Ta sk" ]:
if self . delay > 0 and sel f.l imit > 2:
return Task(
)
cur rent_ ti me + self . delay,
cast (C allback, self .c all ba ck) , # type : ignore [m isc ]
self . delay,
self . li mit - 1,
elif self . delay > 0 and self .l imit 2:
return Ta sk(
cur re nt_t ime + self . delay,
cast (C allback, self .c allba ck) , # type : ignore [m isc ]
else :
return None
В опре делении класса Task есть два обязател ьных и два необязательных поля.
Об язательные поля, sc heduled и callback, опре деляют запланированное время
для выполнения какого-либ о дейс твия и функцию обратного вызова - действ ие,
которое должно быть выпо лнено в запланированное время. Запланированное
время имеет тип int; для сверх точных опе раций модуль времени может ис­
пользовать в качестве времени и число с плавающей запятой. Однако излишние
детал и здесь лучше прои гнорировать. Кроме того, инструмент mypy прекрасно
знает, что целые числа можно принудительно преобра зовы вать в числа с пла­
вающей запятой, поэтому в отношен ии числовых типов не нужно стремит ься
к сверхточности.
Обра тный вызов имеет подсказку CallaЫe [ [ int], None]. Это обоб щает внешний
вид оп редел ения функци и. Опре деление функции обратного вызова должно
выг лядеть как def so me_n ame(a n_a rg : int ) -> None. Если оно не совпа дает
с данным опис анием, туру предупредит о потенциа льном несоответствии
между оп реде лением фун кции обра тног о вызова и контрактом, указанным
в подс казке типа.
