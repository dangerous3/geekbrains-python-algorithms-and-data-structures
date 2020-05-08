# Графы: Поиск кратчайшего пути в ширину (BFS, Breadth-First Search)

from collections import deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]

def bfs(graph, start, finish):
    # первый этап алгоритма
    parent = [None for _ in range(len(graph))] # родитель для каждой вершины
    is_visited = [False for _ in range(len(graph))] # были ли мы уже в данной вершине

    deq = deque([start]) # помещаем в начало очереди стартовую вершину
    is_visited[start] = True

    # второй этап алгоритма
    while len(deq) > 0:
        current = deq.pop()

        # этап алгоритма 2а
        if current == finish:
            # return parent
            break
        # этап алгоритма 2b
        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)

    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0 # стоимость пути
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'Кратчайший путь: {list(way)} длиною в {cost} условных единиц'


s = int(input('От какой вершины идти: '))
f = int(input('До какой вершины идти: '))
print(bfs(g, s, f))