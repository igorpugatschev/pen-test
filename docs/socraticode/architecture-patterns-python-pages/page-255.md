# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 255

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 13. Внедрение зависимостей (и начальная загрузка) 255
классов дескрипторы либо контекстный менеджер, который принимает
аргументы.
Используйте то, что удобнее вам и вашей команде.
Сценарий начальной загрузки
Нам нужно, чтобы сценарий начальной загрузки выполнял следующие
действия:
 y объявлял зависимости по умолчанию, но позволял их переопределять;
 y делал все, что касается «инициализации», нужной для запуска при-
ложения;
 y внедрял все зависимости в обработчики;
 y возвращал основной для приложения объект — шину сообщений.
Вот первая попытка:
Функция начальной загрузки (src/allocation/bootstrap.py)
def bootstrap(
 start_orm: bool = True, 
 uow: unit_of_work.AbstractUnitOfWork =
 unit_of_work.SqlAlchemyUnitOfWork(), 
 send_mail: Callable = email.send,
 publish: Callable = redis_eventpublisher.publish,
) -> messagebus.MessageBus:
 if start_orm:
 orm.start_mappers() 
 dependencies = {'uow': uow, 'send_mail': send_mail, 'publish':
 publish}
 injected_event_handlers = { 
 event_type: [
 inject_dependencies(handler, dependencies)
 for handler in event_handlers
 ]
 for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
 }
 injected_command_handlers = { 
 command_type: inject_dependencies(handler, dependencies)
 for command_type, handler in handlers.COMMAND_HANDLERS.items()
 }
