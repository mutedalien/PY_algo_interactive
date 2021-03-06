# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

init_num = int(input('Введите натуральное число: '))
even_dij = ''   # строка четных чисел
even_count = 0  # количество четных чисел
odd_dij = ''    # строка нечетных чисел
odd_count = 0   # количество енчнтных чисел

while init_num != 0:
    numeral = init_num % 10     # записываем в numeral последнюю цифру числа
    if numeral % 2 == 0:        # проверка на четность
        even_dij += f'{numeral} '
        even_count += 1
    else:
        odd_dij += f'{numeral} '
        odd_count += 1
    init_num = int((init_num - numeral) / 10)   # сдвигаем число на разряд вправо и приводим к типу int

print(f'Количество четных цифр в числе {even_count}: {even_dij}\n'
      f'Количество нечетных цифр в числе {odd_count}: {odd_dij}')