# PyCharm. Профессиональная работа на Python 2024 — страница 534

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

Сделайте то же самое со значениями данных направлений:
# Clean data in `Direction`
df = df[
    (df['Direction'] == 'LL') |
    (df['Direction'] == 'LR') |
    (df['Direction'] == 'LS') |
    (df['Direction'] == 'RL') |
    (df['Direction'] == 'RR') |
    (df['Direction'] == 'RS') |
    (df['Direction'] == 'SL') |
    (df['Direction'] == 'SR') |
    (df['Direction'] == 'SS')
    ]
Мы занимаемся математикой! Здесь на помощь приходит ручной про-
цесс GC. Хорошо, что мы вымыли руки, не так ли? В следующем коде мы выпол-
няем наши вычисления. Результаты возвращаются в виде нового DataFrame,
поэтому для экономии памяти удаляем старые DataFrame по ходу работы. Это
освобождает память, поскольку такая работа требует большого объема памяти:
        direction_group_df = df.groupby('Direction')[numeric_columns][numeric_
columns][numeric_columns] direction_group_df = df.groupby('Direction')[numeric_
columns].mean()
    del df
    gc.collect()
Получив новый результат, мы переиндексируем, а затем сортируем:
direction_group_df = direction_group_df.reindex(['LL', 'LR', 'LS', 'RL', 'RR',
'RS', 'SL', 'SR', 'SS'])
direction_group_df = direction_group_df.sort_index() # to ensure correct order
of data
Эта строка возвращает одномерный массив NumPy, который содержит сред-
ние значения сгруппированных данных. Метод .values.flatten() преобразует
DataFrame в двумерный массив NumPy, а затем сглаживает его в одномерный
массив для простоты использования:
return direction_group_df.values.flatten()
Обработка пользователей с помощью функции
В той же ячейке находится вторая функция:
def process_user(user_id, filenames):
    running_user_data = np.array([])
Эта строка инициализирует пустой массив NumPy с именем running_user_data.
Этот массив будет использоваться для накопления данных по мере того, как
функция перебирает имена файлов, что и делает следующий блок:
Глава 14. Создание конвейера данных в PyCharm  533
