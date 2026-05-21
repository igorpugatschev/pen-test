# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 197

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 9. Катимся в город на шине сообщений 197
class MessageBus(AbstractMessageBus):
 HANDLERS = {
 events.OutOfStock: [send_out_of_stock_notification],
 }
class FakeMessageBus(messagebus.AbstractMessageBus):
 def __init__(self):
 self.events_published = [] # type: List[events.Event]
 self.handlers = {
 events.OutOfStock: [lambda e: self.events_
 published.append(e)]
 }
Поэтому перейдите к коду на GitHub 1 , посмотрите, сможете ли вы получить ра-
бочую версию на основе класса, а затем напишите версию изолированного теста
test_reallocates_if_necessary_isolated() из более ранних.
Если вам нужно больше вдохновения для поиска правильного решения, гляньте
главу 13: там шина сообщений используется как класс.
Поддельная шина сообщений реализована в паттерне UoW (tests/unit/test_handlers.py)
class FakeUnitOfWorkWithFakeMessageBus(FakeUnitOfWork):
 def __init__(self):
 super().__init__()
 self.events_published = [] # тип: List[events.Event]
 def publish_events(self):
 for product in self.products.seen:
 while product.events:
 self.events_published.append(product.events.pop(0))
Т еперь, когда мы активизируем messagebus.handle(), используя FakeUnitOf-
WorkWithFakeMessageBus, он запускает только обработчик для этого события.
Таким образом, мы можем написать более изолированный юнит-тест: вместо
того чтобы проверять все побочные эффекты, мы просто убеждаемся, что
BatchQuantityChanged приводит к AllocationRequired, если размер партии
становится ниже уже размещенного суммарного числа заказанных товаров.
1 См. https://github.com/cosmicpython/code/tree/chapter_09_all_messagebus
