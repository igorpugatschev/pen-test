# Объектно-ориентированный Python, 4-е издание — страница 565

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

564 ГЛ А ВА 12 Н ов ые паттерн ы пр оек ти рован ия
П риме р реал иза ци и папер на Абстра ктна я фа бр ика
UМ L-диаграмму классов для паттерна Абстрактная фабрика сложно понять без
конкретного примера, поэтому сначала рассмотрим такой пример. Им еется две
карточ ные игры, покер и криббедж. Не беспокойтесь, вам не нужно знать все
правила. Отме тьте для себя только то, что некоторые аспекты у них схожи, но
детал и различаются. Схема действ ий ниже, на рис. 12 .7.
Game
+deck: List[Card]
+han d: Hand
+dea l(): Hand
+Score( hand :H an d)-> List [Trick]
1 CardGameFactory
+mak e_card(rank, suit): Card
+mak _hand( cards): Hand
Вы полн ени е
к рибб� - Покер�
Cri bbage Factory PokerF actory
Вып олн ени е
+m ake car d(r aпk, suit): card ---- +m ake_car d(r aпk, suit): card
� +mak _haп d( card s) : Hand +mak_hand( card s ) : Hand
1 ,.
Hand
Cri bba geHand --- � cards: List(Car d)
+upcard(card: Card)
/ v...
�
4 Card 1 PokerHand 1
Crib bageCar d """ rank: int н � suit: Suit
+poin ts: in t
�------- ,..___ 5
1 н
1 Poke rCard 1
� --
CribbageF ace 1 1 Cribb ageFace
Рис. 12 .7. Па ттерн Абстр актная фабр и ка на пр и м ере так их ка рточн ых и гр,
ка к пок ер и крибб едж
1
