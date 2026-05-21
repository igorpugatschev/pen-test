# Объектно-ориентированный Python, 4-е издание — страница 621

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

620 ГЛАВА 13 Тести ров ание об ъек тно - ориен ти рова нн ы х прог ра мм
Вместо проверки интеграции с redis -c epвepoм нужно ограничиться пров еркой
вызова метода se t() соответствующее количество раз и с соответствующими
аргумент ами. Чтобы заменить проблем ный метод объек том, поддающимся ин­
троспек тиве, в текстах можно воспользоваться объектами Мосk( ). Ис пользование
Mock показано в следующем примере:
impor t datet ime
impor t fligh t_stat us _red is
from uni ttest .m ock import Moc k, patch, call
impor t pyt est
@pyt est .f ixture
def moc k_re di s() -> Mock:
moc k_red is _instance = Moc k( set=M oc k( retu rn_val ue=True ))
return moc k_red is _instance
@pyt est . fix tur e
def tracker(
monkeypat ch : pyte st .M onkeyPa tch, moc k_red is : Mock
-> flig ht_s tatu s_red is . Fli ghtS tatusTr acker :
fst = fli ght_ stat us _re di s.F li ghtS tatusTr acke r()
monkeypa tch . setat tr(f st , "r ed is", moc k_red is)
retur n fst
def te st_ mon keypat ch_c lass (
track er : fl ight_st atu s_red is . Fli ghtStat usTracker, moc k_red is : Moc k
-> None :
with pyt est .r aises (V alueE rror) as ех :
tracker .c hang e_s tatus ( "A C101 ", "l os t")
ass ert ex . value .a rgs [0] == "'l ost ' is not а valid Sta tus"
as ser t moc k_re dis . se t . call _count == 0
В приведенном тесте применяется диспе тчер контекста raises ( ) , позво ляющий
убедиться, что при передаче неподходя щего аргумента выдается нужное исклю­
чение. Кроме того, в нем для экзем пляра redis создается объект Mock, который
будет испо льзова ться Fl ightStat usTrack er.
В мок- объекте содержится атрибут set, являющийся мок- методо м, неизменно
возвращающим значение True. Но тест провер яет, что вызов метода redis . set ( )
никогда не состоится. Если подтвердится именно этот факт, он будет означать,
что в код обработки исключений вкралась ошибк а.
Обратите внимание на способ перехода к мок-объекту. Для проверки фикт ивного
метода set ( ) объекта Mock, созданного фи кстурой mock_ redis, испо льзуется вы­
зов mock_red is . set. А call _count является атрибуто м, поддер живаемым всеми
объект ами Mock.
Конечно, для замены в ходе тестирования реального объекта мок- объектом
можно воспо льзо ваться кодом вида fl t. re dis = mock_ red is. Но это чревато
