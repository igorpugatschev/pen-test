# Объектно-ориентированный Python, 4-е издание — страница 220

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

raise ValueErr or(
Тема ти ческ ое исследование 21 9
f"In valid pu rpose : {p u rpose !r }: {p urp ose _enu m}"
)
sup er() .� ini t� (
sepal _leng th=sepal _leng th,
sepa l_wi dth=sepal _wid th,
peta l_l eng th=petal _leng th,
petal_ width=petal _wid th,
self .p ur pose = pu rpose _enum
self . species = species
self ._ classi fication : Optio nal [s tr] None
def mat ches (s elf) -> bool :
return self .s pecies == self .c lassi fica tion
Проверка значения параметра purpose помог ает убедиться, что оно декодируется
либо в Purpose . Training, либо в Purpose . Testing. Если значение purpose не явля­
ется одним из двух допусти мых значений, мы вызовем исключение ValueE rror,
поск ольку данные окажутся непригодными для испо льзован ия.
Мы создали переменную экзем пляра sel f ._ classi fication с именем, начина­
ющимся со знака _. Такой знак, напомним, предп олагает, что имя не предна­
значено для общег о испо льзования клиентами класса. Это не означает «п ри­
ватный», пос кольку в Python нет понятия конфиденциальности пере менных.
Такой записи можно придать значение «с крыт ый» или, возможно, «обратите
внимание».
Вместо непрозрачных объектов, доступных в некоторых языках, Python исполь­
зует конкретный знак, который отличает эту переменную от других. Вы можете
проанализировать использование символа _, но, вероятно, не следует этого делать.
Первый метод @prope rty выглядит следующим обра зом:
@prope rty
def class ification (s elf) -> Opt ion al [s tr] :
if self . pu rpose == Pu rpose .T esting :
return self ._ classi fica ti on
else :
raise Att ribut eE rror (f "T raining samples have по classi fication ")
Пр иведенный код оп ределяет метод, котор ый будет отображаться как имя
атрибута. След ующий пример пока зыва ет создание образца для тестирован ия:
>>> fr om mod el import Kn own Samp le, Purpose
>>> s2 = Kn ow nSamp le (
sepa l_leng th=S .1 ,
sepa l_ wid th=З .5 ,
pet al _leng th=l .4,
pet a l_ width=0 .2,
specie s="Iris- setosa ",
