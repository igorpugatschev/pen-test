# Black Hat Python. Программирование для хакеров и пентестеров — страница 31

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Замена netcat   31
Т еперь начнем собирать некоторые из этих функций вместе, начиная с нашего
клиентского кода. Добавьте в главный блок следующее:
class NetCat:
    def __init__(self, args, buffer=None): 
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def run(self):
        if self.args.listen:
            self.listen() 
        else:
            self.send() 
Мы инициализируем объект NetCat с помощью аргументов из командной
строки и буфера , после чего создаем объект сокета .
Метод run, который служит точкой входа для управления объектом NetCat,
довольно прост: он делегирует выполнение двум другим методам. Если нам
нужно подготовить слушателя, вызываем метод listen , а если нет — метод
send . Последний выглядит так:
def send(self):
    self.socket.connect((self.args.target, self.args.port)) 
    if self.buffer:
        self.socket.send(self.buffer)
    try: 
        while True: 
        recv_len = 1
        response = ''
        while recv_len:
            data = self.socket.recv(4096)
            recv_len = len(data)
            response += data.decode()
            if recv_len < 4096:
                break 
        if response:
            print(response)
            buffer = input('> ')
            buffer += '\n'
            self.socket.send(buffer.encode()) 
    except KeyboardInterrupt: 
        print('User terminated.')
        self.socket.close()
        sys.exit()
