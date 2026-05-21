# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 209

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 10. Команды и обработчик команд 209
Ручное воспроизведение хорошо работает в тех случаях, когда нужно ис-
править баг, перед тем как обработать событие повторно. Однако системы
всегда будут испытывать некоторый фоновый уровень самоустраняющегося
отказа. Сюда входят, например, сбои в сети, взаимоблокировки таблиц
и кратковременные простои, вызванные развертыванием.
В большинстве случаев можно элегантно восстановиться, попробовав еще
раз. Народная мудрость гласит: «Если с первого раза не получилось, по-
вторите операцию с экспоненциальным откатом».
Обработчик с повторной попыткой (src/allocation/service_layer/messagebus.py)
from tenacity import Retrying, RetryError, stop_after_attempt, wait_
exponential 
...
def handle_event(
 event: events.Event,
 queue: List[Message],
 uow: unit_of_work.AbstractUnitOfWork
):
 for handler in EVENT_HANDLERS[type(event)]:
 try:
 for attempt in Retrying( 
 stop=stop_after_attempt(3),
 wait=wait_exponential()
 ):
 with attempt:
 logger.debug('Обработка события %s обработчиком
 %s', event, handler)
 handler(event, uow=uow)
 queue.extend(uow.collect_new_events())
 except RetryError as retry_failure:
 logger.error(
 'Не получилсоь обработать событие %s раз, отказ!,
 retry_failure.last_attempt.attempt_number
 )
 continue
 T enacity — это библиотека, в которой реализованы часто встречающиеся
паттерны для повторных попыток.
 Здесь мы настраиваем шину сообщений на повторение операций до трех
раз с экспоненциально увеличивающимся ожиданием между попытками.
