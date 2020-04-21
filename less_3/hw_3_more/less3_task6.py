# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random
size = 15
array = [random.randint(0, 9) for _ in range(size)]

print(array)

maxN = 0
minN = 10000
maxC = 0
minC = 0
Sum = 0

for i in range(size):
    if maxN < array[i]:
        maxN = array[i]
        maxC = i
    if minN > array[i]:
        minN = array[i]
        minC = i

if maxC > minC:
    for i in range(minC + 1, maxC):
        Sum += array[i]
else:
    for i in range(maxC + 1, minC):
        Sum += array[i]

print(f'Сумма = {Sum}')
