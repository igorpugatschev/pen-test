# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 195

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 9. Катимся в город на шине сообщений 195
Мы добавляем запрос в репозиторий, чтобы упростить реализацию этого
варианта использования. До тех пор пока запрос возвращает один-един-
ственный агрегат, никакие правила не нарушаются. Если же вы пишете
сложные запросы к своим репозиториям, то подумайте об изменении
дизайна. Такие методы, как «получить наиболее популярный продукт»,
get_most_popular_products, или «найти продукты по идентификатору
заказа», find_products_by_order_id , помогут вам найти правильное
решение. В главе 11 и эпилоге будет несколько советов по управлению
сложными запросами.
Новый метод в модели предметной области
Мы добавляем в модель новый метод, который меняет размер партии
и размещение в одной строке кода и публикует новое событие. Изменим
и прежнюю функцию размещения с учетом публикации события.
Модель улучшается с учетом нового требования (src/allocation/domain/model.py)
class Product:
 ...
 def change_batch_quantity(self, ref: str, qty: int):
 batch = next(b for b in self.batches if b.reference == ref)
 batch._purchased_quantity = qty
 while batch.available_quantity < 0:
 line = batch.deallocate_one()
 self.events.append(
 events.AllocationRequired(line.orderid, line.sku,
 line.qty)
 )
...
class Batch:
 ...
 def deallocate_one(self) -> OrderLine:
 return self._allocations.pop()
Подключаем новый обработчик.
Шина сообщений растет (src/allocation/service_layer/messagebus.py)
HANDLERS = {
 events.BatchCreated: [handlers.add_batch],
 events.BatchQuantityChanged: [handlers.change_batch_quantity],
 events.AllocationRequired: [handlers.allocate],
 events.OutOfStock: [handlers.send_out_of_stock_notification],
} # тип: Dict[Type[events.Event], List[Callable]]
И вот новое требование теперь полностью реализовано.
