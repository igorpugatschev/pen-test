# Объектно-ориентированный Python, 4-е издание — страница 620

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

class Fl ightS tatusTr ack er :
def �in it�( self) -> None :
И ми та ци я об ъе ктов с пом ощью мок о в 61 9
self . redis = redi s. Re dis (h os t="12 7.0.0.1 ", por t=6379, db=0)
def cha nge_s ta tus ( self, flig ht : str, statu s: Sta tus ) -> None :
if not isins tan ce( sta tus, Status ):
raise ValueE rror (f" {s tatus !r } is not а valid Sta tu s")
key = f"f l ightno :{ fl ight }"
now = datetime .d atetime . now(tz= datetime .t imezone .u tc)
value = f"{n ow.i soformat ()}l{ status .v alu e}"
self .r edis . set (k ey, value)
def get_s ta tus( self, fl ight : st r) -> tuple [ datetime . date t ime , Stat us ]:
key = f"f l ightno :{ fligh t}"
value = se lf . red is .g et (k ey) . decod e( "u tf-8" )
text_ ti mestamp , tex t_st atus = value .s pli t(" I")
ti mestamp = datet ime .d atetime . fr omi soformat (t ext_ ti mest amp)
sta tus = Sta tus ( tex t_s tat us)
retur n ti mestamp , status
В классе Status дается определение перечислению четырех стро ковых значений.
Чтобы получить конечную ограниченную область действит ельных значений,
предостав лены сим волические имена вида Sta tus . CANC ELLED. Фактические
значения, хранящи еся в базе данных, будут строкам и типа "CANCELLED". Они
на данный момент совпа дают с сим волами, испо льзуе мыми в прилож ении.
В перспективе область значений может расширит ься или измениться, но хоте­
лось бы, чтобы сим волические имена в приложении были отделены от строк,
появля ющихся в базе данных. Обычно в Enum испо льзуются числовые коды, но
их трудно запомнить.
В методе cha nge_ status () много чего нужно протестировать. Пр оверяется при­
надлежность значения аргумента sta tus к одному из экземпляров перечисле­
ния Status, но можно было бы и расширить наши действия. Нужно убедить ся,
что отсутствие смыс ла в аргументе fl ight вызы вает выдачу соответствующей
ошибки. Еще важнее наличие теста на правильный формат ключа и значения
при вызове метода se t() для объе кта redis.
А вот про верять в модульных тестах правиль ность хранения данных объектом
redis нам не нужно. Это, вне всяког о сомнения, должно про веряться при инте­
грационном или приемочном тестировании приложений, а на уровне модульного
тестирования можно предположить, что разработч ики py-r edis протестировали
свой код и данный метод справляется с тем, что от него ожидают. Как правило,
модульные тесты должны сохранять автономность, то есть тестиру емый мо­
дуль должен быть изолирован от внешних ресурсо в, например от запущенног о
экзем пляра redis.
