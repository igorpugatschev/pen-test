# Объектно-ориентированный Python, 4-е издание — страница 106

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема тическ ое исследование 10 5
Ниже приве ден пример опре деления класса:
class Trainin gDa ta :
""" А set of trainin g data and testing data with met hods to load and test the
sampl es . """
def �init �( self, name : st r) -> None :
self . name = name
self . up loaded : datetime . datetime
self . tes ted : datet ime . datet ime
self . tr aining : List [ Sam ple] = []
self .t esting : List [S ample] = []
self .t uning : Lis t [H yperpa rame ter] = []
Здесь определен ряд атрибутов для отслежи вания изменений данного класса.
Например, время загрузки и время тестирования также представляют некото­
рую историю. Атрибуты обучения, тестирования и настройки содержат объекты
Sample и объекты Hyperpa rameter.
Не будем пис ать методы для устан овки всего перечисленного. Это Pytho n,
и прямой доступ к атрибутам значите льно упро щает реализацию сло жных
прилож ений. Обязанности инкапсу лированы в данный класс, но обычно мы
не пишем большое количество методов (г еттеров/сеттер ов).
В главе 5 будут рассмотре ны полез ные приемы, такие как определе ние свойс тв
Py thon, дополните льные способы работы с этими атрибутам и.
Метод load () предназначен для обработки данных, передан ных другим объ­
ектом. Можно было бы создать метод load () для открытия и чтения файла,
но тогда Traini ngData оказался бы привязан к определенному форма ту файла
и логической структуре. Кажется, лучше изолиро вать детали форма та файла от
деталей управления обучающими данными. В главе 5 мы подробно рассмотрим
чтение и прове рку ввода. А в главе 9 продолжим изучение форма тов файлов.
На данный момент для получения обучающих данных будем испо льзова ть
следующий способ:
def load (
self,
raw_d ata_ sour ce : IteraЫe [d ict [ str, str] ]
-> None :
"""L oad and partition the raw dat a"""
for n, row in enumera te( raw_d ata_sou rc e) :
... filter and ext ract subsets (S ee Chapter 6)
... Cr eate self .tr ain ing and self . testing subsets
self . up loaded = datetime .d atetime .n ow (t z=datetim e .t imezone .u tc)
