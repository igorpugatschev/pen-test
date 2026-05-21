# PyCharm. Профессиональная работа на Python 2024 — страница 172

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

заставить AI делать это. Но мы придерживаемся того, что позволяет нам делать
PyCharm «из коробки».
Удалите строку # TODO и вместо нее введите три двойных кавычки (""") и на-
жмите Enter. Вы увидите сгенерированный шаблон строки документации:
"""
:param n:
:return:
"""
Этот шаблон требует некоторого заполнения, чтобы стать полноценной
строкой документации. Обратите внимание на пробел под первым набором
тройных кавычек. Здесь вы должны написать о том, что делает функция. Может
быть, что-то вроде этого:
"""
Check whether an integer is a prime number of not.
Generally, the function goes through all odd numbers
less than the square root of the input integer, and
checks to see if the input is divisible by that number.
:param n:
:return:
"""
Ниже находится раздел параметров, ожидаемых функцией. Здесь функция
принимает один аргумент с именем n. Нам следует немного написать об этом
параметре, включая его тип:
"""
Check whether an integer is a prime number of not.
Generally, the function goes through all odd numbers
less than the square root of the input integer, and
checks to see if the input is divisible by that number.
:param n: the integer to prime check
:return:
"""
Последняя часть – это документация по возвращаемому значению:
"""
Check whether an integer is a prime number of not.
Generally, the function goes through all odd numbers
less than the square root of the input integer, and
checks to see if the input is divisible by that number.
:param n: the integer to prime check
:return: boolean
"""
Глава 4. Редактирование и форматирование с легкостью в PyCharm  171
