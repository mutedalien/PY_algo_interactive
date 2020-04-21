# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба минимальны), так и различаться.


import random
size = 15
array = [random.randint(0, 9) for _ in range(size)]

print(array)

min1 = 100000
min2 = 100000
ind1 = 0
ind2 = 0

for i in range(size):
    if min1 > array[i]:
        min1 = array[i]
        ind1 = i
for i in range(size):
    if ind1 != i and min2 > array[i]:
        min2 = array[i]
        ind2 = i

print(f'Первый минимальный элемент {min1} на позиции {ind1}')
print(f'Второй минимальный элемент {min2} на позиции {ind2}')
