'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random as rd
array = [rd.randint(1, 100) for _ in range(10)]
print(f'Исходный массив: {array}')

max_el = array[0]
min_el = array[0]

for i, item in enumerate(array):
    if item > max_el:
        max_el = item
        index_max = i
    if item < min_el:
        min_el = item
        index_min = i

print(f'Максимальный элемент: {max_el}, его индекс: {index_max}')
print(f'Минимальный элемент: {min_el}, его индекс: {index_min}')

array[index_max] = min_el
array[index_min] = max_el

print(f'Массив решения задачи: {array}')