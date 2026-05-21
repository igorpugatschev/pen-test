# Black Hat Python. Программирование для хакеров и пентестеров — страница 136

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

136   Глава 6. Расширение прокси Burp Proxy
Метод bing_menu срабатывает, когда пользователь щелкает на пункте кон-
текстного меню, который мы определили. Мы извлекаем выделенные HTTP-
запросы , затем получаем адрес сервера каждого из них и передаем его
методу bing_search для дальнейшей обработки. Метод bing_search сначала
определяет, что представляет собой адрес сервера — IP или сетевое имя .
После этого он ищет в Bing все виртуальные хосты с тем же IP-адресом ,
что и у заданного сервера. Если наше расширение также получило доменное
имя, мы дополнительно ищем любые поддомены, которые могли попасть
в индекс Bing .
Т еперь напишем бизнес-логику , необходимую для отправки запросов системе
Bing и разбора результатов с помощью HTTP API из состава Burp. Добавьте
в класс BurpExtender следующий код:
def bing_query(self,bing_query_string):
    print('Performing Bing search: %s' % bing_query_string)
    http_request = 'GET https://%s/bing/v7.0/search?' % API_HOST
    # кодируем наш запрос
    http_request += 'q=%s HTTP/1.1\r\n' % urllib.quote(bing_query_string)
    http_request += 'Host: %s\r\n' % API_HOST
    http_request += 'Connection:close\r\n'
    http_request += 'Ocp-Apim-Subscription-Key: %s\r\n' % API_KEY 
    http_request += 'User-Agent: Black Hat Python\r\n\r\n'
    json_body = self._callbacks.makeHttpRequest(
          API_HOST, 443, True, http_request).tostring()
    json_body = json_body.split('\r\n\r\n', 1)[1] 
    try:
        response = json.loads(json_body) 
    except (TypeError, ValueError) as err:
        print('No results from Bing: %s' % err)
    else:
        sites = list()
        if response.get('webPages'):
            sites = response['webPages']['value']
        if len(sites):
            for site in sites:
                print('*'*100) 
                print('Name: %s       ' % site['name'])
                print('URL: %s        ' % site['url'])
                print('Description: %r' % site['snippet'])
                print('*'*100)
                java_url = URL(site['url'])
                if not self._callbacks.isInScope(java_url): 
                    print('Adding %s to Burp scope' % site['url'])
                    self._callbacks.includeInScope(java_url)
