# Объектно-ориентированный Python, 4-е издание — страница 520

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Патт ерн Состоя ние 51 9
сообщ ения, с символа $. При обнаружении символа $ синтаксический анализатор
переходит в новое состо яние, Header:
class Wa iting ( NMEA_S ta te) :
def feed _byte( self, input : in t) -> NMEA_State :
if inp ut == or d(b "$" ):
return Head er( self .m essag e)
return self
Находясь в состоя нии Header, мы обнаруживаем символ $ и ждем пять символов,
идентифицирующих передатчик сообщ ений (GP) и тип предложе ния (напри­
мер, GLL).
Мы будем накапли вать байты, пока не получим пять, а затем перейдем в со­
стоя ние Body:
class Heade r( NMEA _Sta te) :
def _init _(se lf, mess age : "Messag e") -> None :
self .m essa ge = messag e
self . mess age . reset ( )
def fe ed_by te( self, input : int ) -> NMEA _St ate :
if inp ut == or d(b" $" ):
return Head er( self . messa ge )
siz e = self .m essa ge . body _appe nd ( input )
if size == 5:
return Body (s elf .m essa ge )
return self
Состоя ние Body - это состояние, в котором накапли вается больша я часть со­
общения. Для некоторых приложений мы можем приме нить дополн ительную
обработку и при получении необходимого типа сообщения вернуться к ожиданию
заголовков. При работе с устройствам и, производ ящими большое количество
данных, это может немного сок ратить время обра ботки .
Когда при ходит символ *, тело гото во, и след ующие два байта должны быть
частью контрольной суммы. Это означает переход в состояние Chec ksu m:
class Body ( NMEA_Sta te) :
def fe ed_by te( self, in put : int ) -> NMEA_St ate :
if input == or d(b" $" ):
return Header (s elf . messa ge )
if inp ut == or d(b "*") :
return Chec ksu m( self . mess age )
self . mess age . body _append ( in put )
return self
Состоя ние Checksum похоже на накопление байтов в состоя нии Header: мы ожи­
даем определенное количество входных байт ов. По сле вычисления контрольной
суммы за большинством сообщ ений следуют символы AS CII \r и \n. Если мы
