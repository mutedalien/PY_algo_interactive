'''Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, 
чья прибыль выше среднего и ниже среднего.'''



from collections import namedtuple

n = int(input('Введите число предпиятй: '))
P = namedtuple('P', 'name, first, second, third, fourth, average')
d, up, down = {}, {}, {}
average_all = 0
for i in range(n):
	print('*' * 30)
	name = input('Наименование предприятия: ')
	first = int(input('Прибыль за I квартал: '))
	second = int(input('Прибыль за II квартал: '))
	third = int(input('Прибыль за III квартал: '))
	fourth = int(input('Прибыль за IV квартал: '))
	average = round((first + second + third + fourth) / 4, 4)
	d[i] = P(name, first, second, third, fourth, average)
	average_all += d[i].average


average_all = average_all / n
print(f'\nСреденяя прибыль за год для всех предприятий: {round(average_all, 4)}', '\n')

for v in d.values():
	if v.average < average_all:
		down[v.name] = v.average
	else:
		up[v.name] = v.average


print('Предприятия, с прибылью выше чем средняя')
for k, v in up.items():
	print(f'Предприятие: {k} - средняя прибыль: {v}')

print('\nПредприятия, с прибылью ниже чем средняя')
for k, v in down.items():
	print(f'Предприятие: {k} - средняя прибыль: {v}')

