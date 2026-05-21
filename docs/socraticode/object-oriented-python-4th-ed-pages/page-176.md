# Объектно-ориентированный Python, 4-е издание — страница 176

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

sepa l_leng th=sepal _leng th,
sepa l_wid th=sepal _wi dth ,
petal_leng th=p etal_leng th,
peta l_width=pe tal _wid th,
self .s pecies = species
def _repr _( self) -> str :
retur n (
Тема тическ ое иссле до ван ие 17 5
f"{ self . _c lass_. _na me_} ( "
f" sepal _length ={ self .s epa l_leng th}, "
f" sepal _wi dth= {s elf . sepa l_width }, "
f"p etal _leng th= {s elf . peta l_leng th}, "
f" petal _width ={ self . peta l_widt h}, "
f" species={ self .s pecies !r }, "
f" )"
Посмо трим, как это работает на практике. Ниже представлен пример загруз ки
некоторых валидных данных:
>>> from mod el import Tr aini ngK nown Sample
>» valid = {" sepal_leng th" : "5. 1", "s epa l_ wid th" : "3 .5 ",
"p etal _leng th" : "1.4", "p eta l_ wid th" : "0 .2 ",
"s pecie s" : "Iris-s eto sa "}
>>> rks = Traini ngK nownSam ple . fr om_ dict (v alid )
> » rks
Trainin gKno wnSam ple ( sepal_leng th=5 .l , sepa l_ widt h=З .5 ,
petal_leng th=l .4, petal_ width= 0 .2 , spec ies= 'I ris -s etosa ',
Мы создал и словар1 , valid, который и:i строки ввода создаст csv . DictReader.
Затем из этого сло варя созда ли экземпляр Traini ngKnownSample, rks. Резул ь­
тирующий объект имеет соответс твующие значения с плавающей запят ой, тем
самым показывая, что преобр аэовап ия и:i строк были выпо лнены как надо.
Ниже при веден при мер исключения, возникающего для невалидных данных:
>>> from mod el import Testi ngK nownSam ple, Inva l idSampl eE rror
>» inval id_sp ecies = {" sepa l_leng th" : "5.1", "s epa l_ wid th" : "3. 5",
"p eta l_l eng th" : "1.4 ", "p eta l_ wid th" : "0 .2",
"s pecies ": "n ot hin g kno wn Ьу this ар р"}
>>> eks = TestingK nownSam ple . fr om_ dict (i nval id_sp ecies )
Traceback (m ost recent call las t) :
mod el . Inval idSampl eE rror : invalid spec ies in { 's epa l_l ength ': '5 .1' ,
's e pa l_ width ': '3.5' , 'p etal_leng th ': '1. 4' , 'p eta l_ wid th ': '0. 2',
's pecies ': 'n ot hing kn own Ьу this ар р'}
При создан ии экземпляра TestingKnownSample невалидное значение species
вызвало исключение.
