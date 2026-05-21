# Легкий способ выучить Python 3 еще глубже — страница 154

КОМАНДЫ DIFF И PATCH 153
$ diff A.txt B.txt > AB.diff
$ cat AB.diff
2,4c2,4
< her fleece was white a mud
< and every where that marry
< her lamb would chew cud
> her fleece was white a snow
> and every where that marry went
> her lamb was sure to go
Так получается файл AB.diff, содержащий отличия между A. txt и в. txt,
которые, как видно, заключаются в восстановлении нарушенной рифмы. Как
только вы получили этот АВ. diff, можно использовать patch для примене­
ния изменений:
$ patch A.txt AB.diff
$ diff A.txt B.txt
Эта последняя команда не должна иметь вывода, так как благодаря предше­
ствующей ей команде patch содержимое А. txt стало аналогичным содер­
жимому в. txt.
Реализация этих двух команд должна начинаться с diff, так как у вас есть
инструмент diff, полностью реализованный с помощью Python. Вы може­
те найти его в конце документации difflib (docs.python.org/2/library/difflib.
html#a-command-line-interface-to-difflib). Лучше попытайтесь реализовать
свою версию и сравнить ее с официальной версией.
Самое приятное в этом упражнении - инструмент patch, который Python
не реализовывает за вас. Вам нужно прочесть о классе SeguenceMatcher
в difflib и, в частности, взглянуть на функцию SequenceMatch.get-
opcodes (d0cs.pyth0n.0rg/2/library/difflib.html#difflib.SequenceMatcher.
get_opcodes). Это ваш единственный, но очень хороший ключ к реализации
patch.
