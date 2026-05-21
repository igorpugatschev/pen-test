# Объектно-ориентированный Python, 4-е издание — страница 166

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

И скл ючен ия 16 5
подсчитыва ть остав шие ся товары ... ), а затем разблокирова ть товар. По сути, это
менеджер контекста (о дна из тем главы 8).
Ра ссмотрим пример создания класса In ventor y со строками документа ции,
описывающими работу некотор ых метод ов:
class OutOfStoc k( Exception ):
pass
class Invalidlte mType (E xception ):
pa ss
class In ventor y :
def �init �( self, sto ck: list [ It emType ]) -> None :
pass
def lo ck( self, item _ty pe : Ite mType ) -> None :
""" Context Entr y .
Lock the item type so nobody else сап manip ulate the
in ventor y while we 'r e wo rkin g."""
pass
def unlo ck( self, item _type : It emType ) -> None :
""" Cont ext Exit .
Unlock the item typ e."""
pass
def purchase( self, item _type : It emType ) -> int :
"""I f the item is not loc ked , raise а
Va lueE rror because some thing went wro ng .
If the it em_type does not exist ,
raise Invalid lt emType .
If the item is curr ently out of stoc k,
raise OutOfSt ock .
If the item is availaЫe,
sub tr act one item; retur n the number of items le ft .
# Mocked results .
if item _type .n ame == "Widg et" :
raise OutOfSt oc k( item _type )
eli f item _type . name == "Gadg et ":
return 42
else :
raise Invalid lte mType ( item _type )
Можно было бы передать этот прототип объекта разрабо тчику и попр осить его
реализовать методы, чтобы они работали должным обра зом, пока мы работаем
над кодо м, необходимым для совершения покуп ки. Будем исп ользова ть надеж­
ную обработку исключений Python для анализа различных ветвей в зависимости
от того, как была совершена покупка. И даже напишем тест, чтобы убедиться ,
что не возникнет вопросов относительно работы нашего класса.
