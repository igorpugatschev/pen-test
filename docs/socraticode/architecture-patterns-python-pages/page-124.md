# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 124

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

124 Часть I. Создание архитектуры для поддержки моделирования предметной области
 Паттерн UoW дает доступ к репозиторию партий товара через uow.
batches.
 Когда дело сделано, мы вызываем для него метод commit().
Для любопытных: помощники insert_batch и get_allocated_batch_ref вы-
глядят следующим образом:
Помощники для выполнения всего, что связано с SQL (tests/integration/test_uow.py)
def insert_batch(session, ref, sku, qty, eta):
 session.execute(
 'INSERT INTO batches (reference, sku, _purchased_quantity, eta)'
 ' VALUES (:ref, :sku, :qty, :eta)',
 dict(ref=ref, sku=sku, qty=qty, eta=eta)
 )
def get_allocated_batch_ref(session, orderid, sku):
 [[orderlineid]] = session.execute(
 'SELECT id FROM order_lines WHERE orderid=:orderid AND
 sku=:sku',
 dict(orderid=orderid, sku=sku)
 )
 [[batchref]] = session.execute(
 'SELECT b.reference FROM allocations JOIN batches AS b ON
 batch_id = b.id'
 ' WHERE orderline_id=:orderlineid',
 dict(orderlineid=orderlineid)
 )
 return batchref
UoW и его контекстный менеджер
В тестах мы неявно определили интерфейс для работы, которую должен
выполнять паттерн UoW . Давайте укажем это явным образом с помощью
абстрактного базового класса.
Абстрактный контекстный менеджер UoW (src/allocation/service_layer/unit_of_work.py)
class AbstractUnitOfWork(abc.ABC):
 batches: repository.AbstractRepository 
 def __exit__(self, *args): 
 self.rollback() 
