# Black Hat Python. Программирование для хакеров и пентестеров — страница 92

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

92   Глава 4. Захват сети с помощью Scapy
        if not fname.upper().endswith('.JPG'): 
            continue
        fullname = os.path.join(srcdir, fname)
        newname = os.path.join(tgtdir, fname)
        img = cv2.imread(fullname) 
        if img is None:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        training = os.path.join(train_dir,
            'haarcascade_frontalface_alt.xml')
        cascade = cv2.CascadeClassifier(training) 
        rects = cascade.detectMultiScale(gray, 1.3, 5)
        try:
            if rects.any(): 
                print('Got a face')
                rects[:, 2:] += rects[:, :2] 
        except AttributeError:
            print(f'No faces found in {fname}.')
            continue
        # выделение лиц на изображении
        for x1, y1, x2, y2 in rects:
            cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2) 
        cv2.imwrite(newname, img) 
if name == '__main__':
    detect()
Функция detect принимает в качестве ввода три папки: исходную, конечную
и ту , в которой содержатся ресурсы для OpenCV . Она перебирает каждый
файл JPG в исходной папке (мы ищем лица, поэтому изображения, пред-
положительно, являются фотографиями и, скорее всего, хранятся в файлах
с расширением .jpg ). Затем считываем изображение с помощью библио-
теки компьютерного зрения OpenCV , cv2 , загружаем XML-файл detector
и создаем объект cv2 для обнаружения лиц . Этот объект является классифи-
катором, заранее обученным находить лица, запечатленные анфас. В OpenCV
также есть классификаторы для обнаружения лиц, снятых в профиль, кистей
рук, фруктов и целого ряда других объектов, с которыми вы можете поэкспе-
риментировать самостоятельно. Обнаружив лицо , классификатор возвра-
щает координаты соответствующей прямоугольной области на изображении.
В этом случае мы выводим сообщение в консоль, рисуем зеленую рамку вокруг
лица  и записываем изображение в выходной каталог .
Данные rects, возвращаемые классификатором, имеют вид (x, y, width,
height), где x и y — это координаты левого нижнего угла прямоугольника,
а width и height — его ширина и высота.
