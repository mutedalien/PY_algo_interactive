# матрица

import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
for line in matrix: # перебираем каждую строчку
    for item in line: # берем каждый отдельный элемент
        print(f'{item:>4}', end='') # каждый элемент выводится в формате отступ на 4 знака
    print()

#    7   8   1   9  10
#    4   8   7   3   5
#    4   7   3  10   9
#    8   9   6   8   4
#    2   5   3   4   3
#    3   6  10   3   5
#   10   5   9   6   1