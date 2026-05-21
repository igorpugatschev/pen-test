# Black Hat Python. Программирование для хакеров и пентестеров — страница 91

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Анализ данных в формате pcap   91
(скорее всего, из-за отсутствия ключа TCP в packet) 1 , мы выведем в консоль x
и продолжим работу .
Если после того как мы заново собрали воедино HTTP-данные, байтовая
строка payload не пустая, передаем ее функции get_header , которая по-
зволяет анализировать HTTP-заголовки по отдельности. Дальше добавляем
Response в список responses .
Наконец, мы перебираем список ответов в поиске изображения и, если оно
найдено, записываем его на диск с помощью метода write:
def write(self, content_name):
    for i, response in enumerate(self.responses): 
        content, content_type = extract_content(response, content_name) 
        if content and content_type:
            fname = os.path.join(OUTDIR, f'ex_{i}.{content_type}')
            print(f'Writing {fname}')
            with open(fname, 'wb') as f:
                f.write(content) 
После получения нужных ответов методу write останется только пройтись
по ним , извлечь их содержимое  и записать его в файл . Файлы соз -
даются в выходном каталоге, а их имена формируются с помощью счетчика
из встроенной функции enumerate  и значения content_type . Например,
изображение может иметь название ex_2.jpg. При запуске программы мы
создаем объект Recapper, вызываем метод get_responses , чтобы найти все
ответы в pcap-файле, и затем записываем изображения, извлеченные из этих
ответов, на диск.
В следующей программе проанализируем все изображения и определим, со-
держат ли они человеческие лица. Каждое подходящее изображение будет
скопировано в новый файл на диске с добавлением рамки вокруг лица. Соз-
дайте файл с именем detector.py:
import cv2
import os
ROOT = '/root/Desktop/pictures'
FACES = '/root/Desktop/faces'
TRAIN = '/root/Desktop/training'
def detect(srcdir=ROOT, tgtdir=FACES, train_dir=TRAIN):
    for fname in os.listdir(srcdir):
1  Если ключа TCP нет, будет сгенерировано исключение IndexError. — Здесь и далее при-
меч. пер.
