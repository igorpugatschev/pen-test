# Объектно-ориентированный Python, 4-е издание — страница 343

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

342 ГЛА ВА 8 ОО П и фу нкцио нал ьное про гра мм и рова ние
for path in di rectory .g lo b( "**/* .m d" ):
if any(
pa rent . stem == ". tox"
for pa rent in path . parents
) :
cont inue
log (
f"Fi le {path . relati ve_to (dir ector y)}, "
f"{p ath . stem= }"
if stems .g et (p ath . stem, "") .u ppe r() "S KIP" :
lo g( "Sk ippe d")
cont inue
opt ions = []
if stems .g et ( path . stem, '" ') . upp er( ) "ELL IPSIS ":
opt ions += [" EL LIP SIS "]
search _path = di rector y / "s rc "
print (
f"cd '{ Path .c wd()} '; "
f" PYTHONPATH= '{ search _path} ' doctest '{ pat h} ' -v"
opt ion _args = (
["- о ", ", ". join (o ptio ns )] if options else []
sub proce ss .r un(
[" pyt honЗ ", "-m" , "d oct es t", " -v" ]
+ opti on_args + [s tr(p at h)],
cwd=dir ectory,
env ={ " PYTHONPATH ": str( sea rch _pa th )},
Здесь код обраба тыва ет произвольный спис ок путей к каталогам для запуска
инструмента doctest на файлах разметки в этих каталогах. Рассмот рим опре­
деление каждого параметра подробнее.
• Первый параметр, output, представляет собой открытую папку, в которую
будет записы ваться вывод.
• Па раметру directo ries будут переданы аргументы, не являющиеся ключе­
выми. Все они должны быть объект ами Path( ) .
• Параметр verbose, только ключевой, указыва ет нам, следует ли печа тать
информацию о каждом обработ анном файле.
• Наконец, есть возмо жность указать любое другое ключевое слово в каче­
стве имени файла для сп ециа льной обработ ки. Четыре имени - output,
direc tories, verbose и stems - фак тически являются спец иальными име­
нами, которые должны быть обрабо таны специа льным обра зом. Любой
другой ключевой аргумент будет собран в словарь stems, а эти имена будут
выделены для специа льной обрабо тки. В частности, если в спис ке file stem
указано значение "SKIP", то файл не будет про веряться. Если есть значение
"ellip sis ", то doctest будет помечен флажком специа льной опц ии.
