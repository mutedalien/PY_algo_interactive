# Функция Фибоначчи
import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i) # assert сравнивает значение переменной item и значение func(i)
        print(f'Test {i} OK')

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# cProfile.run('fib(15)')
#          1976 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    1973/1    0.001    0.000    0.001    0.001 main.py:10(fib)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#

#cProfile.run('fib(20)')
#          21894 function calls (4 primitive calls) in 0.010 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#   21891/1    0.010    0.000    0.010    0.010 main.py:10(fib)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# test_fib(fib)
