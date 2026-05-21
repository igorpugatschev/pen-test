# Объектно-ориентированный Python, 4-е издание — страница 604

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

П р о ве дение мо дул ьн ог о тести ро вани я с п омо щью pytest 603
def test _met hod_2 (s elf) -> None :
print (" RUNN IN G ME THOD 1-2" )
class TestC lass2( Base Test ):
def test _metho d_l (s elf ) -> None :
print (" RUNNING ME THOD 2-1")
def test _met hod_2 (s elf) -> None :
print (" RUNNIN G ME THOD 2-2" )
Единственным предназначением класса BaseTest является извлечение четырех
методов, которые в остальном идентичны двум тестовым классам , и использо­
вание наследо вания для сокращения объема повторя ющегося кода. Ит ак, с по­
:шции pyt est у двух подклассов имеются не только два метода тестирования,
но также два метода настройки и два метода демонтажа (о дин на уровне класса,
один на уровне метода ).
Если запустить данные тесты с помощью pytest с откл юченным подав лением
вывода функции print () (п утем установки флажка -s или - -c aptur e=no ), будет
видна очередность вызова различных функций и сам их тестов :
% python - m pytest - -ca pt u re=no tests/tes t_set u p_tea rdo wn.p y
== == === === == === ===== === == tes t sessi on starts
pl atform dar win -- Pyt hon 3.9.0 , pyt es t-6. 2.2 , ру -1 .1 0.0 , p l uggy -0 .1 3.1
rootd ir: /. _/ch _13
colle cted 5 items
tests /test _set u p_t ea rdo wn .p y sett ing u p MODU LE test _ set u p_ teardo wn
RUNN IN G TEST FU NCTION
.s ett ing u p C LASS Tes tClassl
se tting u p METH OD test _method_l
RUNNING ME THOD 1-1
.t earing do wn METH OD te s t_ metho d_l
sett ing u p МЕ ТНОО test_ met hod_2
RU NNIN G ME THOD 1-2
.t earing down ME THOD test _m etho d_2
tearing down CL ASS Te stC l assl
se tt ing u p CL ASS TestC lass2
sett ing up ME THOD tes t_method_l
RU NNING METH OD 2-1
.t earing down ME THOD te st_ meth od_l
s ett ing u p ME THOD test_ method_2
RUNNIN G ME THOD 2-2
.t earing down ME THOD te st_ met hod_2
tearing do wn CL ASS TestC lass2
tearing do wn MODU LE te st_set u p_ tea rdo wn
== === == == = === = == ===== == === 5 pas sed in 0.0 1s
