'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''


def hex_convert(num: int, base: int) -> str:
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        result = LETTERS[num % base] + result
        num //= base
    return result


LETTERS = '0123456789ABCDF'
BASE_HEX = 16
num = int(input('Ведите число: '))
hex_num = hex_convert(num, BASE_HEX)
print(f'Проверка {hex(num)}\n'
      f'Ответ: 0x{hex_num}')

# LETTERS = '0123456789ABCDF'
#
# def transfer(num: int, base: int) -> str:
#     print(f'Проверка в разных системах: {bin(num), oct(num), hex(num)}')
#     result = ''
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
# print(transfer(int(input('Введите число (int): ')), int(input('Введите систему в которую хотите перевести (int): '))))
