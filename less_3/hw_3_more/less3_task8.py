# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = [[0 for _ in range(5)]for _ in range(4)]

for i in range(4):
    sum = 0
    for j in range(4):
        matrix[i][j] = int(input(f'Введите {j+1} элемент {i+1} строки '))
        sum += matrix[i][j]
    matrix[i][j+1] = sum

for line in matrix:
    for item in line:
        print(f'{item:>4}', end=' ')
    print()
