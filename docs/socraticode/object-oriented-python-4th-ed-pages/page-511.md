# Объектно-ориентированный Python, 4-е издание — страница 511

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

51 0 ГЛАВА 11 О бщие паттерн ы про екти рован ия
Примем, что каждая часть броска костей - отдельная команда. Одна команда
определяет бросок костей, а затем с помощью последующих команд корректиру­
ются значения кост ей. Ск ажем, Зd6+2 означает бросок трех кубиков (на пример,
!П], !П], ISI) и добавл ение 2, чтобы получить в сумме 13. В целом класс выглядит
следующим обра зом:
class Dice :
def �init �( self, п: int , d: int , *adj : Ad ju stment ) -> No ne :
self .a djus tments = [c ast (A djus tme nt , Roll (n, d) )] + list (a dj )
self .d ice : list [i nt ]
self .m odifi er : int
def ro ll( self) -> int :
for а in self . adj ustmen ts :
a. apply (s elf)
return sum( self .d ice) + self .m odifier
При необходимости нового броска костей объект Dice применяет для создания
нового броска отдельные объекты Adjustment. В методе _i ni t_ () показан один
из видов объектов Adjustment: объект Roll. Сна чала это добавляе тся в после­
дова тельность коррек тировок. По том любые дополните льные корректи ровки
обраба тываются по порядку. Каждая корректи ровка - другой вид команды.
Ниже приведены виды команд настройки, изменяющие состоя ние объекта Dice:
class Ad ju st ment (a bc .A BC) :
def �init �( self, amount : int ) -> None :
self .a mount = amount
@abc .a bstract method
def apply (s elf, dice : "D ic e" ) -> None :
class Rol l( Adj u stment ):
def �init �( self, п: int , d: int ) -> None :
self .n = п
self .d = d
def apply (s elf, dice : "Dic e" ) -> None :
dice . dice = sorted (
rando m .r andint (l, sel f.d) for in range (s el f.n) )
dice . mod ifier = 0
class Drop (A djus tment ):
def apply (s elf, dice : "Di ce" ) -> None :
dice .d ice = dice .d ic e[s elf . amount :]
class Keep (A djus tment ):
def apply (s elf, dice : "Dic e" ) -> None :
dice . dice = dice .d ic e[ : self . amou nt ]
