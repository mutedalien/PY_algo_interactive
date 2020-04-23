'''Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого — цифры числа.'''

a = list(input('Введите первое число: ').lower())
b = list(input('Введите второе число: ').lower())


d = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 
			'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15}


def hexint(a):
	tmp = list(reversed(a))
	rez = 0
	for i in range(len(tmp)):
		rez += d[tmp[i]]*(16**i)
	
	return rez	


sum = hexint(a) + hexint(b)
mul = hexint(a) * hexint(b)


def inthex(a):
	rez = []
	while a > 0:
		rez.append(list(d.keys())[a % 16])
		a = a // 16

	return list(reversed(rez))

print(f'{a} + {b} = {inthex(sum)}')
print(f'{a} * {b} = {inthex(mul)}')

