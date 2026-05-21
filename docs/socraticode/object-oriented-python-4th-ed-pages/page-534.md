# Объектно-ориентированный Python, 4-е издание — страница 534

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Темат ическое исследова ние 533
>>> manhattan = Manhattan (). distance
>>> traini ng _ data = [T rainin gKno wnSam pl e(s) for s in data ]
>>> h = Hyperpa ramete r(l, ma nhat tan, traini ng_ da ta, k_nn_l )
>» h. classi fy (Unk nownSampl e(S ample (2, 3, 4, 5) ))
, Ь'
Здесь создан экземпляр класса Manhattan и предоставлен метод Distan ce( )
этого объекта (ме тод объекта, а не вычисленное значение расстоя ния) экзем­
пляру Hyperpa rameter. Для классификации ближай ших соседей опре делена
функция k_nn_l ( ).
Обучающие данные представляют собой последова тельность из четырех объ­
ектов KnownSample.
Име ется тонкое различие между функцией расстоя ния, которая оказы вает пря­
мое влияние на то, насколько хорошо работает класс ификация, и алгоритмом
классифи катора, который оптимиз ирует произ водител ьность только незначи­
тельно. Можно возразить, что на самом деле это не одноранговые классы и мы
собрали в один класс слишком много функци й. На самом деле не нужно про­
верять качество алгоритма классифи катора. Вместо этого необхо димо только
проверить про изводительность.
Этот пример правильно оп ределяет местона хожд ение ближайшего к данному
неизвестному образцу соседа. С практической точки зрения для проверки
всех образцов тестовог о набора данных нужно более сложное и более мощное
тестирован ие.
К классу Hyperpa ramet er добав им следующий метод:
def test (s elf, testing : Test inglis t ) -> float :
clas si fier = self .c lass ifier
dis tance = self .d istance
test _re sults = (
Class ifiedK nownSamp le (
t. sample,
classi fier(
self .k , dis tance .d istance,
self .tr ain ing _data , t. sa mple ),
for t in testing
pass _fa il = map(
lambda t: (1 if t. sample .s pecies
test _re sults
ret urn sum( pass _fa il) / len (t esting )
t. classi fication else 0) ,
