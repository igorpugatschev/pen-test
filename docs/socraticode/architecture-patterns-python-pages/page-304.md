# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 304

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

304 Приложение В. Замена инфраструктуры: делаем все с помощью CSV
 ))
 return batches
def main(folder):
 batches_path = Path(folder) / 'batches.csv'
 orders_path = Path(folder) / 'orders.csv'
 allocations_path = Path(folder) / 'allocations.csv'
 batches = load_batches(batches_path)
 with orders_path.open() as inf, allocations_path.open('w') as outf:
 reader = csv.DictReader(inf)
 writer = csv.writer(outf)
 writer.writerow(['orderid', 'sku', 'batchref'])
 for row in reader:
 orderid, sku = row['orderid'], row['sku']
 qty = int(row['qty'])
 line = model.OrderLine(orderid, sku, qty)
 batchref = model.allocate(line, batches)
 writer.writerow([line.orderid, line.sku, batchref])
if __name__ == '__main__':
 main(sys.argv[1])
Выглядит не так уж и плохо! И мы вторично используем объекты модели
предметной области и службу предметной области.
Но это не будет работать. Существующие размещения также должны
быть частью постоянного CSV-хранилища. Можно написать второй тест,
который улучшит ситуацию.
И еще один, с существующими размещениями (tests/e2e/test_csv.py)
def test_cli_app_also_reads_existing_allocations_and_can_append_to_them(
 make_csv
):
 sku = random_ref('s')
 batch1, batch2 = random_ref('b1'), random_ref('b2')
 old_order, new_order = random_ref('o1'), random_ref('o2')
 make_csv('batches.csv', [
 ['ref', 'sku', 'qty', 'eta'],
 [batch1, sku, 10, '2011-01-01'],
 [batch2, sku, 10, '2011-01-02'],
 ])
 make_csv('allocations.csv', [
 ['orderid', 'sku', 'qty', 'batchref'],
