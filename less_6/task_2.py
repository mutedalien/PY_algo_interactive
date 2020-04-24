lst = []

lst.append(1)
lst.extend([2, 3, 4])

print(lst)

# [1, 2, 3, 4]

lst.insert(1, 5)
print(lst)

# [1, 5, 2, 3, 4]
# Это происходит потому, что:
allocated = 0

for newsize in range(100):
    if allocated < newsize:
        new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)
        allocated = newsize + new_allocated
    print(newsize, allocated)

# 0 0
# 1 4
# 2 4
# 3 4
# 4 4
# 5 8
# ...

last = lst.pop()
print(lst, last)

last = lst.pop()
print(lst, last)

# [1, 5, 2, 3] 4
# [1, 5, 2] 3

lst.remove(5)
print(lst)

# [1, 2]