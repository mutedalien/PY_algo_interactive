# Те же операнды, но другая история

a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7]
print(a, b)

a = [1, 2, 3, 4]
b = a
a += [5, 6, 7]
print(a, b)


# [1, 2, 3, 4, 5, 6, 7] [1, 2, 3, 4]
# [1, 2, 3, 4, 5, 6, 7] [1, 2, 3, 4, 5, 6, 7]
