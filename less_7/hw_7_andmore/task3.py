# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

import random


def mediana(massive):
    for n in range(len(massive)):
        right = 0
        left = 0
        for i in range(len(massive)):
            if massive[n] >= massive[i]:
                left += 1  # считаем число элементов, которые оказались бы слева в отсортированном массиве
            if massive[n] <= massive[i]:
                right += 1  # считаем число элементов, которые оказались бы справа в отсортированном массиве
        if left == right:
            return massive[n]


array = [random.randint(0, 100) for i in range(51)]
print(array)
print(mediana(array))
print(sorted(array))  # выведем отсортированный массив, так легче проверить работает ли функция