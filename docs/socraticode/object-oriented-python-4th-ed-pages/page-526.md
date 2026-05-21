# Объектно-ориентированный Python, 4-е издание — страница 526

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Па тте рн С ин глто н 525
Этот вариант класса NMEA_ State не имеет пере менных экземпляра. Все методы
работают со значениями аргументов, переданными клиентом:
class Waiting( NMEA_St ate) :
def fee d_byt e(
self,
mess age : "M essag e",
inp ut : int
-> "N MEA_S ta te" :
return self
if input == or d( b"$" ):
return HEA DER
return self
class Heade r( NMEA _State ):
def enter (s elf, mess age : "Messag e" ) -> "N MEA_S tat e" :
mess age . rese t ()
return self
def fee d_byt e(
self,
message : "Messag e",
in put : int
-> "N MEA_S ta te" :
return self
if input == or d(b "$" ):
return HEA DER
size = mess age . body _append (i nput )
if size == 5:
return BODY
return self
class Body ( NMEA _Sta te) :
def feed _byt e(
self,
mess age : "Messag e",
inp ut : int
-> "N MEA_St ate" :
ret urn self
if in put == or d(b "$" ):
return HEA DER
if input == or d(b"* "):
return CHE CK SUM
size = mess age . body _append (i nput )
return self
class Checksum( NMEA_St ate ):
def fe ed_byt e(
self,
mess age : "Messag e",
inp ut : int
-> "N MEA_S ta te" :
return self
if inp ut == or d(b" $" ):
return HEA DER
