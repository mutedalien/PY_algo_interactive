# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.



graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    lenght = len(graph)
    is_visited = [False] * lenght
    cost = [float('inf')] * lenght
    parent = [-1] * lenght
    cost[start] = 0
    min_cost = 0
    parents=[]
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    # print(start, i, cost[i])
                    parent[i] = start
                    print(parent)
                    parents.append(parent)  # Затрудняюсь найти на текущий момент способ как раскидать parent по
                    # необходимым элементам в соответствии с минимальным весом

        min_cost = float('inf')
        for i in range(lenght):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return cost, parents


start = int(input('Введите начальную вершину: '))
print(dijkstra(graph, start))
