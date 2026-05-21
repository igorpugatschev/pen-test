# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 259

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 13. Внедрение зависимостей (и начальная загрузка) 259
Flask в той форме, в какой мы его написали. Здесь есть на что обратить
внимание.
Что еще меняется в шине сообщений?
Логика обработчика событий и команд остается неизменной (src/allocation/service_layer/
messagebus.py)
def handle_event(self, event: events.Event):
 for handler in self.event_handlers[type(event)]: 
 try:
 logger.debug('обрабатывается событие %s обработчиком %s',
 event, handler)
 handler(event) 
 self.queue.extend(self.uow.collect_new_events())
 except Exception:
 logger.exception('Событие обработки исключения %s', event)
 continue
def handle_command(self, command: commands.Command):
 logger.debug('handling command %s', command)
 try:
 handler = self.command_handlers[type(command)] 
 handler(command) 
 self.queue.extend(self.uow.collect_new_events())
 except Exception:
 logger.exception('Команда обработки исключения %s', command)
 raise
 handle_event и handle_command , по сути, одинаковы, но вместо индек-
сации в статических словарях EVENT_HANDLERS или COMMAND_HANDLERS в них
используются версии с self.
 Чтобы не передавать UoW в обработчик, мы предполагаем, что обра-
ботчики уже имеют все свои зависимости, поэтому требуется лишь один
аргумент, конкретное событие или команда.
Использование начальной загрузки в точках входа
В точках входа нашего приложения мы просто вызываем bootstrap.
bootstrap() и получаем готовую к работе шину сообщений, а не настраи-
ваем UoW и все остальное.
