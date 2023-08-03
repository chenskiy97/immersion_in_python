
def traffic(a: int, b: int, c: int, d: int) -> int:
    return (a + c * (d - b)) if b < d else a


a, b, c, d = input('Введите значения:').split()
a, b, c, d = int(a), int(b), int(c), int(d)
print(traffic(a, b, c, d))



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
# print(roulette(int(input('Введите число:'))))
