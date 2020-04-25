# сортировка выбором

import random

# размер сортируемого массива
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def selection_sort(array):
    for i in range(len(array)):
        idx_min = i
        # неотсортированная часть массива
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        # Перемещаем минимальный элемент в начало
        array[idx_min], array[i] = array[i], array[idx_min]

selection_sort(array)
print(array)
