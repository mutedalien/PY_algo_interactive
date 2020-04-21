# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

import random
size = 15
array = [random.randint(-99, 99) for _ in range(size)]

print(array)

maxNeg = -1000000
Count = 0
for i in range(size):
    if array[i] < 0 and array[i] > maxNeg:
        maxNeg = array[i]
        Count = i

print(f'Максимальный отрицательный элемент {maxNeg} на {Count} позиции')
