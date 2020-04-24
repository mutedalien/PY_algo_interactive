# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

array = [random.randint(-100, 100) for i in range(7)]
print(array)

def median(nums):
    half = len(nums) // 2
    nums.sort()
    if not len(nums) % 2:
        return (nums[half - 1] + nums[half]) / 2
    return nums[half]

print('Медиана:', median(array[:]))
