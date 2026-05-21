# Объектно-ориентированный Python, 4-е издание — страница 196

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

sill y = proper ty(
Управ лен ие пове ден ием объе ктов класса 19 5
_get_s tate, _set_st ate, _d el_ state,
"This is а sill y proper ty ")
Обратите внимание, что атрибут state имеет подсказку типа, str, но не имеет
начального значения. Атр ибут можно удалить, он существует, только пока су­
ществует NorwegianBlue. С нашей стороны необходи мо предоставить подсказку,
чтобы помочь туру понять, каким должен быть тип. Но мы не прис ваиваем
значение по умолчанию, так как это работа метода setter.
Если испо льзова ть экземпляр этого класса, то по запросу он будет выво дить
правильные строки :
>» р = No rwe gianBlue ("P olly" )
>» р. sill y = "P ining for the fjor ds"
Sett ing Polly 's State to 'P inin g for the fjor ds '
»> р. sill y
Gett ing Polly 's State
'P inin g for the fjor ds '
»> del р. sill y
Polly is pushing up daisies l
Кроме того, если мы проана лизируем поясните льный текст для класса Sill y
(в ыдав help( Sill y) в приглаш ении интерпре татора), экземпляр класса покажет
пользова тельскую строку документации для атрибута sill y:
