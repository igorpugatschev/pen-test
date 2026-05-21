# Объектно-ориентированный Python, 4-е издание — страница 500

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Па тте рн Н аб л юдател ь 499
Рассмотрим интересующую нас часть игры Zonk в следующем примере:
from typing impor t List
Hand = Lis t [i nt ]
class ZonkHandHi stor y (O bser vaЫe) :
def �init �( self, player : str, dice _set : Dice) -> None :
supe r() .� ini t�< >
self .p layer = player
self .d i ce_set = dice _set
self .r olls : list [Hand ]
def star t (s elf) -> Hand :
self .d ic e_s et .r ol l()
self . rol ls = [s elf . dice _set .d ice]
self ._ not if y_observers () # Измен ение сост ояния
return self .d i ce_set .d ice
def ro ll( self) -> Hand :
self .d i ce_set .r ol l()
self .r olls . append (s elf .d i ce_set .d ice)
self . _not ify_observ er s() # Изм енение сост ояни я
return self .d i ce_set .d ice
При важных изменениях состоя ния этот класс вызы вает sel f. _not i fy_ obser­
vers () , тем самым уведомляя все экземпляры наблюдателя. Наблюдатели могут
кэшир овать копии бросков, отправлять данные по сети, обно влять виджеты
в графическом интерфейсе и многое другое. Метод _not if y_ obser ver s( ), уна­
следов анный от ObservaЫe, переби рает всех зарегист рирова нных наблюдателей
и сообщает каждо му, что сост ояние бросков изменилось.
Теперь реализуем простой объект -наблюдатель, выводящий некоторое состоя­
ние на консоль:
class SaveZonkHa nd (O bser ver) :
def �init �( self, hand : ZonkHa ndHi story ) -> None :
self . hand = hand
self . count = 0
def �c all �( self) -> None :
self .c ount += 1
messag e = {
}
"pl ayer ": self .h and . player,
"s equence ": self . count ,
"h ands ": js on . dumps (s el f. hand .r olls ),
"tim e" : ti me .t ime(),
print (f" SaveZon kHand {messa ge}" )
Здесь нет ничего особенно сложного. Наблюдаемый объект настраивается в ини­
циализаторе, и, когда вызы вается наблюдатель, мы что -то делае м, например,
как в коде выше, выводим строку. Обра тите внимание, что суперк ласс Observer
