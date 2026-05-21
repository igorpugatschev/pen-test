# Black Hat Python. Программирование для хакеров и пентестеров — страница 219

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Пользовательские подключаемые модули для Volatility   219
Подготовив функцию check_aslr, можем создать класс AslrCheck:
class AslrCheck(interfaces.plugins.PluginInterface): 
    @classmethod
    def get_requirements(cls):
        return [
            requirements.TranslationLayerRequirement( 
                name='primary', description='Memory layer for the kernel',
                architectures=["Intel32", "Intel64"]),
                requirements.SymbolTableRequirement(
                name="nt_symbols", description="Windows kernel symbols"),
            requirements.PluginRequirement( 
                name='pslist', plugin=pslist.PsList, version=(1, 0, 0)),
            requirements.ListRequirement(name = 'pid', 
                element_type = int,
                description = "Process ID to include (all others are excluded)",
                optional = True),
                ]
Первое, что необходимо сделать при создании подключаемого модуля, — это
унаследовать класс PluginInterface . Дальше определяются требования;
чтобы хорошо сориентироваться в том, какие из них вам нужны, можно
просмотреть другие подключаемые модули. Каждому модулю нужен слой
памяти, и мы указываем это требование первым . Помимо этого нам также
нужны таблицы символов . Эти два требования можно встретить почти
у всех подключаемых модулей.
В качестве еще одного требования нам понадобится подключаемый модуль
pslist, который позволит получить все процессы, находящиеся в памяти,
и воссоздать из них PE-файлы . Затем мы возьмем каждый из этих файлов
и проанализируем его на предмет защиты ASLR.
Возможно, нам захочется проверить отдельно взятый процесс с заданным ID,
поэтому создадим еще один дополнительный параметр, в котором сможем
передать список идентификаторов, чтобы ограничить проверку соответству-
ющими процессами :
    @classmethod
    def create_pid_filter(cls, pid_list: List[int] = None) ->
        Callable[[interfaces.objects.ObjectInterface], bool]:
        filter_func = lambda _: False
        pid_list = pid_list or []
