# Объектно-ориентированный Python, 4-е издание — страница 149

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

14 8 ГЛ АВА 4 Ожидаем ы е нео жиданн ос ти
Ze roDi vis ion Er ror : divisi on Ьу zer o
>>> lst = [1, 2,3]
>>> prin t(ls t[З] )
Traceb ack (m ost recent call las t) :
File "<s tdin >", line 1, in <m odule>
IndexE rror : list index out of range
» > lst + 2
Traceb ack (m ost recent call las t) :
File "<s tdin >", line 1, in <m odule>
Typ eE rror : сап only conca tenate lis t (n ot "in t" ) to lis t
»> lst . add
Traceback (m ost recent call las t) :
File "<s tdi n>", line 1, in <m odule>
Att ribu teErr or : 'l ist ' object has no att ri bute 'a dd ·
»> d = {' а' : 'h ell o'}
>» d['b' ]
Traceb ack (m ost recen t call las t) :
File "<s tdi n>", line 1, in <m odule>
KeyE rror : 'Ь'
>>> print (this _i s_not_a_ va r)
Traceb ack (m ost recent call las t) :
File "<s tdi n>", line 1, in <m odule>
Nam eErr or : nam e 't his is not_a_va r' is not defined
Эти исключения подразделяются приблизительно на четыре катег ории.
• Иск лючения первой категор ии указывают на то, что в программе явно
при сутствует синтаксическая ошибка. Такие исключения, как SyntaxError
и NameError, означают, что необходимо найти указанный номер строки и ис­
править ошибку.
• Ис ключения второй катег ории указывают на то, что в среде выпо лнения
Python что-то не так. К такой категории относится, например, исключение
RuntimeError. Во многих случаях выходом из подобной ошибочной ситуа­
ции является загрузка и установка более новой версии Python. Если вы
работаете с версией Release Candida te, сообщите об ошибке специа листам
по сопрово ждению.
• Некоторые исключения могут быть связаны с пробл ема ми, залож енными
еще на этапе проектирован ия. Например, мы не учли должным образом
погра ничный случай, и теперь программа пы тается выч ислить среднее
