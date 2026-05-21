# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 67

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 2. Паттерн «Репозиторий» 67
Следующий тест предусматривает извлечение партий товара и размещений,
поэтому он сложнее:
Т ест репозитория на извлечение сложного объекта (test_repository.py)
def insert_order_line(session):
 session.execute( 
 'INSERT INTO order_lines (orderid, sku, qty)'
 ' VALUES ("order1", "GENERIC-SOFA", 12)'
 )
 [[orderline_id]] = session.execute(
 'SELECT id FROM order_lines WHERE orderid=:orderid AND
 sku=:sku',
 dict(orderid="order1", sku="GENERIC-SOFA")
 )
 return orderline_id
def insert_batch(session, batch_id): 
 ...
def test_repository_can_retrieve_a_batch_with_allocations(session):
 orderline_id = insert_order_line(session)
 batch1_id = insert_batch(session, "batch1")
 insert_batch(session, "batch2")
 insert_allocation(session, orderline_id, batch1_id) 
 repo = repository.SqlAlchemyRepository(session)
 retrieved = repo.get("batch1")
 expected = model.Batch("batch1", "GENERIC-SOFA", 100, eta=None)
 assert retrieved == expected # Batch.__eq__ сравнивает только
 ссылку 
 assert retrieved.sku == expected.sku 
 assert retrieved._purchased_quantity == expected._purchased_quantity
 assert retrieved._allocations == { 
 model.OrderLine("order1", "GENERIC-SOFA", 12),
}
 Здесь тестируется сторона чтения, поэтому сырой SQL готовит данные,
которые затем будут прочитаны методом repo.get().
 Избавим вас от подробностей методов insert_batch и insert_allo cation;
их суть в том, чтобы создать несколько партий товара и для интересующей
нас партии выделить одну существующую строку заказа.
