# PyCharm. Профессиональная работа на Python 2024 — страница 533

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

ячейки в функцию. Код в следующей ячейке длинный, но знакомый, посколь-
ку это всего лишь весь код, который мы написали до сих пор, объединенный
в одну функцию. Если вы разработчик приложений и понимаете принцип про-
ектирования, известный как принцип	 единой	 ответственности	 (SRP), вы
знаете, что это антипаттерн (антишаблон). Однако помните, что это не  код
приложения. Никто не запустит это, кроме как для выполнения анализа, поэ-
тому строгость принципов SOLID, которые обычно применяются к разработке
программного обеспечения, не соблюдается в работе по науке о данных.
Обработка данных Tappy с помощью одной функции
Вот наша функция:
#%% Combine into one function
def read_tappy(file_name):
Здесь мы читаем имя файла CSV, переданное в качестве аргумента нашей
функции. Мы обогащаем данные жестко запрограммированными именами
полей:
df = pd.read_csv(
    'data/Tappy Data/' + file_name,
    delimiter='\t',
    index_col=False,
    names=['UserKey', 'Date', 'Timestamp', 'Hand', 'Hold time',
        'Direction', 'Latency time', 'Flight time']
)
Удаляем ненужный столбец:
df = df.drop('UserKey', axis=1)
Фиксируем даты:
df['Date'] = pd.to_datetime(df['Date'], errors='coerce',
format='%y%M%d').dt.date
# Convert time data to numeric
for column in ['Hold time', 'Latency time', 'Flight time']:
    df[column] = pd.to_numeric(df[column], errors='coerce')
df = df.dropna(axis=0)
Всегда мойте руки, избавляясь от недопустимых значений:
# Clean data in `Hand`
df = df[
    (df['Hand'] == 'L') |
    (df['Hand'] == 'R') |
    (df['Hand'] == 'S')
]
532	  Часть IV. Обработка данных с помощью PyCharm
