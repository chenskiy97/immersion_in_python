# Задание №4
# Работа в консоли в режиме интерпретатора Python.
# Решите квадратное уравнение 5x2-10x-400=0 последовательно сохраняя переменные a, b, c, d, x1 и x2.
# *Попробуйте решить уравнения с другими значениями a, b, c

def the_quadratic_equation(a, b, c):
    print(f'{a}x2 + {b}x {c} = 0')
    d = (b ** 2) - (4 * a * c)
    print(f"Дискриминант = {d}")
    if d > 0:
        return f'x1 = {(-b + (d ** 0.5)) / (2 * a)}, x2 = {(-b - (d ** 0.5)) / (2 * a)}'
    elif d == 0:
        return f'x1 = {(-b / (2 * a))}'
    else:
        return 'Корней нет!'


print(the_quadratic_equation(float(input("a = ")),
                             float(input("b = ")),
                             float(input("c = "))))
