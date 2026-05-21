# Объектно-ориентированный Python, 4-е издание — страница 567

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

566 ГЛАВА 12 Н овы е па ттерны пр оек ти рован ия
соответс твенно. Также по надобится Абстрактна я фабр ика, которая создает
«карты� и «руки�:
import аЬс
class Ca rdGam eF actor y(a bc .A BC) :
@abc . abstra ctmethod
def make_ car d ( self, ra nk : int , sui t : Suit ) -> ··car d" :
@abc .a bstr ac tmethod
def make_hand ( self, *car ds : Card ) -> "Han d" :
Здесь фабр ика выступает настоящим абстрак тным базовым клас сом. Каждая
отдел ьная игра должна предоставлять рас ширения для уникальных игровых
функций Hand и Car d. Кроме того, в игре будет реализован класс CardGameFactory,
котор ый создает ожидаемые классы.
Мы можем определить карты для крибб еджа следующим обра зом:
class Cri bbageCard (Car d) :
@property
def poin ts( self) -> int :
return self .r ank
class Cri bbag eAce(C ar d) :
@property
def poin ts( self) -> int :
return 1
class Cri bbag eFace( Card ):
@property
def poin ts( self) -> int :
return 10
Все приведенные в коде расш ирения базового класса Card имеют дополнительное
свойс тво очков. В криббедже одним из приемов является любая комбинация
карт на 15 очков. Большинс тво карт имеют очки, равные рангу, но валет, дама
и король соответствуют 1 О очкам. Это означает, что расширение Напd имеет до­
вольно слож ный метод подсчета очков, который пока опусти м.
class Cri bbageHand (H and) :
star ter : Card
def upcard ( self, star ter : Car d ) -> "Han d" :
self .s tarter = star ter
return self
def scoring (s elf) -> list [T ri ck] :
""" l S's. Pairs . Runs . Right Jac k."""
... deta ils omitted
return tricks
