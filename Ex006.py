# Функция для проверки, являются ли два множества a и b одинаковой цветности
def same_color(a, b):
    return len(set(a)) == len(set(b)) and len(set(a) | set(b)) == len(set(a))

# Функция для считывания входных данных
def read_input():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    edges = []
    for i in range(m):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
    return n, m, colors, edges

n, m, colors, edges = read_input()

# Словарь, каждому цвету ставим в соответствие множество вершин этого цвета
color_to_vertices = {}
for i in range(1, n+1):
    color_to_vertices[colors[i-1]] = color_to_vertices.get(colors[i-1], set()) | {i}

# Словарь, каждой паре вершин ставим в соответствие цвет этих вершин
vertex_to_color = {}
for u, v, c in edges:
    vertex_to_color[(u, v)] = vertex_to_color.get((u, v), c)

# Проверяем, являются ли вершины i и j смежными
def are_adjacent(i, j):
    return any(c == vertex_to_color.get((i, j), 0) for c in color_to_vertices)

# Выполняем запросы
for i in range(int(input())):
    a, b, c = map(int, input().split())
    if same_color(color_to_vertices[c], set((a, b))) and are_adjacent(a, b):
        print("YES")
    else:
        print("NO")


# 7 13
# 2 3 1
# 3 3
# 1 2 4
# 2 1 1
# 3 4
# 2 3 4
# 1 3 4
# 3 4
# 1 7 3
# 1 1 3
# 3 7
# 3 1
# 2 7 4