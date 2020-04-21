# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

# явная сумма ряда
def summ1(n):
    if n == 1:
        return 1
    return n + summ1(n-1)

# формула суммы арифметческой прогрессии
def summ2(n):
    return int(n * (n + 1) / 2)

n = int(input('Введите n: '))

print(f'Сравните значения: {summ1(n)} и {summ2(n)}, и сделайте для себя выводы о сущности бытия')