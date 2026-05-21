# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 253

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 13. Внедрение зависимостей (и начальная загрузка) 253
 cmd: commands.Allocate, uow: unit_of_work.AbstractUnitOfWork
):
 line = OrderLine(cmd.orderid, cmd.sku, cmd.qty)
 with uow:
 ...
# сценарий начальной загрузки подготавливает фактический UoW
def bootstrap(..):
 uow = unit_of_work.SqlAlchemyUnitOfWork()
 # подготовить версию функции allocate с зависимостью от UoW,
 # захваченного в замыкании
 allocate_composed = lambda cmd: allocate(cmd, uow)
 # либо эквивалентным образом (это обеспечивает более приятную
 # трассировку стека)
 def allocate_composed(cmd):
 return allocate(cmd, uow)
 # альтернатива с частичным применением функции
 import functools
 allocate_composed = functools.partial(allocate, uow=uow) 
# позже, во время выполнения, мы можем вызвать частично примененную
# функцию, и в ней уже будет привязанный UoW
allocate_composed(cmd)
 Разница между замыканиями (лямбда-выражениями или именованными
функциями) и частичными применениями functools.partial состоит в том,
что в первых используется поздняя привязка переменных1 . Это может вы-
звать путаницу , если какая-либо из зависимостей является мутируемой.
Вот тот же самый паттерн для обработчика уведомления об отсутствии
товара в наличии, send_out_of_stock_notification(), который имеет другие
зависимости.
Еще один пример замыкания и частично примененной функции
def send_out_of_stock_notification(
 event: events.OutOfStock, send_mail: Callable,
):
 send_mail(
 'stock@made.com',
 ...
# подготовить версию обработчика send_out_of_stock_notification
# с зависимостями
1 См. https://docs.python-guide.org/writing/gotchas/#late-binding-closures
