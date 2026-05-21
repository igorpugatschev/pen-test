# Объектно-ориентированный Python, 4-е издание — страница 316

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти ческ ое исследован ие 31 5
Tra ini ngK nownSam ple (s epal_leng th =S .1 , sepa l_wi dth= З.5 ,
pe tal_J cng th=l .4, pc tal width-0 .2 , spec ies= 'I ris- setosa ')
# Так нежела1с льно ...
>>> sl. cla ssi fi cat io n = wrong
>>> sl
Trainin gKno wnSample (s cpal _le ngt h"� .l , sepa l_ wid th=3 .5 ,
pe tal leng th=l .4, pet a l_ width - 0.2 , spec ies= 'I ris- setosa ')
>>> sl .cl assifi catio n
wrong
Как правило, Python не запрещ ает нам создавать новый атрибут, например
classi fication, в объекте. Однако такое разрешение с его стороны может быть
источником скрытых ошибок. (Х орошее модульное тестирование часто выявляет
такие ошибки .) Обратите внимание, что дополнительный атрибут не отражается
при работе метода _repr _( ) или сра внениях метода _eq_ (� этого класса.
Пр облема не является серьезной. В последующих разделах мы будем реша ть ее,
используя замороже нные классы данных и класс typing . NamedTuple.
Остальные классы в нашей модел и не получают таких огромных преи муществ
при реализации в виде классов данных, какими являются классы Sample. Ког­
да у класса много атрибутов и мало методо в, определение @dataclass окажет
большую помощь.
Еще один класс, который больше всего выи грал от использования @dаtас lа ss, -
это Hyperpa rameter. Ниже при ведена перва я часть опре деления, тело метода
опущено:
@d ata class
class Hyperpa rame ter :
""" Конкретный на бор па раметров настройки с k и ал го рит мом расст ояни я"""
k: int
al gorithm : Distance
data : weak ref .R efe renc eType [" Trainin gData "]
def clas sif y( self, sample : Sam ple) -> str :
""" Ал го рит м k-NN"""
Здесь выявлена одна интересная особенность, которая становится дост упной,
когда испол ьзуется запись from _f utu re_ import annotat ions. В частнос ти,
существ ование значения weakr ef . Refe renc eType [ "Trainin gData "] имеет два
различных предназначения:
• инструмент mypy обращается к нему для проверки ссылок на типы. Необходим
квалифик атор, weakr ef . Refe renceType [ "TrainingData "]. В этом случае строка
используется как прямая ссылка на еще не определенный класс Traini ngData;
