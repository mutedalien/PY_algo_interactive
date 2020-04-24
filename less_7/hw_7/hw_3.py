# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
import cProfile
from sorting import cocktail_sort

def median(lst):
    ordered_list = cocktail_sort(lst)
    print(ordered_list)

    l = len(lst)
    i = (l - 1) // 2

    if (l % 2):
        return ordered_list[i]
    else:
        return (ordered_list[i] + ordered_list[i + 1]) / 2


def main():
    n = random.randint(1, 10)
    orig_list = [random.randint(0, 50) for _ in range(2 * n + 1)]
    copy_list = orig_list.copy()

    print(orig_list)
    m = median(copy_list)
    print(m)


cProfile.run('main()')