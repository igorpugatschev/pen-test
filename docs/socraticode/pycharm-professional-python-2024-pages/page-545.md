# PyCharm. Профессиональная работа на Python 2024 — страница 545

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

#%%
from sklearn.svm import LinearSVC
combined_user_df['BirthYear'].fillna(combined_user_df['BirthYear'].
mode(dropna=True)[0], inplace=True)
combined_user_df['DiagnosisYear'].fillna(combined_user_
df['DiagnosisYear'].mode(dropna=True)[0], inplace=True)
X_train = combined_user_df.drop(['Parkinsons'], axis=1)
y_train = combined_user_df['Parkinsons']
clf = LinearSVC()
clf.fit(X_train, y_train)
nfeatures = 10
coef = clf.coef_.ravel()
top_positive_coefs = np.argsort(coef)[-nfeatures :]
top_negative_coefs = np.argsort(coef)[: nfeatures]
top_coefs = np.hstack([top_negative_coefs, top_positive_coefs])
Обратите внимание: прежде чем передать имеющиеся у нас данные в мо-
дель ML, необходимо заполнить недостающие значения в двух столбцах, ко-
торые мы определили ранее, – BirthYear и DiagnosisYear. Большинство моделей
машинного обучения не могут хорошо обрабатывать пропущенные значения,
и инженеры по обработке данных должны выбирать, как эти значения следует
заполнять.
Здесь мы используем mode, или наиболее часто встречающуюся точку дан-
ных этих двух столбцов, чтобы заполнить недостающие значения. Это связа-
но с тем, что мода является одной из статистических характеристик, которые
имеют тенденцию хорошо представлять диапазон различных типов данных,
особенно для дискретных или номинальных атрибутов, которые мы здесь име-
ем. Если вы работаете с  числовыми и  непрерывными данными, такими как
длина или площадь, также общепринятой практикой является использование
среднего значения данного атрибута. Наконец, возвращаясь к нашему текуще-
му процессу, этот код обучает модель на нашем наборе данных и впоследствии
получает атрибут модели coef_.
Этот атрибут содержит список важности функций, который визуализируется
в последнем разделе кода:
plt.figure(figsize=(15, 5))
colors = ['red' if c < 0 else 'blue' for c in coef[top_coefs]]
plt.bar(np.arange(2 * nfeatures), coef[top_coefs], color=colors)
feature_names = np.array(X_train.columns)
# Make sure the number of tick locations matches the number of tick labels.
plt.xticks(np.arange(0, 2 * nfeatures), feature_names[top_coefs], rotation=60,
ha='right')
plt.show()
544	  Часть IV. Обработка данных с помощью PyCharm
