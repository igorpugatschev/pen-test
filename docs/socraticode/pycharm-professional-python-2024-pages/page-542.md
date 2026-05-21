# PyCharm. Профессиональная работа на Python 2024 — страница 542

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

Далее перейдем к коробчатым диаграммам 1. В частности, мы будем ис -
пользовать коробчатые диаграммы для визуализации распределения раз-
личных временных данных ( Hold time , Latency time , и Flight time ) среди
пациентов с  болезнью Паркинсона и  без нее. Еще раз мы будем исполь-
зовать функцию поддиаграмм для одновременного создания нескольких
визуализаций:
#%%
column_names = [first_hand + second_hand + '_' + time
for first_hand in ['L', 'R', 'S']
for second_hand in ['L', 'R', 'S']
for time in ['Hold time', 'Latency time', 'Flight time']]
f, ax = plt.subplots(3, 3, figsize=(10, 5))
plt.subplots_adjust(
right = 3,
top = 3
)
for i in range(9):
    temp_columns = column_names[3 * i : 3 * i + 3]
    stacked_df = combined_user_df[temp_columns].stack().reset_index()
stacked_df = stacked_df.rename(
columns={'level_0': 'index', 'level_1': 'Type', 0: 'Time'})
stacked_df = stacked_df.set_index('index')
for index in stacked_df.index:
    stacked_df.loc[index, 'Parkinsons'] = combined_user_df.loc[index, 'Parkinsons']
sns.boxplot(x='Type', y='Time',
hue='Parkinsons',
data=stacked_df,
ax=ax[i // 3][i % 3]
).set_title(column_names[i * 3][: 2], fontsize=20)
plt.show()
В этой ячейке кода каждая поддиаграмма будет визуализировать данные
определенного типа направления ( LL, LR, LS и т. д.) и будет содержать раз-
личные разбиения, обозначающие пациентов с  заболеванием и  без него.
Вы должны получить визуализацию, показанную на рис. 14.24:
1 Коробчатая диаграмма используется для изучения одного или нескольких набо-
ров данных в  графическом виде. Данный тип диаграммы может использовать-
ся для сравнения распределений между несколькими группами или наборами
данных. Для каждой группы или набора данных вычисляются статистика центра
(медиана, среднее) и статистики диапазона (квартили, стандартные отклонения)
для различных моментов времени, и выбранные значения изображаются на диа-
грамме. – Прим. ред.
Глава 14. Создание конвейера данных в PyCharm  541
