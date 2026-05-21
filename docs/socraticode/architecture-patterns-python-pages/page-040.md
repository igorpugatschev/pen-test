# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 40

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

40 Часть I. Создание архитектуры для поддержки моделирования предметной области
Т естирование логики на предмет того, что можно разместить (test_batches.py)
def make_batch_and_line(sku, batch_qty, line_qty):
 return (
 Batch("batch-001", sku, batch_qty, eta=date.today()),
 OrderLine("order-123", sku, line_qty)
 )
def test_can_allocate_if_available_greater_than_required():
 large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)
 assert large_batch.can_allocate(small_line)
def test_cannot_allocate_if_available_smaller_than_required():
 small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
 assert small_batch.can_allocate(large_line) is False
def test_can_allocate_if_available_equal_to_required():
 batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
 assert batch.can_allocate(line)
def test_cannot_allocate_if_skus_do_not_match():
 batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
 different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
 assert batch.can_allocate(different_sku_line) is False
Т ут нет ничего неожиданного. Мы сделали рефакторинг набора тестов,
чтобы не дублировать строки кода для создания партии товара и товарной
позиции заказа для одного и того же артикула, и написали четыре простых
теста для нового метода can_allocate. Опять же обратите внимание, что
используемые нами имена отражают язык экспертов в анализируемой
сфере деятельности (предметной области), а согласованные с ними при-
меры записаны непосредственно в код.
Мы также можем реализовать это прямолинейно, написав метод can_
allocate класса Batch.
Новый метод в модели (model.py)
def can_allocate(self, line: OrderLine) -> bool:
 return self.sku == line.sku and self.available_quantity >= line.qty
Пока что мы можем управлять реализацией, просто увеличивая и уменьшая
количество Batch.available_quantity, но, как только мы перейдем к тестам
deallocate(), то нам понадобится более изящное решение.
