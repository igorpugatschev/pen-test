# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 305

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Приложение В. Замена инфраструктуры: делаем все с помощью CSV 305
 [old_order, sku, 10, batch1],
 ])
 orders_csv = make_csv('orders.csv', [
 ['orderid', 'sku', 'qty'],
 [new_order, sku, 7],
 ])
 run_cli_script(orders_csv.parent)
 expected_output_csv = orders_csv.parent / 'allocations.csv'
 with open(expected_output_csv) as f:
 rows = list(csv.reader(f))
 assert rows == [
 ['orderid', 'sku', 'qty', 'batchref'],
 [old_order, sku, '10', batch1],
 [new_order, sku, '7', batch2],
 ]
Можно продолжать и дальше добавлять в функцию load_batches лишние
строки, а также придумать какой-то способ отслеживания и сохранения
новых размещений — но у нас уже есть модель, которая все это делает!
И это паттерны «Репозиторий» и UoW .
Т ребуется сделать всего одну вещь — реализовать те же самые абстракции,
но в основе которых лежат CSV-файлы, а не база данных. И как вы увидите,
сделать это и правда несложно.
Реализация паттернов «Репозиторий» и UoW
для CSV-файлов
Вот как может выглядеть репозиторий на основе CSV-файлов. Он аб -
страгирует всю логику чтения CSV-файлов с диска, учитывая то, что он
должен читать два разных CSV-файла (один для партий товара и другой
для размещений). Получаем уже знакомый API .list(), который позво-
ляет создавать коллекцию объектов предметной области прямо в памяти.
Репозиторий, использующий CSV-файлы в качестве механизма хранения (src/allocation/
service_layer/csv_uow.py)
class CsvRepository(repository.AbstractRepository):
 def __init__(self, folder):
 self._batches_path = Path(folder) / 'batches.csv'
