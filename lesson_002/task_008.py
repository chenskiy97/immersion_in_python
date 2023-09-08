'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
'''
import fractions


def sum_fractions(n1, d1, n2, d2):
    if d1 == d2:
        return f'{n1 + n2}/{d1}'
    else:
        common = d1 * d2
        n1 *= d2
        n2 *= d1
        return reduce_fraction(n1 + n2, common)


def mult_fractions(n1, d1, n2, d2):
    return reduce_fraction(n1 * n2, d1 * d2)


def reduce_fraction(n, d):
    gcd_val = gcd(n, d)
    return f'{n // gcd_val}/{d // gcd_val}'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


numerator1, denominator1 = map(int, input('Введите первую дробь: ').split('/'))
numerator2, denominator2 = map(int, input('Введите вторую дробь: ').split('/'))

summ = sum_fractions(numerator1, denominator1, numerator2, denominator2)
mult = mult_fractions(numerator1, denominator1, numerator2, denominator2)

f1 = fractions.Fraction(numerator1, denominator1)
f2 = fractions.Fraction(numerator2, denominator2)

print(f'Сумма: {summ} \n'
      f'Произведение: {mult} \n'
      f'Проверка: (+){f1 + f2}, (*){f1 * f2}')

# import fractions
#
#
# def sum_mult(a, b, c, d):
#     res1 = (a / b) + (c / d)
#     res2 = (a / b) * (c / d)
#     f1 = fractions.Fraction(a, b)
#     f2 = fractions.Fraction(c, d)
#     res3 = f1 + f2
#     res4 = f1 * f2
#     return f'summ: {res1}, \n' \
#            f'Произведение: {res2}, \n' \
#            f'Проверка: (+){res3}, (*){res4}'
#
#
# num1 = input('Введите числитель первой дроби: ')
# num2 = input('Введите знаменатель первой дроби: ')
# num3 = input('Введите числитель второй дроби: ')
# num4 = input('Введите знаменатель второй дроби: ')
#
# print(sum_mult(int(num1), int(num2), int(num3), int(num4)))
