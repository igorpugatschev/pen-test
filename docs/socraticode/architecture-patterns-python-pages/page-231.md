# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 231

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 12. Разделение обязанностей команд и запросов 231
При создании API мы можем применять тот же метод проектирования,
вернув 201 Created (Создано) или 202 Accepted (Принято) с заголовком
Location (Местоположение), содержащим URI новых ресурсов. Здесь
важен не используемый код статуса, а логическое разделение работы на
фазу записи и фазу запроса.
Можно разделять команды и запросы ради более быстрых и масштабируе-
мых систем, но сначала давайте исправим нарушение указанного принципа
в нашем коде. Давным-давно мы ввели конечную точку allocate, которая
принимает заказ и вызывает сервисный слой, чтобы найти нужный товар-
ный запас. В конце вызова мы возвращаем 200 OK и идентификатор партии.
Да, мы смогли получить нужные данные, но дизайн получился кривым.
Давайте исправим его так, чтобы вместо возврата простого сообщения OK
предоставлять новую конечную точку , предназначенную только для чтения,
которая будет извлекать состояние размещения заказа.
Т ест API выполняет метод GET после метода POST (tests/e2e/test_api.py)
@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_202_and_batch_is_allocated():
 orderid = random_orderid()
 sku, othersku = random_sku(), random_sku('other')
 earlybatch = random_batchref(1)
 laterbatch = random_batchref(2)
 otherbatch = random_batchref(3)
 api_client.post_to_add_batch(laterbatch, sku, 100, '2011-01-02')
 api_client.post_to_add_batch(earlybatch, sku, 100, '2011-01-01')
 api_client.post_to_add_batch(otherbatch, othersku, 100, None)
 r = api_client.post_to_allocate(orderid, sku, qty=3)
 assert r.status_code == 202
 r = api_client.get_allocation(orderid)
 assert r.ok
 assert r.json() == [
 {'sku': sku, 'batchref': earlybatch},
 ]
@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_returns_400_and_error_message():
 unknown_sku, orderid = random_sku(), random_orderid()
