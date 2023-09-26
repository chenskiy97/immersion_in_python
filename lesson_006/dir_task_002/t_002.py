from random import randint


def ran(min_num, max_num, count):
    numbers = randint(min_num, max_num + 1)
    cnt = 0

    while cnt < count:
        num = int(input(f'Осталось попыток: {count - cnt}. Введите число: '))
        if num == numbers:
            print(f'Вы угадали число {num} за {cnt+1} попыток')
            break
        elif num < numbers:
            print(f'Число меньше загаданного')
        elif num > numbers:
            print(f'Число больше загаданного')
        else:
            continue
        cnt += 1
    else:
        print(f'Вы не угадали число {numbers} за {count} раз')
    return f'Поражение! (Закончились попытки, было загадано {num})'
