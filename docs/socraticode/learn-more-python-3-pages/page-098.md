# Легкий способ выучить Python 3 еще глубже — страница 98

ПУЗЫРЬКОВАЯ И БЫСТРАЯ СОРТИРОВКА, СОРТИРОВКА СЛИЯНИЕМ 97
left := merge_sort(left)
right := merge_sort(right)
return merge(left, right)
function merge(left, right)
var result := empty list
while left is not empty and right is not empty do
if first (left) first (right) then
append first (left) to result
left := rest(left)
else
append first (right) to result
right := rest(right)
while left is not empty do
append first (left) to result
left := rest(left)
while right is not empty do
append first (right) to result
right := rest(right)
return result
Допишите оставшуюся тестовую функцию для test_merge_sort, а затем
попытайтесь это реализовать. Я дам вам одну подсказку - данный алгоритм
лучше всего работает, если задан только первый узел. Вероятно, вам также
понадобится способ подсчитать количество узлов, имея только данный узел.
Двусвязный список такой возможности не предоставляет.
Плутовство при сортировке слиянием
Если ваша попытка затянулась и вам хочется сплутовать, посмотрите, что сде­
лал я:
sorting.ру
1 def count(node):
2 count = О
3
