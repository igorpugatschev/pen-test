# Объектно-ориентированный Python, 4-е издание — страница 214

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти че ское иссле дование 21 3
Гипотеза о возможности альтернативных форма тов предпола гает, что класс
Trainin gData не должен зависеть от определения строки dict [ str, st r], пред­
ложенного обработкой СSV-ф айла. Словарь добавляет в класс Trainin gData
детали, которые могут тому не принадлежать. Детали предста вления исходного
документа не имеют ничего общего с управлением коллекцией обучающих и те­
стовых образцов. Как раз здесь объектно-ориентированный дизайн поможет нам
разобраться в данных и разделить их на две упомянутые выше целевые категории.
Для сопрово ждения нескольких источников данных необходимо использова ть
некоторые общие правила проверки входных значений. Нам понадоб ится сле­
дующий класс:
class SampleRe ader :
See iris . names for attribute ordering in bezdeki ris . data file
ta rget_ class = Sample
header = [
"s epal _length ", "s epal _wid th ",
"p etal _leng th ", "p etal _wid th ", "class"
def �init �( self, sour ce: Path) -> None :
self . source = source
def sample _iter ( self) -> Ite rat or [ Sample ]:
ta rget_c lass = self .t ar get_c lass
with self .s ource . open () as source _fi le :
reader = cs v. DictRead er( sour ce_file, self . heade r)
for row in read er :
tr y:
sample = ta rget_ class (
sepal _leng th =float (r ow[" sepa l_l ength "]),
sepa l_width=float (r ow[" sepal _width "]),
peta l_l eng th=flo at (r ow[" petal_leng th "]),
petal _width=float (r ow[ " peta l_wid th "]),
excep t ValueErr or as ех :
raise BadSampleRo w(f" Invalid {r ow!r }") from ех
yield sample
Этот код создает экземпляр суперк ласса Sample из полей ввода, прочит анных
экземпляром CSV DictReader. Метод sample _ite r( ) исполь зует серию выра­
жений для преобразования входных данных из каждого столбца в полезные
объекты Python. В примере выше предста влены несложные преобра зования,
а реализация представляет собой набор функций float ( ) перево да строковых
