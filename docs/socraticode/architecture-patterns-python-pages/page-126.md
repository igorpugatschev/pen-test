# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 126

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

126 Часть I. Создание архитектуры для поддержки моделирования предметной области
 def commit(self): 
 self.session.commit()
 def rollback(self): 
 self.session.rollback()
 В указанном модуле определяется фабрика сеансов по умолчанию,
которая будет подключаться к базе данных Postgres, но мы позволяем их
переопределять в интеграционных тестах, чтобы вместо нее можно было
использовать SQLite.
 Метод __enter__ отвечает за запуск сеанса базы данных и создание
экземпляра реального репозитория, который может пользоваться этим
сеансом.
 Закрываем сеанс на выходе.
 Наконец, мы добавляем конкретные методы commit() и rollback() ,
в которых используется сеанс базы данных.
Поддельный UoW для тестирования
Вот как мы используем поддельный UoW в тестах сервисного слоя:
Поддельный UoW (tests/unit/test_services.py)
class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
 def __init__(self):
 self.batches = FakeRepository([]) 
 self.committed = False 
 def commit(self):
 self.committed = True 
 def rollback(self):
 pass
 def test_add_batch():
 uow = FakeUnitOfWork() 
 services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, uow) 
 assert uow.batches.get("b1") is not None
 assert uow.committed
