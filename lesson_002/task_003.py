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
