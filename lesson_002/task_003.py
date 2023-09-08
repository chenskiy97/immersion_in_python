'''
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно
'''


def convert(num: int, base: int) -> str:
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        result = LETTERS[num % base] + result
        num //= base
    return result


LETTERS = '0123456789ABCDF'
BASE_BIN = 2
BASE_OCT = 8
num = int(input('Введите число (int): '))
binary = convert(num, BASE_BIN)
octal = convert(num, BASE_OCT)
print(f'\nПроверка в разных системах: {bin(num), oct(num)}\n')
print(f'0b{binary}')
print(f'0x{octal}')

# LETTERS = '0123456789ABCDF'
#
#
# def transfer(num: int, base: int) -> str:
#     print(f'Проверка в разных системах: {bin(num), oct(num), hex(num)}')
#     if num == 0:
#         result = '0'
#     else:
#         result = ''
#     while num > 0:
#         result = LETTERS[num % base] + result
#         num //= base
#     if base == 2:
#         return f'0b{result}'
#     elif base == 8:
#         return f'0o{result}'
#     elif base == 16:
#         return f'0x{result}'
#     else:
#         return f'{base} - система счисления {result}'
#
#
# res = transfer(int(input('Введите число (int): ')),
#                int(input('Введите систему в которую хотите перевести (int): ')))
# print(res)
