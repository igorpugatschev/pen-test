# Объектно-ориентированный Python, 4-е издание — страница 194

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

if not name :
Управ лен ие пове ден ием об ъе кто в класса 19 3
raise Va lueE rror (f" Invalid name {n ame!r }")
self ._ name = name
def _set_name (s elf, name : str) -> None :
if not name :
raise Va lueErr or (f" Invalid name {n ame!r }")
self ._ name = name
def _get_n ame (s elf) -> str :
retur n self ._ name
name = proper ty (_get_name , _set_name )
Срав ните с предыд ущим классом, и вы заметите, что здесь сначала меняется
атрибут name на (п олу-) прива тный атрибут _name. За тем для получения и опре­
деления этой переменной добавляется еще два (п олу-) приватных метода, вы­
полняя прове рку при определении пере менной.
Наконец у нас создана конструкция proper ty. В классе Color Python создает
новый атрибут name. Данный атрибут установлен как свойств о. «З а кулиса ми�
происх одя щего атрибут proper ty делегирует реальную работу двум только
что создан ным методам . При испо льзова нии в контексте дост упа (сп рава от
знака = или : =) перва я функция получает значение. При испо льзован ии в кон­
тексте обновления (с лева от знака = или : = ) вторая функция устанавл ивает
значение.
Данную новую версию класса Color можно использовать точно так же, как и пре­
дыдущую, но теперь она выполняет проверку при опре делении атрибута name:
>» с= Colo r_VP (0 xff0000 , "b right re d")
»> c. name
'b right red '
>>> c. na1 ne
>» с. name
'r ed '
»> c. na me
"r ed "
Traceb ack (m ost recent call las t) :
Fil e "<s tdi n>", lin e 1, in <m odule>
Fil e "s et ti ng_ name_pr operty .p y", li ne 8, in set name
raise Va lueErr or(f" In va lid name {n am e!r }")
Va lueE rror : In va lid name ''
Таким образом, если мы ранее написали код для доступа к атрибуту name, а затем
изменили его, чтобы испо льзова ть объект на основе proper ty, предыдущий код
все равно будет работа ть. Поп ытка установить пустое значение property - это
поведение, которое необходимо запретить. И все это в целом - несомненный
успех !
