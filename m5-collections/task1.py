'''
 Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
 Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
 чья прибыль выше среднего и ниже среднего.
'''

import collections

n = int(input("Введите количество предприятий: "))

firms = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

result = {}

for i in range(n):
    name = str(i + 1) + "-е предприятие"
    Q1 = int(input('Прибыль за 1-й квартал: '))
    Q2 = int(input('Прибыль за 2-й квартал: '))
    Q3 = int(input('Прибыль за 3-й квартал: '))
    Q4 = int(input('Прибыль за 4-й квартал: '))
    result[name] = firms(
        q1=Q1,
        q2=Q2,
        q3=Q3,
        q4=Q4
    )

total_profit = ()

for name, profit in result.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(profit)
print(f'Средняя прибыль за год для всех предприятий: {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in result.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

for name, profit in result.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')