# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 110

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

110 Часть I. Создание архитектуры для поддержки моделирования предметной области
Как выглядит пирамида тестирования
Давайте посмотрим, что этот переход к использованию сервисного слоя
с его собственными тестами сделал с тестовой пирамидой:
Считаем типы тестов
$ grep -c test_ test_*.py
tests/unit/test_allocate.py:4
tests/unit/test_batches.py:8
tests/unit/test_services.py:3
tests/integration/test_orm.py:6
tests/integration/test_repository.py:2
tests/e2e/test_api.py:2
Неплохо! У нас пятнадцать юнит-тестов, восемь интеграционных тестов
и всего два сквозных теста. Это уже здравая тестовая пирамида.
Должны ли тесты слоя предметной области перейти
в сервисный слой?
Посмотрим, что произойдет дальше. Поскольку мы можем тестировать
программу для сервисного слоя, тесты для модели предметной области
больше не нужны. Вместо этого можно переписать все тесты слоя пред-
метной области из главы 1 для сервисного слоя:
Переписывание теста слоя предметной области в сервисном слое (tests/unit/test_services.py)
# тест слоя предметной области:
def test_prefers_current_stock_batches_to_shipments():
 in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100,
 eta=None)
 shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100,
 eta=tomorrow)
 line = OrderLine("oref", "RETRO-CLOCK", 10)
 allocate(line, [in_stock_batch, shipment_batch])
 assert in_stock_batch.available_quantity == 90
 assert shipment_batch.available_quantity == 100
# тест сервисного слоя:
def test_prefers_warehouse_batches_to_shipments():
