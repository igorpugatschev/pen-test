# Black Hat Python. Программирование для хакеров и пентестеров — страница 142

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

142   Глава 6. Расширение прокси Burp Proxy
    for traffic in http_traffic:
        http_service = traffic.getHttpService()
        host         = http_service.getHost()
        self.hosts.add(host) 
        http_response = traffic.getResponse()
        if http_response:
            self.get_words(http_response) 
    self.display_wordlist()
    return
    def get_words(self, http_response):
        headers, body = http_response.tostring().split('\r\n\r\n', 1)
        # пропускаем нетекстовые ответы
        if headers.lower().find("content-type: text") == -1: 
            return
        tag_stripper = TagStripper()
        page_text = tag_stripper.strip(body) 
        words = re.findall("[a-zA-Z]\w{2,}", page_text) 
        for word in words:
            # filter out long strings
            if len(word) <= 12:
                self.wordlist.add(word.lower()) 
        return
Первым делом определяем метод wordlist_menu , который обрабатывает
выбор пунктов меню. Он сохраняет имя ответившего хоста  для дальней-
шего использования, затем извлекает HTTP-ответ и передает его методу
get_words . После этого get_words проверяет заголовок ответа — если ответ
не текстовый, его не нужно обрабатывать . Класс TagStripper   убирает
HTML-код из оставшегося текста страницы. Мы используем регулярное
выражение \w{2,} , чтобы найти все слова, которые начинаются с алфа-
витных символов и содержат не меньше двух букв. Слова, соответствующие
этому шаблону , переводятся в нижний регистр и сохраняются в wordlist .
Т еперь дополним наш скрипт так, чтобы он мог отображать сформированный
словарь и видоизменять его содержимое:
def mangle(self, word):
    year = datetime.now().year
