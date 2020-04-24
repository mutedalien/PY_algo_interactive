# сортировка сложных структур с использованием ключа
import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


# [3, 9, 6, 4, 1, 7, 0, 5, 8, 2]

def revers(array):
    for i in range(len(array)):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]

revers(array)
print(array)

# [4, 1, 8, 6, 9, 7, 5, 3, 2, 0]
# [4, 1, 8, 6, 9, 7, 5, 3, 2, 0]

array.reverse()
print(array)

# [3, 2, 7, 9, 6, 4, 1, 8, 5, 0]
# [3, 2, 7, 9, 6, 4, 1, 8, 5, 0]
# [0, 5, 8, 1, 4, 6, 9, 7, 2, 3]

array.sort()
print(array)

# [8, 4, 7, 2, 0, 3, 1, 6, 9, 5]
# [8, 4, 7, 2, 0, 3, 1, 6, 9, 5]
# [5, 9, 6, 1, 3, 0, 2, 7, 4, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

array.sort(reverse=True)
print(array)

# [2, 9, 6, 7, 3, 5, 1, 0, 4, 8]
# [2, 9, 6, 7, 3, 5, 1, 0, 4, 8]
# [8, 4, 0, 1, 5, 3, 7, 6, 9, 2]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print('*' * 50)
t = tuple(random.randint(0, 100) for _ in range(size))
print(t)

# **************************************************
# (73, 11, 73, 27, 77, 87, 37, 82, 57, 67)

t = tuple(sorted(t, reverse=True))
print(t)

# **************************************************
# (79, 67, 53, 62, 95, 42, 50, 48, 5, 89)
# (95, 89, 79, 67, 62, 53, 50, 48, 42, 5)