# Объектно-ориентированный Python, 4-е издание — страница 501

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

500 ГЛ АВ А 11 Об щие пап ерн ы про екти рован ия
в данном случае фак тически не нужен. Контекст, в котором используется атот
класс, дост аточен для туру, чтобы подтверд ить, что рассма триваемый класс со­
ответствует требуемому протоколу Observer. Хотя нам не нужно указывать, что
это Observer, это может помочь проанализирова ть, что данный класс реализует
протоко л Observer.
В интерак тивной консоли протестируем наблюдатель SaveZonkHand:
>» d = Dice . fro m_text ("б dб" )
>» pl ayer = ZonkHa ndHistor y( "B o" , d)
>>> sa ve_h ist ory = SaveZonkHa nd ( play er)
>>> play er. attach ( sa ve_h ist ory )
>>> rl = player .s tar t()
SaveZ onkHand {' player ': 'В о', ' sequence 1, 'ti aпds ' '[ [1, 1, 2, 3, 6,
6] ] ·, 't i me ' : 1609619907 .5 210 9 }
>>> rl
[ 1, 1, 2, 3, 6, 6]
>>> r2 = pla yer .r ol l()
SaveZ onkHand {' playe r' : 'В о', 's equence ' : 2, ' tiands ': ' [[ 1, 1, 2, 3, б,
6] , [ 1, 2, 2, 6, 6, 6] ] ' , ' t ime ' : ... }
После присоединения наблюдателя к объекту In ventory всякий раз, когда изменя­
ется одно из двух наблюдаемых свойств, вызы вается наблюдатель и его действие.
Обратите внимание, что наблюдатель отслеживает порядковый номер и включает
временную метку. Метки не входят в определение игры и отделены от основ ной
ее обрабо тки, поскольку являются частью класса наблюдателя SaveZonkHand.
Мы можем добавить несколько наблюдателей различных классов. Например,
добав им второй наблюдатель, у которого есть ограниченная работа по проверке
трех пар, и объявим об этом:
class ThreePai rZonkH and :
"" "Observer of Zon kHandHistory" '"'
def �init �( self, hand : ZonkHandHi stor y ) -> None :
self .h and = hand
self . zonked = False
def �c all �{ self) -> None :
la st_ roll = self .h and . ro lls [-1]
dis tinc t_values = set { la st_rol l)
self . zon ked = len {dis tinct _va lues ) == З and all {
la st_ro ll . count (v) == 2 for v in distinc t_values
if self . zon ked :
prin t{"З Pair Zonk !" )
В данном при мере мы не оп реде ляем Obser ver в качестве суп еркласса. Мы
доверил ись инструменту туру, который заметит, как исполь зуется этот класс
и какие протоколы тот должен реализовыва ть.
