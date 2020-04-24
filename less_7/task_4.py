# сортировка вставками

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


# [3, 9, 6, 4, 1, 7, 0, 5, 8, 2]

def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1

        array[j] = spam
        print(array)


insertion_sort(array)
print(array)

# [4, 0, 9, 6, 3, 5, 8, 1, 7, 2]
# [0, 4, 9, 6, 3, 5, 8, 1, 7, 2]
# [0, 4, 9, 6, 3, 5, 8, 1, 7, 2]
# [0, 4, 6, 9, 3, 5, 8, 1, 7, 2]
# [0, 3, 4, 6, 9, 5, 8, 1, 7, 2]
# [0, 3, 4, 5, 6, 9, 8, 1, 7, 2]
# [0, 3, 4, 5, 6, 8, 9, 1, 7, 2]
# [0, 1, 3, 4, 5, 6, 8, 9, 7, 2]
# [0, 1, 3, 4, 5, 6, 7, 8, 9, 2]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
