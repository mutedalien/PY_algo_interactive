"""
Задание 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Company = namedtuple('Company', 'name, profit1, profit2, profit3, profit4', defaults = ['noname', 0, 0, 0, 0])
n = int(input("Введите число предриятий: "))
print("_______________________________________________________")
y = []
sum = [0 for i in range(n)]

for i in range(n):
    x = []
    x.append(str(input("Введите имя предриятия: ")))
    x.append(int(input("Введите прибыль за первый квартал: ")))
    x.append(int(input("Введите прибыль за второй квартал: ")))
    x.append(int(input("Введите прибыль за третий квартал: ")))
    x.append(int(input("Введите прибыль за четвертый квартал: ")))
    print("_______________________________________________________")
    a = Company._make(x)
    sum[i] = a.profit1 + a.profit2 + a.profit3 + a.profit4
    y.append(a)

average = 0
for i in range(n):
    average += sum[i]
average /= n
print("Средняя прибль = ", average)

for i, item in enumerate(y):
    s = item.profit1 + item.profit2 + item.profit3 + item.profit4
    if s > average:
        print(f'У компании под названием {item.name} прибыль за год больше среднего - {s}')
    elif s < average:
        print(f'У компании под названием {item.name} прибыль за год меньше среднего - {s}')
    else:
        print(f'У компании под названием {item.name} прибыль за год равна среднему - {s}')




