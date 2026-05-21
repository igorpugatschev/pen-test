# Объектно-ориентированный Python, 4-е издание — страница 262

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти ческ ое иссл едо ван ие 261
Встроенные структуры Python, такие как lis t, имеют множество альтернатив
инициализации, например такие:
• для создания пустого сп иска использова ть list () ;
• для создания списка из итерируемог о источника данных применить lis t(x).
Чтобы сделать это понятн ым для туру, необхо димо вставить декора тор
@ove rload. Это выявит два разных спо соба использования метода _i nit_( )
класса lis t:
class SamplePartition (L ist [S ampleDict ], аЬс .А ВС) :
@overload
def _init _( self, *, traini ng_s ubse t : float = 0.8 0) -> None :
@overload
def _init_(
self,
iter aЫe : Optio nal [ IteraЫe [ SampleDict ]] None ,
* ,
trainin g_s ubse t : float = 0.8 0,
-> None :
def _in it_(
self,
iter aЫe : Opt io nal [ Iter aЫe[ SampleD ic t] ] Non e,
* ,
trainin g_su bse t : float = 0.8 0,
-> None :
self .t rainin g_s ubse t = traini ng_s ubset
if iteraЫe :
sup er() ._ ini t_( iter aЫe)
else :
supe r( ). _ in it_( )
@abc .a bstractpr operty
@property
def training (s elf) -> List [T rainin gKno wnSample ]:
@abc .a bstr actpr oper ty
@property
def testing (s elf) -> List [T estin gKnownSample ]:
Для мeтoдa _in it_( ) мы определили две перег рузки. Это форма лизмы, чтобы
сообщить туру наше намерение. Пе рвая перег рузка - _init _( ) без позицион­
ных парамет ров. Должен создаться пустой спис ок объектов SampleDict. Вторая
перегрузка - _i nit_( ) с итериру емым источником объектов SampleDict в ка­
честве единственного позиционного параметра. Си мвол * отделяет парамет ры,
