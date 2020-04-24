# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

array = [random.randint(-100, 100) for i in range(10)]
print(array)

def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n+1] > array[n]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array

print(bubble_sort(array))