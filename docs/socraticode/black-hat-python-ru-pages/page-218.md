# Black Hat Python. Программирование для хакеров и пентестеров — страница 218

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

218   Глава 11. Методы компьютерно-технической экспертизы в арсенале хакера
# Ищем все процессы и проверяем наличие защиты ASLR
#
from typing import Callable, List
from volatility.framework import constants, exceptions, interfaces, renderers
from volatility.framework.configuration import requirements
from volatility.framework.renderers import format_hints
from volatility.framework.symbols import intermed
from volatility.framework.symbols.windows import extensions
from volatility.plugins.windows import pslist
import io
import logging
import os
import pefile
vollog = logging.getLogger(__name__)
IMAGE_DLL_CHARACTERISTICS_DYNAMIC_BASE = 0x0040
IMAGE_FILE_RELOCS_STRIPPED = 0x0001
Вначале импортируем нужные нам пакеты и библиотеку pefile для анализа
файлов в формате PE (Portable Executable — переносимый исполняемый
файл). Т еперь напишем вспомогательную функцию для проведения анализа:
def check_aslr(pe): 
    pe.parse_data_directories([
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG']
    ])
    dynamic = False
    stripped = False
    if (pe.OPTIONAL_HEADER.DllCharacteristics & 
        IMAGE_DLL_CHARACTERISTICS_DYNAMIC_BASE):
        dynamic = True
    if pe.FILE_HEADER.Characteristics & IMAGE_FILE_RELOCS_STRIPPED: 
        stripped = True
    if not dynamic or (dynamic and stripped): 
        aslr = False
    else:
        aslr = True
    return aslr
Мы передаем объект PE-файла функции check_aslr , разбираем его и смо-
трим, был ли он скомпилирован с параметром /DYNAMICBASE   и была ли
удалена из файла информация о перемещении адресов . Если PE-файл
не является динамическим или не содержит данных о переносе адресов, это
означает, что он не защищен с помощью ASLR .
