# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 220

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

220 Часть II. Событийно-управляемая архитектура
изменение размера
партии
выпуск команды
Allocate
Обработчик BatchQuantityChanged +
UoW 1
Обработчик события Allocate (ра зместить) +
UoW 2 (или б ольше)
выпуск события(й)
Allocated
размещение
Событие
BatchQuantityChanged
публикация
в к анале line_allocated
Redis Шина
сообщений
Модель
предметной области
Redis Шина
сообщений
Модель
предметной области
Рис. 11.6. Последовательность для потока повторного размещения
Сквозной тест для модели «издатель/подписчик» (tests/e2e/test_external_events.py)
def test_change_batch_quantity_leading_to_reallocation():
 # начать с двух партий и заказа, размещенного в одной из них 
 orderid, sku = random_orderid(), random_sku()
 earlier_batch, later_batch = random_batchref('old'), random_
 batchref('newer')
 api_client.post_to_add_batch(earlier_batch, sku, qty=10,
 eta='2011-01-02') 
 api_client.post_to_add_batch(later_batch, sku, qty=10, eta='2011-
 01-02')
 response = api_client.post_to_allocate(orderid, sku, 10) 
 assert response.json()['batchref'] == earlier_batch
 subscription = redis_client.subscribe_to('line_allocated') 
