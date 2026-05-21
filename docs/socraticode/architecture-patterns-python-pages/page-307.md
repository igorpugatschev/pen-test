# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 307

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Приложение В. Замена инфраструктуры: делаем все с помощью CSV 307
UoW для CSV-файлов: фиксация = csv.writer (src/allocation/service_layer/csv_uow.py)
class CsvUnitOfWork(unit_of_work.AbstractUnitOfWork):
 def __init__(self, folder):
 self.batches = CsvRepository(folder)
 def commit(self):
 with self.batches._allocations_path.open('w') as f:
 writer = csv.writer(f)
 writer.writerow(['orderid', 'sku', 'qty', 'batchref'])
 for batch in self.batches.list():
 for line in batch._allocations:
 writer.writerow(
 [line.orderid, line.sku, line.qty,
 batch.reference]
 )
 def rollback(self):
 pass
И как только мы это сделаем, CLI-приложение для чтения и записи партий
и размещений в CSV-фалы станет таким, каким оно должно быть, — не -
много кода для чтения товарных позиций заказа и еще немного для вызова
существующего сервисного слоя.
Размещение с помощью CSV-файлов в девяти строках (src/bin/allocate-from-csv)
def main(folder):
 orders_path = Path(folder) / 'orders.csv'
 uow = csv_uow.CsvUnitOfWork(folder)
 with orders_path.open() as f:
 reader = csv.DictReader(f)
 for row in reader:
 orderid, sku = row['orderid'], row['sku']
 qty = int(row['qty'])
 services.allocate(orderid, sku, qty, uow)
Та-да! Ну? Вы впечатлены или как?
С любовью,
Боб и Гарри
