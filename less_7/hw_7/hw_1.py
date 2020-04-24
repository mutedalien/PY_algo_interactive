# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random
import cProfile

from sorting import bubble_sort

def main():
    orig_list = [random.randint(-100, 100) for _ in range(100)]
    copy_list = orig_list.copy()

    ordered_list = bubble_sort(copy_list, asc=False)

    del copy_list

    print(orig_list)
    print(ordered_list)


cProfile.run('main()')
