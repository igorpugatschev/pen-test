# Легкий способ выучить Python 3 еще глубже — страница 225

224 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
где сначала мне не удается вставить новую запись, и я использую запрос RE­
PLACE.
exll.sql
1 /* Так сделать не получится, потому что 0 уже занят. */
2 INSERT INTO person (id, first_name, last_name, age)
3 VALUES (0, 'Frank', 'Smith', 100);
4
5 /* Мы можем добиться результата, используя INSERT OR REPLACE. */
6 INSERT OR REPLACE INTO person (id, first_name, last_name, age)
7 VALUES (0, 'Frank', 'Smith', 100);
8
9 SELECT * FROM person;
10
11 /* Для краткости можем использовать просто REPLACE. */
12 REPLACE INTO person (id, first_name, last_name, age)
13 VALUES (0, 'Zed', 'Shaw', 37);
14
15 /* Как видите, теперь я вернулся. */
16 SELECT * FROM person;
Задача упражнения
1. Используйте UPDATE, чтобы вернуть мне имя Zed с помощью моего
person. id.
2. Напишите update, который переименовывает любых мертвых
(dead) животных в DECEASED (скончавшихся). Если вы попытаетесь
указать, что они dead, ничего не выйдет, потому что SQL подумает,
что вы имеете в виду «установите его столбцу с именем DEAD», а это
не то, что вам нужно.
3. Попробуйте использовать подзапрос, как в примере с DELETE.
4. Перейдите на страницу SQL As Understood By SQLite (www.sqlite.org/
lang.html) и начните чтение документации по CREATE TABLE, DROP
TABLE, INSERT, DELETE, SELECT И UPDATE.
