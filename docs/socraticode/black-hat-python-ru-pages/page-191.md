# Black Hat Python. Программирование для хакеров и пентестеров — страница 191

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Создание уязвимой хакерской службы   191
метода. В методе __init__ мы инициализируем ServiceFramework, определяем
местоположение скрипта, который нужно запустить, устанавливаем время
ожидания длиной в 1 минуту и создаем объект события . В методе SvcStop
указываем состояние службы и останавливаем его выполнение . В методе
SvcDoRun запускаем службу и вызываем метод main, в котором будут работать
наши задания . Метод main имеет следующий вид:
def main(self):
    while True: 
        ret_code = win32event.WaitForSingleObject(
        self.hWaitStop, self.timeout)
        if ret_code == win32event.WAIT_OBJECT_0: 
            servicemanager.LogInfoMsg("Service is stopping")
            break
        src = os.path.join(SRCDIR, 'bhservice_task.vbs')
        shutil.copy(src, self.vbs)
        subprocess.call("cscript.exe %s" % self.vbs, shell=False) 
        os.unlink(self.vbs)
Здесь мы инициируем цикл , который выполняется раз в минуту (в соот-
ветствии с параметром self.timeout), пока служба не получит сигнал оста-
новки . В ходе выполнения копируем скрипт в целевой каталог, выполняем
его и удаляем файл .
В главном блоке мы обрабатываем все аргументы командной строки:
if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(BHServerSvc)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(BHServerSvc)
Иногда на компьютере жертвы необходимо создать настоящую службу . Дан-
ный каркас в общих чертах иллюстрирует ее структуру .
По адресу https://nostarch.com/black-hat-python2E/  можно найти скрипт bhservice_
tasks.vbs. Скопируйте его в папку , в которой находится файл bhservice.py,
и присвойте путь к ней переменой SRCDIR. Ваша папка должна выглядеть
так:
06/22/2020 09:02 AM     <DIR>             .
06/22/2020 09:02 AM     <DIR>             ..
06/22/2020 11:26 AM                 2,099  bhservice.py
06/22/2020 11:08 AM                 2,501  bhservice_task.vbs
