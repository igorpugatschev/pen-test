# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 127

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 6. Паттерн UoW 127
 def test_allocate_returns_allocation():
 uow = FakeUnitOfWork() 
 services.add_batch("batch1", "COMPLICATED-LAMP", 100, None, uow) 
 result = services.allocate("o1", "COMPLICATED-LAMP", 10, uow) 
 assert result == "batch1"
 ...
 FakeUnitOfWork и FakeRepository тесно связаны, как и настоящие классы
UnitOfWork и Repository. Это прекрасно, потому что мы признаем, что объ-
екты являются коллабораторами.
 Обратите внимание на сходство с поддельной функцией commit() из
FakeSession (от которой мы теперь можем избавиться). Но это существенное
улучшение, потому что теперь вместо стороннего кода мы подделываем
собственный. Некоторые говорят: «Не владеешь — не имитируй»1 .
 В тестах можно создать экземпляр паттерна UoW и передавать его
в сервисный слой, вместо того чтобы передавать репозиторий и сеанс.
Такой способ гораздо легче.
Использование паттерна UoW в сервисном слое
Вот как выглядит новый сервисный слой:
Сервисный слой c паттерном UoW (src/allocation/service_layer/services.py)
def add_batch(
 ref: str, sku: str, qty: int, eta: Optional[date],
 uow: unit_of_work.AbstractUnitOfWork 
):
 with uow:
 uow.batches.add(model.Batch(ref, sku, qty, eta))
 uow.commit()
def allocate(
 orderid: str, sku: str, qty: int,
 uow: unit_of_work.AbstractUnitOfWork 
) -> str:
 line = OrderLine(orderid, sku, qty)
 with uow:
 batches = uow.batches.list()
1 Don’t mock what you don’t own. См. https://oreil.ly/0LVj3
