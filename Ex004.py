from sys import stdin


def rob_bank(n, k, denominations):
    denominations.sort()
    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for i in range(n + 1):
        for denom in denominations:
            if i - denom >= 0:
                dp[i] = min(dp[i], dp[i - denom] + 1)

    if dp[n] == float("inf"):
        return -1, []

    stolen_denominations = []
    while n > 0:
        for denom in denominations:
            if dp[n] == dp[n - denom] + 1:
                stolen_denominations.append(denom)
                n -= denom
                break

    return len(stolen_denominations), stolen_denominations


n, k = map(int, input().split())
denominations = list(map(int, input().split()))

num_banknotes, stolen_denominations = rob_bank(n, k, denominations)

if num_banknotes == -1:
    print(-1)
else:
    print(num_banknotes)
    print(*stolen_denominations)
