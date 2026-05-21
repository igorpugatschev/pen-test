# Объектно-ориентированный Python, 4-е издание — страница 527

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

526 ГЛ АВА 11 Об щие патте рны проек ти рован ия
if in put in {or d(b" \ n"), or d( b" \ r" )}:
# Непо лная ко нт рол ьная сумма ... Будет не вали дной .
return END
size = mess age .c hecksu m_append (i nput )
if size == 2:
return END
return self
class End ( NMEA _S ta te) :
def feed _byt e(
self,
mess age : "Messag e",
input : int
-> "N MEA_Sta te" :
return self
if input == or d(b "$" ):
return HEA DER
elif input not in {or d(b" \ n"), or d(b" \ r" )}:
return WAIТIN G
return self
def valid ( self, mess age : "Messag e" ) -> bool :
return mess age .v alid
Ниже представл ены переменные уровня модуля , созд анные из экземпляров
каждого класса NMEA_St ate.
WAITIN G = Wa itin g( )
HEADER = Header ()
BODY = Body ()
CHEC KSUM = Checksu m( )
END = En d()
Для изменения состояния внутри каждого из этих классов в процессе синтак­
сического анализа можно обращаться к этим пяти глобальным перем енным.
Возможнос ть сс ылаться на глоба льную перем енную, оп реде ленную после
класса, поначалу кажется немного сложной. Но она отлично работает, так как
имена перемен ных Python не преобр азуются в объекты до начала выполнения.
При создании каждого класса имя типа CHECKSUM представляет собой не более
чем набор симв олов. Но при оценке метода Body. feed_byte () уже необхо димо
вернуть значение CHECKSUM, тогда имя будет разрешено для экземпляра Синг лтон
класса Checksum( ) .
Обра тите внимание на реорг анизацию класса Header. В версии, где каждое
сост ояние имеет _init_( ), при входе в сост ояние Header мы можем явно оце­
нить Mess age . reset ( ). По скольку в этом проек те мы не создаем новые объекты
