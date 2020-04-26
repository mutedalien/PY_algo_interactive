import hashlib


def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми!'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'hash 1 = {ha}\nhash 2 = {hb}')

    return ha == hb


s_1 = input('Введите строку 1: ')
s_2 = input('Введите строку 2: ')

print('Строки одинаковые' if is_eq_str(s_1, s_2, True) else 'Строки разные')

# Введите строку 1: efjkbh;ejkabh
# Введите строку 2: kjegh;jeb'aeb
# hash 1 = 10697a541da8d81027dfccec8b13f327f792e16c
# hash 2 = 708d610e2a9b7f09ae7e58ebf8259481d61cf8a4
# Строки разные
