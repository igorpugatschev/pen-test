# Объектно-ориентированный Python, 4-е издание — страница 372

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Тема ти ческ ое исследова ние 371
В идеале один и тот же код может исполь зоваться в обоих случаях, что снизит
общую сложность прилож ения.
Поск ольку мы, как договарива лись ранее, рассма триваем различные альтернати­
вы представ ления процесса, это приводит к изменениям в логическом представ­
лении. На рис. 8.4 пок азана пересмотрен ная диаграмма, на которой эти классы
пре дста влены как неизменяемые компо зиции. Сю да включены примечания,
подска зывающие, когда эти объекты создаются в процессе обработки приложе­
ния. Выделим также два класса, требующие более тщател ьного рассмот рения.
Создано классификатором
во время тестирования
Создано par1ition( ) � ClassifiedK nownSample
sample: Known Sample
Classifica tion : str
Создано класси фикатором
для пользователя 1 <
'
' '
'
'
'
'
'
'
'
'
'
'
'
'
'
Training KnownSample
sample: KnownSample
'
'
'
'
'
'
'
/н а основе '
'
'
'
'
'
Testing Known Sample
sample: KnownSam ple
KnownSample
sample: Sample
species: str
зки
Classif iedKno wnSampie
sample: Un knownsample
Classification : str
sepal_length : float
sepal_width : float
petal_length: float
petal_width: float
Un known Sample
sample: Sample
Рис . 8 . .4. Изм ененн ое ло ги ческ ое пре дста вле ние
