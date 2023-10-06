'''
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
'''


def the_quadratic_equation(a, b, c):
    print(f'{a}x2 + {b}x {c} = 0')
    d = (b ** 2) - (4 * a * c)
    print(f"Дискриминант = {d}")
    if d > 0:
        return f'x1 = {(-b + (d ** 0.5)) / (2 * a)}, x2 = {(-b - (d ** 0.5)) / (2 * a)}'
    elif d == 0:
        return f'x1 = {(-b / (2 * a))}'
    else:
        d = complex((b ** 2) - (4 * a * c))
        return f' Комплексные корни: x1 = {(-b + (d ** 0.5)) / (2 * a)}, x2 = {(-b - (d ** 0.5)) / (2 * a)}'


print(the_quadratic_equation(float(input("a = ")),
                             float(input("b = ")),
                             float(input("c = "))))
