# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 125

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 6. Паттерн UoW 125
 @abc.abstractmethod
 def commit(self): 
 raise NotImplementedError
 @abc.abstractmethod
 def rollback(self): 
 raise NotImplementedError
 UoW предоставляет атрибут .batches, который обеспечит доступ к ре-
позиторию партий товара.
 Если вы никогда не видели контекстный менеджер, то вот два волшебных
метода — __enter__ и __exit__, которые выполняются соответственно при
входе в блок with и при выходе из него. Это фазы наладки и демонтажа.
 Вызовем этот метод, чтобы явно зафиксировать работу , когда мы будем
готовы.
 Если мы не выполняем фиксацию или выходим из контекстного мене-
джера, инициировав ошибку , то выполняем откат. (Откат ни к чему не
приводит, если была вызвана фиксация commit(). Далее в книге этот вопрос
обсуждается подробнее.)
Настоящий UoW использует сеансы SQLAlchemy
В конкретной реализации добавлено главное, и это сеанс работы с базой
данных.
Настоящий UoW с SQLAlchemy (src/allocation/service_layer/unit_of_work.py)
DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine( 
 config.get_postgres_uri(),
))
class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
 def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
 self.session_factory = session_factory 
 def __enter__(self):
 self.session = self.session_factory() # тип: Session 
 self.batches = repository.SqlAlchemyRepository(self.session) 
 return super().__enter__()
 def __exit__(self, *args):
 super().__exit__(*args)
 self.session.close() 
