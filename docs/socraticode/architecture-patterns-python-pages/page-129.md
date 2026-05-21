# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 129

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 6. Паттерн UoW 129
Интеграционные тесты для поведения по откату (tests/integration/test_uow.py)
def test_rolls_back_uncommitted_work_by_default(session_factory):
 uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
 with uow:
 insert_batch(uow.session, 'batch1', 'MEDIUM-PLINTH', 100, None)
 new_session = session_factory()
 rows = list(new_session.execute('SELECT * FROM "batches"'))
 assert rows == []
def test_rolls_back_on_error(session_factory):
 class MyException(Exception):
 pass
 uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
 with pytest.raises(MyException):
 with uow:
 insert_batch(uow.session, 'batch1', 'LARGE-FORK', 100, None)
 raise MyException()
 new_session = session_factory()
 rows = list(new_session.execute('SELECT * FROM "batches"'))
 assert rows == []
В нашем примере этого нет, но возможно, стоит протестировать пару-
тройку не столь понятных действий базы данных, таких как транзакции,
относительно «реальной» базы данных, то есть того же самого движка.
Пока что нам хватает SQLite, но в главе 7 мы переключим некоторые
тесты на использование реальной базы данных. Здорово, что класс UoW
позволяет нам с легкостью сделать это!
Явные и неявные фиксации
Кратко остановимся на разных способах реализации паттерна UoW .
Можно представить себе немного другую версию UoW , которая по умол-
чанию выполняет фиксацию и откатывает только в том случае, если об-
наруживает исключение.
