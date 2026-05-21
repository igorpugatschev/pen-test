# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 257

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 13. Внедрение зависимостей (и начальная загрузка) 257
Честно говоря, Гарри даже и не пришло в голову , что все это можно сделать проще,
но все-таки вот пример.
Ручное создание частичных встроенных функций (src/allocation/bootstrap.py)
injected_event_handlers = {
 events.Allocated: [
 lambda e: handlers.publish_allocated_event(e, publish),
 lambda e: handlers.add_allocation_to_read_model(e, uow),
 ],
 events.Deallocated: [
 lambda e: handlers.remove_allocation_from_read_model(e, uow),
 lambda e: handlers.reallocate(e, uow),
 ],
 events.OutOfStock: [
 lambda e: handlers.send_out_of_stock_notification(e, send_mail)
 ]
}
injected_command_handlers = {
 commands.Allocate: lambda c: handlers.allocate(c, uow),
 commands.CreateBatch: \
 lambda c: handlers.add_batch(c, uow),
 commands.ChangeBatchQuantity: \
 lambda c: handlers.change_batch_quantity(c, uow),
}
Гарри говорит, что даже не мог себе представить, что напишет так много строк
кода и ему придется искать столько аргументов функций вручную. Однако это
решение является вполне жизнеспособным, поскольку на каждый обработчик
добавляется примерно одна строка, так что такой код легко сопровождать, даже
если этих обработчиков у вас десятки.
Приложение структурировано таким образом, что зависимости всегда внедряются
только в одном месте — в функции-обработчике, поэтому приведенное выше «мега-
ручное» решение и решение Гарри на основе inspect() будут работать нормально.
Если вам вдруг захочется внедрить зависимости во множестве мест и в разное
время, или если когда-нибудь вы попадете в цепочки зависимостей (где ваши
зависимости имеют собственные зависимости и т. д.), то вам может пригодиться
«реальный» фреймворк внедрения зависимостей.
В компании MADE мы частично использовали Inject 1 , и это нормально, хотя
и огорчает Pylint. Вы также можете попробовать Punq 2 , написанный Бобом, или
зависимости команды разработчиков DRY-Python 3 .
1 См. https://pypi.org/project/Inject
2 См. https://pypi.org/project/punq
3 См. https://github.com/dry-python/dependencies
