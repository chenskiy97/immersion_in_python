'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint


def ran(num: int) -> str:
    count = 1
    while count <= 10:
        a = int(input(f'Попытка: {count}/10. Введите число от 0 до 1000: '))
        if 0 > a > 1000:
            return f'Поражение! (Надо было от 0 до 1000)'
        elif a == num:
            return f'Победа! (Количество попыток: {count})'
        elif a < num:
            print('Меньше')
        else:
            print('Больше')
        count += 1
    return f'Поражение! (Закончились попытки, было загадано {num})'


print(ran(randint(0, 1000)))
