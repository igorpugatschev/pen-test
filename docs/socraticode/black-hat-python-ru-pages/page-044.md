# Black Hat Python. Программирование для хакеров и пентестеров — страница 44

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

44   Глава 2. Основные сетевые инструменты
SSH с применением Paramiko
Замена netcat, которую мы создали, довольно полезная, но иногда, чтобы вас
не обнаружили, свой трафик лучше шифровать. Часто для этого создают тун-
нель с помощью протокола SSH. Но что если на атакуемом вами компьютере
нет SSH-клиента, как у 99,81943 % систем Windows?
Конечно, для Windows есть отличные SSH-клиенты, такие как PuTTY , но
эта книга о Python. В Python для создания SSH-клиента или сервера можно
использовать сырые сокеты и чуть-чуть криптографической магии, но зачем
писать самим, если можно взять готовое? Пакет Paramiko, основанный на
PyCrypto, предоставляет простой доступ к протоколу SSH2.
Чтобы показать, как работает эта библиотека, сделаем с ее помощью не-
сколько упражнений: установим соединение и выполним по SSH команду
в удаленной системе, подготовим SSH-клиент и SSH-сервер для реализации
удаленных команд на компьютере с Windows и, наконец, проанализируем
файл с демонстрацией обратного туннеля, входящий в состав Paramiko.
Приступим.
Для начала установите пакет Paramiko с помощью pip (или скачайте его на
сайте http://www.paramiko.org/):
pip install paramiko
Позже мы будем использовать несколько демонстрационных файлов, поэтому
не забудьте скачать их из репозитория Paramiko на GitHub ( https://github.com/
paramiko/paramiko/).
Создайте файл с именем ssh_cmd.py и наберите следующее:
import paramiko
def ssh_command(ip, port, user, passwd, cmd): 
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    client.connect(ip, port=port, username=user, password=passwd)
    _, stdout, stderr = client.exec_command(cmd) 
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())
