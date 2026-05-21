# Объектно-ориентированный Python, 4-е издание — страница 103

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

10 2 ГЛАВ А 2 Об ъе кты в Python
У нас есть два специфичных для прило жения метода класса Sample. Они по­
казаны в следующем фрагменте кода:
def classi fy( self, classi fica ti on : str) -> None :
self .c lassi fication = classi ficat ion
def match es ( self) -> bool :
ret urn self .s pecies == self .c lassi fica tion
Метод classi fy () определяет изменение сост ояния с неклассифицирован ного
на классифицирован ное. Метод match () сравнивает результаты классифи кации
с видом, назначенным Ботаником. Это испол ьзуется для тестирован ия.
Ниже при веден пример того, как могут выг лядеть изменения состоя ния:
>>> fr om mod el import Sample
»> s2 = Sam ple(
sepa l_ length= S.l , sepa l_ widt h=3 .5 , petal_J eng th=l .4, pe tal
width=0 .2 , spe cies="Iris- setosa ")
>>> s2
Kno wnSam ple( sepal _leng th=S .l , sepal _wi dth= З.5 , petal_leng th=l .4 , petal_
width=0 .2 , species= 'I ris- setosa ')
»> s2 .c l ass ification = "wrong"
»> s2
Kno wnSam ple ( sepal _leng th=S .l , sepal _w idth= З.50 pctal_length= l.4 , pe tal_
width=0 .2 , species= 'I ris- setosa ', classi fica ti on= ' wrong ')
Итак, уже имеется работающее определение класса Sample. Метод _repr _( )
довольно сложен, что предполагает некоторые возможные улучшения.
Это может помочь опре делить ответств енность для каждого класса. Например,
в виде краткого перечня атрибутов и методов с небольшим допо лнительным
обос нованием, связывающим их вместе.
Отв етств енн ость клас са
Какой класс отве чает за фактическое выполнение теста? Вызы вает ли класс
Training класс ифи катор для каждого KnownSample в тестах? Или, возможн о,
он предоставляет данные для тестирования классу Hyperparameter, делегируя
ему также и тести рование? По скольку класс Hyperpa rameter отвечает за значе­
ние k и за алгоритм нахождения ближайшег о окружения значения k, кажется
разумным, чтобы класс Hyperpa rameter запус кал тест, испо льзуя собстве нное
значение k и предоставл енный ему список экземпляров KnownSample.
Также кажется очевидным, что класс TrainingData является приемлемым местом
для записи различных версий класса Hyperpa rameter. Это означает, что класс
