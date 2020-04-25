# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).

# Задача пройти по всем вершинам вглубь один раз.
def graph(n):  # Функция генерации графа
    graph = {}
    for i in range(n):
        element = []
        for j in range(n):
            if i != j:
                element.append(j)
        graph[i] = element
    return graph


n = int(input('Введите число вершин системы: '))
graph = graph(n)
print(graph)

visited = set()


def dfs(visited, graph, node):  # Функция прохождения по вершинам графа
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, 0)
