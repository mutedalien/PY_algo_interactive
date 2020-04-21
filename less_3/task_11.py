# Посчитать сумму строк и столбцов матрицы

import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
for line in matrix: # перебираем каждую строчку
    for item in line: # берем каждый отдельный элемент
        print(f'{item:>4}', end='') # каждый элемент выводится в формате отступ на 4 знака
    print()

sum_column = [0] * len(matrix[0]) # массив, считающий сумму по столбцам матрицы (сколько 0 - столько столбцов)

for line in matrix: # внешний цикл
    sum_line = 0

    for i, item in enumerate(line): # в переменной i будет храниться номер столбца, а в item - значение
        sum_line += item # сюда просто прибавляем item
        sum_column[i] += item # а сюда считаем сумму i-того столбца

        print(f'{item:>5}', end='') # строим тело матрицы

    print(f'  | {sum_line}')

print('_' * (len(matrix) * 5)) # разделим исходную матрицу с результатом

for s in sum_column:
    print(f'{s:>5}', end='')