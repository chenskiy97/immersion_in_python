'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

LETTERS = '0123456789ABCDF'

def transfer(num: int, base: int) -> str:
    print(f'Проверка в разных системах: {bin(num), oct(num), hex(num)}')
    result = ''
    while num > 0:
        result = LETTERS[num % base] + result
        num //= base
    if base == 2:
        return f'0b{result}'
    elif base == 8:
        return f'0o{result}'
    elif base == 16:
        return f'0x{result}'
    else:
        return f'{base} - система счисления {result}'


print(transfer(int(input('Введите число (int): ')), int(input('Введите систему в которую хотите перевести (int): '))))