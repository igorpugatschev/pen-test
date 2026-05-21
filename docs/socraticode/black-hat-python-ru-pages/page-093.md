# Black Hat Python. Программирование для хакеров и пентестеров — страница 93

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Анализ данных в формате pcap   93
М ы используем синтаксис срезов, поддерживаемый языком Python , для
преобразования этих данных из одного формата в другой. То есть превра-
щаем rect непосредственно в координаты (x1, y1, x1+width,  y1+height)
или (x1, y1, x2, y2). Именно этот формат ожидает получить на вход метод
cv2.rectangle.
Этот код был великодушно опубликован Крисом Фидэо на странице http://
www.fideloper.com/facial-detection/. Мы внесли в него небольшие изменения. Т е-
перь проверим все это в работе на вашей виртуальной машине Kali.
Проверка написанного
Если вы еще не установили библиотеки OpenCV , выполните в терминале
виртуальной машины Kali следующие команды (опять же спасибо Крису
Фидэо):
#:> apt-get install libopencv-dev python3-opencv python3-numpy python3-scipy
В результате должны быть установлены все файлы, необходимые для обна-
ружения лиц в извлеченных изображениях. Нам также нужно взять файл
с результатами обучения:
#:> wget http://eclecti.cc/files/2008/03/haarcascade_frontalface_alt.xml
Скопируйте скачанный файл в каталог, который мы указали с помощью пере-
менной TRAIN в файле detector.py. Т еперь создайте несколько каталогов для
вывода изображений, скопируйте pcap-файл и запустите наши скрипты. Это
должно выглядеть примерно так:
#:> mkdir /root/Desktop/pictures
#:> mkdir /root/Desktop/faces
#:> python recapper.py
Extracted: 189 images
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--------------xx
Writing pictures/ex_2.gif
Writing pictures/ex_8.jpeg
Writing pictures/ex_9.jpeg
Writing pictures/ex_15.png
...
#:> python detector.py
Got a face
Got a face
...
#:>
