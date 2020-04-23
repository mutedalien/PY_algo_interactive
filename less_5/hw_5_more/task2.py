"""
Задание 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

aa = list(input("Введите первое число: "))
bb = list(input("Введите второе число: "))
if len(bb) > len(aa):
  bb, aa = aa, bb
lst = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

def addition (a, b):
    a = a[::-1]
    b = b[::-1]
    ost = 0
    ss = deque()
    j = 0
    # Тут нужно проходиться по бОльшему числу, чтобы не потерять из него цифры
    for i in a:
        first = lst.index(i)
        if j >= len(b):
            sum = (first + ost) % 16
            ost = (first + ost) // 16
            ss.appendleft(lst[sum])
            if ost > 0:
                ss.appendleft(lst[ost])
        else:
            second = lst.index(b[j])
            sum = (first + second + ost) % 16
            ost = (first + second + ost) // 16
            ss.appendleft(lst[sum])
            j += 1
    return ss

def multiplication (a, b):
    a = a[::-1]
    b = b[::-1]
    ans = []
    pred = []
    # Тут нужно проходиться по меньшему числу, так получится меньше проходок по массивам и меньше промежуточных значений
    for count, i in enumerate(b):
        mm = []
        ost = 0
        first = lst.index(i)
        if count > 0:
            for c in range(count):
                mm.append('0')
        for j in a:
            second = lst.index(j)
            mult = (first * second + ost) % 16
            ost = (first * second + ost) // 16
            mm.append(lst[mult])
        if ost > 0:
            mm.append(lst[ost])
        sliced = mm[::-1]
        if pred is None:
            ans = sliced
            pred = sliced
        else:
            ans = addition(sliced, pred)
            pred = sliced
    return ans

print("Результат сложения: ", addition(aa, bb))
print("Результат умножения: ", multiplication(aa, bb))