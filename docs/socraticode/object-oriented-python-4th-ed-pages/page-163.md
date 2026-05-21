# Объектно-ориентированный Python, 4-е издание — страница 163

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

16 2 ГЛАВА l. О жидаемы е нео жиданно сти
которого принимает текущий баланс и сумму, которую пользователь хочет снять.
Кроме того, добавл ен метод для расчета степени превышения запроса:
>>> from decimal im port De ci mal
>>> class In val idWithd raw al (V alueErr or ):
def _init _( self, balance : Decim al, amount · Dec i ma l) -> Nonc :
supe r-( ) ._ init _( f".:Jcc ount doesn 't have ${. 11 1 юun t}")
self . amount = amount
self . balance = balance
def overage (s elf) -> Decim al :
ret urn self . amount self . balance
Поскольку мы работаем с валютой, мы импо ртировали класс Deci mal. Мы не мо­
жем испо льзовать по умолчанию типы int или float для валюты, где имеется
фик сированное количество десятичных разрядов и чрезвычайно сложные пра­
вила округ ления, предполагаю щие точную десятич ную арифметику.
Об ратите внимание, что номер счета не является частью исключения. Банкиры
не прив етствуют использование номера счета, который можно легко отслед ить.
Рассмотр им пример создания экзем пляра данного исключения:
»> ra1se Inval 1dW1t hd raw al(D ecш al ('2 5.0 0'), De c1 ma l( 'S O.O O' ))
Traceback (m ost recent call las t) :
Inval 1dW1thdraw al · ac count doesn 't have $50 .0 0
Ниже в коде представлена обработка исключения Inval idWithdrawal при его
возникновении:
»> tr y:
balance = Decimal ('2 5.0 0' )
raise In val idWithdraw al(b al ance, Dec im al( '5 0.0 0' ))
ex cept Inval idWithd rawa l as ех :
prin t("I 'm sorr y, but your withd rawa l is
"more than your balance Ьу "
f"$ {ex . overag e( )}")
В этом коде показано правильное испо льзование ключевого слова as для сохра­
нения исключения в локальной перемен ной ех. По соглаш ению большинс тво
разрабо тчиков Python прис ваивают исключению переменную, нанример ех, ехс
или exception; хотя вы можете присваива ть также и нривычные имена, напри­
мер the _e xcep ti on_ rais ed_a bove или aunt_s all y.
У программиста может появиться множество причин для определения собствен­
ных исключений. Бы вает полезно доб авить информацию в исключение или
каким-либо образом зарегист рировать его. Но где полезность пользовательских
