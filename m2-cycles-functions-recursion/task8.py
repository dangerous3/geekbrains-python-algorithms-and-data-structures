'''
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''

num = input("Введите число: ")
digit = input("Введите искомую цифру: ")

counter = 0

for i in num:
    if i == digit:
        counter += 1

print(f'Число {digit} встречается в числе {num} {counter} раз(а)')