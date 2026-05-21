# Объектно-ориентированный Python, 4-е издание — страница 243

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

242 ГЛАВА 6 Абстр ак тны е клас сы и перег рузка о перато ров
положе нию при удержании некоторых из них и повторном броске оставш ихся.
В этом случае будет полезным использование индексов целочисленного спи ска.
Данный подкласс реализует правило броска всех кубик ов:
class Si mpleDi ce (D ic e) :
def ro ll( self) -> No ne :
for d in self .d ice :
d. ro ll( )
Каждый раз, когда приложе ние выпо лняет функцию roll ( ) , все кубики обнов­
ляются:
>>> sd � S1 mpleD1 ce(6, Dб )
>» sd . ro ll ()
>» sd . to tal
23
Об ъект sd является экземпляром конкретного класса SimpleDice, созданного
из абстрактного класса Dice. Экземпляр SimpleDice содержит шесть экзем­
пляров класса Dб. Это также конкре тный класс, создан ный из абстрактного
класса Die.
Рассмо трим еще один подклас с, он предоставит соверш енно другой набор
методо в. Некоторые из них заполняют пробе лы, остав ленные абстрак тными
метод ами. Другие считаются уникальными для подкласса:
class YachtDice (Dic e) :
def �init �( self) -> None :
sup er( ) .� in it�( S, Dб)
self .s aved : Set [i nt ] = se t()
def saving (s elf, positio ns : IteraЫe [in t] ) -> "YachtDice ":
if not all (0 <= п < 6 for п in positio ns) :
raise Va lueErr or (" Invalid position ")
self . saved = set (p ositio ns)
retur n self
def ro ll( self) -> None :
for п, d in enumera te( self .d ice) :
if п not in self .s aved :
d.r ol l()
self . saved = se t()
В конечном счете мы с вами создал и набор сохране нных позиций. Из начально
он пуст. Чтобы предостав ить итерируемую коллекцию целых чисел в качестве
позиций для сохран ения, можно испо льзовать метод sav e():
>>> sd � Ya ch tD 1c e( )
»> sd . r'ol l ()
>» sd . d1ce
