# Объектно-ориентированный Python, 4-е издание — страница 489

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

488 ГЛАВА 11 Об щие патт ерны проек ти рова ния
Чтобы использова ть два приведенных отдельных приложения, надо выпо лнить
следующие действ ия.
1. Откройте рядом два окна терминала. Это поможет изменить заголовки окон
на cl ient (клиент) и ser ver (сервер ). Пользова тели терминала macOS могут
использова ть элемент change title (и зменение заголовка) в меню shell ( оболоч­
ка). По льзова тели Wi ndows - ком анду title.
2. В окне сервера запус тите серверное прилож ение:
pyt hon src/ soc ket _serv er .p y
3. В окне клиента запустите клиентское прилож ение:
pyt hon src/ soc ke t_c lien t .p y
4. В окне клиента введите свои ответы. Например:
How many ro lls : 2 ow many ro lls : 2
Dice pattern ndб [d k+- ]a: dб
5. Клиент отправит команду, прочитает ответ, выведет его на консоль и выйдет.
Запус кайте клиент скол ько угодно раз, чтобы получить после довательность
бросков кост ей.
Резул ьтат будет выг лядеть так, как показано на рис. 11 .2.
sr c:: -Server -python socket __ server.py -60х24 • • •
JI\ ls
D src -Cllent- �zsh -б0х24
\ ls
__pyca che _ socke t_server . ру
socket_ cli ent .p y
\ python socket_server .p y
Receiving b' Dice S 2d6 ' fr om 12 7.О.О.1
Sending b' Dice S 2d6 • [6, 9, 8, 10, 3] ' to
0.1
Rece iving b" Dice 6 4d6k3 ' fr om 12 7.О.О.1
Sending b' Dice 6 4d6k3 = [5, 11, 14, 8, 7,
12 7.О.О.1
Rece iving b' Dice 3 10 d8+2 ' fr om 12 7.О.О.1
Sending b' Dice 3 10 d8+2 = [42, 32, 41 ]' to
.1
о
__pycache_ socket_serv er .p y
socket_ cl ient .p y
JI\ python socket_ cl ient .p y
How many rolls : S
12 7.О. Dice pattern nd6 [ dk+- )a: 2d6
Dice 5 2d6 • [6, 9, 8, 10, 3]
,,
13 )' to { \ python socket _cli ent .p y
How many ro lls : 6
Dice pattern nd6 [d k+- )a: 4d6k3
127 .О.О Dice 6 4d6k3 • [S, 11, 14, 8, 7, 13)
{\
,\ python socket_ cli ent .p y
How many ro lls : З
Dice pattern nd6 [ dk+- ]a: 10 d8+2
Dice 3 10 d8+2 • [42, 32 , 41 )
' 1
Рис. 11. 2. Серве р и клие нт
На схеме слева изображен сервер. Приложение запущено, и оно начало прослу­
шива ть порт 2401 для клиентов . Справа изображен клиент. Каждый раз, когда
запус кается клиент, он подключ ается к об щедосту пному со кету. Опе рация
