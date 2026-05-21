# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 143

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 7. Агрегаты и границы согласованности 143
...мы используем подход с рис. 7.3, где есть новый объект Product для кон-
кретного артикула товарной позиции заказа, отвечающий за все партии то-
вара для этого артикула, и можем вызывать метод .allocate() прямо в нем.
Сервисный слой
Репозитории
просьба предоставить
продукт для ук азанного
артикула
get()
Модель
предметной области
product.allocate(orderline)
allocate()
Репозиторий
продуктов
наличие
Партия товара
Product
allocate()
Рис. 7.3. Нынешняя модель: используем Product, чтобы разместить заказ относительно всех партий товара
Давайте посмотрим, как это выглядит в коде.
Выбранный нами агрегат, Product (src/allocation/domain/model.py)
class Product:
 def __init__(self, sku: str, batches: List[Batch]):
 self.sku = sku 
 self.batches = batches 
 def allocate(self, line: OrderLine) -> str: 
 try:
 batch = next(
 b for b in sorted(self.batches) if b.can_
 allocate(line)
 )
 batch.allocate(line)
 return batch.reference
 except StopIteration:
 raise OutOfStock(f'Артикула {line.sku} нет в наличии')
