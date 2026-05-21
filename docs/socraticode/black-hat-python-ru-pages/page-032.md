# Black Hat Python. Программирование для хакеров и пентестеров — страница 32

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

32   Глава 2. Основные сетевые инструменты
Мы подключаемся к серверу с заданными адресом и портом  и передаем
ему буфер, он у нас есть. Затем используем блок try/catch , чтобы иметь
возможность закрыть соединение вручную нажатием Ctrl+ C . Дальше на -
чинаем цикл , чтобы получить данные от целевого сервера. Если данных
больше нет, выходим из цикла . В противном случае выводим ответ,
останавливаемся, чтобы получить интерактивный ввод, отправляем его 
и продолжаем цикл.
Цикл будет работать, пока не произойдет исключение KeyboardInterrupt
( Ctrl+ C) , в результате чего закроется сокет.
Т еперь напишем метод, который выполняется, когда программа запускается
для прослушивания:
def listen(self):
    self.socket.bind((self.args.target, self.args.port)) 
    self.socket.listen(5)
        while True: 
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            client_thread.start()
Метод listen привязывается к адресу и порту  и начинает прослушивание
в цикле , передавая подключившиеся сокеты методу handle .
Т еперь реализуем логику для загрузки файлов, выполнения команд и созда-
ния интерактивной командной оболочки. Программа может выполнять эти
задания в режиме прослушивания:
def handle(self, client_socket):
    if self.args.execute: 
        output = execute(self.args.execute)
        client_socket.send(output.encode())
    elif self.args.upload: 
        file_buffer = b''
        while True:
            data = client_socket.recv(4096)
            if data:
                file_buffer += data
            else:
                break
        with open(self.args.upload, 'wb') as f:
