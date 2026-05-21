# Объектно-ориентированный Python, 4-е издание — страница 171

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

17 0 ГЛ АВА 4 Ож ида емы е нео жида нн ости
Sample
sepal_length: float ClassifierApp sepal_width : float
petal_length: float
petal_width : float / classify(sample)
"\ ,"'"о ""'о'а"'�"" '"''
Un knownSample Training Data
classification: str load_samples(path) /
Создание
KnownSample
species: str
1 \ Testing KnownSample Training KnownSample
Рис. 4.3. Созда ние объе кта
Схема включает два класса, которые будут создавать два типа обра зцов. Класс
Train ingData будет загружать известные образцы. Общий класс Class ifier App
будет про верять неизвестный образец и класс ифици ровать его.
Объект KnownSample имеет пять атрибутов, каждый из которых содер жит опре­
деленный набор допус тимых значений.
• Измерения sepal _leng th, sepal _w idth, peta l_l ength, peta l_ width - числа
с плавающей запят ой. Для этих значений существует нижняя граница - 0.
• Значение species, предоставл енное экспертом, является строкой с тремя
допус тимыми значениями.
Объект UnknownSample имеет только четыре измерен ия. Идея общего опре­
деления супер класса помог ает обеспечить повторное испо льзование такой
обрабо тки.
