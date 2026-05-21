# Объектно-ориентированный Python, 4-е издание — страница 581

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

580 ГЛАВА 12 Н овы е па п ерны проек ти рован ия
собств енный метод (чтобы было легко выборочно переопределить любой шаг),
и имеется еще один управля ющий метод, вызывающий по очереди эти шаги.
Без какого -либо содержимого метода класс может выг лядеть как первый шаг
на пути:
class Que ryTem plate :
def _init _( self, db _name : str "s ales .d b" ) -> None :
def connect (s elf) -> None :
pass
def construct _query (s elf ) -> None :
pass
def do _query (s elf) -> None :
pass
def outp ut_c ontext (s elf) -> Contex tManag er[T ext IO] :
pass
def outp ut_r esul ts( self) -> None :
pass
def proces s_fo rmat (s elf) -> None :
self . connect ()
self . constru ct_ quer y( )
sel f. do_ quer y ( )
self . format_re sults ( )
self . outp ut_r esul ts( )
Метод proces s_fo rmat() является основным методом, вызываемым внешним
клиентом. Он гарантирует, что каждый шаг выпо лняется по порядку , независи­
мо от того, реализован этот шаг в классе или в подклассе. Для наших приме ров
мы ожидаем , что методы constru ct_q uer y () и output_ context () , скорее всего,
изменятся .
Испо льзуя абстрак тный базовый класс, форма лизуем ожидае мый результат.
Альтернативой для отсутст вующего метода в шаблоне является вызов исклю­
чения Notimplemente dError. Если создать подкласс QueryTemplate, это обеспечи т
проверку во время выпо лнения. И возможно, стоит сделать намеренную ошибк у
в имени, чтобы переопр еделить метод constru ct_ quer y( ) .
Оста льные методы двух рассмат риваемых классов будут идентичны:
class Que ryTem plate :
def _init _( self, db _name : str = "s ales .d b" ) -> None :
self . db _name = db _name
self .c onn : sqli teЗ . Connection
