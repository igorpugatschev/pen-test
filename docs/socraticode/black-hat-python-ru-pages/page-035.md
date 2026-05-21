# Black Hat Python. Программирование для хакеров и пентестеров — страница 35

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Замена netcat   35
Как видите, получили собственную командную оболочку . Поскольку мы на-
ходимся в системе Unix, то можем выполнять локальные команды и получать
в ответ их вывод, как если бы все взаимодействие происходило через SSH
или локальный терминал. Мы можем сделать то же самое в системе Kali,
но так, чтобы она выполнила отдельную команду . Для этого воспользуемся
параметром -e:
$ python netcat.py -t 192.168.1.203 -p 5555 -l -e="cat /etc/passwd"
Т еперь при подключении к Kali из локальной системы мы получим в ответ
вывод команды:
% python netcat.py -t 192.168.1.203 -p 5555
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
В локальной системе также можно было бы использовать netcat:
% nc 192.168.1.203 5555
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
Наконец, мы могли бы воспользоваться клиентом для отправки запроса ста-
рым добрым способом:
$ echo -ne "GET / HTTP/1.1\r\nHost: reachtim.com\r\n\r\n"
    |python ./netcat.py -t reachtim.com-p 80
HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Mon, 18 May 2020 12:46:30 GMT
Content-Type: text/html; charset=iso-8859-1
Content-Length: 229
Connection: keep-alive
Location: https://reachtim.com/
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
