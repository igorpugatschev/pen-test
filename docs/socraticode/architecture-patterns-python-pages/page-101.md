# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 101

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 4. Первый вариант использования: API фреймворка Flask и сервисный слой 101
 request.json['orderid'], 
 request.json['sku'], 
 request.json['qty'], 
 )
 try:
 batchref = services.allocate(line, repo, session) 
 except (model.OutOfStock, services.InvalidSku) as e:
 return jsonify({'message': str(e)}), 400 
 return jsonify({'batchref': batchref}), 201 
 Создаем экземпляр сеанса базы данных и несколько объектов репози-
тория.
 Извлекаем из веб-запроса команды пользователя и передаем их в службу
предметной области.
 Возвращаем несколько ответов в формате JSON с соответствующими
кодами статуса.
Обязанности приложения Flask связаны со всякими веб-штуками: сеансом
по запросу , разбором информации из параметров POST , кодами статуса
ответа и JSON. Вся логика оркестровки находится в слое варианта ис-
пользования/служб, а логика предметной области остается в пределах
предметной области.
Наконец, мы можем уверенно урезать сквозные тесты, оставив всего два:
один для счастливого пути и другой — для несчастливого.
Сквозные тесты проверяют только счастливые и несчастливые пути (test_api.py)
@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_allocated_batch(add_stock):
 sku, othersku = random_sku(), random_sku('other')
 earlybatch = random_batchref(1)
 laterbatch = random_batchref(2)
 otherbatch = random_batchref(3)
 add_stock([
 (laterbatch, sku, 100, '2011-01-02'),
 (earlybatch, sku, 100, '2011-01-01'),
 (otherbatch, othersku, 100, None),
 ])
 data = {'orderid': random_orderid(), 'sku': sku, 'qty': 3}
 url = config.get_api_url()
 r = requests.post(f'{url}/allocate', json=data)
