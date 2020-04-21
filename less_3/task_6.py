# Ключ словаря - изменяемый объект

set_x = {1, 2, 3}
lst_x = [1, 4, 9]
dict_x = {frozenset(set_x): lst_x}
dict_y = {tuple(lst_x): set_x}
