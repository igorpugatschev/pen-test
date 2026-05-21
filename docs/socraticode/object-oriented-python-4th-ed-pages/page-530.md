# Объектно-ориентированный Python, 4-е издание — страница 530

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти ческ ое иссле дова ние 529
Рассмо трим, как это выг лядит на UМ L-диаграмме (рис. 11 . 10).
Training Data
name: str
uploaded: datetime
tested: datetime
�Тестиро ван ие "111 Об учен ие
Hyperparameter
k: int
quality: float
distance: Distance
classifier: Classifier
test( ): float
classify(sample: Sample): str
Расст оя ние
Sample
sepal_length : float
sepal_width : float
petal_length : float
petal width : float
Классифика тор
Classifier
classify( k: int, d: Distance , train: Sample, unk: Sample): float
Distance K_NN _Bis ect
distanc e( s1 : Sample, s2: Sample): float
Chebyshev Manha ttan Euclidean
Рис. 11. 10. Классы Hyperpa ram eter и Dis ta nc e
на U М L- ди а грамме
K_NN _HeapQ
