# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 306

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

306 Приложение В. Замена инфраструктуры: делаем все с помощью CSV
 self._allocations_path = Path(folder) / 'allocations.csv'
 self._batches = {} # тип: Dict[str, model.Batch]
 self._load()
 def get(self, reference):
 return self._batches.get(reference)
 def add(self, batch):
 self._batches[batch.reference] = batch
 def _load(self):
 with self._batches_path.open() as f:
 reader = csv.DictReader(f)
 for row in reader:
 ref, sku = row['ref'], row['sku']
 qty = int(row['qty'])
 if row['eta']:
 eta = datetime.strptime(row['eta'],
 '%Y-%m-%d').date()
 else:
 eta = None
 self._batches[ref] = model.Batch(
 ref=ref, sku=sku, qty=qty, eta=eta
 )
 if self._allocations_path.exists() is False:
 return
 with self._allocations_path.open() as f:
 reader = csv.DictReader(f)
 for row in reader:
 batchref, orderid, sku = row['batchref'],
 row['orderid'], row['sku']
 qty = int(row['qty'])
 line = model.OrderLine(orderid, sku, qty)
 batch = self._batches[batchref]
 batch._allocations.add(line)
 def list(self):
 return list(self._batches.values())
А вот как будет выглядеть паттерн UoW для CSV-файлов.
