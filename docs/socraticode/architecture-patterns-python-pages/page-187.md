# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 187

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 9. Катимся в город на шине сообщений 187
def allocate(
- orderid: str, sku: str, qty: int,
- uow: unit_of_work.AbstractUnitOfWork
+ event: events.AllocationRequired, uow:
 unit_of_work.AbstractUnitOfWork
) -> str:
- line = OrderLine(orderid, sku, qty)
+ line = OrderLine(event.orderid, event.sku, event.qty)
 ...
+
+def send_out_of_stock_notification(
+ event: events.OutOfStock, uow: unit_of_work.AbstractUnitOfWork,
+):
+ email.send(
 ...
Попутно мы сделали API сервисного слоя более структурированным и по-
следовательным. Раньше это была россыпь примитивов, теперь же в нем
используются четко определенные объекты (см. врезку выше).
Шина сообщений теперь собирает события из UoW
Т еперь обработчикам событий нужен UoW . Кроме того, поскольку шина
сообщений занимает уже центральное место в приложении, имеет смысл
возложить на нее обязанность по сбору и обработке новых событий явным
образом. До сих пор существовала некоторая циклическая зависимость
между UoW и шиной сообщений, так что это сделает ее односторонней.
Обработчик принимает UoW и управляет очередью (src/allocation/service_layer/
messagebus.py)
def handle(event: events.Event, uow: unit_of_work.AbstractUnitOfWork): 
 queue = [event] 
 while queue:
 event = queue.pop(0) 
 for handler in HANDLERS[type(event)]: 
 handler(event, uow=uow) 
 queue.extend(uow.collect_new_events()) 
 Т еперь UoW проходит через шину сообщений всякий раз, когда за-
пускается.
 Когда мы начинаем обрабатывать первое событие, мы запускаем очередь.
