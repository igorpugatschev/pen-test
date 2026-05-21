# PyCharm. Профессиональная работа на Python 2024 — страница 425

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

Рис. 11.27.	Кликните правой кнопкой мыши папку индексов и добавьте индекс, как показано
На этот раз мы кликаем правой кнопкой мыши папку indexes и выбираем
New	|	Index.	Отсюда знакомый диалог, как показано на рис. 11.28.
На этом этапе код нашей таблицы не помещается на скриншоте, поэтому вот
что у нас есть:
create table authors
(
author_id int auto_increment,
first_name varchar(30) null,
last_name varchar(30) null,
email varchar(255) not null,
constraint authors_pk
primary key (author_id)
);
create unique index authors_email_uindex
on authors (email);
alter table authors
add constraint authors_uq
unique (email);
Когда вы будете довольны структурой таблицы, нажмите ОК,	 и  PyCharm
применит сгенерированный код DDL к  базе данных. Результаты можно уви-
деть в источнике данных. Посмотрите на рис. 11.29.
424	  Часть III. Веб-разработка в PyCharm
