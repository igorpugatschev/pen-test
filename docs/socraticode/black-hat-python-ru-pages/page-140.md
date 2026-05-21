# Black Hat Python. Программирование для хакеров и пентестеров — страница 140

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

140   Глава 6. Расширение прокси Burp Proxy
аналогичный тому , который был описан в предыдущей главе, может привести
к получению доступа к сайту .
Ключевым аспектом подбора паролей является использование подходящего
словаря. Если вы спешите, у вас нет возможности проверить 10 млн паро-
лей, поэтому вы должны быть способны создать список, ориентированный
на интересующий сайт. Конечно, в Kali Linux есть скрипты, которые могут
пройтись по веб-сайту и сгенерировать словарь на основе его содержимого. Но
раз уж мы применяем Burp для сканирования, зачем слать дополнительный
трафик лишь для того, чтобы сгенерировать список слов? К тому же у этих
скриптов есть громадное количество аргументов командной строки, которые
нужно помнить. Мы, к примеру , уже заучили достаточно аргументов, чтобы
впечатлить друзей, поэтому со спокойной душой можем переложить всю
тяжелую работу на Burp.
Создайте файл bhp_wordlist.py и наберите следующий код:
from burp import IBurpExtender
from burp import IContextMenuFactory
from java.util import ArrayList
from javax.swing import JMenuItem
from datetime import datetime
from HTMLParser import HTMLParser
import re
class TagStripper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.page_text = []
    def handle_data(self, data):
        self.page_text.append(data) 
    def handle_comment(self, data):
        self.page_text.append(data) 
    def strip(self, html):
        self.feed(html)
        return " ".join(self.page_text) 
class BurpExtender(IBurpExtender, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers   = callbacks.getHelpers()
