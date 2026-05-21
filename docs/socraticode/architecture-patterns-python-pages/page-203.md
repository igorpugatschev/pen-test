# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 203

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 10. Команды и обработчик команд 203
 У нее все еще есть основная точка входа handle() , принимающая
message — команду либо событие.
 Мы отправляем события и команды двум разным вспомогательным
функциям, которые показаны ниже.
Вот как происходит работа с событиями:
События не могут прервать поток (src/allocation/service_layer/messagebus.py)
def handle_event(
 event: events.Event,
 queue: List[Message],
 uow: unit_of_work.AbstractUnitOfWork
):
 for handler in EVENT_HANDLERS[type(event)]: 
 try:
 logger.debug('handling event %s with handler %s', event,
 handler)
 handler(event, uow=uow)
 queue.extend(uow.collect_new_events())
 except Exception:
 logger.exception('Exception handling event %s', event)
 continue 
 События передаются диспетчеру , который может делегировать их
многочисленным обработчикам для каждого события.
 Он отлавливает и логирует ошибки, но не позволяет им прерывать об-
работку сообщений.
И вот как выполняются команды:
Команды заново инициируют исключения (src/allocation/service_layer/messagebus.py)
def handle_command(
 command: commands.Command,
 queue: List[Message],
 uow: unit_of_work.AbstractUnitOfWork
):
 logger.debug('handling command %s', command)
 try:
 handler = COMMAND_HANDLERS[type(command)] 
 result = handler(command, uow=uow)
 queue.extend(uow.collect_new_events())
 return result 
 except Exception:
 logger.exception('Exception handling command %s', command)
 raise 
