# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 311

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Приложение Г. Паттерны «Репозиторий» и UoW с Django 311
Как видите, реализация основана на моделях Django, имеющих некоторые
настраиваемые методы для трансляции в модель предметной области и из
нее1 .
Специализированные методы в классах ORM Django
для трансляции в модель предметной области и из нее
Эти специализированные методы выглядят примерно так:
ORM Django со специализированными методами конверсии модели предметной области (src/
djangoproject/alloc/models.py)
from django.db import models
from allocation.domain import model as domain_model
class Batch(models.Model):
 reference = models.CharField(max_length=255)
 sku = models.CharField(max_length=255)
 qty = models.IntegerField()
 eta = models.DateField(blank=True, null=True)
 @staticmethod
 def update_from_domain(batch: domain_model.Batch):
 try:
 b = Batch.objects.get(reference=batch.reference) 
 except Batch.DoesNotExist:
 b = Batch(reference=batch.reference) 
 b.sku = batch.sku
 b.qty = batch._purchased_quantity
 b.eta = batch.eta 
 b.save()
 b.allocation_set.set(
 Allocation.from_domain(l, b) 
 for l in batch._allocations
 )
 def to_domain(self) -> domain_model.Batch:
 b = domain_model.Batch(
 ref=self.reference, sku=self.sku, qty=self.qty, eta=self.eta
1 Разработчики из проекта DRY-Python создали инструмент mappers, который, как
нам кажется, способен минимизировать стереотипный код для подобных решений.
См. https://mappers.readthedocs.io/en/latest
