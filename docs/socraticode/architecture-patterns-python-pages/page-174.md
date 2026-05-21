# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 174

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

174 Часть II. Событийно-управляемая архитектура
 После фиксации мы перебираем все объекты, которые репозиторий
видел, и передаем их события в шину сообщений.
 Этот фрагмент опирается на репозиторий, который отслеживает агре-
гаты, загруженные с использованием нового атрибута .seen, как показано
в следующем листинге.
А что произойдет, если один из обработчиков откажет? Обработку оши-
бок подробно обсудим в главе 10.
Репозиторий отслеживает проходящие через него агрегаты (src/allocation/adapters/repository.py)
class AbstractRepository(abc.ABC):
 def __init__(self):
 self.seen = set() # type: Set[model.Product] 
 def add(self, product: model.Product): 
 self._add(product)
 self.seen.add(product)
 def get(self, sku) -> model.Product: 
 product = self._get(sku)
 if product:
 self.seen.add(product)
 return product
 @abc.abstractmethod
 def _add(self, product: model.Product): 
 raise NotImplementedError
 @abc.abstractmethod 
 def _get(self, sku) -> model.Product:
 raise NotImplementedError
class SqlAlchemyRepository(AbstractRepository):
 def __init__(self, session):
 super().__init__()
 self.session = session
 def _add(self, product): 
 self.session.add(product)
