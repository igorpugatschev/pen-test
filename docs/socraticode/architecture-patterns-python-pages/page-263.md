# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 263

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 13. Внедрение зависимостей (и начальная загрузка) 263
Задаем абстрактную и конкретную реализации
Мы представим более общий API уведомлений. В один и тот же день
уведомления могут рассылаться через электронную почту , SMS или Slack.
Абстрактная (с использованием абстрактных базовых классов) и конкретная реализации (src/
allocation/adapters/notifications.py)
class AbstractNotifications(abc.ABC):
 @abc.abstractmethod
 def send(self, destination, message):
 raise NotImplementedError
...
class EmailNotifications(AbstractNotifications):
 def __init__(self, smtp_host=DEFAULT_HOST, port=DEFAULT_PORT):
 self.server = smtplib.SMTP(smtp_host, port=port)
 self.server.noop()
 def send(self, destination, message):
 msg = f'Subject: allocation service notification\n{message}'
 self.server.sendmail(
 from_addr='allocations@example.com',
 to_addrs=[destination],
 msg=msg
 )
Меняем зависимость в сценарии начальной загрузки.
Уведомления в шине сообщений (src/allocation/bootstrap.py)
def bootstrap(
 start_orm: bool = True,
 uow: unit_of_work.AbstractUnitOfWork =
 unit_of_work.SqlAlchemyUnitOfWork(),
- send_mail: Callable = email.send,
+ notifications: AbstractNotifications = EmailNotifications(),
 publish: Callable = redis_eventpublisher.publish,
) -> messagebus.MessageBus:
Создаем поддельную версию для тестов
Прорабатываем и определяем поддельную версию для юнит-тестов.
