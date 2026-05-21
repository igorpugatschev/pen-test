# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 168

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

168 Часть II. Событийно-управляемая архитектура
Классы событий (src/allocation/domain/events.py)
from dataclasses import dataclass
class Event: 
 pass
@dataclass
class OutOfStock(Event): 
 sku: str
 Если событий много, есть смысл ввести родительский класс, который
будет хранить общие атрибуты. Это также пригодится для подсказок типов
в канале передачи сообщений, как вы увидите позже.
 dataclasses отлично подходят и для событий предметной области.
Модель инициирует события
Когда модель предметной области регистрирует произошедший факт, мы
говорим, что она инициирует событие.
Вот как это будет выглядеть снаружи; если мы просим Product разместить
заказ на товар, но у него не получается это сделать, то он должен иници-
ировать событие.
Т ест агрегата на предмет инициирования им события (tests/unit/test_product.py)
def test_records_out_of_stock_event_if_cannot_allocate():
 batch = Batch('batch1', 'SMALL-FORK', 10, eta=today)
 product = Product(sku="SMALL-FORK", batches=[batch])
 product.allocate(OrderLine('order1', 'SMALL-FORK', 10))
 allocation = product.allocate(OrderLine('order2', 'SMALL-FORK', 1))
 assert product.events[-1] == events.OutOfStock(sku="SMALL-FORK") 
 assert allocation is None
 Агрегат будет выявлять новый атрибут .events со списком случившихся
фактов в форме объектов Event.
Вот как модель выглядит изнутри.
Модель инициирует событие предметной области (src/allocation/domain/model.py)
class Product:
 def __init__(self, sku: str, batches: List[Batch], version_
