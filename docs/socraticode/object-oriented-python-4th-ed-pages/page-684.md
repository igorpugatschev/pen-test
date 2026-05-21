# Объектно-ориентированный Python, 4-е издание — страница 684

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Б иб лио те ка Asyn clO 683
Здесь определены три стандартных сигнала: SIGIN T, SIGТERM и SIGABRT - и особ ый
сигнал для Windows: SIGBREAK. Все они предназначены для закрытия сервера,
завершения обработки запросов и завершения цикла обработки после окончания
работы всех ожидающих выполнения сопрог рамм.
Как уже было показано в предыдущем примере использования Async IO, основ­
ная программа также является весьма лакон ичным способом запуска цикла
обработки событи й:
if name == "_ main_" ·
# These oft en have co mmand-line or envi ronment ove rrides
HOST, PORT = "l oca lhost ", 18842
with Path (" one . log" ). ope n(" w" ) as TAR GET :
tr y :
if sys . pl atform == "win3 2" :
# htt ps :/ /git hub . com/ enco de/h tt px/ is sues /91 4
loop = asyncio . get_ event_lo op ()
loop . run _until _comp lete(m ain (H OST, PORT ))
loop .r un_u nti l_c omplete (a sy nci o. sle ep(l) )
loop .c los e()
else :
except
asyncio .r un(m ain (H OST , POR T) )
asy nci o . exceptio ns . Cancelle dErr or,
Keyb oardi nterrup t ):
ending = {" line s_col lected ": LIN E_CO UNT}
print (e nding )
TARG ET .w rite (js on . dumps (e nding) + " \ n")
При ее запуске открывается файл и устанавливается значение глобальной пере­
менной TAGET, которая используется функцией serialize () . Функция main()
здесь задействуется для создан ия сервера, ожидающег о подк лючения. Когда
задача ser ver _f orev er () отменяется с выдачей исключения Cancell edError
или Keyboardinter rupt, финальную итоговую строку можно поместить в файл
журнала. Этой строкой подтверждается нормальное завершение всех операций
и представляется дока зател ьство пол ьзователям, что ни одна строка не была
потеря на.
Для работы под управлением Windo ws вместо более полноценного метода run()
нужно воспо льзова ться методом run_ until _c omple te( ). Кроме этого, в цикл
обработки событий следует поместить еще одну сопрограмму, as yncio . sl eep ( ),
позволяющую дождаться окончательной обработки от любых других сопро­
грам м.
