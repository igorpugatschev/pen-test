# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 115

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 5. TDD на повышенной и пониженной передачах 115
Фабричные функции для фикстур — это один из способов (tests/unit/test_services.py)
class FakeRepository(set):
 @staticmethod
 def for_batch(ref, sku, qty, eta=None):
 return FakeRepository([
 model.Batch(ref, sku, qty, eta),
 ])
 ...
def test_returns_allocation():
 repo = FakeRepository.for_batch("batch1", "COMPLICATED-LAMP",
 100, eta=None)
 result = services.allocate("o1", "COMPLICATED-LAMP", 10, repo,
 FakeSession())
 assert result == "batch1"
По меньшей мере это переместило бы все зависимости тестов от предметной
области в одно конкретное место.
Добавление отсутствующей службы
Но можно пойти еще дальше. Если бы у нас была служба для добавления
товарных запасов, то мы могли бы использовать ее и выразить тесты сер-
висного слоя с помощью общепринятых вариантов использования, убрав
все зависимости от предметной области.
Т ест для новой службы add_batch (tests/unit/test_services.py)
def test_add_batch():
 repo, session = FakeRepository([]), FakeSession()
 services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, repo, session)
 assert repo.get("”b1") is not None
 assert session.committed
Если вы обнаружите, что вам приходится делать что-то связанное со
слоем предметной области непосредственно в тестах сервисного слоя,
возможно, ваш сервисный слой недоработан.
И реализация занимает всего пару строк кода.
