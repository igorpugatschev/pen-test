# Объектно-ориентированный Python, 4-е издание — страница 266

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти ческ ое иссле дова ние 265
Инк ремен тал ьна я стр ате гия
Рассмотрим альтернативу разде лению списка. Вместо того чтобы расширять
класс lis t для предоставл ения двух подсп исков, немног о переформулиру­
ем задач у. Ск аже м, оп редел им по дкласс SamplePar ti tion, котор ый делает
случай ный выбор между тестированием и обу чением для каждого объекта
SampleDict, представл енного с помощью инициализации или методов append ()
или extend () .
Ни же пр едставл ена абст ракция , резюмир ующая эту идею. В постро ении
сп иска мы используем три метода и два свойства, кот орые будут предостав­
лять множества для обучения и тес тирования. Нет никакого наследования
от List, так как не предо ставл ены никакие другие функци и, подобн ые сп искам,
даже _l en_( ).
Итак, класс имеет только пять методо в:
class Dea lin gPartition (a bc .A BC) :
@abc .a bstra ctmethod
def _in it_(
self,
items : Opt iona l[ IteraЫe [ SampleDict ]],
* ,
traini ng_s ubset : Tuple [i nt , int ] = (8, 10 ),
-> None :
@abc .a bstract method
def extend (s elf, items : IteraЫe [ SampleDict ]) -> None :
@abc .a bst ra ctmethod
def append (s elf, item : SampleDi ct ) -> None :
@proper ty
@abc . abstra ctm ethod
def training (s elf) -> List [T rain ingKno wnSample ]:
@prope rty
@abc . abstr actmethod
def testing (s elf) - > Lis t [ Testi ngKnownSample ]:
Это определение не имеет конкретной реализации. Здесь пр едставл ено пять
мест (заполн ителей), в которых можно оп редел ить методы для реализации
необходимого алгоритма. По сравнению с предыдущим примером немного из­
менено определение параметра trainin g_s ubset. Он опре делен как два целых
числа, что позволяет считать и действова ть посте пенно.
