def find_x(n, m, roads):
    edges = sorted(roads, key=lambda x: x[2])  # Сортируем ребра по весу в порядке неубывания
    min_diff = float('inf')
    parent = list(range(n+1))

    def find_parent(node):
        if parent[node] != node:
            parent[node] = find_parent(parent[node])
        return parent[node]

    # Функция для добавления ребра в остовное дерево
    def add_edge(u, v, w):
        root_u, root_v = find_parent(u), find_parent(v)
        if root_u != root_v:
            parent[root_v] = root_u
            return w, 1  # возвращаем вес добавленного ребра и флаг того, что ребро добавлено в дерево
        return 0, 0  # возвращаем 0 и флаг того, что ребро не добавлено в дерево

    # Находим минимальное остовное дерево по алгоритму Крускала
    tree_weight = 0
    for u, v, w in edges:
        w, added = add_edge(u, v, w)
        if added:
            tree_weight += w

    # Проверяем разность весов для всех вершин исключительно соседних ребер
    for u, v, w in roads:
        if find_parent(u) != find_parent(v):  # Если ребра не лежат в остовном дереве
            diff = abs(w - tree_weight)  # Разность весов
            if diff < min_diff:
                min_diff = diff

    return min_diff

n, m = map(int, input().split())
roads = []
for _ in range(m):
    u, v, w = map(int, input().split())
    roads.append((u, v, w))

result = find_x(n, m, roads)
print(result)





# 5 6
# 1 2 8
# 2 3 6
# 2 3 2
# 3 1 4
# 5 4 1
# 4 5 8