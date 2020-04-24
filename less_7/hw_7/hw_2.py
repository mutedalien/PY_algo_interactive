# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# аданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
import cProfile

from sorting import merge_sort

def main():
    orig_list = [round(random.uniform(0, 50), 3) for _ in range(500)]
    copy_list = orig_list.copy()

    ordered_list = merge_sort(copy_list)

    del copy_list

    print(orig_list)
    print(ordered_list)


cProfile.run('main()')
