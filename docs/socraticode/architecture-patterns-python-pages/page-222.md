# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 222

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

222 Часть II. Событийно-управляемая архитектура
Redis — это еще один тонкий адаптер вокруг шины сообщений
Слушатель «издатель/подписчик» Redis (мы называем его потребителем
событий) очень похож на Flask: он делает передачу из внешнего мира
в наши события.
Простой слушатель сообщений Redis (src/allocation/entrypoints/redis_eventconsumer.py)
r = redis.Redis(**config.get_redis_host_and_port())
def main():
 orm.start_mappers()
 pubsub = r.pubsub(ignore_subscribe_messages=True)
 pubsub.subscribe('change_batch_quantity') 
 for m in pubsub.listen():
 handle_change_batch_quantity(m)
def handle_change_batch_quantity(m):
 logging.debug('handling %s', m)
 data = json.loads(m['data']) 
 cmd = commands.ChangeBatchQuantity(ref=data['batchref'],
 qty=data['qty']) 
 messagebus.handle(cmd, uow=unit_of_work.SqlAlchemyUnitOfWork())
 main() подписывает на канал change_batch_quantity при загрузке.
 Главная задача точки входа в систему — десериализовать JSON, кон -
вертировать его в команду и передать ее в сервисный слой — примерно
так же, как это делает Flask.
Также создаем новый нисходящий адаптер для выполнения противопо-
ложной задачи — конвертирования событий предметной области в пу-
бличные события.
Простой издатель сообщений Redis (src/allocation/adapters/redis_eventpublisher.py)
r = redis.Redis(**config.get_redis_host_and_port())
def publish(channel, event: events.Event): 
 logging.debug('publishing: channel=%s, event=%s', channel, event)
 r.publish(channel, json.dumps(asdict(event)))
 Здесь берется жестко закодированный канал, но вы также можете сохра-
нить попарную связку между классами/именами событий и подходящим
