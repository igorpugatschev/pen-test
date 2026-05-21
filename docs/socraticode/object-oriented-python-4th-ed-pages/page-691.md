# Объектно-ориентированный Python, 4-е издание — страница 691

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

690 ГЛ АВА 14 Ко нк уре нтна я обрабо тка да нных
В зависи мости от желаемой области мореплавания могут понадобиться допол­
нительные или другие зоны.
Для опис ания предстоящей работы потр ебуется класс MarineWX. Это при мер
паттер на Команда, где каждый экзем пляр является еще одним желаемым дей­
ствием. Для сбора данных из метеоро логической службы в этом классе имеется
метод run():
class Mari neWX :
advisor y_pat = re . compi le (r " \ n\ . \ . \ .( .* ?) \ . \ . \ . \ n", re .M 1 re .S)
def �init �( self, zone : Zo ne) -> None :
sup er() .� ini t�< >
self .z one = zone
self .d oc = ""
async def run ( self) -> No ne :
as ync with httpx . AsyncCl ient () as cl ient :
response = await cli ent .g et (s elf . zone .f oreca st_ url)
self .d oc = resp onse . text
@property
def advisor y( self) -> str :
if (m atch : = self . advi sor y_pat .s earch (s elf .d oc)) :
return match . group (l) .r eplace (" \ n", " " )
return ""
def �repr �( self) -> st r:
return f"{s elf . zone . zone _name } {s elf . advisor y}"
В этом приме ре метод ru n() посредством экземпляра класса As yncClie nt из
модуля httpx загружает из службы пог оды текст овый документ. Обособ ленное
свойство advis ory () анализирует текст в поиск ах паттерна, которым помеча ется
сообщение о морской пог оде. Разделы документа метеоро логической службы
действительно помечены многоточ иями и представля ют собой текст овый блок
и три точки. Си стема морских прогнозов разработана таким обра зом, чтобы
обеспечить простой в обработке форма т с небольшим объе мом документа.
Пока во всем этом нет ничего уникального или приме чательного. Нами опре­
делены хранилище информации о зоне и класс, собира ющий для этой зоны
данные. Важной частью здесь является функция main () . Она испо льзует задачи
Async IO для сбора как можно большег о объема данных с наибольшей возмож­
ной скоростью .
async def task _mai n() -> No ne :
star t = ti me . pe rf_c oun te r( )
for ecasts = [M ari neWX(z) for z in ZONES]
