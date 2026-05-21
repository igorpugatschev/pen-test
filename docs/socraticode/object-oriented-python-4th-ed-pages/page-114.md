# Объектно-ориентированный Python, 4-е издание — страница 114

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

class Suppli er( Cont act ):
Н асл едован ие. Базовы е пон яти я 11 З
def order (s elf, ord er : "Ord er" ) -> None :
prin t (
"I f this were а real syste m we would send "
f" ' {orde r} ' order to '{ self . name} '"
Теперь, если протестирова ть данный класс в интерпре таторе, можно увидеть,
что все контакты, включая Поставщики, принима ют имя и адрес электро нной
почты в своем мeтoдe _in it_ ( ), и только экземпляры Supplier содержат метод
order () :
>» с � Conta ct( "S ome BocJy ", "so mebody @examp le . ne t")
>» s � ScJpplier (" ScJp Plie r" , "su pplier @lexample .n et")
>» prin t(c. na1 ne , c.e ma il , s. nan 1e , s.e ma il)
Some Body so mebody @exam pl e. net Sup Plier supplier @e xam ple . net
>>> from ppri nt import pprint
>>> pprint (c. all _contact s)
[C ontact ( '!J usty ', 'ciuc,ty(a)exampl e. com ' ),
Cont act ( 'S t ev e', 's teve@:i tmayb eahack . сот ' ) ,
Cont act ( 'S ome Body ' , 's o1 1 1ebody fiicxample . net ' ),
Sup plier'( 'S up Plier ', 's 1J ppl ier (ii:examp le . ne t') ]
>» c. orde г("I neecJ plieгs ")
Traceb ack (m ost recent caJ l las t) :
File "<s tdi п>" , 1 ine 1, in <n юdule>
Att ribut eEr тo1 ': 'C ontмt · obJ ect has no att гibute · orde1' '
»> s.o rder (" I neecJ pliers ")
If thi s wе ге а real system we wou ld send 'I need pl iers · order to 'S up
Plier '
Класс Supplier может вы полнять все, что спо собен делать контакт (вк лючая
добавле ние себя в спис ок Contact .a ll _con tacts), и, кроме того, все те допол­
нительные функци и, котор ые он должен обраба ты вать, являясь постав щиком.
В этом и есть преи мущество наследования.
Об ратите внимание, что в списк е Contact . all _cont acts собраны все экземпляры
класса Contact и подкласса Supplier. При использов ании self . all _c ontacts
не все объекты содержались бы в классе Contact, а экземпляры Supplier были бы
помещены в Suppli er . all _con tacts.
Н асл едов а н ие от встрое нн ых ти пов
Одним из применений таког о типа наследования является добавле ние функ­
циональности к встр оенным класса м. Ис пользуя класс Contact, как уже было
пок азано, можно добавить контакты в список всех контакто в. Что, если пона­
добит ся в этом сп иске выполнить поиск по имени? Для таких случаев можно
