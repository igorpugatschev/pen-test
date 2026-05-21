# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 264

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

264 Часть II. Событийно-управляемая архитектура
Поддельные уведомления (tests/unit/test_handlers.py)
class FakeNotifications(notifications.AbstractNotifications):
 def __init__(self):
 self.sent = defaultdict(list) # тип: Dict[str, List[str]]
 def send(self, destination, message):
 self.sent[destination].append(message)
 ...
И используем ее.
Т есты изменяются незначительно (tests/unit/test_handlers.py)
def test_sends_email_on_out_of_stock_error(self):
 fake_notifs = FakeNotifications()
 bus = bootstrap.bootstrap(
 start_orm=False,
 uow=FakeUnitOfWork(),
 notifications=fake_notifs,
 publish=lambda *args: None,
 )
 bus.handle(commands.CreateBatch("b1", "POPULAR-CURTAINS", 9, None))
 bus.handle(commands.Allocate("o1", "POPULAR-CURTAINS", 10))
 assert fake_notifs.sent['stock@made.com'] == [
 f"POPULAR-CURTAINS нет в наличии",
 ]
Выясняем, как провести интеграционное тестирование реального кода
Т еперь мы тестируем реальный код, обычно с помощью сквозного или
интеграционного теста. Для среды разработки Docker в качестве реального
почтового сервера мы использовали сервер MailHog 1 .
Конфигурационный файл docker-compose с подделкой реального почтового сервера (docker-
compose.yml)
version: "3"
services:
 redis_pubsub:
 build:
 context: .
1 См. https://github.com/mailhog/MailHog
