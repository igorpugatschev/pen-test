# Объектно-ориентированный Python, 4-е издание — страница 134

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

def pla y( self) -> No ne :
print (f" playing {s elf . filepa th} as mрЗ" )
class WavFile(A udioFile ):
ext = ". wav' '
def pla y( self ) -> None :
print (f" playing {s elf . filepa th} as wav")
class OggFile (A udioF ile) :
ext = ". ogg"
def pla y( self) -> None :
print (f" playing {s elf . filepa th} as og g" )
По ли мор фи зм 13 3
Все аудиофайлы необходимо проверять, чтобы убедиться , что при инициали­
зации им было задано валидное расширение. Если имя файла зака нчивается
некоррек тным обозначением форма та, возникает исключение (б олее подробно
исключения будут рассмотрены в главе 4).
Вы уже поняли, как метод _init _( ) в родител ьском классе получает доступ
к переменной класса ext из разных подклас сов? Это и есть принцип полимор­
физма. Родите льский класс AudioFile имеет подсказку типа, объя сняющую
туру, что добавлен атрибут ext. В действительности он не хранит ссылку на
атрибут ext. Когда унаследованный метод используется подклассом, происх одит
определение подкласса атрибута ext. По дсказка типа помог ает туру обнаружить
класс, в котором отсутствует назначение атрибута.
Кроме того, каждый подкласс AudioFile реализует метод pla y() по- своему (дан ­
ный пример в действ ительности не воспроиз водит музыку: для того чтобы опи­
сать алгоритмы сжатия аудио, нужна отдельная книга!). Это также полиморфи зм.
Для воспроизве дения файла, независимо от его типа, медиаплеер испо льзует
один и тот же код. Ему все равно, какой подкласс AudioFile испо льзуется. При
распаковке аудиофайла применяется инкапсуляция. Проверим все это, полагая,
что пример ниже будет работать, как мы ожидае м:
>» p_l = MP ЗFile( Path (" Hear t of the Sunrise .m p З" ))
>» p_l .p la y()
pla ying Heart of the Sunrise .m pЗ as mрЗ
»> р_2 = WavF il e(P ath ("R oundab out .w av" ))
»> p_ 2.p la y()
playing Rou ndab o ut .w av as wav
»> р_З = Og gFile (P at h( "H ear t of the Sunrise . ogg" ))
»> р_З .р lа у()
playing Heart of the Sunrise . ogg as ogg
>» р_4 = MP ЗFile( Pa th( "The Fish .m ov" ))
Traceb ack (m ost recent call las t) :
Va lueErr or : Invalid file format
