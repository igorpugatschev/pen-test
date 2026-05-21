# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 185

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 9. Катимся в город на шине сообщений 185
События BatchCreated и AllocationRequired (src/allocation/domain/events.py)
@dataclass
class BatchCreated(Event):
 ref: str
 sku: str
 qty: int
 eta: Optional[date] = None
...
@dataclass
class AllocationRequired(Event):
 orderid: str
 sku: str
 qty: int
Затем переименуем services.py в handlers.py, добавим прежний обработчик
сообщений для send_out_of_stock_notification и, самое главное, поменяем
все обработчики так, чтобы они имели одинаковые данные на входе, со-
бытие и UoW .
Обработчики и службы — это одно и то же (src/allocation/service_layer/handlers.py)
def add_batch(
 event: events.BatchCreated, uow: unit_of_work.AbstractUnitOfWork
):
 with uow:
 product = uow.products.get(sku=event.sku)
 ...
def allocate(
 event: events.AllocationRequired,
 uow: unit_of_work.AbstractUnitOfWork
) -> str:
 line = OrderLine(event.orderid, event.sku, event.qty)
 ...
def send_out_of_stock_notification(
 event: events.OutOfStock, uow: unit_of_work.AbstractUnitOfWork,
):
 email.send(
 'stock@made.com',
 f'Артикула {event.sku} нет в наличии',
 )
