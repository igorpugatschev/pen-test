# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 313

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Приложение Г. Паттерны «Репозиторий» и UoW с Django 313
 insert_batch('batch1', 'HIPSTER-WORKBENCH', 100, None)
 uow = unit_of_work.DjangoUnitOfWork()
 with uow:
 batch = uow.batches.get(reference='batch1')
 line = model.OrderLine('o1', 'HIPSTER-WORKBENCH', 10)
 batch.allocate(line)
 uow.commit()
 batchref = get_allocated_batch_ref('o1', 'HIPSTER-WORKBENCH')
 assert batchref == 'batch1'
@pytest.mark.django_db(transaction=True) 
def test_rolls_back_uncommitted_work_by_default():
 ...
@pytest.mark.django_db(transaction=True) 
def test_rolls_back_on_error():
 ...
 Поскольку в этих тестах было мало вспомогательных функций, их
основная часть практически такая же, как и в SQLAlchemy .
 mark.django_db(transaction=True) из pytest-django требуется для тести-
рования наших форм поведения, связанных с транзакциями и откатом.
Реализация оказалась довольно простой, хотя нам потребовалось не-
сколько попыток, чтобы выяснить, какой именно вызов Django будет
работать.
UoW после адаптации для Django (src/allocation/service_layer/unit_of_work.py)
class DjangoUnitOfWork(AbstractUnitOfWork):
 def __enter__(self):
 self.batches = repository.DjangoRepository()
 transaction.set_autocommit(False) 
 return super().__enter__()
 def __exit__(self, *args):
 super().__exit__(*args)
 transaction.set_autocommit(True)
 def commit(self):
 for batch in self.batches.seen: 
 self.batches.update(batch) 
