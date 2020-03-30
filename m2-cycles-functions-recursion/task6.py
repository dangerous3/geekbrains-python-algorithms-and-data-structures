'''
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
'''

import random as rd

num = rd.randint(0, 100)

attempts = 0

your = int(input("Введите целое число от 0 до 100: "))

while attempts < 10:
    if your == num:
        print(f"Вы угадали: загаданное число {your}!")
        break
    else:
        attempts += 1
        your = int(input("Неверно! Попробуйте еще раз угадать число от 1 до 100: "))

if attempts > 9:
    print(f"Вы не угадали загаданное число {num} за {attempts} попыток")

