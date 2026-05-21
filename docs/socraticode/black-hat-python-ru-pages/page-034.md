# Black Hat Python. Программирование для хакеров и пентестеров — страница 34

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

34   Глава 2. Основные сетевые инструменты
$ python netcat.py --help
usage: netcat.py [-h] [-c] [-e EXECUTE] [-l] [-p PORT] [-t TARGET] [-u UPLOAD]
BHP Net Tool
optional arguments:
  -h, --help            show this help message and exit
  -c, --command         initialize command shell
  -e EXECUTE, --execute EXECUTE
                        execute specified command
  -l, --listen          listen
  -p PORT, --port PORT  specified port
  -t TARGET, --target TARGET
                        specified IP
  -u UPLOAD, --upload UPLOAD
                        upload file
Example:
      netcat.py -t 192.168.1.108 -p 5555 -l -c # командная оболочка
      netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # загружаем в файл
      netcat.py -t 192.168.1.108 -p 5555 -l -e="cat /etc/passwd"
      # выполняем команду
      echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.108 -p 135
          # шлем локальный текст на порт сервера 135
      netcat.py -t 192.168.1.108 -p 5555 # соединяемся с сервером
Т еперь перейдите в систему Kali и запустите слушателя с использованием
собственного IP-адреса и порта 5555, чтобы предоставить доступ к командной
оболочке:
$ python netcat.py -t 192.168.1.203 -p 5555 -l -c
Откройте еще один терминал в своей локальной системе и запустите скрипт
в клиентском режиме. Помните, он читает из stdin до тех пор, пока не полу-
чит сигнал о конце файла (end-of-file, EOF). Чтобы послать EOF , нажмите
на клавиатуре Ctrl+ D:
% python netcat.py -t 192.168.1.203 -p 5555
CTRL+D
<BHP:#> ls -la
total 23497
drwxr-xr-x 1 502 dialout      608 May 16 17:12 .
drwxr-xr-x 1 502 dialout      512 Mar 29 11:23 ..
-rw-r--r-- 1 502 dialout     8795 May 6 10:10 mytest.png
-rw-r--r-- 1 502 dialout    14610 May 11 09:06 mytest.sh
-rw-r--r-- 1 502 dialout     8795 May 6 10:10 mytest.txt
-rw-r--r-- 1 502 dialout     4408 May 11 08:55 netcat.py
<BHP: #> uname -a
Linux kali 5.3.0-kali3-amd64 #1 SMP Debian 5.3.15-1kali1 (2019-12-09)
           x86_64 GNU/Linux
