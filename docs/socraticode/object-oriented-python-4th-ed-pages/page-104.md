# Объектно-ориентированный Python, 4-е издание — страница 104

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти чес кое и ссле дован и е 10 3
Traini ngData может определ ить, какой из экземпляров Hyperpa rameter им еет
значен ие k, классифицир ующее ирисы с наибол ьшей точностью.
В дан ном случае существуе т несколько свя занных изменений состо яния. Часть
работы будут вы полнять как классы Hyperpa ramet er, так и классы Traini ngData.
Сис тема в целом будет измен ять свое состоя ние по мере и: iменения состоя ния
отдельных элементов. Это иног да описы вается как неочеви дное поведен ие.
Вме сто того чтобы пис ать огро мный кла сс-«монст р�, кот орый вы полняет
множество дейс твий, мы нап исали взаи моде йствующие между собой классы
меньшег о размера.
Метод tes t() для Traini ngData не представлен на UМ L-диаграмме. В свое время
мы включил и tes t() в класс Hyperpa rameter, но тогда не было необхо димым
добавлять его в Train ingData.
Ни же представлен пример нача ла создания определ ения класса:
class Hyperpa rame ter :
"'"'А hyperpa rameter value and the ov erall quali ty of the classi fica tion . """
def _init _( self, k: int , training : "Trainin gData ") -> No ne :
sel f.k = k
self .d ata : weak ref . Refe renc eType [" Traini ngDa ta "] = weak ref .r ef (tr aining)
self .q ual ity : float
Об ратите вни мание, какой вид им еют подсказки типов для еще не опреде лен­
ных кла ссов. Когда класс будет оп ределяться позже в файл е, люба я ссылка
на еще не определен ный класс станет прямой ссьu�кой. Прямые ссылки на еще
не опреде ленный класс Trainin gData предоставля ются в ви де строк, а не про­
стого имени класса. Когда ин струмент туру анализир ует код, он преобра зует
строки в правильные имена классов.
Тести рование опре деляется следу ющим методом:
def test (s elf) -> None :
"" "R un the entir e test suit e."""
traini ng_d ata : Opt ional [ "Train in gData" ] = self . data ()
if not traini ng_d ata :
raise Runtim eErr or (" Br oken Weak Refere nc e" )
pass _count , fail _count = 0, 0
for sample in traini ng_d ata . testing :
sample .c lassi fication = self . clas sif y( sam ple)
if sample .m atches ():
pass _count += 1
else :
fai l_c ount += 1
self . quali ty = pas s_count / (p ass _count + fai l_c ou nt )
