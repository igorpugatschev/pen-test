# Объектно-ориентированный Python, 4-е издание — страница 472

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

def par tit io n_2 (
sa mples : IteraЫe [ Kno wnSamp le] ,
trainin g_r ule : CallaЫ e[ [in t], bool ]
-> tuple [T raininglis t , Testinglist ]:
rule _mu ltiple = 60
Тема тичес кое иссле дование 471
partitio ns : Mod uloDict = collectio ns . def aultdict (l ist )
for s in samples :
partitio ns[h ash (s) % rule _multiple ]. append (s)
trainin g_partition s: lis t [ Iterator [T raini ngKno wnSam pl e] ] = []
testi ng_par titi ons : lis t [ Iterator [T esti ngK nownSamp le] ] []
for i, р in enumerate (p ar titio ns .v alue s( )):
if trainin g_rule (i) :
traini ng_par titio ns . append (
Traini ngK nownSample (s) for s in р)
else :
testi ng_par titio ns . app end (
Test ing Kno wnSam pl e(s) for s in р)
training = list ( iter to ols .c hain( *tr aini ng_partition s))
testing = lis t ( ite rtoo ls . chain ( *testi ng_parti tions ))
return training, testing
В данном случае рассмотрим следующие три шага.
1. Создаем 60 отдельных сп исков обра зцов, которые могут иметь дубликаты.
Храним эти наборы вместе, чтобы избежать разделения дубликатов, поэтому
они находятся как в тестовых, так и в обучающих подмножествах.
2. Создаем два списка итера торов. Каждый список име ет итератор для под­
множества катег орий. Функция trainin g_r ul e( ) испо льзуется, чтобы
мы убе дились, что получаются 12 /60, 15 /60 или 20 /60 катег орий при
тестирован ии, а оста льные - при обу чении. Поск ольку каж дый из этих
итераторов ленив, списки итераторов можно испо льзова ть для накопле­
ния да нных.
3. Наконец, испо льзуем i ter tools . chain для получения значений из последо­
вательности генераторов. Цепочка итераторов будет получать элементы от
каждого из различных отдельных итераторов в категории для создания двух
после дних наборов данных.
Обратите внимание, что подсказка типа для Modul oDict опре деляет подтип
универс ального Defaul tDict. Он предоставляет ключ int, а значением будет
lis t [ KnownSampl e]. Та ким обра зом, мы пре достав или данный именованный
тип, чтобы избежать повторения длинного опреде ления словарей, с котор ыми
будем работа ть.
