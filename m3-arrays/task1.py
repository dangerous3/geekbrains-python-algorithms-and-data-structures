'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
'''
# Заполняем исходный массив для результатов нулями
k = [0] * 8
# Диапазон натуральных чисел 2..99
for i in range(2, 100):
    # Диапазон делителей 2..9
    for j in range(2, 10):
        # Проверка кратности
        if i % j == 0:
            k[j - 2] += 1

# Вывод результатов
i = 0
while i < len(k):
    print(f'Кратно {i + 2} - {k[i]} чисел')
    i += 1
