# Black Hat Python. Программирование для хакеров и пентестеров — страница 223

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Пользовательские подключаемые модули для Volatility   223
728     svchost.exe     0x7ff78eed0000 True
Volatility was unable to read a requested page:
Page error 0x7ff65f4d0000 in layer primary2_Process928 (Page Fault at entry
0xd40c9d88c8a00400 in page entry)
 * Memory smear during acquisition (try re-acquiring if possible)
 * An intentionally invalid page lookup (operating system protection)
 * A bug in the plugin/volatility (re-run with -vvv and file a bug)
No further results will be produced
Здесь не так уж много полезной информации. Каждый процесс защищен с по-
мощью ASLR. Но тут также наблюдается модификация данных, выполненная
в момент создания образа памяти. В результате содержимое таблицы памяти
не совпадает с самой памятью или же указатели в виртуальной памяти могут
ссылаться не на те данные. Хакерство — непростое занятие. Как отмечается
в описании ошибки, вы можете попытаться повторно получить образ памяти
(найти или создать новый снимок).
Проанализируем демонстрационный образ PassMark Windows 10:
PS>vol -p .\plugins\windows -f WinDump.mem aslrcheck.AslrCheck
Volatility 3 Framework 1.2.0-beta.1
Progress:    0.00               Scanning primary2 using PdbSignatureScanner
PID     Filename        Base    ASLR
356     smss.exe        0x7ff6abfc0000 True
2688    MsMpEng.exe     0x7ff799490000 True
2800    SecurityHealth  0x7ff6ef1e0000 True
5932    GoogleCrashHan  0xed0000       True
5380    SearchIndexer.  0x7ff6756e0000 True
3376    winlogon.exe    0x7ff65ec50000 True
6976    dwm.exe         0x7ff6ddc80000 True
9336    atieclxx.exe    0x7ff7bbc30000 True
9932    remsh.exe       0x7ff736d40000 True
2192    SynTPEnh.exe    0x140000000    False
7688    explorer.exe    0x7ff7e7050000 True
7736    SynTPHelper.ex  0x7ff7782e0000 True
Почти все процессы защищены. Защиты ASLR нет только у SynTPEnh.exe .
Поиск в интернете показывает, что это программный компонент устройства
Synaptics Pointing Device, которое, наверное, предназначено для сенсорного
экрана. Если он установлен в C:\Program Files, с ним, скорее всего, все в по-
рядке, но, возможно, его стоит отложить на потом для проверки методом
фаззинга.
