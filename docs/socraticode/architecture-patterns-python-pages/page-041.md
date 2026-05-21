# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 41

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 1. Моделирование предметной области 41
Для этого теста нужна более умная модель (test_batches.py)
def test_can_only_deallocate_allocated_lines():
 batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET",
 20, 2)
 batch.deallocate(unallocated_line)
 assert batch.available_quantity == 20
В этом тесте мы убеждаемся, что отмена размещения товарной позиции
заказа в партии не имеет никакого эффекта в случае, если эта позиция не
была ранее размещена в этой партии. Для этого класс Batch должен по-
нимать, какие товарные позиции заказа были размещены, а какие — нет.
Давайте посмотрим на реализацию.
Модель предметной области теперь отслеживает размещения (model.py)
class Batch:
 def __init__(
 self, ref: str, sku: str, qty: int, eta: Optional[date]
 ):
 self.reference = ref
 self.sku = sku
 self.eta = eta
 self._purchased_quantity = qty
 self._allocations = set() # тип 'множество': Set[OrderLine]
 def allocate(self, line: OrderLine):
 if self.can_allocate(line):
 self._allocations.add(line)
 def deallocate(self, line: OrderLine):
 if line in self._allocations:
 self._allocations.remove(line)
 @property
 def allocated_quantity(self) -> int:
 return sum(line.qty for line in self._allocations)
 @property
 def available_quantity(self) -> int:
 return self._purchased_quantity - self.allocated_quantity
 def can_allocate(self, line: OrderLine) -> bool:
 return self.sku == line.sku and self.available_quantity >=
 line.qty
