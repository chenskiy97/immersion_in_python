'''
n, m = map(int, input().split())
edges = {}
for _ in range(m):
    v, u, w = map(int, input().split())
    if v not in edges:
        edges[v] = []
    if u not in edges:
        edges[u] = []
    edges[v].append(w)
    edges[u].append(w)

states_before = len(edges)

lo = 0
hi = 10**9
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    temp_edges = {}
    for v in edges:
        temp_edges[v] = [w for w in edges[v] if w > mid]
    components = 0
    visited = set()

    def dfs(v):
        if v in visited:
            return
        visited.add(v)
        for u in temp_edges[v]:
            dfs(u)

    for v in edges:
        if v not in visited:
            components += 1
            dfs(v)

    if components == states_before:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
'''

# Считываем необходимую сумму и количество номиналов купюр
n, m = map(int, input().split())

# Считываем номиналы купюр и создаем словарь для их хранения
nominals = list(map(int, input().split()))
nominals_dict = {}

# Заполняем словарь номиналами купюр и подсчитываем их количество
for nominal in nominals:
    if nominal not in nominals_dict:
        nominals_dict[nominal] = 1
    else:
        nominals_dict[nominal] += 1

# Создаем список для хранения украденных купюр
stolen_nominals = []

# Перебираем номиналы купюр и пытаемся украсть нужную сумму
for nominal in nominals:
    if n <= 0:
        break
    if nominals_dict[nominal] >= 2 and n - nominal >= 0:
        stolen_nominals.extend([nominal, nominal])
        n -= nominal * 2
    elif nominals_dict[nominal] >= 1 and n - nominal >= 0:
        stolen_nominals.append(nominal)
        n -= nominal

# Если получилось украсть нужную сумму, выводим результат
if n == 0:
    print(len(stolen_nominals))
    print(*stolen_nominals)
else:
    print(-1)
