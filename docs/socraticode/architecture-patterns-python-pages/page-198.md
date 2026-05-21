# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 198

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

198 Часть II. Событийно-управляемая архитектура
Т естирование переразмещения изолированно (tests/unit/test_handlers.py)
def test_reallocates_if_necessary_isolated():
 uow = FakeUnitOfWorkWithFakeMessageBus()
 # тестовые условия, как и раньше
 event_history = [
 events.BatchCreated("batch1", "INDIFFERENT-TABLE", 50, None),
 events.BatchCreated("batch2", "INDIFFERENT-TABLE", 50,
 date.today()),
 events.AllocationRequired("order1", "INDIFFERENT-TABLE", 20),
 events.AllocationRequired("order2", "INDIFFERENT-TABLE", 20),
 ]
 for e in event_history:
 messagebus.handle(e, uow)
 [batch1, batch2] = uow.products.get(sku="INDIFFERENT-TABLE").batches
 assert batch1.available_quantity == 10
 assert batch2.available_quantity == 50
 messagebus.handle(events.BatchQuantityChanged("batch1", 25), uow)
 # подтвердить истинность на новых порожденных событиях,
 # а не на последующих побочных эффектах
 [reallocation_event] = uow.events_published
 assert isinstance(reallocation_event, events.AllocationRequired)
 assert reallocation_event.orderid in {'order1', 'order2'}
 assert reallocation_event.sku == 'INDIFFERENT-TABLE'
Необходимость прибегать к этому зависит от сложности цепочки событий.
На чните с edge-to-edge-тестирования и прибегайте к нему только в случае
необходимости.
Выводы
Подведем итоги.
Чего мы достигли
События — это простые классы данных, которые определяют структуры
для данных на входе в систему и сообщений внутри системы. Они доволь-
но мощные с точки зрения DDD, поскольку события часто очень хорошо
переводятся на деловой язык (погуглите «событийный штурм», если еще
этого не сделали).
