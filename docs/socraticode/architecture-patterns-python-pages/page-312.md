# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 312

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

312 Приложение Г. Паттерны «Репозиторий» и UoW с Django
 )
 b._allocations = set(
 a.line.to_domain()
 for a in self.allocation_set.all()
 )
 return b
class OrderLine(models.Model):
 #...
 Для объектов-значений objects.get_or_create может работать, но для
сущностей понадобится явный блок try-get/except для обработки вставок
новых строк в данные или их обновление, если они существуют (upsert) 1 .
 Мы показали здесь самый сложный пример. Если вы все же решите его
повторить, то имейте в виду , что будет много стереотипного кода! К сча-
стью, он несложный.
 Отношения также нуждаются в осторожном индивидуальном подходе.
Как и в главе 2, мы используем инверсию зависимостей. Объектно-
реляционное отображение (Django) зависит от модели, а не наоборот.
Паттерн UoW с Django
Т есты не слишком меняются.
Адаптированные тесты UoW (tests/integration/test_uow.py)
def insert_batch(ref, sku, qty, eta): 
 django_models.Batch.objects.create(reference=ref, sku=sku,
 qty=qty, eta=eta)
def get_allocated_batch_ref(orderid, sku): 
 return django_models.Allocation.objects.get(
 line__orderid=orderid, line__sku=sku
 ).batch.reference
@pytest.mark.django_db(transaction=True)
def test_uow_can_retrieve_a_batch_and_allocate_to_it():
1 @mr-bo-jangles предположил, что вы можете использовать update_or_create ( https://
oreil.ly/HTq1r), но это выходит за рамки нашего кунг-фу Django.
