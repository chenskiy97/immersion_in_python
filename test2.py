# class DisjointSet:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, x, y):
#         px, py = self.find(x), self.find(y)
#
#         if px == py:
#             return False
#
#         if self.rank[px] < self.rank[py]:
#             self.parent[px] = py
#         elif self.rank[px] > self.rank[py]:
#             self.parent[py] = px
#         else:
#             self.parent[py] = px
#             self.rank[px] += 1
#         return True
#
#     def count_sets(self):
#         return sum(1 for i in range(len(self.parent)) if self.parent[i] == i)
#
#
# n, m = 7, 13
# data = [
#     (2, 3, 1),
#     (3, 3),
#     (1, 2, 4),
#     (2, 1, 1),
#     (3, 4),
#     (2, 3, 4),
#     (1, 3, 4),
#     (3, 4),
#     (1, 7, 3),
#     (1, 1, 3),
#     (3, 7),
#     (3, 1),
#     (2, 7, 4),
# ]
#
# dsu = DisjointSet(n)
# for query in data:
#     q, x, *args = query
#     if q == 1:
#         dsu.union(x - 1, args[0] - 1)
#     elif q == 2:
#         print("YES" if dsu.find(x - 1) == dsu.find(args[0] - 1) else "NO")
#     else:
#         print(dsu.rank[dsu.find(x - 1)] + 1)
# #
# # n, m = map(int, input().split())
# # dsu = DisjointSet(n)
# # for i in range(m):
# #     q, x, *args = map(int, input().split())
# #     if q == 1:
# #         dsu.union(x-1, args[0]-1)
# #     elif q == 2:
# #         print("YES" if dsu.find(x-1) == dsu.find(args[0]-1) else "NO")
# #     else:
# #         print(dsu.rank[dsu.find(x-1)] + 1)

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

    def count_sets(self):
        return sum(1 for i in range(len(self.parent)) if self.parent[i] == i)

input_data = '''7 13
2 3 1
3 3
1 2 4
2 1 1
3 4
2 3 4
1 3 4
3 4
1 7 3
1 1 3
3 7
3 1
2 7 4'''

lines = input_data.split('\n')

n, m = map(int, lines[0].split())
dsu = DisjointSet(n)
for i in range(1, len(lines)):
    q, x, *args = map(int, lines[i].split())
    if q == 1:
        dsu.union(x-1, args[0]-1)
    elif q == 2:
        print("YES" if dsu.find(x-1) == dsu.find(args[0]-1) else "NO")
    else:
        print(dsu.rank[dsu.find(x-1)])



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
