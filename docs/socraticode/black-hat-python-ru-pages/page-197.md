# Black Hat Python. Программирование для хакеров и пентестеров — страница 197

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Привилегии маркеров в Windows   197
представленные далее, в системные вызовы с помощью библиотеки ctypes.
Это возможно, но потребует намного больше усилий.
Откройте файл process_monitor.py  и добавьте следующий код непосред-
ственно над уже имеющейся функцией log_to_file:
def get_process_privileges(pid):
    try:
        hproc = win32api.OpenProcess( 
            win32con.PROCESS_QUERY_INFORMATION, False, pid
            )
        htok = win32security.OpenProcessToken(hproc, win32con.TOKEN_QUERY) 
        privs = win32security.GetTokenInformation( 
            htok,win32security.TokenPrivileges
            )
        privileges = ''
        for priv_id, flags in privs:
            if flags == (win32security.SE_PRIVILEGE_ENABLED | 
                    win32security.SE_PRIVILEGE_ENABLED_BY_DEFAULT):
                privileges += f'{win32security.LookupPrivilegeName(None,
                                 priv_id)}|' 
    except Exception:
        privileges = 'N/A'
    return privileges
Мы используем ID процесса, чтобы получить его дескриптор . Дальше берем
маркер процесса  и запрашиваем информацию о нем , отправляя структуру
win32security.TokenPrivileges. Вызов GetTokenInformation возвращает спи-
сок кортежей. Первым элементом кортежа является привилегия, а второй эле-
мент говорит о том, включена она или нет. Поскольку нас интересуют только
включенные привилегии, мы сначала проверяем биты SE_PRIVILEGE_ENABLED
и SE_PRIVILEGE_ENABLED_BY_DEFAULT , а затем сохраняем удобочитаемое на-
звание соответствующей привилегии .
Т еперь отредактируем уже имеющийся код, чтобы правильно выводить и за-
писывать эту информацию. Найдите строчку
privileges = "N/A"
и замените ее следующим кодом:
privileges = get_process_privileges(pid)
Итак, мы добавили код для отслеживания привилегий. Т еперь еще раз запу-
стим скрипт process_monitor.py и проверим его вывод. Вы должны получить
сведения о привилегиях:
