# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 249

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 13. Внедрение зависимостей (и начальная загрузка) 249
Неявные зависимости против явных
В этот момент вы можете слегка забеспокоиться. Давайте поговорим об
этом. Мы показали два способа управления зависимостями и их тестиро-
вания.
Для базы данных была создана хорошо продуманная структура явных за-
висимостей и простых вариантов их переопределения в тестах. Основные
функции-обработчики декларируют явную зависимость от UoW .
Обработчики явно зависят от UoW (src/allocation/service_layer/handlers.py)
def allocate(
 cmd: commands.Allocate, uow: unit_of_work.AbstractUnitOfWork
):
Что упрощает внесение поддельного UoW в тесты сервисного слоя.
Т есты сервисного слоя относительно поддельного UoW (tests/unit/test_services.py)
uow = FakeUnitOfWork()
messagebus.handle([...], uow)
UoW объявляет явную зависимость от фабрики сеансов.
UoW зависит от фабрики сеансов (src/allocation/service_layer/unit_of_work.py)
class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
 def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
 self.session_factory = session_factory
 ...
Мы пользуемся ее преимуществами в интеграционных тестах, чтобы ино-
гда использовать SQLite вместо Postgres.
Интеграционные тесты с другой БД (tests/integration/test_uow.py)
def test_rolls_back_uncommitted_work_by_default(sqlite_session_
factory):
 uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory) 
 Интеграционные тесты изымают session_factory для Postgres, под -
ставляя такую же фабрику для SQLite.
