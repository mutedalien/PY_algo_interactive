# 9. Среди натуральных чисел, которые были введены, найти наибольшее
# по сумме цифр. Вывести на экран это число и сумму его цифр.


def num_summ(n):
    summ = 0
    while n != 0:
        summ += n % 10
        n = (n - n % 10) / 10
    return int(summ)


great = 0  # тут будет наибольшее по сумме цифр число
num_great = 0  # тут сумма цифр этого числа

a = int(input('Введите количество чисел: '))

for i in range(a):
    n = int(input(f'Ведите {i + 1} число: '))
    if num_summ(n) > num_great:
        great = n
        num_great = num_summ(n)

print(f'Число {great} наибольше по сумме цифр.'
      f'Сумма цифр: {num_great}')
