# Объектно-ориентированный Python, 4-е издание — страница 690

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Б иб лио те ка Asyn clO 689
Для этого может пригодиться метод asyncio . to_ th read( ) , назначающий отдельно
взятым потокам блокирующие запросы, позво ляя тем самым основному потоку
чередовать работу сонрограмм.
Можно также создавать отдельные задачи, которые чередуются с помощью цикла
обработки событ ий. В этом случае сопрог раммы, реализующие задачи, совместно
занимаются диспе тчеризацией чтения данных наряду с вычислениями, произ­
водимыми в отношении тех данных, которые уже были считаны.
В приме ре ниже для НТТР -запроса, лояльного к Async IO, испо льзуется би­
блио тека httpx. Дополн ительный пакет нужно будет установить с помощью
команды conda install https (е сли в качестве диспе тчера виртуальной среды
испо льзуется conda) или команды pyt hon -m pip install httpx.
Рассмотрим приложение для отправки запросов в службу погоды США, реа­
лизованное с использованием as ync io. Сос редот очимся на прогнозируемых
:юнах, полез ных для моряков в районе Чесапик ского залива. И начнем с ряда
011 ределений:
import asyncio
impor t httpx
import re
impor t ti me
fr om urllib . req uest import url open
from typing import Optio nal, NamedTu ple
class Zo ne( Name dTuple ):
zone _name : str
zone _co de : str
sam e_c od e: str # Sp ecial Area Messaging En coder
@property
def for eca st_ url ( self) -> str :
return (
f"h ttps :/ /tgftp .n ws . noaa . gov/data/f or ecas ts"
f" /marine/coast al/an/{ self . zone _code .l owe r( )}.t xt "
При наличии кортежа по имени Zone пр оанализируем катал ог резул ьтатов
морских прогнозов и созда дим список экземпляров Zone, начинающийся со
следующего:
ZONES = [
Zone (" Chesap eake Ва у from Pooles Island to Sandy Point , MD ",
"A NZ531 ", "0 7353 1" ),
Zone (" Chesap eake Ва у fr om Sa ndy Point to North Be ach, MD" ,
"A NZ53 2", "0 7353 2" ),
