# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 223

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 11. Событийно-управляемая архитектура: использование событий для интеграции микросервисов 223
каналом, позволяя одному или нескольким типам сообщений переходить
в разные каналы.
Новое исходящее событие
Вот как будет выглядеть событие Allocated:
Новое событие (src/allocation/domain/events.py)
@dataclass
class Allocated(Event):
 orderid: str
 sku: str
 qty: int
 batchref: str.
Оно улавливает все, что нужно знать о размещении: сведения о товарной
позиции заказа и о том, в какой партии товара она была размещена.
Добавляем его в модельный метод allocate() (естественно, предварительно
добавив тест).
Product.allocate() выдает новое событие для регистрации того, что произошло (src/allocation/
domain/model.py).
class Product:
 ...
 def allocate(self, line: OrderLine) -> str:
 ...
 batch.allocate(line)
 self.version_number += 1
 self.events.append(events.Allocated(
 orderid=line.orderid, sku=line.sku, qty=line.qty,
 batchref=batch.reference,
 ))
 return batch.reference
Обработчик ChangeBatchQuantity у нас уже есть, поэтому нужно добавить
лишь обработчик, который публикует исходящее событие.
Шина сообщений растет (src/allocation/service_layer/messagebus.py)
HANDLERS = {
 events.Allocated: [handlers.publish_allocated_event],
 events.OutOfStock: [handlers.send_out_of_stock_notification],
} # тип: Dict[Type[events.Event], List[Callable]]
