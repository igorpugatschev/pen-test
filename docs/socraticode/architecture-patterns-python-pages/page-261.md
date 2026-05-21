# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 261

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 13. Внедрение зависимостей (и начальная загрузка) 261
 bus = bootstrap.bootstrap(
 start_orm=True, 
 uow=unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory), 
 send_mail=lambda *args: None, 
 publish=lambda *args: None, 
 )
 yield bus
 clear_mappers()
def test_allocations_view(sqlite_bus):
 sqlite_bus.handle(commands.CreateBatch('sku1batch', 'sku1', 50,
 None))
 sqlite_bus.handle(commands.CreateBatch('sku2batch', 'sku2', 50,
 date.today()))
 ...
 assert views.allocations('order1', sqlite_bus.uow) == [
 {'sku': 'sku1', 'batchref': 'sku1batch'},
 {'sku': 'sku2', 'batchref': 'sku2batch'},
 ]
 Мы по-прежнему хотим запускать ORM…
 ...потому что собираемся использовать реальный UoW , пусть и с базой
данных прямо в памяти.
 Но отправлять имейлы или публиковать что-либо не нужно, поэтому
мы вставляем эти пустые команды.
В юнит-тестах, напротив, можно вторично использовать поддельный UoW ,
FakeUnitOfWork.
Начальная загрузка в юнит-тесте (tests/unit/test_handlers.py)
def bootstrap_test_app():
 return bootstrap.bootstrap(
 start_orm=False, 
 uow=FakeUnitOfWork(), 
 send_mail=lambda *args: None, 
 publish=lambda *args: None, 
 )
 Запускать ORM не нужно…
 ...потому что поддельный UoW его не использует.
 Нужно также подделать имейлы и адаптеры Redis.
