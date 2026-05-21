# Black Hat Python. Программирование для хакеров и пентестеров — страница 220

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

220   Глава 11. Методы компьютерно-технической экспертизы в арсенале хакера
        filter_list = [x for x in pid_list if x is not None]
        if filter_list:
            filter_func = lambda x: x.UniqueProcessId not in filter_list
        return filter_func
Для обработки дополнительного ID процесса используется метод класса,
который создает функцию фильтрации, а она возвращает False  для всех
ID, находящихся в списке. То есть функция фильтрации определяет, будет
ли процесс отфильтрован (отброшен), поэтому мы возвращаем True только
в случае, если PID нет в списке:
def _generator(self, procs):
    pe_table_name = intermed.IntermediateSymbolTable.create( 
        self.context,
        self.config_path,
        "windows",
        "pe",
        class_types=extensions.pe.class_types)
    procnames = list()
    for proc in procs:
        procname = proc.ImageFileName.cast("string",
            max_length=proc.ImageFileName.vol.count, errors='replace')
        if procname in procnames:
            continue
        procnames.append(procname)
        proc_id = "Unknown"
        try:
            proc_id = proc.UniqueProcessId
            proc_layer_name = proc.add_process_layer()
        except exceptions.InvalidAddressException as e:
            vollog.error(f"Process {proc_id}: invalid address {e}
              in layer {e.layer_name}")
            continue
        peb = self.context.object( 
                self.config['nt_symbols'] + constants.BANG + "_PEB",
                layer_name = proc_layer_name,
                offset = proc.Peb)
        try:
            dos_header = self.context.object(
                    pe_table_name + constants.BANG + "_IMAGE_DOS_HEADER",
                    offset=peb.ImageBaseAddress,
                    layer_name=proc_layer_name)
        except Exception as e:
            continue
