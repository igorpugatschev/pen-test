# Black Hat Python. Программирование для хакеров и пентестеров — страница 190

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

190   Глава 10. Повышение привилегий в Windows
Создание уязвимой хакерской службы
Создаваемая нами служба имитирует ряд уязвимостей, которые часто встре-
чаются в крупных корпоративных сетях. Позже в этой главе мы ее атакуем.
Эта служба будет периодически копировать скрипт во временную папку
и запускать его оттуда. Для начала создайте файл bhservice.py:
import os
import servicemanager
import shutil
import subprocess
import sys
import win32event
import win32service
import win32serviceutil
SRCDIR = 'C:\\Users\\tim\\work'
TGTDIR = 'C:\\Windows\\TEMP'
Здесь мы выполняем импорт, устанавливаем исходный каталог для файла
скрипта и затем выбираем целевой каталог, из которого он будет запущен
службой. Т еперь создадим саму службу в виде класса:
class BHServerSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "BlackHatService"
    _svc_display_name_ = "Black Hat Service"
    _svc_description_ = ("Executes VBScripts at regular intervals." +
                            " What could possibly go wrong?")
    def __init__(self,args): 
        self.vbs = os.path.join(TGTDIR, 'bhservice_task.vbs')
        self.timeout = 1000 * 60
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
    def SvcStop(self): 
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
    def SvcDoRun(self): 
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()
Это каркас тех функций, которые должна предоставлять любая служба. Дан-
ный класс наследует win32serviceutil.ServiceFramework и определяет три
