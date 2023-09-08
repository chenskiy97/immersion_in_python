'''
Для решения данной задачи можно использовать алгоритм Дейкстры. Введем массив dp[1…n], где dp[i] - это количество дорог длины i, которые ведут в город i. Также инициализируем dp[0] = 1.

Затем для каждого города i выполним следующие действия:

Найдем количество дорог длины x, которые ведут из города i. Для этого используем формулу dp[i - x] + dp[i + x].
Если полученное значение больше или равно 0, то увеличиваем dp[i].
Если dp[i] > dp[j] для всех j, то добавляем город i в штат.
После того, как все города будут обработаны, выберем максимальное значение dp[i], которое соответствует количеству дорог, уничтоженных духом Чогэном.
'''
from collections import deque

# Функция для выполнения обхода в ширину, возвращает количество компонент связности
def bfs(d, max_dist):
    count = 0
    visited = [False] * len(d)
    for i in range(len(d)):
        if not visited[i]:
            count += 1
            queue = deque([i])
            visited[i] = True
            while queue:
                u = queue.popleft()
                for v, w in d[u]:
                    if w <= max_dist and not visited[v]:
                        queue.append(v)
                        visited[v] = True
    return count

n, m = map(int, input().split())
# Создаем список смежности для хранения графа
d = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    d[u - 1].append((v - 1, w))
    d[v - 1].append((u - 1, w))

# Ищем наименьшее значение x при котором количество штатов не изменится
lo, hi = 0, max(w for adj in d for _, w in adj)
while lo < hi:
    mid = (lo + hi + 1) // 2  # Мы округляем до ближайшей верхней целой
    if bfs(d, mid) == n - 1:  # Мы ищем n - 1 компонент связности
        lo = mid
    else:
        hi = mid - 1

print(lo)



# 5 6
# 1 2 8
# 2 3 6
# 2 3 2
# 3 1 4
# 5 4 1
# 4 5 8

