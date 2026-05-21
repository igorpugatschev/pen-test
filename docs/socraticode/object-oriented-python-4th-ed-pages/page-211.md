# Объектно-ориентированный Python, 4-е издание — страница 211

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

21 0 ГЛ АВА 5 Ко гда бе з ОО П не обо йтись
@abstra ctmethod
def tr an sfor m( self, ext racted : Path) -> None :
В методе _i ni t_( ) мы удалили три параметра: pattern, find и replace, кото­
рые были слишком специфичны для ZipReplace. За тем переимен овали метод
fi nd_re pla ce( ) в process _ files ( ), разбили сложный метод copy_a nd_ tran sfor m()
и принудили его вызыва ть несколько других методов для выполнения реальной
работы. Также добавлен плей схолдер для метода tran sform( ). Изменения имени
пом огают продемонстрирова ть более общий характер нового класса.
Этот новый класс ZipProcessor является подклассом АВС, абстрактн ого базовог о
класса, что позво ляет нам предоставлять плей схолдеры вместо методов. Более
подробно АБС будет опис ан в главе 6. Этот абстрак тный класс на самом деле
не опре деляет метод tr ansfor m( ). Если сейча с попыт аться создать экземпляр
класса ZipProcessor, отсут ствующий метод tran sfor m( ) вызовет исключение.
Форма льный вид @abstract method дает понять, что не хватает какого-то фраг­
мента и этот фрагмент должен быть вполне конкретным, ожида емым.
Теперь, прежде чем перейти к приложению для обработки изображений, создадим
версию исходного класса ZipReplace. Она будет основана на классе ZipProcessor
и послужит для испо льзования родител ьского класса следующим обра зом:
class TextTw eaker (Z ip Proc essor ):
def �init �( self, ar chi ve : Path } -> None :
su pe r( ). � ini t�( archive)
self .f ind : str
self . repla ce : str
def find _and_rep lace( self, find : st r, rep lace : str) -> "T extTwea ker" :
self . find = find
self . replace = replace
retur n self
def transf orm (s elf, extracted : Path) -> None :
input _text = extracted . read _text ()
outp ut_text = re .s ub( self . find , self . rep lace, inp ut_text )
extracted . write _text (o utpu t_text )
Эт от код короче исходной версии, поск ольку он наследует возможности об­
работки ZIP от родител ьского класса. Сна чала имп ортируем только что напи­
санный базовый класс и принуждаем TextTweaker расширять этот класс. Затем
испо льзуем super () для инициализации родител ьског о класса.
Необходимо предоставлять два дополнительных параметра, поэтому мы исполь­
зовали технику, называемую плавным интерфейсом. Метод find_a nd_re place ()
