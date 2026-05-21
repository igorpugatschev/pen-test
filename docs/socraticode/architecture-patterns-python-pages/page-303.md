# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 303

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Приложение В. Замена инфраструктуры: делаем все с помощью CSV 303
 [batch3, sku2, 100, '2011-01-02'],
 ])
 orders_csv = make_csv('orders.csv', [
 ['orderid', 'sku', 'qty'],
 [order_ref, sku1, 3],
 [order_ref, sku2, 12],
 ])
 run_cli_script(orders_csv.parent)
 expected_output_csv = orders_csv.parent / 'allocations.csv'
 with open(expected_output_csv) as f:
 rows = list(csv.reader(f))
 assert rows == [
 ['orderid', 'sku', 'qty', 'batchref'],
 [order_ref, sku1, '3', batch1],
 [order_ref, sku2, '12', batch2],
 ]
Погрузившись в реализацию и отбросив мысли о репозиториях и всем
в этом роде, возможно, вы начнете с чего-то такого:
Первая проба компонента, который читает/пишет CSV-файлы (src/bin/allocate-from-csv)
#!/usr/bin/env python
import csv
import csv import sys
from datetime import datetime
from pathlib import Path
from allocation import model
def load_batches(batches_path):
 batches = []
 with batches_path.open() as inf:
 reader = csv.DictReader(inf)
 for row in reader:
 if row['eta']:
 eta = datetime.strptime(row['eta'], '%Y-%m-%d').date()
 else:
 eta = None
 batches.append(model.Batch(
 ref=row['ref'],
 sku=row['sku'],
 qty=int(row['qty']),
 eta=eta
