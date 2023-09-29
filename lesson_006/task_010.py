'''
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите
код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг
друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если
бьют - ложь.
'''


def check_queens(x, y):
    n = 8
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


x_coords = [8, 1, 2, 3, 4, 5, 6, 7]
y_coords = [8, 3, 1, 7, 5, 2, 4, 6]

print(check_queens(x_coords, y_coords))

