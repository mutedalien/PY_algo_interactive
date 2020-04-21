# Обмен значений главной и побочной диагоналей квадратной матрицы
import random

size = 5  # размер матрицы

matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
for line in matrix:  # перебираем каждую строчку
    for item in line:  # берем каждый отдельный элемент
        print(f'{item:>4}', end='')  # каждый элемент выводится в формате отступ на 4 знака
    print()

for i in range(size):  # i и j - индексы элементов матрицы
    for j in range(size):
        if i == j:  # если совпадают, значит указываем на диагональ
            spam = matrix[i][j]
            matrix[i][j] = matrix[i][size - 1 - j]
            matrix[i][size - 1 - j] = spam

print('*' * 30)
for line in matrix:  # перебираем каждую строчку
    for item in line:  # берем каждый отдельный элемент
        print(f'{item:>4}', end='')  # каждый элемент выводится в формате отступ на 4 знака
    print()


#    7   3   6   6   9
#    6   6   1   4   6
#    6   3   8   9   6
#    1   3   1  10   8
#    5   5   4   3   8
# ******************************
#    9   3   6   6   7
#    6   4   1   6   6
#    6   3   8   9   6
#    1  10   1   3   8
#    8   5   4   3   5