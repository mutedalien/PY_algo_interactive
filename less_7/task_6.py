# сортировка Хоара (быстрая)

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


# [3, 9, 6, 4, 1, 7, 0, 5, 8, 2]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное')

    print(s_ar, m_ar, l_ar)
    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


array_new = quick_sort(array)
print(array_new)


# [9, 5, 6, 8, 1, 7, 4, 3, 2, 0]
# [5, 6, 8, 1, 7, 4, 3, 2, 0] [9] []
# [] [0] [5, 6, 8, 1, 7, 4, 3, 2]
# [5, 6, 1, 7, 4, 3, 2] [8] []
# [1, 3, 2] [4] [5, 6, 7]
# [1, 2] [3] []
# [1] [2] []
# [5] [6] [7]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# тоже самое, но не тратя памяти
def quick_sort_no_memory(array, fst, lst):

    if fst >= lst:
        return

    print(array)

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:

       while array[i] < pivot:
           i += 1

       while array[j] > pivot:
           j -= 1

       if i <= j:
           array[i], array[j] = array[j], array[i]
           i, j = i + 1, j - 1

    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)

quick_sort_no_memory(array, 0, len(array) - 1)
print(array)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 5, 6, 3, 4, 1, 7, 9, 8]
# [0, 2, 5, 6, 3, 4, 1, 7, 8, 9]
# [0, 2, 5, 1, 3, 4, 6, 7, 8, 9]
# [0, 2, 3, 1, 5, 4, 6, 7, 8, 9]
# [0, 2, 1, 3, 5, 4, 6, 7, 8, 9]
# [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
# [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
