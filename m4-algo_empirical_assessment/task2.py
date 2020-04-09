'''
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
'''

import cProfile

# Первый вариант решения (Решето Эратосфена)
def sieve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result
# Конец первого варианта решения

# cProfile.run('sieve(100000)')

'''
Лучшее время вычисления значений функции sieve() от значений 100, 1000 и 10000

python3 -m timeit -n 1000 -s "import task2" "task2.sieve(100)" 
1000 loops, best of 3: 29.4 usec per loop

python3 -m timeit -n 1000 -s "import task2" "task2.sieve(1000)"
1000 loops, best of 3: 356 usec per loop

python3 -m timeit -n 1000 -s "import task2" "task2.sieve(10000)"
1000 loops, best of 3: 4.08 msec per loop
'''

# Второй вариант решения

# Вывод простых чисел вплоть до n
def prime(n):
    n = int(n)
    lst = [2]
    for i in range(3, n + 1, 2):
    	if (i > 10) and (i % 10 == 5):
    		continue
    	for j in lst:
    		if j * j - 1 > i:
    			lst.append(i)
    			break
    		if (i % j == 0):
    			break
    	else:
    		lst.append(i)
    return lst
# Конец второго варианта решения

'''Лучшее время вычисления значений функции prime() от значений 100, 1000 и 10000

python3 -m timeit -n 1000 -s "import task2" "task2.prime(100)"
1000 loops, best of 3: 29 usec per loop

python3 -m timeit -n 1000 -s "import task2" "task2.prime(1000)"
1000 loops, best of 3: 433 usec per loop

python3 -m timeit -n 1000 -s "import task2" "task2.prime(10000)"
1000 loops, best of 3: 6.65 msec per loop
'''

'''Итог: Улучшить алгоритм Эратосфена за разумное в рамках курса не удалось, идем дальше'''