def christmas_tree(rows):
    spaces = rows - 1
    stars = 1

    for i in range(rows):
        print((' ' * spaces) + ('*' * stars) + (' ' * spaces))
        stars += 2
        spaces -= 1


christmas_tree(int(input('Введите кол-во строк: ')))
