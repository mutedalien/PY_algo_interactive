# сортировка выбором

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


# [3, 9, 6, 4, 1, 7, 0, 5, 8, 2]

def selection_sort(array):
    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        array[idx_min], array[i] = array[i], array[idx_min]
        print(array)

selection_sort(array)
print(array)

# [0, 2, 6, 4, 3, 5, 7, 1, 9, 8]
# [0, 2, 6, 4, 3, 5, 7, 1, 9, 8]
# [0, 1, 6, 4, 3, 5, 7, 2, 9, 8]
# [0, 1, 2, 4, 3, 5, 7, 6, 9, 8]
# [0, 1, 2, 3, 4, 5, 7, 6, 9, 8]
# [0, 1, 2, 3, 4, 5, 7, 6, 9, 8]
# [0, 1, 2, 3, 4, 5, 7, 6, 9, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
