# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 61

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 2. Паттерн «Репозиторий» 61
Когда вы впервые пытаетесь создать конфигурацию ORM, порой неплохо
писать для нее тесты, как в следующем примере:
Т естирование ORM напрямую (одноразовые тесты) (test_orm.py)
def test_orderline_mapper_can_load_lines(session): 
 session.execute(
 'INSERT INTO order_lines (orderid, sku, qty) VALUES '
 '("order1", "RED-CHAIR", 12),'
 '("order1", "RED-TABLE", 13),'
 '("order2", "BLUE-LIPSTICK", 14)'
 )
 expected = [
 model.OrderLine("order1", "RED-CHAIR", 12),
 model.OrderLine("order1", "RED-TABLE", 13),
 model.OrderLine("order2", "BLUE-LIPSTICK", 14),
 ]
 assert session.query(model.OrderLine).all() == expected
def test_orderline_mapper_can_save_lines(session):
 new_line = model.OrderLine("order1", "DECORATIVE-WIDGET", 12)
 session.add(new_line)
 session.commit()
 rows = list(session.execute('SELECT orderid, sku, qty FROM
 "order_lines"'))
 assert rows == [("order1", "DECORATIVE-WIDGET", 12)]
 Если вы не знакомы с библиотекой pytest, то нам стоит объяснить ис-
пользование аргумента session в этом тесте. Вообще-то для понимания
этой книги вам не нужно разбираться в деталях pytest или ее фикстурах.
Мы ограничимся лишь кратким объяснением. Вы можете определять об-
щие зависимости для своих тестов как фикстуры (fixture) и pytest введет
их в тесты, где они нужны, посмотрев на их функциональные аргументы.
В данном случае это сеанс базы данных SQLAlchemy .
Скорее всего, эти тесты вам не пригодятся — как вы вскоре увидите, ин-
вертировав зависимость от ORM и модели предметной области, останется
сделать лишь крохотный дополнительный шаг для реализации еще одной
абстракции — паттерна «Репозиторий», для которого будет легче писать
тесты и который позже обеспечит простой шаблон интерфейса для тести-
рования.
