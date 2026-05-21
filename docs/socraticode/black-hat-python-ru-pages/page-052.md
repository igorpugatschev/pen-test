# Black Hat Python. Программирование для хакеров и пентестеров — страница 52

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

52   Глава 2. Основные сетевые инструменты
def reverse_forward_tunnel(server_port, remote_host,
                           remote_port, transport):
    transport.request_port_forward('', server_port) 
    while True:
        chan = transport.accept(1000) 
        if chan is None:
            continue
    thr = threading.Thread( 
        target=handler, args=(chan, remote_host, remote_port)
    )

    thr.setDaemon(True)
    thr.start()
Paramiko предоставляет два основных метода взаимодействия: transport ,
ответственный за установление и поддержание зашифрованного соединения,
и channel, который ведет себя как сокет для отправки и приема данных по
зашифрованному сеансу , установленному с помощью transport. Здесь мы на-
чинаем использовать функцию request_port_forward из состава Paramiko для
перенаправления TCP-соединений, поступающих через порт SSH-сервера ,
и создаем новый канал передачи данных . Затем по этому каналу вызывается
функция handler .
Но мы еще не закончили. Нам нужно написать функцию handler для управ-
ления взаимодействием в каждом потоке:
def handler(chan, host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except Exception as e:
        verbose('Forwarding request to %s:%d failed: %r' % (host, port, e))
        return
    verbose(
        'Connected! Tunnel open %r -> %r -> %r'
        % (chan.origin_addr, chan.getpeername(), (host, port))
    )
    while True: 
        r, w, x = select.select([sock, chan], [], [])
        if sock in r:
            data = sock.recv(1024)
            if len(data) == 0:
                break
            chan.send(data)
        if chan in r:
            data = chan.recv(1024)
            if len(data) == 0:
