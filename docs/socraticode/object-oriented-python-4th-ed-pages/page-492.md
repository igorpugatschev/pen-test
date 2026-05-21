# Объектно-ориентированный Python, 4-е издание — страница 492

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

-> None :
self .d ice _roller dice
self . remote _addr remote_ addr
Па тте рн Дек ор ато р 491
def �c all �( self, req uest : bytes ) -> byt es :
print (f" Receiving {r equest !r } fr om {s elf . remote _ad dr }")
dice _roller = self .d ice _rol ler
response = dice _roller( request )
print (f"S ending {r esp onse !r } to {s elf . remot e_add r} ")
return resp on se
Ниже представл ен прим ер второг о декоратора, кото рый сжим ает данные, при­
меняя сжатие gzip для полученных байт ов:
import gzip
import io
class ZipRol ler :
def �init �( self, dice : CallaЫe [[ bytes ], bytes ]) -> None :
self .d i ce_roller = dice
def �c all �( self, req uest : bytes ) -> byte s:
dice _roller = self .d ice _roller
response = dice _roll er( reque st)
buffer = io . BytesI O( )
with gzip .G zipFile (f il eobj = buffe r, mode= "w" ) as zip file :
zip fi le . write (r esp onse )
return buffer .g et value ()
Этот декор атор сжима ет входящие данные перед их отправкой клиенту. Он де­
кори рует базо вый объект dice _r oller, вычисляющий ответ на запрос.
Теперь, когда имеется два декоратора, напишем код, который наклады вает один
декоратор на другой:
def dice _re sp ons e(c lient : soc ket .s oc ket ) -> None :
request = cl ient . recv ( 1024 )
tr y:
remote _addr = cl ient . get peern ame ()
ro ller _l ZipRoller (dice .d ice _rol ler)
ro ller _2 = LogR oller ( ro ller _l , remot e_addr= remote _add r)
res pon se = ro ller _2( request )
excep t (ValueError, KeyE rr or) as ех :
response = re pr(e x) .e nco de( "u tf-8" )
cli ent .s end ( resp on se)
Цель состоит в том, чтобы разделить три асп екта этого приложения.
• Архи вирование полученного документа.
• Ведение журнала или запись в лог -файл (л огирован ие).
• Вы полнение базо вых вычис лений.
