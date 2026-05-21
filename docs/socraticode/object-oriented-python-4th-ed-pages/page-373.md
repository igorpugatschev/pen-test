# Объектно-ориентированный Python, 4-е издание — страница 373

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

372 ГЛ АВА 8 ООП и фу нк ци она ль ное пр о гр амм и рован ие
Классы Test ingKnownSample и TrainingKnownSample не вводят новых атрибутов
или методов, имеют очень незначительные различия, а именно те, что пере­
числены ниже.
• Эк земпляры Traini ngKnownSample никогда не испо льзуются для класс ифи­
кации.
• Экземпляры Testi ngKnownSample и UnknownSample исполь зуются для клас­
сифик ации и тестирован ия. Созда дим объект Classi fiedK nownSample из
объекта Testing KnownSample путем переупаковки экземпляра KnownSample
в новый контейнер. Это приведет к более последова тельному и логичному
набору определений.
Идея заключа ется в том, что метод classi fier () класса Hyperpa rameter
должен работать с объектами двух клас сов, обобщ енных подсказкой типа
Union[Testin gKnownSample, UnknownSampl e]. Такая подсказка помо жет обнару­
жить код прилож ения, неправильно использующий классы.
Диаграммы призваны показать способы применения этих объекто в. Наличие по­
добных деталей делает подсказки типов более информативными и уточняющими.
Функ ци я pa rtiti on()
Опре делим несколько версий функции training( ) , чтобы раздел ить данные 110
принципу 80/2 0, 75/25 или 67 /33:
def traini ng_80 (s: Kn ownSa mple, i: int ) -> bool :
return i % 5 != 0
def trainin g_75 (s: Known5am ple, i: in t) -> bool :
return i % 4 != 0
def training _67 (s: Known5amp le, i: in t) -> bool :
ret urn i % З != 0
А теперь посмотрим на функцию parti ti on (), которая принимает одну из функ­
ций traini ng_xx () в качестве аргумента. Функция traini ng_xx () применяется
к выборке, чтобы принять решение, является та обучающей или нет:
Traininglist = List [T rainin gK nownSamp le]
Test inglist = List [ Testi ngKno wnSam ple]
def partiti on(
sa mpl es : IteraЫe [ Kn ownSam pl e],
rule : CallaЫ e[[ Kn ownSa mple, in t], bool ]
-> Tuple [T ra ininglist, Tes tinglist ]:
traini ng_s amples = [
Traini ngKnownSample (s)
