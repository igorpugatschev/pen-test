# Black Hat Python. Программирование для хакеров и пентестеров — страница 135

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Использование Bing в сочетании с Burp   135
Это первая часть расширения для работы с Bing. Не забудьте подставить свой
ключ для Bing API в . У вас есть возможность выполнять 1000 бесплатных
запросов в месяц. Мы начинаем с  класса BurpExtender  , реализующего
стандартные интерфейсы IBurpExtender и IContextMenuFactory, последний
позволит нам показывать контекстное меню при щелчке правой клавишей
мыши на запросе в Burp. Это меню будет содержать пункт Send to Bing (От -
править в Bing). Мы регистрируем обработчик , который будет определять,
на каком сайте щелкнул пользователь, позволяя нам формировать запросы
к Bing. Затем мы создаем метод createMenuItem, который принимает объект
IContextMenuInvocation и определяет с его помощью, какой HTTP-запрос вы -
брал пользователь. Напоследок мы отображаем пункт меню и обрабатываем
событие щелчка с помощью метода bing_menu .
Т еперь давайте выполним запрос к Bing, выведем результаты и добавим любые
обнаруженные виртуальные хосты в целевую область Burp:
def bing_menu(self,event):
    # извлекаем подробности о том, по чему щелкнул пользователь
    http_traffic = self.context.getSelectedMessages() 
    print("%d requests highlighted" % len(http_traffic))
    for traffic in http_traffic:
        http_service = traffic.getHttpService()
        host         = http_service.getHost()
        print("User selected host: %s" % host)
        self.bing_search(host)
    return
def bing_search(self,host):
    # проверяем, что нам передали: IP или сетевое имя
    try:
        is_ip = bool(socket.inet_aton(host)) 
    except socket.error:
        is_ip = False
    if is_ip:
        ip_address = host
        domain = False
    else:
        ip_address = socket.gethostbyname(host)
        domain = True
    start_new_thread(self.bing_query, ('ip:%s' % ip_address,)) 
    if domain:
        start_new_thread(self.bing_query, ('domain:%s' % host,)) 
