# Измерение времени работы с исползованием cProfile

import cProfile


def get_len(array):
    return len(array)


def get_sum(array):
    s = 0
    for i in array:
        s += i
    return s


def main():
    lst = [i for i in range(100)]
    a = get_len(lst)
    b = get_sum(lst)


cProfile.run('main()')

#          8 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:14(main)
#         1    0.000    0.000    0.000    0.000 main.py:15(<listcomp>)
#         1    0.000    0.000    0.000    0.000 main.py:5(get_len)
#         1    0.000    0.000    0.000    0.000 main.py:8(get_sum)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
