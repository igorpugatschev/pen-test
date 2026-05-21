# Объектно-ориентированный Python, 4-е издание — страница 556

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

@overload
def �g etitem �( self, index : slice) -> byt es :
Па тте рн Л егк овес 555
def �get item �( self, in dex : Union [i nt, slic e] ) -> Union [i nt , byt es ]:
return self .c ontent [i ndex ]
Это опре деление класса Buffe r в действ ительности не содержит много нового
кода. Мы предостав или три специальных метода, которые делегировали работу
базовому объекту bytes. Абстрак тный базовый тип Sequence предоставляет не­
сколько методов, таких как index( ) и count().
Три опре деле ния перегруже нного метода _get item_( ) - это то, как мы со­
общаем туру о важном различии между такими выр ажениями, как buff er [i]
и buf f er [s tar t : end]. Пе рвое выр ажение получа ет из буфера один элемент
типа int, второе испо льзует срез и возвращает объект bytes. Окон чательное
опре деление метода _get i tem_ () реализует две перег рузки, делегируя работу
объекту self . content s.
Еще в главе 11 вы изучили испо льзование дизайна на основе состо яний для
получения и вычисления контрольных сумм. Но сей час для работы с большим
объемом бы стро поступающих сообщений G PS применим другой подход.
Поступим вот так:
>» raw = Buffer (b"$ GPG LL ,3 75 1.6 5,S,1 4507 .3 6, E * 77" )
Сим вол $ обозначает начало сообщения. Симво л * обозначает конец сообщения .
Симво лы, следующие за звездочкой *, являются значением контрольной суммы.
В этом приме ре мы прои гнорируем два байта контрольной суммы, предполагая ,
что это правильно. Рассмотрим абстрактный класс Mess age с некоторыми общими
методам и, помог ающими анализировать сообщения GPS:
class Me ssag e(a bc .A BC) :
def �init �( self) -> None :
self .b uff er : wea kr ef . Refe renc eType [B uff er]
self . offset : int
self .e nd : Opt iona l[i nt ]
self . co mmas: lis t [i nt ]
def fr om_buffe r( self, buff er : Buf fe r, off set : int ) -> "Messag e" :
self .b uffer = wea kref .r ef( buffe r)
self . offset = offset
self . co mmas = [o ffset ]
self .e nd = None
for index in range (o ffset , off set + 82) :
if buf fer[ index ] == or d(b ", "):
self . commas . append ( index)
