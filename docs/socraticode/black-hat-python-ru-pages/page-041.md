# Black Hat Python. Программирование для хакеров и пентестеров — страница 41

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Написание TCP-прокси   41
Создадим функцию server_loop для настройки соединения и управления им:
def server_loop(local_host, local_port,
                remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        server.bind((local_host, local_port)) 
    except Exception as e:
        print('problem on bind: %r' % e)
        print("[!!] Failed to listen on %s:%d" % (local_host, local_port))
        print("[!!] Check for other listening sockets
                    or correct permissions.")
        sys.exit(0)
    print("[*] Listening on %s:%d" % (local_host, local_port))
    server.listen(5)
    while True: 
        client_socket, addr = server.accept()
        # выводим информацию о локальном соединении
        line = "> Received incoming connection from %s:%d" % (addr[0], addr[1])
        print(line)
        # создаем поток для взаимодействия с удаленным сервером
        proxy_thread = threading.Thread( 
            target=proxy_handler,
            args=(client_socket, remote_host,
            remote_port, receive_first))
        proxy_thread.start()
Функция server_loop создает сокет , привязывает его к локальному адресу
и начинает прослушивать . В главном цикле , когда приходит запрос
на соединение, мы передаем его функции proxy_handler  в новом потоке ,
которая занимается отправкой и приемом битов на том или ином конце
потока данных.
Осталось только написать функцию main:
def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: ./proxy.py [localhost] [localport]", end='')
        print("[remotehost] [remoteport] [receive_first]")
        print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    receive_first = sys.argv[5]
    if "True" in receive_first:
