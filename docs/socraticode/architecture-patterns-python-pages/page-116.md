# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 116

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

116 Часть I. Создание архитектуры для поддержки моделирования предметной области
Новая служба для add_batch (service_layer/services.py)
def add_batch(
 ref: str, sku: str, qty: int, eta: Optional[date],
 repo: AbstractRepository, session,
):
 repo.add(model.Batch(ref, sku, qty, eta))
 session.commit()
def allocate(
 orderid: str, sku: str, qty: int, repo: AbstractRepository,
 session
) -> str:
 ...
Стоит ли добавлять новую службу только потому , что она поможет устра-
нить зависимости из тестов? Скорее всего, нет. Но в данном случае нам
почти наверняка в один прекрасный день понадобится служба add_batch.
Т еперь можно переписать все тесты сервисного слоя исключительно
с точки зрения самих служб, используя только примитивы без каких-либо
зависимостей от модели.
В тестах служб теперь используются только службы (tests/unit/test_services.py)
def test_allocate_returns_allocation():
 repo, session = FakeRepository([]), FakeSession()
 services.add_batch("batch1", "COMPLICATED-LAMP", 100, None, repo,
 session)
 result = services.allocate("o1", "COMPLICATED-LAMP", 10, repo,
 session)
 assert result == "batch1"
def test_allocate_errors_for_invalid_sku():
 repo, session = FakeRepository([]), FakeSession()
 services.add_batch("b1", "AREALSKU", 100, None, repo, session)
 with pytest.raises(services.InvalidSku, match="Недопустимый
 артикул NONEXISTENTSKU"):
 services.allocate("o1", "NONEXISTENTSKU", 10, repo,
 FakeSession())
Т еперь все действительно выглядит приятно. Т есты сервисного слоя зави-
сят только от него самого, что дает нам полную свободу для рефакторинга
модели по своему усмотрению.
