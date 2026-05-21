# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 96

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

96 Часть I. Создание архитектуры для поддержки моделирования предметной области
Это скорее проверка исправности, которую мы должны реализовать на
уровне базы данных, прежде чем вызывать службу предметной области.
Т еперь мы рассмотрим еще два сквозных теста:
Еще больше тестов в слое сквозных тестов (test_api.py)
@pytest.mark.usefixtures('restart_api')
def test_400_message_for_out_of_stock(add_stock): 
 sku, smalL_batch, large_order = random_sku(), random_batchref(),
 random_orderid()
 add_stock([
 (smalL_batch, sku, 10, '2011-01-01'),
 ])
 data = {'orderid': large_order, 'sku': sku, 'qty': 20}
 url = config.get_api_url()
 r = requests.post(f'{url}/allocate', json=data)
 assert r.status_code == 400
 assert r.json()['message'] == f'Артикула {sku} нет в наличии'
@pytest.mark.usefixtures('restart_api')
def test_400_message_for_invalid_sku(): 
 unknown_sku, orderid = random_sku(), random_orderid()
 data = {'orderid': orderid, 'sku': unknown_sku, 'qty': 20}
 url = config.get_api_url()
 r = requests.post(f'{url}/allocate', json=data)
 assert r.status_code == 400
 assert r.json()['message'] == f'Недопустимый артикул {unknown_sku}'
 В первом тесте мы пытаемся разместить больше товаров, чем есть в на-
личии.
 Во втором случае артикула просто не существует (потому что мы ни
разу не вызывали add_stock), и для приложения он недействителен.
Конечно, мы могли бы реализовать это и в приложении Flask.
Приложение Flask начинает портиться (flask_app.py)
def is_valid_sku(sku, batches):
 return sku in {b.sku for b in batches}
@app.route("/allocate", methods=['POST'])
def allocate_endpoint():
 session = get_session()
 batches = repository.SqlAlchemyRepository(session).list()
 line = model.OrderLine(
