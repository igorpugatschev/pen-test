# Объектно-ориентированный Python, 4-е издание — страница 319

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

31 8 ГЛА ВА 7 Ст руктуры да нны х Python
Вот изменения в иерарх ии классов Sample. Они относительно незначительные,
и легко проп устить и не заметить строчку frozen=True , присутствующую в не­
скольких местах.
@d atacla ss( frozen=Tr ue)
class Sample :
sepal _leng th : float
sepa l_width : float
peta l_l eng th : float
peta l_widt h: float
@d atacl ass( frozen= True )
class Kno wnSample (Sa mple ):
species : str
@da taclass
class TestingK nownSam ple :
sample : Kno wnSample
classi ficati on : Opt ion al [s tr] None
@da tacl ass( frozen= True )
class Traini ngKno wnSam ple :
"" "Н ево зможно кла сси фицир ов ат ь ." ""
sample : KnownSample
При создании экземпляров Traini ngKnownSample или Test ingKnownSample необ­
ходимо учиты вать композицию этих объекто в: внутри каждого из этих классов
есть заморож енный объект KnownSample. В следующем примере показан один из
способов создания сост авного объекта.
>>> from mode l_f import Tr ainin gKnownSam ple, KnownSample
>>> sl = Trainin gKno wnSamp le(
sample=Kn ownSamp le(
sepa l_ length= S.1 , sepa l_ wid th=З .5 ,
petal_leng th=l .4 , peta l_ wid th= 0.2 , specie s="Iris- set osa "
»> sl
Traini ngK nown Sam ple (s a mple=Kn own Sam ple ( sepal _leng th=5 .l , sepa l_ wi dth=З .5 ,
petal_leng th=l .4 , pet al _ width=0 .2 , species= 'I ri s- setosa '))
Вложенная конструкция экземпляра Traini ngKnownSample, содер жащая объект
KnownSample, является дово льно прозрач ной для понимания. Она раскрыва ет
неизменяемый объект KnownSample.
С такой замороже нной конструкцией будет легче находить обычно сложно об­
наруживаемые ошибки. В следующем примере показано исключение, вызванное
неправильным испо льзованием Traini ngKnownSample:
