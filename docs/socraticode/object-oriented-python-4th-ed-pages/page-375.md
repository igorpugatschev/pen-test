# Объектно-ориентированный Python, 4-е издание — страница 375

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

374 ГЛА ВА 8 ОО П и фун кциона л ьное пр ог рамм и рован ие
training : Traininglist = []
testing : Test inglis t = []
for i, s in enumera te( sampl es) :
trainin g_u se = rul e(s, i)
if trainin g_use :
training . append (T rainin gKno wnSample (s))
else :
testing .a ppend ( Testi ngKnownSample (s))
return training, testing
Чтобы определить, будут ли данные испо льзова ться для обучения, в функции
parti ti on_l () мы задействовали функцию rule. Ожидается , что в качестве аргу­
мента для параметра rule будет предоставлена одна из функций traini ng_ xx( ),
определенных ранее в этом примере.
На основе вы вода созда дим соответс твующий класс для каждого экземпляра
выборки, а затем присвоим выборку соответствующему списку. Здесь не проверя­
ется наличие дубликатов между тестовыми и обучающими выборкам и. Некоторые
специалисты по исследованию данных советуют отказаться от тестовых образцов,
которые точно совпа дают с обучающими образцам и: это искажает результаты
рабочего тести рования. Мы же видим, куда можно вставить это необходимое
решение: между моментом присвоения переменной tr ainin g_u se и моментом
окончательного добавления в любой из списков. Если переменная traini ng_u se
равна False и элемент уже существует в обучающем наборе, то этот элемент тоже
должен быть испо льзован для обучения.
По зже можно будет пров ести небольшой рефак торинг приведенного алгоритма,
выпо лнив преобра зование типов. Это позволит создать словарь с различными
�п улами� объектов Knownsample в зависи мости от предполаг аемого использова­
ния. Пока у нас только два пула - тренировоч ный, где правило traini ng_xx ()
равно True, и тест овый:
from collections impor t def aul td ict, Counter
def par tit ion_ lp (
sampl es : Itera Ыe [ Kn ownSample ],
rule : CallaЫe [[ Kno wnSample, in t], bool ]
-> tuple [ Trainingl ist, Te stinglist ]:
pool s: defaultd ict [b oo l, list [K nownSample ]] = def aultdict (l ist )
partition = ((r ul e(s, i), s) for i, s in en umerate (s amples ))
for us age_poo l, sample in partition :
poo ls [u sage_pool ]. append (s ample )
training = [T raini ngK nown Sam pl e(s) for s in pool s[T rue ] ]
testing = [T esti ngKnownSample (s) for s in poo ls [ Fals e] ]
ret urn tr aining, testing
