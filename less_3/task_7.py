#  Двоичный бинарный поиск элементов в массиве
import random


def bin_search(array, value):
    left = 0  # левая переменная - первый элемент массива
    right = len(array) - 1  # правая переменная равна последнему элементу массива
    pos = len(array) // 2  # серединка массива

    while array[pos] != value and left <= right:

        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1
        pos = (left + right) // 2

    return -1 if left > right else pos  # возвращаем значение


a = [random.randint(0, 1000) for _ in
     range(100)]  # сгенерируем массив случайных чисел (100 элементов в диапазоне от 0 до 1000)
a.sort()  # упорядочим список
print(a)
# распечатаем список и выберем какой элемент искать
n = int(input('Какой элемент найти: '))
print(bin_search(a, n))
