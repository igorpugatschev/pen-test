# Объектно-ориентированный Python, 4-е издание — страница 234

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Container
Со зда ние абс тр актног о ба зовог о класса 233
lteraЫe Sized
+ _con tains_J item) +_iter_J) + _len_(item)
Collection
Mapping
+ _getitem_J key)
+k eys()
+i tems()
+ values()
+ get(key, default)
MutaЫeMapping
+ _setitem_Jkey, va/ue)
+ _delitem_(key)
dict
Рис . 6.2 . Абст рак ции Mapping
Мы видим, что определение Mapping зависит от определения класса Collection.
Оп ределение абстра ктного класса Collection, в свою очередь, зависит от трех
других абстрак тных базовых классов: Sized, IteraЫe и Container. Каждая из
этих абстрак ций требует специальных методов.
