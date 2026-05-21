# PyCharm. Профессиональная работа на Python 2024 — страница 540

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

Рис. 14.22.	Недостающие данные отображаются на гистограмме
К счастью, наша диаграмма очень скудна. Лишь небольшой объем данных
отсутствует или является неполным. Отсутствуют некоторые значения для
BirthYear и DiagnosisYear. Вы даже можете увидеть это в предварительном про-
смотре, показанном на рис. 14.21. Анализ пропущенных значений важен, и мы
вернемся к процессу заполнения этих значений позже. А пока давайте продол-
жим процесс визуализации.
Замечательной функцией Matplotlib являются поддиаграммы, которые по-
зволяют нам создавать несколько визуализаций одновременно. В следующей
ячейке кода мы создаем несколько визуализаций с помощью этой функции,
чтобы подчеркнуть потенциальные различия между пациентами с болезнью
Паркинсона и без нее:
#%%
f, ax = plt.subplots(2, 2, figsize=(20, 10))
sns.distplot(
combined_user_df.loc[combined_user_df['Parkinsons'] == 0,
'BirthYear'].dropna(axis=0),
kde_kws = {'label': "Without Parkinson's"},
ax = ax[0][0]
)
sns.distplot(
combined_user_df.loc[combined_user_df['Parkinsons'] == 1,
'BirthYear'].dropna(axis=0),
kde_kws = {'label': "With Parkinson's"},
ax = ax[0][1]
)
sns.countplot(x='Female', hue='Parkinsons', data=combined_user_df,
ax=ax[1][0])
sns.countplot(x='Tremors', hue='Parkinsons', data=combined_user_df,
Глава 14. Создание конвейера данных в PyCharm  539
