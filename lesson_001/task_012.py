'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def ran(num: int) -> str:
    count = 1
    while count <= 10:
        a = int(input(f'Попытка: {count}/10. Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
        if LOWER_LIMIT > a > UPPER_LIMIT:
            return f'Поражение! (Надо было от 0 до 1000)'
        elif a == num:
            return f'Победа! (Количество попыток: {count})'
        elif a < num:
            print('Меньше')
        else:
            print('Больше')
        count += 1
    return f'Поражение! (Закончились попытки, было загадано {num})'


print(ran(randint(LOWER_LIMIT, UPPER_LIMIT)))
