# Объектно-ориентированный Python, 4-е издание — страница 218

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти ческ ое иссле дование 21 7
Sample
sepal_length: float
sepal_width : float
petal_length: float
petal_width : float
/ KnownSample � о sample_id: int Un known Sample
о species: str о classifi cati on: Classification о purpose: Purpose
о classificati on: Classification classify( param: Hyperparamet er) -> str
classify(param: Hyperparamete r) -> str
/ � Classification
species: str
parameter: Hyper parameter
Рис. 5. 1. Диа гра мма класса Sa mpl e
Мы усовершенс твовали иерархию классов, чтобы отразить два принципиа льно
разных типа обра зцов.
• Экземпляр KnownSample испо льзуется для тестирования или обу чения.
Отличие от других классов реализуется в методе , выпо лняющем класс и­
фи кацию. Оно зависит от атрибута purpose, изобра женного с маленьким
квадратом (и ли иногда знаком - ) в качестве префикса. В Python не суще­
ствует при ватных перем енных, но этот маркер может быть полезен как
предуп режд ающий в качестве примечания к дизайну. А общедост упные
атрибуты изоб ражаются с маленьким кружком (и ли знаком +) в качестве
префикса.
Когда purpose имеет значение Train ing, метод classi fy () вызове т ис­
ключение. Образец не может быть перекла ссифицирован. Это све дет
обучение к нулю.
Когда purpose имеет значение Testi ng, метод classi fy( ) будет работать
корректно, применяя заданный Hyperpa ramet er для вычис ления вида.
