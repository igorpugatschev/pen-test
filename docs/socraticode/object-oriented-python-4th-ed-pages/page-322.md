# Объектно-ориентированный Python, 4-е издание — страница 322

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Темат ическ ое исследован ие 321
или все же нет. Зачастую нужно задать себе этакий метафор ический вопрос
«Я вляется ли яблоко фрукт ом?» (is -a) - чтобы выявить более узкие подклассы
и общие суперк ласс ы. Проблема заключается в том, что яблоко также может
быть и десертом, и это обстоятельство запутывает, казалось бы, прос тое решение,
обременяя его дополните льными деталями.
Не забывайте, что яблоко (в виде яблочного пюре) может быть частью основного
блюда. По добное усло жнение может еще больше затруднить ответ на вопрос
«является ли» (is -a). В нашем случае использование отношений типа «являет­
ся ли» (is -a ) между образ цами - известными, неизвестными, тестир овочными
и обучающими - может оказаться не самым лучшим варианто м. По хоже, что
у нас есть несколько ролей (то есть тестирование, обучение, классифик ация ),
котор ые связаны с каждым образцом, и может быть только два подкласса Sample:
известный и неизвестный.
Оп реде ления классов TestingKno wnSample и Traini ngKnownSample следуют
правилу утиной типизации. Они имеют схожие атрибуты и во многих случаях
могут быть взаимозамен яемы.
class Testing Kn ownSample :
def _init_(
self, sample : KnownS ampl e, classi fi cat ion : Opt ion al [s tr] None
-> None :
self . sample = sample
self .c las sifica tion = class ification
def _repr _( self) -> str :
return (
f"{ self ._ class _._ name_} (s ample= {s elf .s ample !r }, "
f" classi ficatio n={ self .c lassi fication !r })"
class Traini ngK nownSamp le( NamedTu pl e) :
sample : Kno wnSample
В данном случае и Test ingKnownSample, и Training KnownSample явля ются со­
ста вными объект ами, содержащ ими объект KnownSample. Основное различие
заключается в наличии (и ли отсутствии) дополнительного атрибута - значения
classi fication.
Вот пример создания Traini ngKnownSample и поп ытки (не удачной) задать атри­
бут classi ficat ion:
>>> fr om mode l_t import Tra 1ni ngK nownSamp le, Kno wnSamp le, Sam ple
>>> sl = Tra1n1n gK nownSam ple (
. . . sample=Kn ownSam ple (
. . . sample=Sam ple( sepal _leng th=S .1 , sepa l_ width= З.S ,
. . . peta l_leng th=l .4, pe tal _width=0 .2),
