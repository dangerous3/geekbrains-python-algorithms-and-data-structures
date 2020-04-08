'''
Даны два целых числа A и B.
Необходимо вывести все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания, если
если A > B
'''

def func(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'

print(func(1, 10))
print(func(100, 10))