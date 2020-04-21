# Удаление элемента списка во время его этерирования

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for i, item in enumerate(list_1):
    del item

print(list_1)

for i, item in enumerate(list_2):
    list_2.remove(item)

print(list_2)

for i, item in enumerate(list_3):
    list_3.pop(i)

print(list_3)

for i, item in enumerate(list_4[:]):
    list_4.remove(item)

print(list_4)
