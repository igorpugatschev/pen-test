# Объектно-ориентированный Python, 4-е издание — страница 641

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

640 ГЛ АВА 13 Тести рова ние об ъек тн о- ори ен тирова нных про гр амм
for kno wn in traini ng_d ata .t raining
k_nearest = (k nown .s pecies for d, known in dis tances [: sel f.k ] )
frequen cy : Count er[ str] = collectio ns . Count er(k _nearest )
best _fit , *o thers = frequen cy . most _c ommon ()
spec ies , votes best _fit
return species
Атр ибут al gori thm класса Hyperpa rameter является ссылкой на экзем пляр
одного из объектов выч исления расстоя ния. При замене мок- объект должен
быть вызываемым и возвра щать соответствующее допускающее сортировк у
число.
Атрибут data является ссылкой на объект Training Data. Мок- объект для заме­
ны объекта data должен содержать атрибут train ing, представля ющий собой
список имитируемых обра зцов. Поск ольку эти значения передаются другому
мок- объе кту без как ой-л ибо проме жуточ ной обрабо тки, для подтверждения
предоста вления обучающих данных имитируе мой функции выч исления рас­
стоя ния можно обратиться к объе кту sentinel.
Замы сел тако й: наблюдать, как метод classi fy ( ) «вы полняет все необходимые
действия ». Для подтверж дения выдачи запросов и фиксации их резул ьтатов
предоставляются Mock- и sentinel-o бъeк ты.
При более сложном тестировании понадобятся некоторые сым итированные дан­
ные образцов. Все будет зависеть от sentinel-o бъeктoв. Объекты будут переданы
для вычисления имитируем ого расстоя ния. Оп ределение ряда испо льзуемых
имитируемых объекто в- обра зцов выглядит следующим обра зом:
from �f utu re� import ann ot ations
fr om mod el import Hyperpa rame ter
from uni ttest .m ock impor t Moc k, sent inel, call
@pyt est .f ixture
def sa mple _d ata () -> list [M ock ]:
return [
Moc k( name= " Samplel ", species=sentinel .S peciesЗ ),
Mock(n ame= " Sample2 ", species=se ntinel .S peciesl ),
Mock(n ame=" SampleЗ ", species=sentinel .S pecie sl ),
Mock( name=" Sample 4", species=sentinel .S peciesl ),
Moc k(na me="S ampl eS ", species=sentinel .S pec iesЗ ),
Эта фи кстура представляет собой список мок-о бъектов для KnownSamples.
Для того чтобы упростить отладку, каждому образцу дано уникальное имя.
Здесь также предоставлен атрибут species, поск ольку именно он исполь зуется
методом classi fy( ). Никакие другие атрибуты не предоста влены, поск ольку
тестируе мым модул ем они не исп ользую тся . Фи кстура sample _d ata будет
