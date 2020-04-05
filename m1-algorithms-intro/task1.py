''' Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.'''

a = 5
b = 6

c = a & b
print(f'Результат операции a & b (И) в десятичной системе счисления: {c}')

c = a | b
print(f'Результат операции a | b (ИЛИ) в десятичной системе счисления: {c}')

c = a ^ b
print(f'Результат операции a ^ b (ИСКЛЮЧАЮЩЕЕ ИЛИ) в десятичной системе счисления: {c}')

c = ~ a
# Применение побитового отрицания к неотрицательному числу даст отрицательное число, что связано с особенностями
# представления отрицательных чисел в виде дополнительного кода.
print(f'Результат операции ~ a (ОТРИЦАНИЕ) в десятичной системе счисления: {c}')

с = a << 2
# Битовый сдвиг влево на n бит равносилен (для положительных чисел) умножению на 2^n
print(f'Результат побитового сдвига числа а влево на два знака (a << 2) в десятичной системе счисления: {c}')

с = a >> 2
# Оператор a >> n возвращает число, которое получается из a сдвигом всех бит на n позиций вправо, при этом самые
# правые n бит отбрасываются. для положительных чисел битовый сдвиг числа вправо на n равносилен целочисленному
# делению на 2^n
print(f'Результат побитового сдвига числа а вправо на два знака (a >> 2) в десятичной системе счисления: {c}')