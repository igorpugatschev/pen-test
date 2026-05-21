# Объектно-ориентированный Python, 4-е издание — страница 167

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

16 6 ГЛАВА l. Ожида емы е нео жида нн ост и
Чтобы завершить код приме ра, опре делим Ite mType:
class It emType :
def �init �( self, name : str) -> None :
self .n ame = name
self . on_hand = 0
Ни же в коде представлен интерак тивный сеанс с ис поль зованием класса
Inv entor y:
»> widget = It emType (" W idge t")
> » gadget = It emType ( "G adg et ")
>>> inv = Inv entor y ([ w idget , gadget j)
>>> it em _t o_buy = widget
>>> in v. lo ck( it em_to_b uy )
>» tr y:
nu m_ left = inv . purchase (i tem _to_b uy)
exc ept Invalidite mType :
print (f"S orry , we don 't sell {it e1 11 to buy .n am e}")
exc ept OutOfStoc k:
print (" S orтy , that item is out of stoc k .")
else :
pr'int (f"P urchase co mple te . There ar e {n u1 11_lef t}
{i t em_to_buy .n am e)s lef t")
finally :
inv . unlo ck( it em_t o_ buy )
Sorry , that ite m is out of sto ck.
Все возможные пункты обработки исключений испо льзуются для обеспечения
того, чтобы правильные действия выпо лнялись в нужное время. Хоть OutOfStock
и не является исключительной ситуацией, чтобы обработать его, можно исполь­
зовать исключение. Этот же код можно написать с исполь зованием структуры
i f ... eli f ... else, но она усложнит чтение и соп ровождение кода.
Кроме того, одно из сообщ ений, There ar e {n um_l eft } {i tem_to_ buy . name}s
left, отобра жается с грамма тическими ошибка ми. Когда остал ся только один
элемент, требуется скрупулезна я проверка синтаксиса There is {n um_l eft }
{i tem_t o_b uy .n ame} lef t. Чтобы поддерживать разум ный подход к перево ду,
лучше не акцентировать внимание на грамматике внутри f-стро ки. А для выб ора
необходимого сообщения с соответс твующей грамматикой предпоч тительнее
испо льзова ть блок else:
msg = (
f"th ere is {n um_l eft } {i tem_to_buy .n ame} le ft "
if num_l eft == 1
else f" there are {n um_left } {i tem_to_buy .n ame}s lef t")
print (msg)
