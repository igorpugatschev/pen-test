# Black Hat Python. Программирование для хакеров и пентестеров — страница 43

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Написание TCP-прокси   43
0010 20 73 75 63 63 65 73 73 66 75 6C 2E 20 43 6F 6E     successful. Con
0020 73 69 64 65 72 20 75 73 69 6E 67 20 50 41 53 56    sider using PASV
0030 2E 0D 0A                                           ...
[<==] Received 6 bytes from local.
0000 4C 49 53 54 0D 0A                                  LIST..
[<==] Received 63 bytes from remote.
0000 31 35 30 20 48 65 72 65 20 63 6F 6D 65 73 20 74    150 Here comes t
0010 68 65 20 64 69 72 65 63 74 6F 72 79 20 6C 69 73    he directory lis
0020 74 69 6E 67 2E 0D 0A 32 32 36 20 44 69 72 65 63    ting...226 Direc
0030 74 6F 72 79 20 73 65 6E 64 20 4F 4B 2E 0D 0A       tory send OK...
0000 50 4F 52 54 20 31 39 32 2C 31 36 38 2C 31 2C 32    PORT 192,168,1,2
0010 30 33 2C 32 31 38 2C 31 31 0D 0A                   03,218,11..
0000 32 30 30 20 50 4F 52 54 20 63 6F 6D 6D 61 6E 64    200 PORT command
0010 20 73 75 63 63 65 73 73 66 75 6C 2E 20 43 6F 6E    successful. Con
0020 73 69 64 65 72 20 75 73 69 6E 67 20 50 41 53 56    sider using PASV
0030 2E 0D 0A                                           ...
0000 51 55 49 54 0D 0A                                  QUIT..
[==>] Sent to remote.
0000 32 32 31 20 47 6F 6F 64 62 79 65 2E 0D 0A          221 Goodbye...
[==>] Sent to local.
[*] No more data. Closing connections.
В другом терминале Kali мы инициировали сеанс FTP , подключившись к IP-
адресу гостевой ВМ Kali с использованием порта по умолчанию 21:
tim@kali:$ ftp 192.168.1.203
Connected to 192.168.1.203.
220 Welcome to ftp.sun.ac.za
Name (192.168.1.203:tim): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
lrwxrwxrwx     1 1001    1001           48 Jul 17 2008 CPAN -> pub/mirrors/
ftp.funet.fi/pub/languages/perl/CPAN
lrwxrwxrwx     1 1001    1001           21 Oct 21 2009 CRAN -> pub/mirrors/
ubuntu.com
drwxr-xr-x     2 1001    1001         4096 Apr 03 2019 veeam
drwxr-xr-x     6 1001    1001         4096 Jun 27 2016 win32InetKeyTeraTerm
226 Directory send OK.
ftp> bye
221 Goodbye.
Здесь явно видно, что нам удалось получить приветственное сообщение по
FTP и отправить имя пользователя и пароль и что наш прокси-сервер завер-
шает работу предсказуемым образом.
