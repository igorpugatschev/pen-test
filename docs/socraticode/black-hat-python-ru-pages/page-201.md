# Black Hat Python. Программирование для хакеров и пентестеров — страница 201

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Наперегонки с чужим кодом   201
                    print(f'[>] Renamed from {full_filename}')
                elif action == FILE_RENAMED_TO:
                    print(f'[<] Renamed to {full_filename}')
                else:
                    print(f'[?] Unknown action on {full_filename}')
        except Exception:
            pass
if __name__ == '__main__':
    for path in PATHS:
        monitor_thread = threading.Thread(target=monitor, args=(path,))
        monitor_thread.start()
Мы создаем список каталогов, которые хотим отслеживать , — в нашем
случае это две широко используемые папки для временных файлов. Если вам
захочется понаблюдать за другими местами, можете отредактировать этот
список по своему усмотрению.
Для каждого из этих путей мы создаем поток мониторинга, который вы-
зывает функцию start_monitor . Вначале она пытается получить дескрип-
тор каталога, за которым мы хотим следить . Затем вызывается функция
ReadDirectoryChangesW , которая уведомляет нас о вносимых изменениях.
Мы получаем имя измененного файла и тип произошедшего события . Даль-
ше выводим полезную информацию о том, что случилось с этим конкретным
файлом, и если обнаружилось, что он изменен, отображаем для наглядности
все его содержимое .
Проверка написанного
Откройте командную оболочку cmd.exe и запустите file_monitor.py:
C:\Users\tim\work> python.exe file_monitor.py
Откройте вторую командную оболочку cmd.exe  и выполните следующие
команды:
C:\Users\tim\work> cd C:\Windows\temp
C:\Windows\Temp> echo hello > filetest.bat
C:\Windows\Temp> rename filetest.bat file2test
C:\Windows\Temp> del file2test
Вы должны увидеть приблизительно такой вывод:
[+] Created c:\WINDOWS\Temp\filetest.bat
[*] Modified c:\WINDOWS\Temp\filetest.bat
[vvv] Dumping contents ...
