# Объектно-ориентированный Python, 4-е издание — страница 642

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Те мати ч еск ое и сс ле дов ание 641
применяться для создания экземп ляра Hyperpa rameter, которому будет при­
дано имитируемое выч исление расстоя ния и упомянутый сы митиров анный
набор данных. Ис пользуема я тестова я фи кстура имеет следующий вид:
@pyt est .f ix tur e
def hyperpa rame ter (s ample _d ata : list [Mock] ) -> Hyperpa rameter :
mocke d_dis tance = Moc k( distan ce =Mo ck(s ide _effe ct= [l l, 1, 2, З, 13] ))
moc ked_ traini ng_data = Moc k( train ing=sample _dat a)
moc ke d_we ak ref = Moc k(
retu rn_value= mock ed_ traini ng_data )
fixture = Hyperpa rame ter(
k=З, alg orit hm=moc ked_ dis tance, train ing=sentinel .U nused )
fixture .d ata = mock ed_weakr ef
return f ixt ure
Объект mock ed_ distance будет предоставлять последо вательность результа­
тов, похожих на результаты вычислений расстоя ний. Выч исления расстоя ний
тестируются отдел ьно, а с помощью данного мок- объекта метод classi fy '()
оказы вается изолирован от кон кре тных вычис лений. Здесь по средством
Мосk -о бъекта, который будет вести себя как слабая ссылка, задается список
сы митиро ванных экземпляров KnownSample; обучающим атрибутом этого мок­
объе кта будут данные образца.
Чтобы убедиться, что экземпляр Hyperpa rameter выдает прав ильные запрос ы,
анализируется метод classi fy ( ). Весь сценарий, включая эти два заключитель­
ных шага THEN, выглядит так:
GIVEN (З АДАНО ) фикст ура дан ных образца с пять ю экзе мпля рами , отражаю щими
два вида
WH EN (К ОГ ДА ) примен яется ал горитм k -N N
THEN (Т ОГ ДА ) резул ьтат пр едс тав ляет со бой ви ды с наиб олее бл изки ми тр емя
расс тояния ми
AND (И) при 9том было вызвано сы митирован ное вы чи сление расст ояний со все ми
обучаю щими дан ными
Завершающий тест с учетом указанных выше фи кстур выг лядит следующим
образо м:
def te st_hy perpa rame ter( sample _data : list [Mock ], hyperpa rame ter : Moc k)
-> None :
s = hyperpa ramet er .c lassi fy ( sentinel . Unkno wn )
ass ert s == sentinel .S pec iesl
as ser t hyperpa ramete r. al gorithm .d istance .m ock _calls
call( sentinel . Un kno wn , sample _da ta[0] ),
ca ll( sentinel . Unkno wn , sample _d ata [l] ),
call ( sentinel . Un kno wn , sample _d ata [2] ),
call ( sentinel . Unkn own , sample _d ata [З] ),
call ( sentinel . Unk nown , sample _da ta [4] ),
