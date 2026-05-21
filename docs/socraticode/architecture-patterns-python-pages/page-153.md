# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 153

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 7. Агрегаты и границы согласованности 153
Интеграционный тест на параллельное поведение (tests/integration/test_uow.py)
def test_concurrent_updates_to_version_are_not_allowed(postgres_
 session_factory):
 sku, batch = random_sku(), random_batchref()
 session = postgres_session_factory()
 insert_batch(session, batch, sku, 100, eta=None, product_version=1)
 session.commit()
 order1, order2 = random_orderid(1), random_orderid(2)
 exceptions = [] # тип: List[Exception]
 try_to_allocate_order1 = lambda: try_to_allocate(order1, sku,
 exceptions)
 try_to_allocate_order2 = lambda: try_to_allocate(order2, sku,
 exceptions)
 thread1 = threading.Thread(target=try_to_allocate_order1) 
 thread2 = threading.Thread(target=try_to_allocate_order2) 
 thread1.start()
 thread2.start()
 thread1.join()
 thread2.join()
 [[version]] = session.execute(
 "SELECT version_number FROM products WHERE sku=:sku",
 dict(sku=sku),
 )
 assert version == 2 
 [exception] = exceptions
 assert 'не получилось сериализовать доступ из-за параллельного
 обновления' in str(exception) 
 orders = list(session.execute(
 "SELECT orderid FROM allocations"
 " JOIN batches ON allocations.batch_id = batches.id"
 " JOIN order_lines ON allocations.orderline_id = order_lines.id"
 " WHERE order_lines.sku=:sku",
 dict(sku=sku),
 ))
 assert len(orders) == 1 
 with unit_of_work.SqlAlchemyUnitOfWork() as uow:
 uow.session.execute('select 1')
 Мы запускаем два потока выполнения, у которых точно будет нужное
параллельное поведение: read1, read2, write1, write2.
 Мы убеждаемся, что номер версии был увеличен только один раз.
