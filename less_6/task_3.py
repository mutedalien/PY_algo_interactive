import sys

print(sys.version, sys.platform)

# 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] win32

a = 5
b = 125.54
c = 'Hello World'

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

# 14
# 16
# 36

lst = [i for i in range(10)]
print(sys.getsizeof(lst))


# 92

def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


show_size(a)
show_size(b)
show_size(c)
show_size(lst)

#  type= <class 'int'>, size= 14, object= 5
#  type= <class 'float'>, size= 16, object= 125.54
#  type= <class 'str'>, size= 36, object= Hello World
#  type= <class 'list'>, size= 92, object= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 	 type= <class 'int'>, size= 12, object= 0
# 	 type= <class 'int'>, size= 14, object= 1
# 	 type= <class 'int'>, size= 14, object= 2
# 	 type= <class 'int'>, size= 14, object= 3
# 	 type= <class 'int'>, size= 14, object= 4
# 	 type= <class 'int'>, size= 14, object= 5
# 	 type= <class 'int'>, size= 14, object= 6
# 	 type= <class 'int'>, size= 14, object= 7
# 	 type= <class 'int'>, size= 14, object= 8
# 	 type= <class 'int'>, size= 14, object= 9

print('*' * 50)
t = tuple(lst)
show_size(t)

# **************************************************
#  type= <class 'tuple'>, size= 60, object= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 	 type= <class 'int'>, size= 12, object= 0
# 	 type= <class 'int'>, size= 14, object= 1
# 	 type= <class 'int'>, size= 14, object= 2
# 	 type= <class 'int'>, size= 14, object= 3
# 	 type= <class 'int'>, size= 14, object= 4
# 	 type= <class 'int'>, size= 14, object= 5
# 	 type= <class 'int'>, size= 14, object= 6
# 	 type= <class 'int'>, size= 14, object= 7
# 	 type= <class 'int'>, size= 14, object= 8
# 	 type= <class 'int'>, size= 14, object= 9

print('*' * 50)
s = set(lst)
show_size(s)

# **************************************************
#  type= <class 'set'>, size= 364, object= {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# 	 type= <class 'int'>, size= 12, object= 0
# 	 type= <class 'int'>, size= 14, object= 1
# 	 type= <class 'int'>, size= 14, object= 2
# 	 type= <class 'int'>, size= 14, object= 3
# 	 type= <class 'int'>, size= 14, object= 4
# 	 type= <class 'int'>, size= 14, object= 5
# 	 type= <class 'int'>, size= 14, object= 6
# 	 type= <class 'int'>, size= 14, object= 7
# 	 type= <class 'int'>, size= 14, object= 8
# 	 type= <class 'int'>, size= 14, object= 9

print('*' * 50)
d = {str(i): i for i in range(10)}
show_size(d)

# **************************************************
#  type= <class 'dict'>, size= 196, object= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	 type= <class 'tuple'>, size= 28, object= ('0', 0)
# 		 type= <class 'str'>, size= 26, object= 0
# 		 type= <class 'int'>, size= 12, object= 0
# 	 type= <class 'tuple'>, size= 28, object= ('1', 1)
# 		 type= <class 'str'>, size= 26, object= 1
# 		 type= <class 'int'>, size= 14, object= 1
# 	 type= <class 'tuple'>, size= 28, object= ('2', 2)
# 		 type= <class 'str'>, size= 26, object= 2
# 		 type= <class 'int'>, size= 14, object= 2
# 	 type= <class 'tuple'>, size= 28, object= ('3', 3)
# 		 type= <class 'str'>, size= 26, object= 3
# 		 type= <class 'int'>, size= 14, object= 3
# 	 type= <class 'tuple'>, size= 28, object= ('4', 4)
# 		 type= <class 'str'>, size= 26, object= 4
# 		 type= <class 'int'>, size= 14, object= 4
# 	 type= <class 'tuple'>, size= 28, object= ('5', 5)
# 		 type= <class 'str'>, size= 26, object= 5
# 		 type= <class 'int'>, size= 14, object= 5
# 	 type= <class 'tuple'>, size= 28, object= ('6', 6)
# 		 type= <class 'str'>, size= 26, object= 6
# 		 type= <class 'int'>, size= 14, object= 6
# 	 type= <class 'tuple'>, size= 28, object= ('7', 7)
# 		 type= <class 'str'>, size= 26, object= 7
# 		 type= <class 'int'>, size= 14, object= 7
# 	 type= <class 'tuple'>, size= 28, object= ('8', 8)
# 		 type= <class 'str'>, size= 26, object= 8
# 		 type= <class 'int'>, size= 14, object= 8
# 	 type= <class 'tuple'>, size= 28, object= ('9', 9)
# 		 type= <class 'str'>, size= 26, object= 9
# 		 type= <class 'int'>, size= 14, object= 9
