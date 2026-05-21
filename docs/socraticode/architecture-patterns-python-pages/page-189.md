# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 189

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 9. Катимся в город на шине сообщений 189
В тестах обработчиков используются события (tests/unit/test_handlers.py)
class TestAddBatch:
 def test_for_new_product(self):
 uow = FakeUnitOfWork()
- services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, uow)
+ messagebus.handle(
+ events.BatchCreated("b1", "CRUNCHY-ARMCHAIR", 100, None), uow
+ )
 assert uow.products.get("CRUNCHY-ARMCHAIR") is not None
 assert uow.committed
...
class TestAllocate:
 def test_returns_allocation(self):
 uow = FakeUnitOfWork()
- services.add_batch("batch1", "COMPLICATED-LAMP", 100, None, uow)
- result = services.allocate("o1", "COMPLICATED-LAMP", 10, uow)
+ messagebus.handle(
+ events.BatchCreated("batch1", "COMPLICATED-LAMP", 100,
 None), uow
+ )
+ result = messagebus.handle(
+ events.AllocationRequired("o1", "COMPLICATED-LAMP", 10), uow
+ )
 assert result == "batch1"
Уродливый костыль: шине сообщений приходится возвращать результаты
API и сервисный слой теперь хотят знать ссылку на размещенную партию
товара, когда вызывают обработчик allocate(). Это означает, что нужно
вставить костыль в шину сообщений, чтобы она смогла возвращать события.
Шина сообщений возвращает результаты (src/allocation/service_layer/messagebus.py)
def handle(event: events.Event, uow: unit_of_work.AbstractUnitOfWork):
+ results = []
 queue = [event]
 while queue:
 event = queue.pop(0)
 for handler in HANDLERS[type(event)]:
- handler(event, uow=uow)
+ results.append(handler(event, uow=uow))
 queue.extend(uow.collect_new_events())
+ return results
