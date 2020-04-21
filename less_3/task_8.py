# Разложить положительные и отрицательные числа по разным массивам

import random

array = [random.randint(-100, 100) for _ in range(100)]  # создаем массив с случайн полож и отр числами
print(array)

# создаем два массива для полож и отр чисел
arr_below = []
arr_lager = []

for item in array:
    if item > 0:
        arr_lager.append(item)
    elif item < 0:
        arr_below.append(item)
print(arr_below)
print(arr_lager)

# или так:
arr_below1 = [item for item in array if item < 0]
arr_lager1 = [item for item in array if item > 0]
print(arr_below)
print(arr_lager)
# но так цикл обходит массив дважды, сперва для +, потом для -
