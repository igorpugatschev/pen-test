# Объектно-ориентированный Python, 4-е издание — страница 580

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

conn . execute (
IN SER T IN TO Sales
Па тте рн Ша 9ло нн ы й ме тод 579
VALUE S( 'T im ', 16000, 2010, 'H onda Fi t', 't ru e' )
conn . ex ecute (
INSER T INTO Sales
VALUE S( 'T im ', 9000 , 2006 , 'F ord Focus ', 'f alse ')
co nn . execu te(
INSER T IN TO Sales
VALUE S( 'H annah ', 8000, 2004, 'D odge Neon ', 'f als e' )
conn . execu te(
INSER T INTO Sales
VALUES (' Hannah ', 28000 , 2009 , 'F ord Mustang ', 't ru e')
co nn . execu te(
INSER T IN TO Sales
VALUES (' Hannah ', 50000, 2010, 'L incoln Navigat or ', 't ru e')
co nn . execute (
INSER T IN TO Sales
VALUE S( ' Jas on ', 20000 , 2008 , 'T oyota Prius ', 'f als e')
conn . commit ()
return conn
Надеемся, вы см ожете разобраться в приведенном коде, даже если не знаете
SQ L. Для хранения данных мы создали таблицу Sales и использовали шесть
операторов inser t, добавля ющие записи о продажах. Данные хранятся в файле
sales . db. Теперь у нас есть образец базы данных с таблицей, с которой мы можем
работать при создании Шаблонного метода.
Пос кольку мы уже опр еделили примерные шаги, которые должен выпо лнять
Шабло нный метод, начнем с оп ределения базового класса. Каждый шаг имеет
