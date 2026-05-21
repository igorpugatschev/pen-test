# Black Hat Python. Программирование для хакеров и пентестеров — страница 222

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

222   Глава 11. Методы компьютерно-технической экспертизы в арсенале хакера
Мы получаем список процессов с помощью подключаемого модуля pslist 
и возвращаем данные из генератора, используя метод представления
TreeGrid . Метод TreeGrid применяется во многих подключаемых моду-
лях, позволяя выводить ровно по одной строчке с результатами для каждого
проанализированного процесса.
Проверка написанного
Проанализируем один из образов, доступных на сайте V olatility , — Malware —
Cridex. Передайте своему подключаемому модулю ключ -p с путем к своей
папке plugins:
PS>vol -p .\plugins\windows -f cridex.vmem aslrcheck.AslrCheck
Volatility 3 Framework 1.2.0-beta.1
Progress:    0.00               Scanning primary2 using PdbSignatureScanner
PID     Filename        Base    ASLR
368     smss.exe        0x48580000       False
584     csrss.exe       0x4a680000       False
608     winlogon.exe    0x1000000        False
652     services.exe    0x1000000        False
664     lsass.exe       0x1000000        False
824     svchost.exe     0x1000000        False
1484    explorer.exe    0x1000000        False
1512    spoolsv.exe     0x1000000        False
1640    reader_sl.exe   0x400000         False
788     alg.exe         0x1000000        False
1136    wuauclt.exe     0x400000         False
Как видите, это система Windows XP и ни один из процессов не защищен
с помощью ASLR.
А далее показан результат для Windows 10 сразу после установки и со всеми
обновлениями:
PS>vol -p .\plugins\windows -f WinDev2007Eval-Snapshot4.vmem aslrcheck.AslrCheck
Volatility 3 Framework 1.2.0-beta.1
Progress:   33.01               Scanning primary2 using PdbSignatureScanner
PID     Filename        Base    ASLR
316     smss.exe        0x7ff668020000 True
428     csrss.exe       0x7ff796c00000 True
500     wininit.exe     0x7ff7d9bc0000 True
568     winlogon.exe    0x7ff6d7e50000 True
592     services.exe    0x7ff76d450000 True
600     lsass.exe       0x7ff6f8320000 True
696     fontdrvhost.ex  0x7ff65ce30000 True
