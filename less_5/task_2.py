from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

# deque([])
# deque(['a', 'b', 'c', 'd', 'e', 'f'])
# deque([1, 2, 3, 4, 5])

b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
c.clear()
print(b, c, sep='\n')

# deque([])
# deque(['a', 'b', 'c', 'd', 'e', 'f'])
# deque([1, 2, 3, 4, 5])
# deque(['d', 'e', 'f'], maxlen=3)
# deque([], maxlen=4)

print('*' * 50)
d = deque([i for i in range(5)])
d.append(5)
d.appendleft(6)
print(d)

# deque([])
# deque(['a', 'b', 'c', 'd', 'e', 'f'])
# deque([1, 2, 3, 4, 5])
# deque(['d', 'e', 'f'], maxlen=3)
# deque([], maxlen=4)
# **************************************************
# deque([6, 0, 1, 2, 3, 4, 5])

d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

# deque([])
# deque(['a', 'b', 'c', 'd', 'e', 'f'])
# deque([1, 2, 3, 4, 5])
# deque(['d', 'e', 'f'], maxlen=3)
# deque([], maxlen=4)
# **************************************************
# deque([6, 0, 1, 2, 3, 4, 5])
# deque([12, 11, 10, 6, 0, 1, 2, 3, 4, 5, 7, 8, 9])

print('*' * 50)
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')

# deque([])
# deque(['a', 'b', 'c', 'd', 'e', 'f'])
# deque([1, 2, 3, 4, 5])
# deque(['d', 'e', 'f'], maxlen=3)
# deque([], maxlen=4)
# **************************************************
# deque([6, 0, 1, 2, 3, 4, 5])
# deque([12, 11, 10, 6, 0, 1, 2, 3, 4, 5, 7, 8, 9])
# **************************************************
# deque([1, 2, 3], maxlen=7)
# 4
# 0

print('*' * 50)
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)

# deque([])
# deque(['a', 'b', 'c', 'd', 'e', 'f'])
# deque([1, 2, 3, 4, 5])
# deque(['d', 'e', 'f'], maxlen=3)
# deque([], maxlen=4)
# **************************************************
# deque([6, 0, 1, 2, 3, 4, 5])
# deque([12, 11, 10, 6, 0, 1, 2, 3, 4, 5, 7, 8, 9])
# **************************************************
# deque([1, 2, 3], maxlen=7)
# 4
# 0
# **************************************************
# 1
# 3
# deque([0, 1, 6, 2, 3, 4], maxlen=7)

g.reverse()
print(g)

g.rotate(3)
print(g)

# deque([0, 1, 6, 2, 3, 4], maxlen=7)
# deque([4, 3, 2, 6, 1, 0], maxlen=7)
# deque([6, 1, 0, 4, 3, 2], maxlen=7)

import random

array = [random.randint(-100, 100) for _ in range(10)]
print(array)

deq = deque()

for item in array:

    if item > 0:
        deq.append(item)
    elif item < 0:
        deq.appendleft(item)

print(deq)

# [-73, -97, 18, -55, -4, -39, -55, -11, -45, -65]
# deque([-65, -45, -11, -55, -39, -4, -55, -97, -73, 18])
