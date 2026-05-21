# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 176

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

176 Часть II. Событийно-управляемая архитектура
Подделки сервисного слоя нуждаются в настройке (tests/unit/test_services.py)
class FakeRepository(repository.AbstractRepository):
 def __init__(self, products):
 super().__init__()
 self._products = set(products)
 def _add(self, product):
 self._products.add(product)
 def _get(self, sku):
 return next((p for p in self._products if p.sku == sku), None)
...
class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
 ...
 def _commit(self):
 self.committed = True
УПРАЖНЕНИЕ ДЛЯ ЧИТАТЕЛЯ
Вы считаете, что все эти методы ._add() и ._commit() являются «сверхгрубыми»,
выражаясь словами нашего любимого научного редактора Хайнека? Они «вызыва-
ют у вас желание настучать Гарри по голове плюшевой змеей»? Но слушайте, эти
листинги нужны только для примеров, а не для идеального решения! Попробуйте
придумать что-нибудь получше.
Один из способов в стиле «композиция важнее наследования» — реализация
класса-оболочки.
Оболочка добавляет функциональность, а затем делегирует (src/adapters/repository.py)
class TrackingRepository:
 seen: Set[model.Product]
 def __init__(self, repo: AbstractRepository):
 self.seen = set() # type: Set[model.Product]
 self._repo = repo
 def add(self, product: model.Product): 
 self._repo.add(product) 
 self.seen.add(product)
 def get(self, sku) -> model.Product:
 product = self._repo.get(sku)
