def task(num):
    if num > 0 and num < 10:
        return num ** 2
    elif num > 9 and num < 100:
        return sum(int(i) for i in str(num))
    elif num > 99 and num < 1000:
        return int(''.join(i for i in str(num)[::-1]))
    else: return 'Введите другое чило'


print(task(int(input('Введите чиcло от 1 до 999: '))))
