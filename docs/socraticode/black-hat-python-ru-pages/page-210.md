# Black Hat Python. Программирование для хакеров и пентестеров — страница 210

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

210   Глава 11. Методы компьютерно-технической экспертизы в арсенале хакера
видите, мы имеем дело с ВМ под управлением Windows 10.0, у которой есть
один процессор и один слой памяти.
Можете в образовательных целях применить к образу памяти несколько
подключаемых модулей, одновременно анализируя их код. Чтение кода
и сопоставление его с соответствующим выводом покажет вам, как этот
код должен работать, и раскроет общий образ мышления тех, кто отвечает
за безопасность.
Дальше, воспользовавшись подключаемым модулем registry.printkey, мы
можем вывести значения ключа в реестре. В реестре Windows имеется множе -
ство ценной информации, и V olatility позволяет найти любое значение, кото -
рое вас интересует. Здесь мы ищем установленные службы. Эта информация
находится по ключу /ControlSet001/Services , который принадлежит базе
данных диспетчера управления службами (Service Control Manager, SCM):
PS>vol -f WinDev2007Eval-7d959ee5.vmem windows.registry.printkey
       --key 'ControlSet001\Services'
Volatility 3 Framework 1.2.0-beta.1
Progress:   33.01               Scanning primary2 using PdbSignatureScanner
... Key                                         Name    Data       Volatile
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services .NET CLR Data      False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services Appinfo            False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services applockerfltr      False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services AtomicAlarmClock   False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services Beep               False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services fastfat            False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services MozillaMaintenance False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services NTDS               False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services Ntfs               False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services ShellHWDetection   False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services SQLWriter          False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services Tcpip              False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services Tcpip6             False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services terminpt           False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services W32Time            False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services WaaSMedicSvc       False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services WacomPen           False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services Winsock            False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services WinSock2           False
\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services WINUSB             False
Этот вывод содержит список всех служб, установленных в системе (мы его
сократили для экономии места).
