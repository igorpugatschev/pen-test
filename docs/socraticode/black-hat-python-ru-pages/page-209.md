# Black Hat Python. Программирование для хакеров и пентестеров — страница 209

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Сбор общих сведений   209
Сначала включите свою ВМ и запустите несколько процессов (например,
блокнот, калькулятор и браузер) — мы проанализируем ее память и пона-
блюдаем за тем, как эти процессы стартуют. Затем сделайте снимок с по-
мощью своего гипервизора. В папке, в которой гипервизор хранит образы
виртуальных машин, появится новый файл с расширением .vmem или .mem.
Давайте его исследуем!
Стоит отметить, что в интернете тоже можно найти множество образов па-
мяти. Один из них, который мы рассматриваем в этой главе, предоставлен
компанией PassMark Software по адресу: https://www.osforensics.com/tools/volatility-
workbench.html/. На веб-сайте V olatility Foundation тоже есть несколько образов,
с которыми можно поэкспериментировать: https://github.com/volatilityfoundation/
volatility/wiki/Memory-Samples/.
Сбор общих сведений
Соберем общие сведения об анализируемом компьютере. Подключаемый
модуль windows.info  показывает информацию об операционной системе
и ядре в нашем снимке памяти:
PS>vol -f WinDev2007Eval-Snapshot4.vmem windows.info 
Volatility 3 Framework 1.2.0-beta.1
Progress:   33.01               Scanning primary2 using PdbSignatureScanner
Variable        Value
Kernel Base     0xf80067a18000
DTB             0x1aa000
primary 0       WindowsIntel32e
memory_layer    1 FileLayer
KdVersionBlock  0xf800686272f0
Major/Minor     15.19041
MachineType     34404
KeNumberProcessors     1
SystemTime      2020-09-04 00:53:46
NtProductType   NtProductWinNt
NtMajorVersion  10
NtMinorVersion  0
PE MajorOperatingSystemVersion   10
PE MinorOperatingSystemVersion   0
PE Machine      34404
Мы указали имя файла со снимком с помощью ключа -f и нужный подклю-
чаемый модуль для Windows, windows.info . V olatility читает и анализирует
снимок памяти, выводя общую информацию о данной системе Windows. Как
