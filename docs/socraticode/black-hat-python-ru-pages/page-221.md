# Black Hat Python. Программирование для хакеров и пентестеров — страница 221

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Пользовательские подключаемые модули для Volatility   221
        pe_data = io.BytesIO()
        for offset, data in dos_header.reconstruct():
            pe_data.seek(offset)
            pe_data.write(data)
        pe_data_raw = pe_data.getvalue() 
        pe_data.close()
        try:
            pe = pefile.PE(data=pe_data_raw) 
        except Exception as e:
            continue
        aslr = check_aslr(pe) 
        yield (0, (proc_id, 
                   procname,
                   format_hints.Hex(pe.OPTIONAL_HEADER.ImageBase),
                   aslr,
                   ))
Мы создаем специальную структуру данных под названием pe_table_name ,
которая используется при обходе каждого процесса, загруженного в память.
Затем берем блок операционного окружения процесса (Process Environment
Block, PEB), представляющий собой особый регион памяти, и сохраняем его
в объект . PEB  — это структура данных, содержащая множество полезных
данных о текущем процессе. Мы записываем этот регион памяти в файло-
подобный объект (pe_data) , создаем объект PE с помощью библиотеки
pefile  и передаем его вспомогательному методу check_aslr . В заверше-
ние возвращаем с помощью ключевого слова yield кортеж с ID и названием
процесса, адресом, по которому он размещен в памяти, а также логическим
результатом проверки на наличие защиты ASLR .
Т еперь создадим метод run, которому не нужно никаких аргументов, так как
все параметры указаны в объекте config:
def run(self):
    procs = pslist.PsList.list_processes(self.context, 
                                         self.config["primary"],
                                         self.config["nt_symbols"],
                                         filter_func =
            self.create_pid_filter(self.config.get('pid', None)))
    return renderers.TreeGrid([ 
        ("PID", int),
        ("Filename", str),
        ("Base", format_hints.Hex),
        ("ASLR", bool)],
        self._generator(procs))
