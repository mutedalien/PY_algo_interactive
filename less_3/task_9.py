# Вставка элемента в произвольное место массива

import random

array = [random.randint(-100, 100) for _ in range(100)]  # создаем массив с случайн полож и отр числами
print(array)

num = int(input('Введите целое число для вставки: '))
pos = int(input('На какую позицию вставить число: '))

array.append(None)
i = len(array) - 1

while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1
array[pos] = num
print(array)
