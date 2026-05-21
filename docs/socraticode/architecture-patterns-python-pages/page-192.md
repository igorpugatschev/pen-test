# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 192

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

192 Часть II. Событийно-управляемая архитектура
Новое событие
Событие, которое сообщает нам о том, что размер партии товара изменил-
ся, очень простое; ему нужна только ссылка на партию и ее новый размер.
Новое событие (src/allocation/domain/events.py)
@dataclass
class BatchQuantityChanged(Event):
 ref: str
 qty: int
Т ест-драйв нового обработчика
Вспоминая урок из главы 4, мы можем «ехать на повышенной передаче»
и писать юнит-тесты на максимально возможном уровне абстракции с по-
мощью событий. Вот как они могут выглядеть:
Т есты обработчика для change_batch_quantity (tests/unit/test_handlers.py)
class TestChangeBatchQuantity:
 def test_changes_available_quantity(self):
 uow = FakeUnitOfWork()
 messagebus.handle(
 events.BatchCreated("batch1", "ADORABLE-SETTEE", 100,
 None), uow
 )
 [batch] = uow.products.get(sku="ADORABLE-SETTEE").batches
 assert batch.available_quantity == 100 
 messagebus.handle(events.BatchQuantityChanged("batch1", 50), uow)
 assert batch.available_quantity == 50 
 def test_reallocates_if_necessary(self):
 uow = FakeUnitOfWork()
 event_history = [
 events.BatchCreated("batch1", "INDIFFERENT-TABLE", 50, None),
 events.BatchCreated("batch2", "INDIFFERENT-TABLE", 50,
 date.today()),
 events.AllocationRequired("order1", "INDIFFERENT-TABLE", 20),
 events.AllocationRequired("order2", "INDIFFERENT-TABLE", 20),
 ]
 for e in event_history:
