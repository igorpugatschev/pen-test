# Black Hat Python. Программирование для хакеров и пентестеров — страница 168

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

168   Глава 8. Распространенные троянские задачи в Windows
и сравним его с тем, когда этот компьютер был включен, — это должно стать
хорошим индикатором того, находимся ли мы в виртуальном окружении.
Затем мы можем принять решение о том, стоит ли продолжать выполнение.
Вначале напишем код для обнаружения виртуальных сред. Создайте файл
sandbox_detect.py и наберите следующее:
from ctypes import byref, c_uint, c_ulong, sizeof, Structure, windll
import random
import sys
import time
import win32api
class LASTINPUTINFO(Structure):
    fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_ulong)
    ]
def get_last_input():
    struct_lastinputinfo = LASTINPUTINFO()
    struct_lastinputinfo.cbSize = sizeof(LASTINPUTINFO) 
    windll.user32.GetLastInputInfo(byref(struct_lastinputinfo))
    run_time = windll.kernel32.GetTickCount() 
    elapsed = run_time - struct_lastinputinfo.dwTime
    print(f"[*] It's been {elapsed} milliseconds since the last event.")
    return elapsed
while True: 
    get_last_input()
    time.sleep(1)
Мы импортировали необходимые модули и создали структуру LASTINPUTINFO
для хранения временной метки (в миллисекундах), обозначающей момент
обнаружения последнего события ввода в системе. Дальше создаем функ-
цию get_last_input, чтобы, собственно, определить этот момент. Обратите
внимание на то, что прежде чем выполнять вызов, переменную cbSize  
нужно инициализировать с использованием размера структуры. Затем мы
вызываем функцию GetLastInputInfo , которая присваивает полю struct_
lastinputinfo.dwTime временную метку . Следующий шаг состоит в опреде-
лении того, как долго проработала система. Для этого применяется вызов
функции GetTickCount . Переменная elapsed должна быть равна разности
между временем работы системы и временем последнего ввода. Небольшой
фрагмент кода, размещенный в конце , позволяет выполнить простую про-
верку; чтобы увидеть его в действии, запустите скрипт и подвигайте мышью
или нажмите клавишу на клавиатуре.
