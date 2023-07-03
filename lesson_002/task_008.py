'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
'''
import fractions


def sum_mult(a, b, c, d):
    res1 = (a / b) + (c / d)
    res2 = (a / b) * (c / d)
    f1 = fractions.Fraction(a, b)
    f2 = fractions.Fraction(c, d)
    res3 = f1 + f2
    res4 = f1 * f2
    return f'Сумма: {res1}, \n' \
           f'Произведение: {res2}, \n' \
           f'Проверка: (+){res3}, (*){res4}'


num1 = input('Введите числитель первой дроби: ')
num2 = input('Введите знаменатель первой дроби: ')
num3 = input('Введите числитель второй дроби: ')
num4 = input('Введите знаменатель второй дроби: ')

print(sum_mult(int(num1), int(num2), int(num3), int(num4)))
