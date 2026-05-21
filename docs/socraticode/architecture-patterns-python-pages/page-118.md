# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 118

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

118 Часть I. Создание архитектуры для поддержки моделирования предметной области
Т есты API теперь могут добавлять свои собственные партии (tests/e2e/test_api.py)
def post_to_add_batch(ref, sku, qty, eta):
 url = config.get_api_url()
 r = requests.post(
 f'{url}/add_batch',
 json={'ref': ref, 'sku': sku, 'qty': qty, 'eta': eta}
 )
 assert r.status_code == 201
@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_allocated_batch():
 sku, othersku = random_sku(), random_sku('other')
 earlybatch = random_batchref(1)
 laterbatch = random_batchref(2)
 otherbatch = random_batchref(3)
 post_to_add_batch(laterbatch, sku, 100, '2011-01-02')
 post_to_add_batch(earlybatch, sku, 100, '2011-01-01')
 post_to_add_batch(otherbatch, othersku, 100, None)
 data = {'orderid': random_orderid(), 'sku': sku, 'qty': 3}
 url = config.get_api_url()
 r = requests.post(f'{url}/allocate', json=data)
 assert r.status_code == 201
 assert r.json()['batchref'] == earlybatch
Выводы
Создав сервисный слой, вы действительно можете перенести большую
часть тестового охвата на юнит-тесты и разработать правильную пирамиду
тестирования.
Вот что вам может помочь:
 y Выражайте сервисный слой с помощью примитивов, а не объектов
предметной области.
 y В идеальном мире у вас будут все нужные службы для полного тестиро-
вания сервисного слоя, и вам не придется взламывать состояние через
репозитории или базу данных. Это окупается и в сквозных тестах.
Вперед к следующей главе!
