# Объектно-ориентированный Python, 4-е издание — страница 179

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

17 8 ГЛ АВА 4 Ожидаем ые неожиданн ости
if value in self :
ret urn value
raise Va lueErr or (f"in valid {value lr }")
>» species � Doma in ({"I ri s-s etosa ", "I ris-v ersic olo ur" ,
"Iris-v ir ginica "})
>» species . valida te ( "I ris-v ers icolour" )
·r ris -versic olo ur '
>» species . val idate ( "o dob enidae" )
Traceb ack (m ost recent call las t) :
Va lueE rror : inv alid 'o doben idac '
Здесь можем примени ть функцию spec . val idate () аналогично тому, как ис­
пользова ли функцию floa t(). Данный код проверит строку, не принуждая ее
изменить значение на другое, и вместо этого в результате вернется строка. Для
невалидных значений вызы вается исключение ValueErr or.
Это позволяет перепи сать тело метода fr om_dict () следующим обра зом:
@c las smethod
def fro m_dic t(c ls, row : dic t [s tr, st r] ) -> "K nownSamp le" :
tr y:
return cls(
species=speci es . val idate (r ow[" specie s" ]),
sepa l_leng th =float (r ow[ "se pal _leng th "]),
sepal _wi dth =float (r ow["s epa l_width "]),
peta l_lengt h=float (r ow [ " petal_ length "' ] ),
pet al _width=float ( row [ " peta l_width '' ]),
except ValueE rror as ех :
raise Inval idSample Err or(f" invalid {r ow!r }")
По добная вариация основана на том, что глобаль ная переменна я species пред­
ставляет собой набор допус тимых обра зцов. Для создания необходи мого объ­
екта или возникновения исключения вполне логичен уже упомянутый выше
принцип EAFP.
Как уже упоминалось ранее, этот дизайн состоит из двух частей. Мы рассмотрели
основной элемент, вызвав соответствующее исключение. Теперь проанализи­
руем контекст, в котором испо льзована функция fro m_ dict () , и подумае м, как
могли бы сообщить об ош ибках пользова телю.
Чтение фа йло в CSV
Рассмо трим общий шаблон для создания объектов из исходных данных CSV.
Идея состоит в том, чтобы обратиться к методам fr om_dict () различных классов
для создания объекто в, которые испо льзует наше прилож ение:
