# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 324

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

324 Приложение Д. Валидация
Вот как можно использовать этот метод из конечной точки Flask API:
API выталкивает ошибки валидации вверх (src/allocation/flask_app.py)
@app.route("/change_quantity", methods=['POST'])
def change_batch_quantity():
 try:
 bus.handle_message('ChangeBatchQuantity', request.body)
 except ValidationError as e:
 return bad_request(e)
 except exceptions.InvalidSku as e:
 return jsonify({'message': str(e)}), 400
def bad_request(e: ValidationError):
 return e.code, 400
И теперь его можно подключить к асинхронному процессору сообщений.
Ошибки валидации при обработке сообщений Redis (src/allocation/redis_pubsub.py)
def handle_change_batch_quantity(m, bus: messagebus.MessageBus):
 try:
 bus.handle_message('ChangeBatchQuantity', m)
 except ValidationError:
 print('Пропуск невалидного сообщения')
 except exceptions.InvalidSku as e:
 print(f'Не получается изменить товар — отсутствующий артикул {e}')
Обратите внимание, что точки входа занимаются исключительно тем,
что получают сообщения из внешнего мира и сообщают об успехе или
неудаче. Шина сообщений занимается валидацией наших запросов и мар-
шрутизацией их в правильный обработчик, а обработчики сосредоточены
исключительно на логике варианта использования.
Когда вы получаете невалидное сообщение, обычно мало что можно
сделать, кроме как зарегистрировать ошибку и продолжить. В компа-
нии MADE мы используем метрики для подсчета числа получаемых
системой сообщений и доли успешно обработанных, пропущенных или
невалидных из них. Инструменты мониторинга предупредят нас, если
мы увидим всплеск «плохих» сообщений.
