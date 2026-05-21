# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 258

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

258 Часть II. Событийно-управляемая архитектура
Шина сообщений получает обработчики во время
выполнения
Шина сообщений больше не будет статичной; ей нужно предоставлять
уже внедренные обработчики. Поэтому мы преобразовываем ее из модуля
в конфигурируемый класс.
Шина сообщений как класс (src/allocation/service_layer/messagebus.py)
class MessageBus: 
 def __init__(
 self,
 uow: unit_of_work.AbstractUnitOfWork,
 event_handlers: Dict[Type[events.Event], List[Callable]], 
 command_handlers: Dict[Type[commands.Command], Callable], 
 ):
 self.uow = uow
 self.event_handlers = event_handlers
 self.command_handlers = command_handlers
 def handle(self, message: Message): 
 self.queue = [message] 
 while self.queue:
 message = self.queue.pop(0)
 if isinstance(message, events.Event):
 self.handle_event(message)
 elif isinstance(message, commands.Command):
 self.handle_command(message)
 else:
 raise Exception(f'Сообщение {message} не было
 Событием или Командой')
 Шина сообщений становится классом…
 ...который получает свои уже внедренные обработчики зависимостей.
 Основная функция handle(), по существу , та же самая, только теперь
несколько атрибутов и методов в ней перемещены в self.
 Такое использование self.queue не безопасно в плане потоков и может
привести к проблемам, если используются потоки исполнения, потому
что экземпляр шины является глобальным в контексте приложения
