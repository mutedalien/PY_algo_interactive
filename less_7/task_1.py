# сортировка пузырьком

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

# [3, 9, 6, 4, 1, 7, 0, 5, 8, 2]

n = 1
while n < len(array):
    for i in range(len(array) - n):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    print(array)
print(array)

# [2, 1, 8, 3, 9, 5, 4, 6, 7, 0]
# [1, 2, 3, 8, 5, 4, 6, 7, 0, 9]
# [1, 2, 3, 5, 4, 6, 7, 0, 8, 9]
# [1, 2, 3, 4, 5, 6, 0, 7, 8, 9]
# [1, 2, 3, 4, 5, 0, 6, 7, 8, 9]
# [1, 2, 3, 4, 0, 5, 6, 7, 8, 9]
# [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]
# [1, 2, 0, 3, 4, 5, 6, 7, 8, 9]
# [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
