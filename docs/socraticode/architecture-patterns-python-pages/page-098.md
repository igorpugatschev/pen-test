# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 98

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

98 Часть I. Создание архитектуры для поддержки моделирования предметной области
Поддельный репозиторий, коллекция партий товара в памяти (test_services.py)
class FakeRepository(repository.AbstractRepository):
 def __init__(self, batches):
 self._batches = set(batches)
 def add(self, batch):
 self._batches.add(batch)
 def get(self, reference):
 return next(b for b in self._batches if b.reference == reference)
 def list(self):
 return list(self._batches)
Вот где он будет полезен — он позволяет тестировать слой служб с помо-
щью хороших, быстрых юнит-тестов.
Юнит-тестирование с подделками в слое служб (test_services.py)
def test_returns_allocation():
 line = model.OrderLine("o1", "COMPLICATED-LAMP", 10)
 batch = model.Batch("b1", "COMPLICATED-LAMP", 100, eta=None)
 repo = FakeRepository([batch]) 
 result = services.allocate(line, repo, FakeSession())  
 assert result == "b1"
def test_error_for_invalid_sku():
 line = model.OrderLine("o1", "NONEXISTENTSKU", 10)
 batch = model.Batch("b1", "AREALSKU", 100, eta=None)
 repo = FakeRepository([batch]) 
 with pytest.raises(services.InvalidSku, match="Недопустимый
 артикул NONEXISTENTSKU"):
 services.allocate(line, repo, FakeSession())  
 Поддельный репозиторий FakeRepository содержит объекты Batch, ко-
торые будут использоваться в тесте.
 Модуль служб ( services.py) определит функцию allocate() сервисного
слоя. Он будет находиться между функцией allocate_endpoint() в слое API
и функцией allocate() службы предметной области из модели1 .
1 Т ермины «службы сервисного слоя» и «службы предметной области» и вправду
имеют обескураживающе схожие названия. Мы рассмотрим эту тему позже в разделе
«Почему все называется службой?» на с. 102.
