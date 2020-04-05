'''
Определить, какое число в массиве встречается чаще всего.
'''

import random as rd
array = [rd.randint(1, 100) for _ in range(20)]
print(f'Исходный массив: {array}')

k = array[0]
counter_max = 1
for i in range(len(array) - 1):
    counter = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            counter += 1
    if counter > counter_max:
        counter_max = counter
        k = array[i]

if counter_max > 1:
    print(f'{counter_max} раз(а) встречается число {k}')
else:
    print('Каждый элемент массива содержится в нем один раз')