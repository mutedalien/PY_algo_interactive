# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random


def bubble_sort(massive):
    n = 1
    while n < len(massive):
        flag = 0
        for i in range(len(massive)-n):
            if massive[i] > massive[i+1]:
                massive[i], massive[i+1] = massive[i+1], massive[i]
                flag = 1  # обмен произошел?
        n += 1
        if not flag:  # если не было ни одного обмена, можно выйти раньше из внешнего цикла
            break
    return massive


array = [random.randint(-100, 99) for i in range(50)]
print(array)
print(bubble_sort(array))


