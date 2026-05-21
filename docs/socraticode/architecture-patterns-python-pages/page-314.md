# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 314

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

314 Приложение Г. Паттерны «Репозиторий» и UoW с Django
 transaction.commit() 
 def rollback(self):
 transaction.rollback() 
 Метод set_autocommit(False) был лучшим способом дать команду Django
немедленно прекратить автоматическую фиксацию каждой операции ORM
и начать транзакцию.
 Затем мы используем явный откат и фиксации.
 Единственная трудность: поскольку , в отличие от SQLAlchemy , мы не
оборудуем сами экземпляры модели предметной области, команда commit()
должна явно пройти через все объекты, которые были затронуты каждым
репозиторием, и вручную обновить их обратно в ORM.
API: представления Django — это адаптеры
Django-файл views.py в конечном итоге почти идентичен старому flask_app.py,
так как из нашей архитектуры следует, что мы имеем дело с очень тонкой
оболочкой вокруг сервисного слоя (который, кстати, совсем не изменился):
Приложение Flask ¦ представления Django (src/djangoproject/alloc/views.py)
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoproject.django_
 project.settings'
django.setup()
@csrf_exempt
def add_batch(request):
 data = json.loads(request.body)
 eta = data['eta']
 if eta is not None:
 eta = datetime.fromisoformat(eta).date()
 services.add_batch(
 data['ref'], data['sku'], data['qty'], eta,
 unit_of_work.DjangoUnitOfWork(),
 )
 return HttpResponse('OK', status=201)
@csrf_exempt
def allocate(request):
 data = json.loads(request.body)
