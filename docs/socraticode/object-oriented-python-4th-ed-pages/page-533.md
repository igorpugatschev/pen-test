# Объектно-ориентированный Python, 4-е издание — страница 533

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

532 ГЛАВА 11 Об щие патте рны пр оек ти рован ия
прост ейша я версия, которая накапли вает и сорти рует различные вычис ления
расстоя ния в поисках k-бл ижай ших сосед ей:
Fr om collections import Counter
def k_nn_l (
k: in t,
dist : Distan ceFunc ,
traini ng_d ata : Traininglis t ,
unk nown : AnySamp le
-> str :
dis tances = sorted (
map( lambda t: Mea su red (dis t(t, unk nown ), t), training _data ))
k_nearest = distances [:k ]
k_f requencies : Count er [s tr] = Cou nt er(
s. sample .s ample . species for s in k_nearest
mode, fq = k_freq uencies . most _c ommon (1) (0]
return mode
Им ея эти два семейства функций расстоя ния и общие алгоритмы класс ифи като­
ра, можно определить класс Hyperparameter таким образом, чтобы он опирался на
два подкл ючаемых объекта стратегии. Опр еделение класса становится довольно
компа ктным, так как детал и были разнесены по отдельным иерархиям классов,
которые по мере необходимости можно расширять:
class Hype rpa rame ter( NamedTu ple) :
k: int
distance : Distance
traini ng_d ata : Traininglis t
classi fier : Classi fier
def classi fy (s elf, unk nown : AnySamp le) -> str :
classi fier = self .c las sifier
distance = self .d istance
return classi fier(
self .k , distance . distance, self .t rain ing _data, unkno wn )
Рассмотрим пример создания и испо льзования экземп ляра Hyperpa rameter. Он
пок азыва ет, как объекты страте гии предоставляются объекту Hyperpara meter:
»> data = [
KnownSampl e( sample=Sam pl e(l, 2, з' 4) ' species= "a "),
KnownSam pl e(s a mple=Sa mp le (2, з' 4, 5)' spec ies= "b "),
Kn own Sam ple( sample=Sa mpl e(З, 4, 5 ' 6) ' sp ec ic s= " с" ) '
Kn own Sam ple( sample= Sam ple(4, с
�' 6, 7) ' spec ie s= "d" ),
