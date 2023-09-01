# def traffic(a: int, b: int, c: int, d: int) -> int:
#     return (a + (d - b) * c) if b < d else a
#
#
# a, b, c, d = input('Введите значения:').split()
# a, b, c, d = int(a), int(b), int(c), int(d)
# print(traffic(a, b, c, d))

# def roulette(n):
#     count = 0
#     while n > 1:
#         if n % 2 != 0:
#             count += 1
#         n = n // 2
#         count += 1
#     return count
#
#
# N = int(input())
# print(roulette(N))

#
# n = int(input())
# e = 0
# p = 1
# while p < n:
#     e += 1
#     p *= 2
# print(e)

# from functools import reduce
#
# numbers = [
#     input(),
#     input()
# ]
# result = reduce(lambda x, y: x + y, map(lambda i: int(i), numbers))
# print(result)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# result = (a + (d - b) * c) if b < d else a
# print(result)
# print((a + (d - b) * c) if b < d else a)

# numbers = input().split()
# a, b, c, d = map(lambda i: int(i), numbers)
# result = (a + (d - b) * c) if b < d else a
# print(result)

#
# n, t = input().split()
# floors = input().split()
# num = int(input())
#
# n, t = int(n), int(t)
# floors = list(map(int, floors))

a, b = int(input()), int(input())
result = a + b
print(result)
