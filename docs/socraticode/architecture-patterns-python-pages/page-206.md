# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 206

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

206 Часть II. Событийно-управляемая архитектура
Когда клиент становится VIP-персоной впервые,
мы должны отправить ему имейл с поздравлениями
Мы применяем технические приемы, уже рассмотренные в этой книге,
и создаем новый агрегат History, который регистрирует заказы и может
инициировать события предметной области, когда эти правила удовлет-
воряются. Мы структурируем код следующим образом:
VIP-клиент (пример кода для другого проекта)
class History: # Агрегат
 def __init__(self, customer_id: int):
 self.orders = set() # Set[HistoryEntry]
 self.customer_id = customer_id

 def record_order(self, order_id: str, order_amount: int): 
 entry = HistoryEntry(order_id, order_amount)
 if entry in self.orders:
 return
 self.orders.add(entry)
 if len(self.orders) == 3:
 self.events.append(
 CustomerBecameVIP(self.customer_id)
 )
def create_order_from_basket(uow, cmd: CreateOrder): 
 with uow:
 order = Order.from_basket(cmd.customer_id, cmd.basket_items)
 uow.orders.add(order)
 uow.commit() # инициирует OrderCreated
def update_customer_history(uow, event: OrderCreated): 
 with uow:
 history = uow.order_history.get(event.customer_id)
 history.record_order(event.order_id, event.order_amount)
 uow.commit() # инициирует CustomerBecameVIP
 def congratulate_vip_customer(uow, event: CustomerBecameVip): 
 with uow:
 customer = uow.customers.get(event.customer_id)
 email.send(
 customer.email_address,
