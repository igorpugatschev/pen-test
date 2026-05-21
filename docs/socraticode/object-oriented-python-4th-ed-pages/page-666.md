# Объектно-ориентированный Python, 4-е издание — страница 666

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

М но гопро цесс на я об ра б отка да н н ы х 665
потребляют системные ресурсы и зачастую требуют перезагр узки компьютера. )
Теперь давайте посмотрим на код, позво ляющий про вести поиск:
if name _ma in _" ·
ds = Di rector ySe arch ()
base = Path .c wd( ). pa rent
all _pat hs = lis t( al l_sour ce(b ase, "*.р у "))
ds . setup _sea rch (all _paths )
for ta rget in (" import ", "cla ss", "d ef" ):
star t = ti me . pe rf_c oun te r( )
count = 0
for line in ds . search (tar get) :
# print (l ine )
count += 1
millis econds = 100 0* (ti me . pe rf_counter () -star t)
print (
f" Found {c oun t } {tar get !r } in {l en (a ll _pat hs )} files "
f" in {millise con ds : .З f}ms "
ds . tea rd own_s ea rc h()
Этот код создает объект Director ySea rch, ds, и пр едоставляет все исходные
пути , начина я с родит еля текущего рабочего ката лога, через выр ажение
base = Path . cwd (). parent. Пос ле того как рабочие процессы подгот овлены, объ­
ект ds выпо лняет поиск нескольких расп ростран енных строк: "i mport", "class"
и "def". Об ратите внимание на закомментированную инструкцию print ( line ),
осущ еств ляющую вы вод подходя щих результа тов. Ин терес для нас все еще
пр едставляет произво дите льность. В самом начале первое чтение файла за­
нимает доли секунды . Но после того, как все файлы прочитаны, время поиска
резко возрастает. На MacBook Рго со 13 4 файлами исходного кода выводима я
на экран информация выг лядит так:
pythoп src/di rcctor 'y �scarcl r .p y
PlD : 36566 , paths 17
PID : 36567 , pa th'> 17
PID : 36570, ра t lis 17
PID : 365 71, pat hs 17
PlD : )656 9 , ра t lis 17
р lD: 36 5 68 , pa ths 17
р J IJ : 365 72 ' paths 16
PlD : 36573, pat hs 16
Fou1 1d 579 'i ni pOl 't ' in 13 4 i i l о s in 111 . 561n is
FouncJ 838 'class ' iп 134 filc s in 1. 010 n1s
Found 1138 'd ef ' in 13 4 fil es in 1. 22 4nis
Поиск слова �имп орн занял около 111 миллисекунд (0 ,1 11 секунды ). А почему
он вы полнялся гораздо медленнее двух других поисков? Дело в том, что при
помещении первого запроса в очередь функция sear ch () все еще читала файл ы.
На произво дите льность первог о запроса повлияли однокра тные начальные
