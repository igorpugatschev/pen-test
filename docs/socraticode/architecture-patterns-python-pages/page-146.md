# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 146

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

146 Часть I. Создание архитектуры для поддержки моделирования предметной области
торий, FakeRepository, а затем передать новую модель в сервисный слой,
чтобы проверить, как она выглядит с объектом Product в качестве основной
точки входа.
Сервисный слой (src/allocation/service_layer/services.py)
def add_batch(
 ref: str, sku: str, qty: int, eta: Optional[date],
 uow: unit_of_work.AbstractUnitOfWork
):
 with uow:
 product = uow.products.get(sku=sku)
 if product is None:
 product = model.Product(sku, batches=[])
 uow.products.add(product)
 product.batches.append(model.Batch(ref, sku, qty, eta))
 uow.commit()
def allocate(
 orderid: str, sku: str, qty: int,
 uow: unit_of_work.AbstractUnitOfWork
) -> str:
 line = OrderLine(orderid, sku, qty)
 with uow:
 product = uow.products.get(sku=line.sku)
 if product is None:
 raise InvalidSku(f'Недопустимый артикул {line.sku}')
 batchref = product.allocate(line)
 uow.commit()
 return batchref
А что насчет производительности?
Мы уже несколько раз упоминали, что добавляем агрегаты в модели,
потому что хотим получить высокопроизводительное ПО, но здесь мы
загружаем все партии, когда требуется всего одна. Такое решение вполне
может показаться неэффективным, но есть несколько причин, почему нас
это устраивает.
Во-первых, мы целенаправленно моделируем данные так, чтобы делать
один запрос к базе данных на чтение и один запрос на обновление для
сохранения изменений. Системы с таким подходом работают намного
лучше систем, которые выдают много специальных запросов. В послед-
