'''
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
варианты и выведите 4 успешных расстановки.
'''
import random


def check_queens(x, y):
    n = 8
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


x_coords = list(range(1, 9))
y_coords = list(range(1, 9))

random.shuffle(x_coords)
random.shuffle(y_coords)

print(x_coords)
print(y_coords)

print(check_queens(x_coords, y_coords))
