# Алгоритм Дейкстры (поиск кратчайшего пути на взвешенном графе)

g = [
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
    length = len(graph) # длина графа
    is_visited = [False] * length # посещали вершину или нет
    cost = [float('inf')] * length # стоимость пути до конкретной вершины (по умолчанию - бесконечность)
    parent = [-1] * length

    cost[start] = 0 # стоимость пути до стартовой вершины
    min_cost = 0 # минимальная стоимость (двигаемся мы далее по графу или уже нет)

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost

s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))
