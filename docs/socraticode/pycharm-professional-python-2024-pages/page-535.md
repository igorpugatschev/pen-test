# PyCharm. Профессиональная работа на Python 2024 — страница 535

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

for filename in filenames:
    if user_id in filename:
        running_user_data = np.append(running_user_data, read_tappy(filename))
Этот цикл перебирает список имен файлов. Если предоставленный иденти-
фикатор пользователя найден в имени файла, он вызывает функцию read_tap-
py() (которая возвращает сглаженный массив средних значений NumPy) и до-
бавляет его содержимое в массив running_user_data.
После перебора имен файлов и добавления данных следующая строка пре-
образует массив running_user_data в двумерный массив, каждая строка которого
содержит 27 столбцов. Такое сглаживание временных данных позволяет про-
вести дальнейший анализ:
running_user_data = np.reshape(running_user_data, (-1, 27))
Последняя строка вычисляет средние значения по строкам ( axis=0) массива
running_user_data с помощью np.nanmean(). Функция np.nanmean() игнорирует зна-
чения NaN при вычислении среднего значения:
return np.nanmean(running_user_data, axis=0)
Подводя итог, можно сказать, что функция process_user обрабатывает дан-
ные для конкретного пользователя, перебирая соответствующие имена фай-
лов, агрегируя данные с помощью функции read_tappy, изменяя форму данных
и вычисляя средние значения, игнорируя значения NaN. Конечным результатом
является массив средних значений для каждого столбца данных.
Обработка всех данных
Решающий момент! Следующая ячейка обрабатывает данные для всех доступ-
ных пользователей, агрегируя и вычисляя средние значения на основе данных
Tappy. Для начала немного приберемся. Мы собираемся игнорировать любые
предупреждения:
#%% Run through all available data
import warnings
warnings.filterwarnings("ignore")
Совершим еще одно путешествие по папке Tappy Data:
filenames = os.listdir('data/Tappy Data/')
Далее создадим имена столбцов для окончательного DataFrame:
column_names = [first_hand + second_hand + '_' + time
    for first_hand in ['L', 'R', 'S']
    for second_hand in ['L', 'R', 'S']
    for time in ['Hold time', 'Latency time', 'Flight time']]
user_tappy_df = pd.DataFrame(columns=column_names)
534	  Часть IV. Обработка данных с помощью PyCharm
