# 4. Определить, какое число в массиве встречается чаще всего

import random
size = 15
array = [random.randint(0, 10) for _ in range(size)]

print(array)
maxCount = 1
for i in range(size - 1):
    Count = 1
    for k in range(i + 1, size):
        if array[i] == array[k]:
            Count += 1
    if Count > maxCount:
        maxCount = Count
        Number = array[i]

if maxCount > 1:
    print(f'Число {Number} Встречается {maxCount} раз')
else:
    print('Все числа встречаются по одному разу')
