# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 202

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

202 Часть II. Событийно-управляемая архитектура
 orderid: str
 sku: str
 qty: int
@dataclass
class CreateBatch(Command): 
 ref: str
 sku: str
 qty: int
 eta: Optional[date] = None
@dataclass
class ChangeBatchQuantity(Command): 
 ref: str
 qty: int
 commands.Allocate заменит events.AllocationRequired.
 commands.CreateBatch заменит events.BatchCreated.
 commands.ChangeBatchQuantity заменит events.BatchQuantityChanged.
Различия в обработке исключений
Замена имен и глаголов — это прекрасно, но жонглирование словами не
поменяет поведение системы. Мы хотим обращаться с событиями почти
так же, как с командами, но не одинаково. Давайте посмотрим, как изме-
няется шина сообщений.
Направляем события и команды по-разному (src/allocation/service_layer/messagebus.py)
Message = Union[commands.Command, events.Event]
def handle(message: Message, uow: unit_of_work.AbstractUnitOfWork): 
 results = []
 queue = [message]
 while queue:
 message = queue.pop(0)
 if isinstance(message, events.Event):
 handle_event(message, queue, uow) 
 elif isinstance(message, commands.Command):
 cmd_result = handle_command(message, queue, uow) 
 results.append(cmd_result)
 else:
 raise Exception(f'{message} was not an Event or Command')
 return results
