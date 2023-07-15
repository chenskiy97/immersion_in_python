def christmas_tree(height: int):
    for i in range(height):
        print(f'{"*" * (i * 2 + 1):^{height * 2 + 1}}')


christmas_tree(int(input('Введите кол-во строк: ')))
