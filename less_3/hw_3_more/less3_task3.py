# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
size = 10
array = [random.randint(0, 99) for _ in range(size)]

maxitem = 0
minitem = 99
maxi = 0
mini = 0
print(array)
for i in range(size):
    if maxitem < array[i]:
        maxitem = array[i]
        maxi = i
    if minitem > array[i]:
        minitem = array[i]
        mini = i

spam = array[maxi]
array[maxi] = array[mini]
array[mini] = spam
print(array)
