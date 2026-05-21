# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 309

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Приложение Г. Паттерны «Репозиторий» и UoW с Django 309
Код для этого приложения находится в ветке appendix_django на GitHub 1 :
git clone https://github.com/cosmicpython/code.git
cd code
git checkout appendix_django
Паттерн «Репозиторий» с Django
Мы использовали плагин под названием pytest-django 2 для управления
тестовой базой данных.
Переписывание первого теста репозитория свелось к минимуму — просто
замена сырого SQL вызовом ORM/QuerySet Django:
Первый тест репозитория после адаптации (tests/integration/test_repository.py)
from djangoproject.alloc import models as django_models
 @pytest.mark.django_db
 def test_repository_can_save_a_batch():
 batch = model.Batch("batch1", "RUSTY-SOAPDISH", 100,
 eta=date(2011, 12, 25))
 repo = repository.DjangoRepository()
 repo.add(batch)
 [saved_batch] = django_models.Batch.objects.all()
 assert saved_batch.reference == batch.reference
 assert saved_batch.sku == batch.sku
 assert saved_batch.qty == batch._purchased_quantity
 assert saved_batch.eta == batch.eta
Второй тест более сложный, так как имеет дело с размещениями, но при
этом все еще состоит из знакомого кода Django:
Сложный второй тест репозитория (tests/integration/test_repository.py)
@pytest.mark.django_db
def test_repository_can_retrieve_a_batch_with_allocations():
 sku = "PONY-STATUE"
1 См. https://oreil.ly/A-I76
2 См. https://github.com/pytest-dev/pytest-django
