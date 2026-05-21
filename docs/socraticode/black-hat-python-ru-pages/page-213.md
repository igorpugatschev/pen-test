# Black Hat Python. Программирование для хакеров и пентестеров — страница 213

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Сбор сведений о пользователе   213
** 776     556      svchost.exe     0xa50bba7bd080  15        0       False
** 8       556      svchost.exe     0xa50bba7bd080  18        0       False
*** 4556     8      ctfmon.exe      0xa50bba7bd080  10        1       False
*** 5388   704      MicrosoftEdge.  0xa50bba7bd080  35        1       False
*** 6448   704      Calculator.exe  0xa50bba7bd080  21        1       False
*** 3324   704      smartscreen.ex  0xa50bba7bd080   7        1       False
** 2136    556      vmtoolsd.exe    0xa50bba7bd080  11        0       False
*** 8916  2136      cmd.exe         0xa50bba7bd080   0        0       False
**** 4768 8916      ipconfig.exe    0xa50bba7bd080   0        0       False
* 4704     624      userinit.exe    0xa50bba7bd080   0        1       False
** 4732   4704      explorer.exe    0xa50bba7bd080  92        1       False
*** 6432  4732      PowerToys.exe   0xa50bba7bd080  14        1       False
**** 5340 6432      Microsoft.Powe  0xa50bba7bd080  15        1       False
*** 7364  4732      cmd.exe         0xa50bba7bd080   1        -       False
**** 2464 7364      conhost.exe     0xa50bba7bd080   4        1       False
*** 7092  4732      cmd.exe         0xa50bba7bd080   1        -       False
**** 3312 7092      notepad.exe     0xa50bba7bd080   3        1       False
**** 7124 7092      nc64.exe        0xa50bba7bd080   1        1       False
*** 8564  4732      python-3.8.6-a  0xa50bba7bd080   1        1       True
**** 1036 8564      python-3.8.6-a  0xa50bba7bd080   5        1       True
Т еперь мы имеем более четкое представление о происходящем. Звездочки
в строках описывают отношения между родительскими и дочерними про-
цессами. Например, процесс userinit  (PID 4704) породил explorer.exe
(PID 4732), а тот в свою очередь — cmd.exe (PID 7092). Из cmd.exe пользо-
ватель запустил notepad.exe и еще один процесс под названием nc64.exe.
Поищем пароли с помощью подключаемого модуля hashdump:
PS> vol -f WinDev2007Eval-7d959ee5.vmem windows.hashdump
Volatility 3 Framework 1.2.0-beta.1
Progress:   33.01               Scanning primary2 using PdbSignatureScanner
User               rid     lmhash                            nthash
Administrator      500     aad3bXXXXXXaad3bXXXXXX fc6eb57eXXXXXXXXXXX657878
Guest              501     aad3bXXXXXXaad3bXXXXXX 1d6cfe0dXXXXXXXXXXXc089c0
DefaultAccount     503     aad3bXXXXXXaad3bXXXXXX 1d6cfe0dXXXXXXXXXXXc089c0
WDAGUtilityAccount 504     aad3bXXXXXXaad3bXXXXXX ed66436aXXXXXXXXXXX1bb50f
User              1001     aad3bXXXXXXaad3bXXXXXX 31d6cfe0XXXXXXXXXXXc089c0
tim               1002     aad3bXXXXXXaad3bXXXXXX afc6eb57XXXXXXXXXXX657878
admin             1003     aad3bXXXXXXaad3bXXXXXX afc6eb57XXXXXXXXXXX657878
В этом выводе показаны имена пользователей, а также LM- и NT-хеши их
паролей. Похищение хешей паролей — цель многих хакеров, которым удается
проникнуть на компьютер с Windows. Эти хеши можно взламывать отдельно
в попытке извлечь пароль жертвы или применять их в атаке вида pass-the-
hash для получения доступа к другим сетевым ресурсам. Кем бы ни была ваша
