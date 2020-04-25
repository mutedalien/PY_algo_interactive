# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?

from functools import reduce

n = int(input('Сколько встретилось друзей: '))
graph = [[int(i > j) for i in range(n)] for j in range(n)]
count = reduce(lambda acc, x: acc + sum(x), graph, 0)
print(f'Количество рукопожатий:  {count}')