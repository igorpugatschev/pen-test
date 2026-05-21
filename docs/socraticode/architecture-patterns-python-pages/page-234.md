# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 234

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

234 Часть II. Событийно-управляемая архитектура
 messagebus.handle(commands.CreateBatch('sku2batch', 'sku2', 50,
 today), uow)
 messagebus.handle(commands.Allocate('order1', 'sku1', 20), uow)
 messagebus.handle(commands.Allocate('order1', 'sku2', 20), uow)
 # добавим фальшивую партию и заказ,
 # чтобы убедиться, что мы получаем правильные значения
 messagebus.handle(commands.CreateBatch('sku1batch-later', 'sku1',
 50, today), uow)
 messagebus.handle(commands.Allocate('otherorder', 'sku1', 30), uow)
 messagebus.handle(commands.Allocate('otherorder', 'sku2', 10), uow)
 assert views.allocations('order1', uow) == [
 {'sku': 'sku1', 'batchref': 'sku1batch'},
 {'sku': 'sku2', 'batchref': 'sku2batch'},
 ]
 Мы выполняем настройку интеграционного теста с помощью публич-
ной точки входа в наше приложение — шины сообщений. Благодаря этому
тесты теряют связанность с какими-либо деталями реализации/инфра-
структуры хранения.
«Очевидная» альтернатива 1: использование
существующего репозитория
Как насчет добавления вспомогательного метода в репозиторий products?
Простое представление, в котором используется репозиторий (src/allocation/views.py)
from allocation import unit_of_work
def allocations(orderid: str, uow: unit_of_work.AbstractUnitOfWork):
 with uow:
 products = uow.products.for_order(orderid=orderid) 
 batches = [b for p in products for b in p.batches] 
 return [
 {'sku': b.sku, 'batchref': b.reference}
 for b in batches
 if orderid in b.orderids 
 ]
 Репозиторий возвращает объекты Product, и нужно найти все продукты
для артикулов в заданном порядке, поэтому в репозитории создается новый
вспомогательный метод с именем .for_order().
