def revolver_for_joe(n, s, prices):
    result = 0
    for i in prices:
        if s >= i > result:
            result = i
    return result


n, s = map(int, input().split())

rev_prices = list(map(int, input().split()))

kindest_revolver = revolver_for_joe(n, s, rev_prices)
print(kindest_revolver)
