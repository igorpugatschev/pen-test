# Black Hat Python. Программирование для хакеров и пентестеров — страница 134

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

134   Глава 6. Расширение прокси Burp Proxy
дурным тоном (и к тому же нарушением условий применения большинства
поисковых систем). Чтобы избежать неприятностей, отправим эти запросы
программным образом с помощью Bing API и проанализируем результаты
самостоятельно (чтобы получить бесплатный ключ для Bing API, посетите
страницу https://www.microsoft.com/en-us/bing/apis/bing-web-search-api/ ). В этом
расширении мы не станем реализовывать никаких вычурных элементов гра-
фического интерфейса Burp, если не считать контекстного меню, — просто
будем выводить результаты в консоль Burp при выполнении каждого запро-
са, а любые обнаруженные URL-адреса будут автоматически добавляться
в целевую область Burp.
Мы уже обсуждали, как обращаться с документацией API Burp и переводить
ее в код на языке Python, поэтому сразу приступим к программированию.
Создайте файл bhp_bing.py и наберите следующее:
from burp import IBurpExtender
from burp import IContextMenuFactory
from java.net import URL
from java.util import ArrayList
from javax.swing import JMenuItem
from thread import start_new_thread
import json
import socket
import urllib
API_KEY = "ВАШ_КЛЮЧ" 
API_HOST = 'api.cognitive.microsoft.com'
class BurpExtender(IBurpExtender, IContextMenuFactory): 
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self.context = None
        # подготавливаем наше расширение
        callbacks.setExtensionName("BHP Bing")
        callbacks.registerContextMenuFactory(self) 
        return
    def createMenuItems(self, context_menu):
        self.context = context_menu
        menu_list = ArrayList()
        menu_list.add(JMenuItem(
            "Send to Bing", actionPerformed=self.bing_menu))
        return menu_list
