# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 240

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

240 Часть II. Событийно-управляемая архитектура
Вот как выглядит код обновления модели представления:
Обновление при размещении (src/allocation/service_layer/handlers.py)
def add_allocation_to_read_model(
 event: events.Allocated, uow:
 unit_of_work.SqlAlchemyUnitOfWork,
):
 with uow:
 uow.session.execute(
 'INSERT INTO allocations_view (orderid, sku, batchref)'
 ' VALUES (:orderid, :sku, :batchref)',
 dict(orderid=event.orderid, sku=event.sku,
 batchref=event.batchref)
 )
 uow.commit()
Хотите верьте, хотите нет, но этот код в целом рабочий! И он будет рабо-
тать с теми же интеграционными тестами, что и остальные варианты.
О'кей, теперь обработаем отмену размещения, Deallocated.
Второй слушатель для обновлений модели чтения
events.Deallocated: [
 handlers.remove_allocation_from_read_model,
 handlers.reallocate
],
...
def remove_allocation_from_read_model(
 event: events.Deallocated, uow:
 unit_of_work.SqlAlchemyUnitOfWork,
):
 with uow:
 uow.session.execute(
 'DELETE FROM allocations_view '
 ' WHERE orderid = :orderid AND sku = :sku',
На рис. 12.2 показан процесс между двумя запросами.
На рисунке можно увидеть две транзакции в операции POST/запись: одну
для обновления модели записи и другую для обновления модели чтения,
которая может использоваться операцией GET/чтение.
