from collections import defaultdict

a = defaultdict()
print(a)

s = 'hgjehgefjgyiwybcfsgegheghgehheblbehggksufhruthfgqehguyegkqu'
b = defaultdict(int)
for i in s:
    b[i] += 1

print(b)

# defaultdict(None, {})
# defaultdict(<class 'int'>, {'h': 9, 'g': 11, 'j': 1, 'e': 9, 'b': 2, 'l': 1, 'f': 1, 'q': 2, 'u': 2, 'y': 1, 'k': 1})

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)

# defaultdict(None, {})
# defaultdict(<class 'int'>, {'h': 10, 'g': 12, 'j': 2, 'e': 9, 'f': 4, 'y': 3, 'i': 1, 'w': 1, 'b': 3, 'c': 1, 's': 2, 'l': 1, 'k': 2, 'u': 4, 'r': 1, 't': 1, 'q': 2})
# defaultdict(<class 'list'>, {'cat': [1, 2], 'dog': [5, 1], 'mouse': [1]})

list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('dog', 1), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)
print(c)

# defaultdict(None, {})
# defaultdict(<class 'int'>, {'h': 10, 'g': 12, 'j': 2, 'e': 9, 'f': 4, 'y': 3, 'i': 1, 'w': 1, 'b': 3, 'c': 1, 's': 2, 'l': 1, 'k': 2, 'u': 4, 'r': 1, 't': 1, 'q': 2})
# defaultdict(<class 'list'>, {'cat': [1, 2], 'dog': [5, 1], 'mouse': [1]})
# defaultdict(<class 'list'>, {'cat': [1, 2], 'dog': [5, 1], 'mouse': [1]})

f = defaultdict(lambda: 'uncnown')
f.update(rex='dog', thomas='cat')
print(f)
print(f['rex'])
print(['jerry'])

# defaultdict(None, {})
# defaultdict(<class 'int'>, {'h': 10, 'g': 12, 'j': 2, 'e': 9, 'f': 4, 'y': 3, 'i': 1, 'w': 1, 'b': 3, 'c': 1, 's': 2, 'l': 1, 'k': 2, 'u': 4, 'r': 1, 't': 1, 'q': 2})
# defaultdict(<class 'list'>, {'cat': [1, 2], 'dog': [5, 1], 'mouse': [1]})
# defaultdict(<class 'list'>, {'cat': [1, 2], 'dog': [5, 1], 'mouse': [1]})
# defaultdict(<function <lambda> at 0x02FA4070>, {'rex': 'dog', 'thomas': 'cat'})
# dog
# ['jerry']
