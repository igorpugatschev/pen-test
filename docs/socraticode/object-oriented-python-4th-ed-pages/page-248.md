# Объектно-ориентированный Python, 4-е издание — страница 248

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Пер егру зка опер аторов 247
базовый класс, котор ый содержит игральные кости разных видов. Прове рьте
предыду щий класс Dice, который предпо лагал кости одного вида. Это не аб­
страк тный класс, в нем содержится определение броска, при котором перебра­
сы ваются все кости . Начнем с определе ния некоторых основ, а затем включим
спе циальный метод _аdd_ () :
class DDi ce :
def _in it_( self, *d ie_ class : Type [Di e] ) -> None :
self .d ice = [d c() for dc in die _cla ss]
self .a djus t : int = 0
def pl us( self, adj us t : int 0} -> "D Dice ":
self .a dj ust = adj us t
return self
def ro ll( self} -> None :
for d in self .d ice :
d.r ol l()
@property
def tota l(s elf} -> int :
return su m(d . face for d in self .d ice) + self .a dj ust
Согласит есь, очень похоже на определенный выше класс Dice. Добавлен атрибут
adjus t, установ ленный методом plus (), чтобы была возможность испо льзо­
вать DDice (Dб, Dб, Dб) .p lus (2). Это подходит для некоторых настольных игр
(T TRP G).
Кроме того, помни те, что мы предоставляем классу DDice типы игра льных
косте й, а не экземпляры игральных косте й. Мы испо льзуем объект класса Dб,
а не экземпляр Die, созд анный выражением вроде Dб( ). В методе _init _( )
создаются экземпляр ы классов DDice.
Для определения сложного броска костей применим оператор + (п люс) с объ­
ектами DDice, классами Die и целыми числами:
def _a dd _( self, di e_class : Any ) -> "D Dic e" :
if isi nstan ce(di e_class, type ) and issubcl ass ( di e_class, Di e) :
new_c lasses = [typ e(d} for d in self .d ice] + [d ie_cla ss]
new = DDi ce (* new_c lasses ). plus (s elf .a djust)
return new
elif is instan ce(di e_class, int) :
new_c lasses = [t yp e(d} for d in self .d ice]
new = DDi ce (* new_c lasses ). pl us(di e_cla ss)
return new
else :
retur n Not imple mented
