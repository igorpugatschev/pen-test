# Black Hat Python. Программирование для хакеров и пентестеров — страница 212

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

212   Глава 11. Методы компьютерно-технической экспертизы в арсенале хакера
Исследуем эту информацию немного подробнее, применив подключаемый
модуль pslist, который выводит список процессов, запущенных в момент
создания снимка:
PS>vol -f WinDev2007Eval-7d959ee5.vmem windows.pslist
Volatility 3 Framework 1.2.0-beta.1
Progress:   33.01               Scanning primary2 using PdbSignatureScanner
PID     PPID    ImageFileName   Offset(V)   Threads Handles SessionId   Wow64
4       0       System         0xa50bb3e6d040 129       -       N/A     False
72      4       Registry       0xa50bb3fbd080 4         -       N/A     False
6452    4732    OneDrive.exe   0xa50bb4d62080 25        -       1       True
6484    4732    FreeDesktopClo 0xa50bbb847300 1         -       1       False
6212    556     SgrmBroker.exe 0xa50bbb832080 6         -       0       False
1636    556     svchost.exe    0xa50bbadbe340 8         -       0       False
7092    4732    cmd.exe        0xa50bbbc4d080 1         -       1       False
3312    7092    notepad.exe    0xa50bbb69a080 3         -       1       False
3824    4732    powershell.exe 0xa50bbb92d080 11        -       1       False
6448    704     Calculator.exe 0xa50bb4d0d0c0 21        -       1       False
4036    6684    firefox.exe    0xa50bbb178080 0         -       1       True
6432    4732    PowerToys.exe  0xa50bb4d5a2c0 14        -       1       False
4052    4700    PowerLauncher. 0xa50bb7fd3080 16        -       1       False
5340    6432    Microsoft.Powe 0xa50bb736f080 15        -       1       False
8564    4732    python-3.8.6-a 0xa50bb7bc2080 1         -       1       True
7124    7092    nc64.exe       0xa50bbab89080 1         -       1       False
3324    704     smartscreen.ex 0xa50bb4d6a080 7         -       1       False
7364    4732    cmd.exe        0xa50bbd8a8080 1         -       1       False
8916    2136    cmd.exe        0xa50bb78d9080 0         -       0       False
4768    8916    ipconfig.exe   0xa50bba7bd080 0         -       0       False
Здесь мы видим сами процессы и смещение их адресов в памяти. Некоторые
столбцы были опущены для экономии места. В этом списке есть несколько
интересных процессов, включая cmd и notepad, которые нам уже встречались
в выводе cmdline.
Было бы неплохо взглянуть на процессы, представленные в иерархическом
виде, чтобы понять, какие из них породили другие. Для этого воспользуемся
подключаемым модулем pstree:
PS>vol -f WinDev2007Eval-7d959ee5.vmem windows.pstree
Volatility 3 Framework 1.2.0-beta.1
Progress:   33.01               Scanning primary2 using PdbSignatureScanner
PID       PPID    ImageFileName   Offset(V)    Threads Handles SessionId Wow64
4            0      System          0xa50bba7bd080 129      N/A     False
* 556      492      services.exe    0xa50bba7bd080   8        0       False
** 2176    556      wlms.exe        0xa50bba7bd080   2        0       False
** 1796    556      svchost.exe     0xa50bba7bd080  13        0       False
