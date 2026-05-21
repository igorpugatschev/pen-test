# Объектно-ориентированный Python, 4-е издание — страница 264

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Темат ическ ое иссле дова ние 263
спец иалистов по обработке данных варьируются: 80 к 20 %, 67 к 33 % и даже
50 к 50 %. Поск ольку мнения экспе ртов различаются, необходи мо предоставить
специа листам возмо жность корректирова ть коэф фициент раздел ения.
Пу сть разделение будет свойс твом класса. Можем даже создать отдельные под­
классы для реализации альтернативных разделений:
class Sh ufflin gSamp lePar tition ( SamplePartition ):
def _in it_(
self,
iteraЬle : Opt io na l[ Iter aЫe [ SampleDict ]] Non e,
* ,
traini ng_s ubset : float = 0.8 0,
-> None :
sup er() ._ init _( itera Ыe, trainin g_s ubse t=t raini ng_s ubse t )
sel f. spli t : Opt io nal [ int] = None
def shu ffle (s elf) -> None :
if not self .s plit :
ran dom .s huffle (s elf)
self .s plit = in t(l en ( self ) * self .tr ainin g_subse t )
@proper ty
def tr aining (s elf) -> List [T rainin gKnownSample ]:
self . shuf fle( )
return [Trainin gKnownSample (* *sd) for sd in sel f[ : sel f. spli t]]
@property
def testing (s elf) -> List [T esti ngKno wnSam ple] :
self . shu ffle ( )
return [T esti ngKnownSample (* *sd ) for sd in self [ self .s pli t :]]
Пос кольку мы расшир яем супер класс SampleParti tion, мы можем испо льзовать
перегруженные определения метода _ini t_ () . Для этого подкласса необходимо
предостав ить конкретную реализацию, совместимую с суперкла ссом.
Оба свойства, training и testing, испо льзуют внутренний метод shu ffle ().
Этот метод работает с атрибутом spli t, чтобы гарантировать, что выб орки будут
перетас ованы только один раз. В дополнение к отслеживанию того , перемешаны
данные или нет, атрибут self . spli t также показыва ет, где раздел ить обра зцы
на обучающие и тестовые подмножества.
Свойс тва traini ng и testing также имеют дело со срезами спис ка Python для
разделения необработанных объектов SampleDict и создания полезных объектов
Tra ini ngKnownSample и TestingKnownSample из необработан ных данных. Они
полаг аются на генерац ию списк а для применения конструктора класса, напри­
мер Trainin gKnownSample, к словарю значений строк в подмн ожестве списка
self [ : self . spli t ] ]. Генерация списк а избавляет нас от необходимости создавать
