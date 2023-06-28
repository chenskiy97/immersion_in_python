'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint


def ran(num):
    count = 0
    while count < 10:
        a = int(input('введите чило от 0 до 1000: '))
        if a != num:
            if a >= 0 and a <= 1000:
                if a > num:
                    print('Больше')
                    count += 1
                if a < num:
                    print('Меньше')
                    count += 1
            else: return 'Поражение! (Надо было от 0 до 1000)'
        else: return 'Победа!'
    return ('Поражение! (Закончились попытки)')

print(ran(randint(0, 1000)))
