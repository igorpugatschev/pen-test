# Black Hat Python. Программирование для хакеров и пентестеров — страница 211

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Сбор сведений о пользователе   211
Сбор сведений о пользователе
Давайте соберем информацию о пользователе ВМ. Подключаемый модуль
cmdline выводит аргументы командной строки каждого процесса, который
был запущен в момент создания снимка. Это поможет нам лучше понять по-
ведение и намерения пользователя:
PS>vol -f WinDev2007Eval-7d959ee5.vmem windows.cmdline
Volatility 3 Framework 1.2.0-beta.1
Progress:   33.01               Scanning primary2 using PdbSignatureScanner
PID     Process Args
72      Registry        Required memory at 0x20 is not valid (process exited?)
340     smss.exe        Required memory at 0xa5f1873020 is inaccessible (swapped)
564     lsass.exe       C:\Windows\system32\lsass.exe
624     winlogon.exe    winlogon.exe
2160    MsMpEng.exe     "C:\ProgramData\Microsoft\Windows Defender\
                        platform\4.18.2008.9-0\MsMpEng.exe"
4732    explorer.exe    C:\Windows\Explorer.EXE
4848    svchost.exe     C:\Windows\system32\svchost.exe -k ClipboardSvcGroup -p
4920    dllhost.exe     C:\Windows\system32\DllHost.exe /Processid:{AB8902B4-09CA-
                        4BB6-B78DA8F59079A8D5}
5084    StartMenuExper  "C:\Windows\SystemApps\Microsoft.Windows. . ."
5388    MicrosoftEdge.  "C:\Windows\SystemApps\Microsoft.MicrosoftEdge_. . ."
6452    OneDrive.exe    "C:\Users\Administrator\AppData\Local\Microsoft\OneDrive\
                        OneDrive.exe"
/background
6484    FreeDesktopClo  "C:\Program Files\Free Desktop Clock\FreeDesktopClock.exe"
7092    cmd.exe         "C:\Windows\system32\cmd.exe" 
3312    notepad.exe     notepad 
3824    powershell.exe  "C:\Windows\System32\WindowsPowerShell\v1.0\
                        powershell.exe"
6448    Calculator.exe  "C:\Program Files\WindowsApps\
                        Microsoft.WindowsCalculator_. . ."
6684    firefox.exe     "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
6432    PowerToys.exe   "C:\Program Files\PowerToys\PowerToys.exe"
7124    nc64.exe        Required memory at 0x2d7020 is inaccessible (swapped)
3324    smartscreen.ex  C:\Windows\System32\smartscreen.exe -Embedding
4768    ipconfig.exe    Required memory at 0x840308e020 is not valid
                        (process exited?)
В этом списке перечислены ID процессов, их названия и аргументы, с ко-
торыми они были запущены. Как видите, большинство процессов были за-
пущены самой системой, скорее всего, во время загрузки. А вот cmd.exe 
и note pad.exe  — это типичные процессы, которые запускает пользователь.
