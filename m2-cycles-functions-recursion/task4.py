'''
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
'''

n = int(input('Введите количество элементов: '))

sum = 0

for i in range(1, n + 1):
    an = (((-1) ** (i + 1)) / (2 ** (i - 1)))
    # Вывод элемента последовательности
    # print(f'{i} элемент: {an}')
    sum += an

print(f'Сумма равна: {sum}')
