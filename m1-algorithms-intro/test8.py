'''Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if c < a < b or b < a < c:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)
