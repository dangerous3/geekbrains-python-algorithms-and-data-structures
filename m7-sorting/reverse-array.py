# Разворот массива

import random

# размер сортируемого массива
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def revers(array):
    for i in range(len(array) // 2):
        # Меняем местами пару элементов массива, раположенных зеркально относительно середины массива
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]

revers(array)
print(array)

array.reverse()
print(array)

array.sort(reverse=True)
print(array)

print('*' * 50)
t = tuple(random.randint(0, 100) for _ in range(size))
print(t)

t = tuple(sorted(t, reverse=True))
print(t)