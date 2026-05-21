# Объектно-ориентированный Python, 4-е издание — страница 675

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

674 ГЛАВА 1lt Ко нк уре нтн а я обра бо тка да нн ых
Asyn clO в де йств ии
Каноническим примером блокирующей функции является вызов ti me. sl eep ( ).
Вызва ть функцию slee p( ) модуля ti me напрямую невозможно, поскольку это
при вело бы к перехва ту управления и остан овке цикла обработки событ ий.
В коде ниже будет использова ться версия sl ee p( ), имеющаяся в модуле as yncio.
Применяемый в выражении awai t цикл обработки событий может в ожидании
завершения sl ee p( ) чередова ть данную работу с выпо лнением другой сопро­
граммы. Чтобы проиллюстрирова ть основы цикла обработки событий Asy ncIO,
воспо льзуемс я асинхронной версией этого вызова:
import as ynci o
impor t rand om
async def rando m_sle ep( count er : float ) -> None :
delay = random .r ando m( ) • 5
print (f"{ counter} sleeps for {delay :. 2f} seconds ")
await asyncio .s leep (d elay )
print (f"{ counter} awaken s, refre shed ")
async def sl eepers ( how_many : int = 5) -> None :
print (f" Creating {h ow_many} tasks ")
tasks = [
asyncio .c reate _task( rando m_sleep (i) )
for i in range ( how_many )]
print (f"W aiting for {h ow_many} task s")
await asyncio .g ather (* tasks )
if _name_ == "_ main _" :
asyncio .r un( sle epers (S) )
print (" Done with the sl eepers ")
В этом примере рассматрив аются несколько особенностей Аsуnс IО­
прог рам мирования. Обща я обработка запус кается функцией as yncio . run ( ) .
В результате запуска ется цикл обработки событи й, вып олняющий сопрограмму
sl eepers (). Внутри сопрог раммы sl eepers () создается несколько отдельно взя­
тых задач, являющихся экземплярами сопрогра ммы random_s lee p() с заданным
значением аргумента. Функция random_ sl eep () использует as yncio . sl eep () для
имитации продолжите льно выполняющегося запроса.
По скольку все это создано с использованием функций, определяемых с помощью
. as ync def и вы раже ния await, охватывающего as yncio . sl ee p(), вы полнение
функций random_ sl ee p( ) и общей функции sl eepers () чередуется . Пр итом что
запросы random_s lee p() запуска ются в порядке значения их параметра counter,
они заверша ются в совершенно ином порядке.
