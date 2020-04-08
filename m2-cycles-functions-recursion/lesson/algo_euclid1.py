'''
Алгоритм Евклида нахождения НОД (наибольшего общего делителя, gcd, greatest common divisor).
Простейший циклический алгоритм, основанный на вычитании.
'''

def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m

print(gcd(54, 24))
print(gcd(540, 24012655620))