# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 193

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 9. Катимся в город на шине сообщений 193
 messagebus.handle(e, uow)
 [batch1, batch2] = uow.products.get(
 sku="INDIFFERENT-TABLE").batches
 assert batch1.available_quantity == 10
 assert batch2.available_quantity == 50
 messagebus.handle(events.BatchQuantityChanged("batch1", 25), uow)
 # размещение заказа order1 или order2 будет отменено, и у нас
 # будет 25 - 20
 assert batch1.available_quantity == 5 
 # и 20 будет повторно размещено в следующей партии
 assert batch2.available_quantity == 30 
 Простой случай реализуется тривиально — просто изменяем размер
партии.
 Если попытаться уменьшить размер партии, но при этом был разме-
щен более крупный заказ, то придется отменить размещение по крайней
мере одного заказа, чтобы затем повторно разместить его в новой партии
товара.
Реализация
Новый обработчик очень прост.
Обработчик делегирует обязанности в слой модели (src/allocation/service_layer/handlers.py)
def change_batch_quantity(
 event: events.BatchQuantityChanged, uow:
 unit_of_work.AbstractUnitOfWork
):
 with uow:
 product = uow.products.get_by_batchref(batchref=event.ref)
 product.change_batch_quantity(ref=event.ref, qty=event.qty)
 uow.commit()
Мы понимаем, что понадобится новый тип запроса в репозиторий.
Новый тип запроса в репозиторий (src/allocation/adapters/repository.py)
class AbstractRepository(abc.ABC):
 ...
 def get(self, sku) -> model.Product:
 ...
