# Объектно-ориентированный Python, 4-е издание — страница 253

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

252 ГЛАВА 6 Абстрак тны е класс ы и пере грузка операто ров
. .. def �set 1tem �( self, key , value ) -> None :
. . . if key in self :
. . . ra1se Va lu eE rror (f" dupl нate {k cy l r} ')
. . . super( ). � set1te m�( key, value )
Выполнив его, получим следу ющее:
>>> nd = NoDu pDict ()
>» nd ["a"] = 1
»> nd [" a"] = 2
Traceback (m ost recent call las t) :
Fi le "<d octest examples .m d[l O]>", line 1, in <m odule>
nd ["a '] = 2
Fil e "<d octest exam ples .m d[7]>", line 4, in
raise Va lueE rror (f" dupl ica te {k eylr }")
Va lueE rror : dupli cate 'а'
setitem
Мы еще не закончили, но получается все очень даже неплохо.
В некотор ых случаях наш словарь отклоняет дубликаты. Однако он не блоки­
рует повторяющиеся ключи при попытке создать словарь из другого словаря.
А не хотел ось бы, чтобы это имело место:
»> NoDu pD1ct ({" a" : 42, "а" · 3.1 4})
{' а' : З. 14}
Итог: одни выра жения правильно вызы вают исключения, в то время как другие
по-пр ежнему тихо игнорируют повторяющиеся ключи.
Основ ная проблема заключается в том, что не все методы, устанавл ивающие
элементы, испо льзуют _set i te m_ ( ). Чтобы преодолеть это, понадобится пере­
определить _in it_ ( ) .
Необходи мо еще и добавить подсказки к первона чальному коду. Это позволит
использовать туру, чтобы убедиться, что созданная реализация в целом работает.
Пр оанализируем следующий код с методом _in it_ ( ):
fr om �f utu re� impor t ann ot ations
from typing impor t cast, Any , Union, Tuple, Dict , IteraЫe, Mapping
from collections impor t HashaЫe
Dictlnit = Union [
IteraЫe [T uple [H ashaЫe, Any ] ],
Mapping [H ashaЫe, Any] ,
No ne]
class NoDu pDict (D ict [H ashaЫe, Any ] ):
def �setitem �( self, key : HashaЫe, value : Any ) -> None :
