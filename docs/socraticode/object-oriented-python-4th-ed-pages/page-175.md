# Объектно-ориентированный Python, 4-е издание — страница 175

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

17 4 ГЛ АВА 4 Ожид аемы е нео жиданн ости
уже говорилос ь, - наиболее часто испо льзуемый принцип в Python. Однако
в случае обработки значения обра зцов фун кция преобра зования, подобна я
float () , отсутствует, то есть ничто не может создать исключение или сообщение
о невалидных данных. По этому в примере для оценки значения этого атрибута
использован принцип LBYL.
Метод fr om_dict( ) определяется с помощью зaпиcи @clas smethod. Это означает,
что фак тический объект класса становится первым парамет ром, cls. А любой
подкласс, который наследует эти данные, будет иметь метод, адаптированный для
этого подкласса. Можно создать новый подкласс, например Traini ngKnownSample,
испо льзуя следующий код:
class Tr ainin gKnownSa mple ( Kn ownSam ple) :
pass
Ме тоду Traini ngKnownSample . fr om_d ict () будет присвоен класс Trainin g­
KnownSample в качестве значения парам етра cls. Без каког о-либо другог о кода
метод fro m_ dict() этог о класса будет создавать экзем пляры класса Training ­
KnownSample.
Хотя Это работает правильно и хорошо, туру не сможет определить, работает ли
код. Для явного отображе ния типов пр едлагается ис пользова ть следу ющее
определение:
class Trainin gKnownSam ple ( KnownSample ):
@c las smethod
def fr om_dict (c ls, row : dic t [s tr, st r] ) -> "Trainin gK nownSample ":
return cast (T rainin gKno wnSamp le, su pe r( ). fr om_dic t (r ow) )
В качестве альтернативы можпо сфо рмировать более нростое определение класса
и поместить метод cas t( ) в те места кода, где фактически используется from_ dict ( ),
например cas t (T rainin gKnownSample, Training KnownSample . fr om_d ict ( data)).
Поск ольку этот метод применяе тся не очень часто, нельзя с увер енностью
утвер ждать, что како й- то из нредложенных вариантов щюще.
Пр оанализируйте оставшу юся часть класса KnownSample:
class Kn ownSam ple( Sample ):
def _in it_(
self,
species : str,
sepal _leng th : flo at ,
sepa l_width : float ,
petal_leng th : flo at ,
peta l_widt h: float ,
-> None :
sup er() ._ in it_(
