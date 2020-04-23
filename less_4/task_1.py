# Измерение времени работы с исползованием timeit

import timeit

x = 2 + 2
print(timeit.timeit('x = 2 + 2'))
print(timeit.timeit('x = sum(range(10))'))

# 0.017706
# 0.7737179000000001