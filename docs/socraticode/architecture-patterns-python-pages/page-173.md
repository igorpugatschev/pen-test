# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 173

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 8. События и шина сообщений 173
Опять же в случае с нашими приложениями этот паттерн реализован
именно так. То, что подойдет для вас, будет зависеть от конкретных ком-
промиссов, с которыми вы столкнетесь. Мы же просто хотим показать вам
то, что считаем наиболее элегантным решением, в котором паттерн UoW
отвечает за сбор и инициирование событий.
Вариант 3: UoW публикует события в шине
сообщений
Паттерн UoW уже включает блок try/finally и знает обо всех задейство-
ванных агрегатах, так как предоставляет доступ к репозиторию. Вполне
подходящее место для обнаружения событий и передачи их в шину со-
общений.
UoW вместе с шиной сообщений (src/allocation/service_layer/unit_of_work.py)
class AbstractUnitOfWork(abc.ABC):
 ...
 def commit(self):
 self._commit() 
 self.publish_events() 
 def publish_events(self): 
 for product in self.products.seen: 
 while product.events:
 event = product.events.pop(0)
 messagebus.handle(event)
 @abc.abstractmethod
 def _commit(self):
 raise NotImplementedError
...
class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
 ...
 def _commit(self): 
 self.session.commit()
 Изменяем метод фиксации: будем требовать приватный метод ._com-
mit() из подклассов.
