# Объектно-ориентированный Python, 4-е издание — страница 688

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Б иб л ио те ка Async lO 687
существует более шести миллиардов перест ановок; больши нству комп ьютеров
для сортировки по порядку 13 элементов согласно данному алгоритму может
потребо ! аться не один год.
Функция main() занима ется сортировкой и записью в журна л нескольких
регистра ционных сообщ ений. Ею выпо лняе тся большой объем вычис ле­
ний, при этом задейств уются ресурсы центра льного процессора, но не при­
нос ится практически ник акой поль зы. Пр ограмма main, которой можно
воспользова ться для вы полнения запросов к журналу, пок а неэффектив ная
сортировка тратит компьютерное время на обработку данных, выг лядит сле­
дующим обра зом:
def main(w orkload : int, sor ter : Sorter BogoSort ()) -> int :
to tal = 0
for i in range (w ork load ):
samples = rando m. randint (З, 10)
data = [r ando m. rando m( ) for _ in range (s amples )]
ordered = sorter .s ort (d ata )
to tal += sa mples
return total
if name _ma in_" ·
LOG_H OST , LOG_PO RT = "l ocalh ost ", 188 42
soc ket_ handler = logg ing .h andlers . Soc ketHa ndler (
LOG_HO ST, LOG_ PORT )
st ream_handler = loggi ng . Stream Ha ndl er( sys . stderr )
logg ing . basi cConfig (
handlers= [ soc ket_ handler, st ream_ha ndle r] ,
level= logg ing .I NFO)
star t = ti me . pe rf_c ou nter ()
workload = rand om .r andin t (1 0, 20 )
logg er . inf o(" sorting %d collectio ns ", workload )
samples = main(w orklo ad, BogoSort ())
end = ti me . perf _counter ()
logg er . info (
"s orted %d collecti on s, taking %f s", worklo ad, end - star t )
lo gging .s hut down ()
Сценарий верхнего уровня запус кается путем создания экземпляра SocketHand­
ler, кот орый записыва ет регистрацио нное сообщение в по казан ный выше
сервис сборщика сообщ ений. Экземп ляр StreamHandler записы вает сообщение
в консоль. Оба объекта пре доставляются в качестве обработч иков для всех
оп ределенных сервисов регистрац ии. После конфиг урирования системы ве­
дения регистра ционных записей вызы вается функция main() с произвольной
рабочей нагрузкой.
