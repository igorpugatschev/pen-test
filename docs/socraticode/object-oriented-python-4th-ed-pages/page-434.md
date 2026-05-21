# Объектно-ориентированный Python, 4-е издание — страница 434

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема тическ ое исследование 433
Чте ние фа йлов CSV с помощью csv.r ea der
Средство чтения CSV без словаря создает список строк из каждой строки. Однако
это не то, что ожидает метод load () нашей коллекции Traini ngData.
Мы имеем два варианта выполнения требований к интерфейсу для метода load () .
1. Необходимо преобразова ть сп исок значений столбца в словарь.
2. Изменить метод load { ), чтобы использовать список значений в фиксирован­
ном порядке. Недостатком этого может стать принудительное соотв етств ие
метода load () класса TrainingData определенной структуре файла. В качестве
альтерна тивы пришлось бы переуп орядоч ивать входные значения, чтобы
они соответствовали требованиям loa d(). Сделать это так же сложно, как
создать словарь.
В нашем случае создание словаря кажется относительно простым, что позволяет
методу load () работать с данными, в которых располож ение столбцов отличается
от первона чально ожидаемого результата.
Рассмотр им пример класса CSVIrisR eader _2, котор ый испо льзует csv . reade r( )
для чтения файла и создает словари на основе информации об атрибутах, опу­
бликованной в файле iris . names.
class CSVI risR eader _2 :
Attri bute In format ion :
1. sepal length in cm
2. sepal width in cm
З. petal length in cm
4. pet al width in cm
5. class :
Iris Setosa
Iris Ve rsi colour
Iris Vir ginica
def �init �( self, source : Path) -> None :
self . source = source
def data _it er( self) -> Iterator [dict [s tr, str] ]:
with self .s ource . open () as source _fi le :
reader = csv . rea der( source _fi le)
for row in read er :
yield dict (
sepa l_l eng th=ro w[0] , # в са нтиметрах
sepal _wi dth=r ow[l] , # в са нтиметрах
petal_length= row [2] , # в са нтиметрах
peta l_wi dth=r ow[З] , # в са нтиметрах
species=r ow[4) # строк а кл асса
