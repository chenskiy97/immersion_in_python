def winning_sequence(n, a, b):
    l, r = 0, n - 1
    while l < n and a[l] == b[l]:
        l += 1
    while r >= 0 and a[r] == b[r]:
        r -= 1
    if sorted(a[l:r + 1]) == b[l:r + 1]:
        return "YES"
    else:
        return "NO"


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = winning_sequence(n, a, b)
print(result)
