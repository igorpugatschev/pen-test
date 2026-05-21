# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 308

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

ПРИЛОЖЕНИЕ Г
Паттерны «Репозиторий» и UoW
с Django
Предположим, что вы хотите использовать Django вместо SQLAlchemy
и Flask. Как все будет выглядеть? Первое, что нужно сделать, — это выбрать
место установки. Мы помещаем его в отдельный пакет рядом с основным
кодом размещения заказов:
├── src
│ ├── allocation
│ │ ├── __init__.py
│ │ ├── adapters
│ │ │ ├── __init__.py
...
│ ├── djangoproject
│ │ ├── alloc
│ │ │ ├── __init__.py
│ │ │ ├── apps.py
│ │ │ ├── migrations
│ │ │ │ ├── 0001_initial.py
│ │ │ │ └── __init__.py
│ │ │ ├── models.py
│ │ │ └── views.py
│ │ ├── django_project
│ │ │ ├── __init__.py
│ │ │ ├── settings.py
│ │ │ ├── urls.py
│ │ │ └── wsgi.py
│ │ └── manage.py
│ └── setup.py
└── tests
 ├── conftest.py
 ├── e2e
 │ └── test_api.py
 ├── integration
 │ ├── test_repository.py
...
