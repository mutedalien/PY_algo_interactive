# Модуль Collections

from collections import Counter

a = Counter()
b = Counter('abracadabra')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')

# Counter()
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'blue': 4, 'red': 2})
# Counter({'dogs': 5, 'cats': 4})

print(b['z'])
b['z'] = 0
print(b)
print(list(b.elements()))
print(b.most_common(2))

# Counter()
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'blue': 4, 'red': 2})
# Counter({'dogs': 5, 'cats': 4})
# 0
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'z': 0})
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
# [('a', 5), ('b', 2)]

g = Counter(a=4, b=6, c=2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
print(g)

# Counter()
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'blue': 4, 'red': 2})
# Counter({'dogs': 5, 'cats': 4})
# 0
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'z': 0})
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
# [('a', 5), ('b', 2)]
# Counter({'b': 6, 'a': 4, 'c': 2, 'd': 0})
#
# Process finished with exit code 0

print('*' * 50)
print(set(g))
print(dict(g))
g.clear()
print(g)

# Counter()
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'blue': 4, 'red': 2})
# Counter({'dogs': 5, 'cats': 4})
# 0
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'z': 0})
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
# [('a', 5), ('b', 2)]
# Counter({'b': 6, 'a': 4, 'c': 2, 'd': 0})
# **************************************************
# {'a', 'c', 'b', 'd'}
# {'a': 4, 'b': 6, 'c': 2, 'd': 0}
# Counter()
#
# Process finished with exit code 0

print('*' * 50)
x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x + y)
print(x - y)
print(x & y)
print(x | y)

# Counter()
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'blue': 4, 'red': 2})
# Counter({'dogs': 5, 'cats': 4})
# 0
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'z': 0})
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
# [('a', 5), ('b', 2)]
# Counter({'b': 6, 'a': 4, 'c': 2, 'd': 0})
# **************************************************
# {'c', 'a', 'd', 'b'}
# {'a': 4, 'b': 6, 'c': 2, 'd': 0}
# Counter()
# **************************************************
# Counter({'a': 4, 'b': 3})
# Counter({'a': 2})
# Counter({'a': 1, 'b': 1})
# Counter({'a': 3, 'b': 2})
#
# Process finished with exit code 0
