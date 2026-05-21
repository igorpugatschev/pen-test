# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 260

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

260 Часть II. Событийно-управляемая архитектура
Flask вызывает сценарий начальной загрузки (src/allocation/entrypoints/flask_app.py)
-from allocation import views
+from allocation import bootstrap, views
 app = Flask(__name__)
-orm.start_mappers() 
+bus = bootstrap.bootstrap()
 @app.route("/add_batch", methods=['POST'])
@@ -19,8 +16,7 @@ def add_batch():
 cmd = commands.CreateBatch(
 request.json['ref'], request.json['sku'],
 request.json['qty'], eta,
 )
- uow = unit_of_work.SqlAlchemyUnitOfWork() 
- messagebus.handle(cmd, uow)
+ bus.handle(cmd) 
 return 'OK', 201
 Больше не нужно вызывать start_orm(); это сделают этапы инициали-
зации в загрузочном сценарии.
 Нам также не нужно явно создавать конкретный тип UoW ; об этом по
умолчанию позаботится сценарий начальной загрузки.
 Шина сообщений теперь является конкретным экземпляром, а не гло-
бальным модулем1 .
Внедрение зависимостей в тестах
В тестах мы можем использовать bootstrap.bootstrap() с переопреде-
ленными значениями по умолчанию для получения собственной шины
сообщений. Вот пример интеграционного теста:
Переопределение значений по умолчанию bootstrap (tests/integration/test_views.py)
@pytest.fixture
def sqlite_bus(sqlite_session_factory):
1 Если разобраться,она все еще глобальна в области видимости модуля flask_app .
Это может вызвать проблемы, если вы когда-нибудь захотите протестировать свое
приложение Flask в процессе с помощью Flask T est Client, а не Docker, как мы. Если
хотите глубже погрузиться в тему , стоит изучить фабрики приложений Flask. См.
https://oreil.ly/_a6Kl
