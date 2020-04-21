# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

size = 15

matrix = [[random.randint(0, 99) for _ in range(size)]for _ in range(size)]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end=' ')
    print()

maxN = 0

for j in range(size):
    minN = 10000
    for i in range(size):
        if minN > matrix[i][j]:
            minN = matrix[i][j]
    if maxN < minN:
        maxN = minN

print(
    f'Максимальный элемент среди минимальных элементов столбцов = {maxN}')
