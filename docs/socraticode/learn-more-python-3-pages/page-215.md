# Легкий способ выучить Python 3 еще глубже — страница 215

214 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
я указываю, что мне нужно INTEGER (целое число), а также PRIMARY
KEY (первичный ключ). Это означает, что SQLites должна относиться
к этому столбцу по-особенному.
Строки 3-4
Столбцы first_name и last_name, тип обоих - TEXT (текст).
Строка 5
Столбец аде, это просто INTEGER.
Строка 6
Завершение списка столбцов закрывающей скобкой и точкой с запятой.
Создание многотабличной базы данных
Создание одной таблицы не слишком полезно. Теперь я хочу, чтобы вы созда­
ли три таблицы, в которых можно хранить данные.
ех2.sql
1 CREATE TABLE person (
2 id INTEGER PRIMARY KEY,
3 first_name TEXT,
4 last_name TEXT,
5 age INTEGER
6 ) ;
7
8 CREATE TABLE pet (
9 id INTEGER PRIMARY KEY,
10 name TEXT,
11 breed TEXT,
12 age INTEGER,
13 dead INTEGER
14 ) ;
15
16 CREATE TABLE person_pet (
17 person_id INTEGER,
18 pet_id INTEGER
