# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 99

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 4. Первый вариант использования: API фреймворка Flask и сервисный слой 99
 Также нужен FakeSession, чтобы подделывать сеанс базы данных, как
показано в следующем фрагменте кода:
Поддельный сеанс базы данных (test_services.py)
class FakeSession():
 committed = False
 def commit(self):
 self.committed = True
У казанный поддельный сеанс — лишь временное решение. В главе 6 мы
от него избавимся и вскоре сделаем все еще лучше. А пока поддельный
.commit() позволяет перенести третий тест из сквозного слоя (E2E-слоя).
Второй тест в сервисном слое (test_services.py)
def test_commits():
 line = model.OrderLine('o1', 'OMINOUS-MIRROR', 10)
 batch = model.Batch('b1', 'OMINOUS-MIRROR', 100, eta=None)
 repo = FakeRepository([batch])
 session = FakeSession()
 services.allocate(line, repo, session)
 assert session.committed is True
Типичная функция службы
Напишем функцию службы, которая выглядит примерно так:
Базовая служба размещения заказов (services.py)
class InvalidSku(Exception):
 pass
def is_valid_sku(sku, batches):
 return sku in {b.sku for b in batches}
def allocate(line: OrderLine, repo: AbstractRepository, session) -> str:
 batches = repo.list() 
 if not is_valid_sku(line.sku, batches): 
 raise InvalidSku(f'Недопустимый артикул {line.sku}')
 batchref = model.allocate(line, batches) 
 session.commit() 
 return batchref
