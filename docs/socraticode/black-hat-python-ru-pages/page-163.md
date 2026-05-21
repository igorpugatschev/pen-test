# Black Hat Python. Программирование для хакеров и пентестеров — страница 163

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Создание снимков экрана   163
при использовании анализаторов трафика или кейлоггеров. К счастью, мы
можем воспользоваться пакетом pywin32 , чтобы получить снимки экрана
путем выполнения системных вызовов Windows API. У становите этот пакет
с помощью pip:
pip install pywin32
Для захвата снимков и определения таких общих свойств, как размер экрана,
используется интерфейс GDI (Graphics Device Interface — интерфейс графи-
ческого устройства), доступный в Windows. Некоторое специализированное
ПО делает снимки только текущего активного окна или приложения, но мы
будем захватывать весь экран. Приступим. Создайте файл screenshotter.py
и наберите следующий код:
import base64
import win32api
import win32con
import win32gui
import win32ui
def get_dimensions(): 
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return (width, height, left, top)
def screenshot(name='screenshot'):
    hdesktop = win32gui.GetDesktopWindow() 
    width, height, left, top = get_dimensions()
    desktop_dc = win32gui.GetWindowDC(hdesktop) 
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC() 
    screenshot = win32ui.CreateBitmap() 
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    mem_dc.BitBlt((0,0), (width, height), 
                    img_dc, (left, top), win32con.SRCCOPY)
    screenshot.SaveBitmapFile(mem_dc, f'{name}.bmp') 
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())
def run(): 
    screenshot()
    with open('screenshot.bmp') as f:
