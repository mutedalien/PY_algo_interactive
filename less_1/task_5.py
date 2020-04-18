a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
c = int(input("Введите целое число c: "))

if a > b:
    if a > c:
        print(f'Максимум = {a}')
    else:
        print(f'Максимум = {c}')
else:
    if b > c:
        print(f'Максимум = {b}')
    else:
        print(f'Максимум = {c}')