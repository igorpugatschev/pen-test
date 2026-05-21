# Объектно-ориентированный Python, 4-е издание — страница 640

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Те м ати ч еск ое и сс ле дов ание 639
М одул ьное тести ров ание клас са Hy per par ame ter
Класс Hyperpa rameter зависит от вычисления расстоя ния. Для тестирования
таких вот сложных классов есть две страте гии.
• Пр оведение интегра ционного теста, в котором испо льзуются уже протест и­
рованные вычис ления расстоя ний.
• Применение модульного теста, изолирующего класс Hyperparameter от любых
вычислений расстоя ний и подтверждающего работосп особность этого класса.
В соответс твии с общим эм пирическим правилом каждая строка кода должна
быть проверена как минимум одним модульным тестом. После этого можно так­
же воспо льзова ться интеграционными тестами, позво ляющими убедиться, что
определения интерфейсов соблюдаются всеми модулями, классами и функциями.
Принцип «п ротестируйт е все� важнее, чем «сделайте так, чтобы было получено
правильное число�. Одним из спос обов убедиться в протес тированно сти всего
кода является подсчет строк.
Рассмот рим тести рование метода classi fy( ) класса Hyperpa rameter, для чего
воспо льзуемся мок- объект ами, позволя ющими изолирова ть класс Hyperpa ­
rameter от любых вычислений расст ояния. Также будет имитироваться объект
TrainingData, что позволит усилить изолированность экземпляра данного класса.
По дверга емый тестирован ию код выглядит следующим обра зом:
class Hyperparame ter :
def _in it_(
self,
k: int ,
al gorithm : "D istance ",
tr aining : "Trainin gDat a"
-> None :
sel f.k = k
self .a lgorithm = alg orithm
self .d ata : weakr ef . Ref erence Type [" Train in gData" ] \
weak ref .r ef (tr aining)
self .q ual ity : float
def classi fy (
self,
sample : Union [ Unkn ownSa mple, Testi ngKnownSam pl e] ) -> str :
"" "T he k-NN al gorith m" ""
traini ng_data = self . data ()
if not trainin g_data :
raise Runt imeE rror (" No Traini ngData object ")
dis tances : lis t [t uple [f loat , Training Kno wnSamp le] ] sorted (
(s elf .a lgo rithm .d ista nce( sample, kno wn ), kno wn )
