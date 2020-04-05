'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''

import random as rd
array = [rd.randint(-100, 100) for _ in range(60)]
print(f'Исходный массив: {array}')

neg_array = []
for i, item in enumerate(array):
    if item < 0:
        neg_array.append(item)

max_el = neg_array[0]
for i, item in enumerate(neg_array):
    if item > max_el:
        max_el = item


print(f'Максимальный элемент из отрицательных чисел в массиве: {max_el}, его индекс: {array.index(max_el)}')