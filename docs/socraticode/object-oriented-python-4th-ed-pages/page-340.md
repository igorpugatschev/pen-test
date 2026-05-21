# Объектно-ориентированный Python, 4-е издание — страница 340

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

def get_ pag es (*l inks : str) -> None :
for link in links :
url = urlp arse (l ink)
Аль те рна ти ва перег рузке ме тодо в 339
name = "i ndex . html " if url . path in ("", "/") else url . path
ta rget = Path (u rl . netloc . replac e(" ." , "_ ")) / name
prin t (f" Create {tar get } fr om {l ink !r }")
# и т.п.
Симв ол * в параметре *links означает: �я приму любое количество аргументов
и помещу их все в кортеж с именем links». Если предостав ить только один
аргумент, это будет сп исок с одним элементом; если не предоставить никаких
аргументов - пустой список. Таким обра зом, все подобные вызовы функций
являются допусти мыми:
>>> get_pag es ()
>>> get_pag es ( ' https :/ / www. archlinux .o rg' )
Cr eate www_ archlinu x_ org/ ind ex . html fr om 'h ttps : // www. archli nux .o rg '
>>> get_ pages (' https :/ / www. archli nux .o rg' ,
'h ttps : //dus ty .p hill ips . codes ',
'h ttps :/ / itmayb eah ack . com '
Cr eate www_ archlinux _o rg/in dex .h tml fr om 'h ttps : //w ww. archlinux .o rg'
Cr eate dust y_ph illips _cod es/ index . html fr om 'h ttps : // dusty . phillips .c odes '
Cr eate itmayb eahac k_com/ index . html fr om 'h ttps :/ /i tmayb eaha ck. com '
Об ратите внимание: подсказка типа предпо лагает, что в данном при мере все
значения позиционных аргументов имеют один и тот же тип, str. Такое случается
часто, ведь функция переменных параметров - это не более чем синтаксический
сахар, спасающий от написания глупо выглядящего списк а. Альтернатива, то есть
ситуация, когда тип не является единым для всех элементов кортежа переменных
парамет ров, чревата путаницей: зачем писать функцию, ожидающую сложную
коллекцию различных типов, но почему-т о не указыва ть это в опре делениях
параметро в? Не пиш ите такую функцию.
Также можно принимать произво льные аргументы в виде ключевых слов. Они
поступают в функцию в виде словаря, в объя влении функции указыва ются
двумя звездочками (к ак в **k wargs). Этот инструмент обычно испо льзуется
при настройке конфиг ураци и.
След ующий класс позволяет задать набор опций со значениями по умолчанию:
from �f utu re� import ann ot ations
fr om typing import Dict , Any
class Opt io ns(D ict [s tr, Any ] ):
defau lt_opt io ns : dict [s tr, Any ]
"p or t" : 21,
