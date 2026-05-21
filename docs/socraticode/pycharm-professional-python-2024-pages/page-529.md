# PyCharm. Профессиональная работа на Python 2024 — страница 529

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

df = pd.read_csv(
    'data/Tappy Data/' + file_name,
    delimiter = '\t',
    index_col = False,
    names = ['UserKey', 'Date', 'Timestamp', 'Hand', 'Hold time',
'Direction', 'Latency time', 'Flight time']
)
Для наших целей нам не нужно поле UserKey:
df = df.drop('UserKey', axis=1)
print(df.head())
Запуская эту ячейку, мы создаем новый DataFrame с именем df. Обязательно
выберите его на панели переменных консоли, показанной на рис. 14.16:
Рис. 14.16.	Наш новый DataFrame можно просмотреть, нажав кнопку View as DataFrame
Форматирование данных даты и времени
Следующая ячейка фиксирует наши данные Datetime:
#%% Format datetime data
528	  Часть IV. Обработка данных с помощью PyCharm
