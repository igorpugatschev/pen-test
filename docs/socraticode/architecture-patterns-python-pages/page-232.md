# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 232

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

232 Часть II. Событийно-управляемая архитектура
 r = api_client.post_to_allocate(
 orderid, unknown_sku, qty=20, expect_success=False,
 )
 assert r.status_code == 400
 assert r.json()['message'] == f'Недопустимый артикул {unknown_sku}'
 r = api_client.get_allocation(orderid)
 assert r.status_code == 404
Итак, как могло бы выглядеть приложение Flask?
Конечная точка для просмотра размещений (src/allocation/entrypoints/flask_app.py)
from allocation import views
...
@app.route("/allocations/<orderid>", methods=['GET'])
def allocations_view_endpoint(orderid):
 uow = unit_of_work.SqlAlchemyUnitOfWork()
 result = views.allocations(orderid, uow) 
 if not result:
 return 'not found', 404
 return jsonify(result), 200
 Отлично, вопрос с views.py снят; можно держать там только то, что читаем,
и это будет настоящий views.py, а не как у Django — нечто, что знает, как
создавать представления данных, предназначенные только для чтения…
Хватайте свой обед, ребята
Гм, пожалуй, мы можем просто добавить метод списка к нашему существу-
ющему объекту репозитория.
Представления выполняют... сырой SQL? (src/allocation/views.py)
from allocation.service_layer import unit_of_work
def allocations(orderid: str, uow: unit_of_work.SqlAlchemyUnitOfWork):
 with uow:
 results = list(uow.session.execute(
 'SELECT ol.sku, b.reference'
 ' FROM allocations AS a'
 ' JOIN batches AS b ON a.batch_id = b.id'
 ' JOIN order_lines AS ol ON a.orderline_id = ol.id'
 ' WHERE ol.orderid = :orderid',
 dict(orderid=orderid)
