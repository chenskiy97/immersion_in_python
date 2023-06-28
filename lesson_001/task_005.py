def solution(n, e):
    return ', '.join(str(int(x)) for x in range(n + 1) if x % e != 0)


print(solution(20, 3))

# Решал на codewars похожее когда-то :))