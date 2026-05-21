# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 194

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

194 Часть II. Событийно-управляемая архитектура
 def get_by_batchref(self, batchref) -> model.Product:
 product = self._get_by_batchref(batchref)
 if product:
 self.seen.add(product)
 return product
 @abc.abstractmethod
 def _add(self, product: model.Product):
 raise NotImplementedError
 @abc.abstractmethod
 def _get(self, sku) -> model.Product:
 raise NotImplementedError
 @abc.abstractmethod
 def _get_by_batchref(self, batchref) -> model.Product:
 raise NotImplementedError
 ...
class SqlAlchemyRepository(AbstractRepository):
 ...
 def _get(self, sku):
 return self.session.query(model.Product).filter_
 by(sku=sku).first()
 def _get_by_batchref(self, batchref):
 return self.session.query(model.Product).join
 (model.Batch).filter(
 orm.batches.c.reference == batchref,
 ).first()
И в поддельный репозиторий, FakeRepository, тоже.
Обновляем поддельный репозиторий (tests/unit/test_handlers.py)
class FakeRepository(repository.AbstractRepository):
 ...
 def _get(self, sku):
 return next((p for p in self._products if p.sku == sku), None)
 def _get_by_batchref(self, batchref):
 return next((
 p for p in self._products for b in p.batches
 if b.reference == batchref
 ), None)
