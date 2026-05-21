# Объектно-ориентированный Python, 4-е издание — страница 159

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

15 8 ГЛАВА /+ Ожидаемы е нео жиданн ости
print (f" \ nRaising {ch oic e}" )
if choice :
raise choice (" An error ")
else :
prin t( "n o exception raise d")
exc ept Va lueErr or :
prin t(" Caught а Va lueErr or" )
excep t Typ eErr or :
print (" Caught а Type Err or ")
excep t Ex ception as е:
print (f"C aught some ot her err or : {e._ class _._ name_} ")
else :
print (" This code cal led if there is no exception ")
finall y :
print (" This cl eanup code is al ways call ed ")
Запустим код (он, кста ти, иллюстрирует почти все сценарии обработки ис­
ключений, которые можно придумать) и проанализируем результаты вы вода:
Обратите внимание, как оператор print в блоке finally выпо лняется независимо
от того, что происхо дит. Это один из способов продолжить вы полнение ряда
задач после завершения вы полнения кода (д аже если возникло исключение).
Вот примеры ситуаций, когда это может понадобиться :
• восста новление соеди нения с базой данных;
• закрытие открытого файла;
• закрытие соединения, называемого «рукопожатием закрытия ».
Все это, как правило, обраба тыва ется менеджерами контекста (см. главу 8).
