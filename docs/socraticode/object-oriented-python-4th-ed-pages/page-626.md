# Объектно-ориентированный Python, 4-е издание — страница 626

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Объе кт senti neL
И ми та ци я об ъек тов с п омо щью м а ко в 625
Во многих проек тах встречается класс со значениями атрибуто в, которые могут
быть предоставл ены в качестве параметров другим объектам, причем в этом клас­
се отсутствует реальная обработка этих объектов. Например, классу может быть
предоставлен объект Path, а затем этот класс предоставляет принятый объект
функции операционной системы. Получается, что созданный класс не занимается
ничем, кроме пром ежуточного сохранения объекта. С точки зрения модульного
тестирования для тестируемог о класса объект непрозрачен - создаваемый класс
не обр ащается внутрь объекта, к состоя нию или к метод ам.
Для создания непрозрачных объектов в модуле uni ttest . mock имеется удобный
объект sentinel, которым можно воспользо ваться в тесто вых сценариях, чтобы
убедиться, что приложение сохранило и переслало объект нетронуты м.
Рассмотрим класс Fil eChecksu m, сохраняющий объект, вычисленный функцией
sha25 6() модуля hashl ib:
class File Chec ksum :
def �init �( self, sour ce : Path) -> None :
self . source = source
self . checksum = hashl ib . sha256 (s ource . rea d_byt es ())
Этот код можно изолиро вать от других модулей, чтобы прове сти модульное
тести рование. Для модуля hashlib будет создан мок- объект, а для результата -
sentinel:
from un ittest .m ock import Moc k, sentinel
@pytest . fixture
def moc k_hashlib (m onkeypa tch) -> Mock:
moc ked_ hashlib = Mock( sha25 6=M oc k( retu rn_va lue=sentin el . checksu m) )
monkeypa tch . setat tr( checks um_writer, "h ashli b" , mock ed_ hashlib)
return moc ked_ hashlib
def te st_file _checksu m(m ock _hashlib, tmp_pat h) -> None :
source _file = tmp_path / "s ome_file"
source _fi le . write _text ("")
cw = checks um_wri ter .F il eCh ecksum( source _file )
as ser t cw . source == source _file
as ser t cw. checksu m == sentin el . checksu m
Нашим объектом mocked_ hashlib предоставляется метод sha2 56, возвраща ющий
уникальный объект sentin el . checksu m. У этого объекта, созданного объектом
sentinel, крайне небольшое число методов или атрибут ов. В качестве уникаль­
ного объекта может быть взято любое имя атрибута; в данном случае выбрано
имя "ch ecksu m". По лученный объект предназначен исключительно для проверки
