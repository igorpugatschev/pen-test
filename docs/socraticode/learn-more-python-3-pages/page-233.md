# Легкий способ выучить Python 3 еще глубже — страница 233

232 ЛЕГКИЙ СПОСОБ ВЫУЧИТЬ PYTHON 3 ЕЩЕ ГЛУБЖЕ
Миграция и развитие данных
Давайте применим некоторые из приобретенных вами навыков. Я попрошу
вас взять вашу базу данных и «развить» схему до другой формы. Вам нуж­
но убедиться, что вы хорошо разобрались в предыдущем упражнении, и ваш
файл code.sql работает как надо. Если какое-то из этих условий не было
выполнено, вернитесь и исправьте ситуацию.
Чтобы убедиться, что вы готовы попытаться выполнить это упражнение, за­
пустите свой code. sql. Ваша . schema должна запускаться следующим об­
разом:
Exercise 13 Session
$ sqlite3 exl3.db < code.sql
$ sqlite3 exl3.db .schema
CREATE TABLE person (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INTEGER
) ;
CREATE TABLE person_pet (
person_id INTEGER,
pet_id INTEGER
) ;
CREATE TABLE pet (
id INTEGER PRIMARY KEY,
name TEXT,
breed TEXT,
age INTEGER,
dead INTEGER,
dob DATETIME
Убедитесь, что ваши таблицы выглядят так же, как мои. Если они отличаются,
вернитесь и удалите из последнего упражнения любые команды, касающие­
ся ALTER TABLE ИЛИ ДРУГИХ изменений.
