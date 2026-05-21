# Black Hat Python. Программирование для хакеров и пентестеров — страница 40

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

40   Глава 2. Основные сетевые инструменты
        client_socket.send(remote_buffer)
    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            line = "[==>]Received %d bytes from localhost." % len(local_buffer)
            print(line)
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote.")
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print("[<==] Received %d bytes from remote." % len(remote_buffer))
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[<==] Sent to localhost.")
        if not len(local_buffer) or not len(remote_buffer): 
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break
Эта функция содержит основную логику нашего прокси-сервера. Для на-
чала мы подключаемся к удаленному узлу . Затем убеждаемся в том, что
не нужно инициировать соединение с удаленной стороной и запрашивать
данные, прежде чем входить в главный цикл . Некоторые серверы ожида-
ют этого от клиентов (например, FTP-серверы обычно вначале отправляют
приветственное сообщение). Затем на обоих концах соединения использу-
ется функция receive_from . Она принимает объект соединенного сокета
и получает данные. Мы сохраняем содержимое пакета, чтобы позже его
можно было проанализировать в поисках чего-нибудь интересного. Дальше
передаем вывод функции response_handler  и отправляем принятый буфер
локальному клиенту . В остальном код прокси-сервера довольно простой: мы
подготавливаем цикл для непрерывного чтения данных локального клиента,
обрабатываем прочитанное и передаем результат удаленному клиенту , затем
читаем ответ удаленного клиента, обрабатываем прочитанное и передаем
результат локальному клиенту . Так продолжается до тех пор, пока данные
не перестанут приходить. Когда больше нечего отправлять ни на одном из
концов соединения , мы закрываем локальный и удаленный сокеты и вы-
ходим из цикла.
