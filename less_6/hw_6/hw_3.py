# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде
# комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой
# переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.


# 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] win32

# Алгоритм: Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486,
#  то надо вывести число 6843.

import sys
from memory_profiler import profile


@profile()
def my_slice(a):
    print(sys.getrefcount(a[::-1]))
    print(sys.getsizeof(a[::-1]))
    return a[::-1]


@profile()
def my_reverse(a):
    a = list(a)
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    print(sys.getsizeof(a))
    print(sys.getrefcount(a))
    return "".join(a)


@profile()
def my_recursion(a):
    print(sys.getsizeof(a))
    print(sys.getrefcount(a))
    if len(a) == 1:
        return a
    else:
        return a[-1] + my_recursion(a[:-1])


my_str = "123456789012345678901234567890"

print("Срез:")
print(my_slice(my_str))

print("Список:")
print(my_reverse(my_str))

print("Рекурсия:")
print(my_recursion(my_str))
print(sys.version, sys.platform)


