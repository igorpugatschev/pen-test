# Объектно-ориентированный Python, 4-е издание — страница 570

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Пок ер
CardGame Factory
+make_card(r ank , sui t): Card
+m ak_hand(c ards ): Hand
Па тте рн Абстрак тная фабр и ка 569
Game
+deck: List[Card]
+han d: Hand
+deal(): Hand
+score( hand :H and )-> List[T rick]
Баз а
Hand
Card
rank: in t
suit: Sui t
CardGameF actory
+mak e_card(r ank, suit): Card
+mak _hand(c ards) : Hand
4
CribbageF ace
Рис. 12 .8. Абстрак тная фабр и ка без абс тр актны х ба зовы х классов
В этом случае Абстрактна я фабрика становится концепцией, а не фактич еским
абстрак тным базовым классом. Необходимо для всех классов, которые прет ен­
дуют на роль реализаций CardGameFactory, составить адекватную докуме нтацию
в строках документ ации. Уточ ним намерения, определив протокол с помощью
typing . Protocol. Например, так:
class Ca rdGam eFac tor yProtoc ol (P rotocol ):
def make_car d( self, ra nk : int, suit : Suit ) -> "Car d" :
def make_hand (s elf, *car ds : Card ) -> "H and" :
