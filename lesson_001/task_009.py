for i in range(2, 11):
    for j in range(2, 6):
        print(f'{j:^3} * {i:^3} = {(j * i):^3}\t', end="")
    print()
print()
for x in range(2, 11):
    for y in range(6, 10):
        print(f'{y:^3} * {x:^3} = {(y * x):^3}\t', end="")
    print()