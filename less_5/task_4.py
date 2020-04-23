from collections import OrderedDict

a = {'cat': 5, 'mouse': 4, 'dog': 2}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])

b = {'cat': 5, 'mouse': 4, 'dog': 2}
new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(new_b)

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])

print(new_a == new_b)

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])
# False

new_b.move_to_end('mouse', last=False)
print(new_b)

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])
# False
# OrderedDict([('mouse', 4), ('dog', 2), ('cat', 5)])

new_b.popitem(last=False)
print(new_b)

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])
# False
# OrderedDict([('mouse', 4), ('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5)])

new_b['cow'] = 1
print(new_b)

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])
# False
# OrderedDict([('mouse', 4), ('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5), ('cow', 1)])

new_b['dog'] = 8
print(new_b)

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])
# False
# OrderedDict([('mouse', 4), ('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5), ('cow', 1)])
# OrderedDict([('dog', 8), ('cat', 5), ('cow', 1)])

print('*' * 50)
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
print(new_c)

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])
# False
# OrderedDict([('mouse', 4), ('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5), ('cow', 1)])
# OrderedDict([('dog', 8), ('cat', 5), ('cow', 1)])
# **************************************************
# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])

for key in reversed(new_c):
    print(key, new_c[key])

# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# OrderedDict([('dog', 2), ('mouse', 4), ('cat', 5)])
# False
# OrderedDict([('mouse', 4), ('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5)])
# OrderedDict([('dog', 2), ('cat', 5), ('cow', 1)])
# OrderedDict([('dog', 8), ('cat', 5), ('cow', 1)])
# **************************************************
# OrderedDict([('cat', 5), ('dog', 2), ('mouse', 4)])
# mouse 4
# dog 2
# cat 5