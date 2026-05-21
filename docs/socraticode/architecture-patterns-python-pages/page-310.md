# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 310

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

310 Приложение Г. Паттерны «Репозиторий» и UoW с Django
 d_line = django_models.OrderLine.objects.create(orderid="order1",
 sku=sku, qty=12)
 d_b1 = django_models.Batch.objects.create(
 reference="batch1", sku=sku, qty=100, eta=None
 )
 d_b2 = django_models.Batch.objects.create(
 reference="batch2", sku=sku, qty=100, eta=None
 )
 django_models.Allocation.objects.create(line=d_line, batch=d_batch1)
 repo = repository.DjangoRepository()
 retrieved = repo.get("batch1")
 expected = model.Batch("batch1", sku, 100, eta=None)
 assert retrieved == expected # Batch.__eq__ only compares
 reference
 assert retrieved.sku == expected.sku
 assert retrieved._purchased_quantity == expected._purchased_
 quantity
 assert retrieved._allocations == {
 model.OrderLine("order1", sku, 12),
 }
Вот как в итоге выглядит фактический репозиторий:
Репозиторий Django (src/allocation/adapters/repository.py)
class DjangoRepository(AbstractRepository):
 def add(self, batch):
 super().add(batch)
 self.update(batch)
 def update(self, batch):
 django_models.Batch.update_from_domain(batch)
 def _get(self, reference):
 return django_models.Batch.objects.filter(
 reference=reference
 ).first().to_domain()
 def list(self):
 return [b.to_domain() for b in django_models.Batch.objects.all()]
