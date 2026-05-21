# Black Hat Python. Программирование для хакеров и пентестеров — страница 27

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

TCP-сервер   27
# принимаем какие-нибудь данные
data, addr = client.recvfrom(4096) 
print(data.decode())
client.close()
Как видите, при создании объекта сокета мы поменяли его тип на SOCK_
DGRAM . Дальше нужно просто вызвать функцию sendto()  и передать ей
данные и сервер, которому вы хотите их отправить. Поскольку протокол UDP
не поддерживает соединения, перед взаимодействием нет вызова connect().
В конце нужно вызвать recvfrom() , чтобы получить ответные UDP-данные.
Вы можете заметить, что вместе с данными этот вызов возвращает информа-
цию об удаленном адресе и порте.
И вновь мы не пытаемся быть превосходными сетевыми программистами —
нам нужен быстрый, простой и надежный способ писать инструменты для
выполнения повседневных хакерских задач. Давайте перейдем к созданию
простых серверных программ.
TCP-сервер
В Python TCP-серверы создаются так же просто, как и клиенты. Собственный
TCP-сервер может пригодиться при написании командных оболочек или прок-
си-серверов (и то, и другое мы реализуем позже). Для начала создадим стандарт-
ный многопоточный TCP-сервер. Наберите в своем редакторе следующий код:
import socket
import threading
IP = '0.0.0.0'
PORT = 9998
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) 
    server.listen(5) 
    print(f'[*] Listening on {IP}:{PORT}')
    while True:
        client, address = server.accept() 
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client,
                                          args=(client,))
        client_handler.start() 
def handle_client(client_socket): 
    with client_socket as sock:
