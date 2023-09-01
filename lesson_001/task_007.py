def task(num):
    if 0 < num < 10:
        return num ** 2
    elif 9 < num < 100:
        # return sum(int(i) for i in str(num))
        return (num // 10) * (num % 10)
    elif 99 < num < 1000:
        # return int(''.join(i for i in str(num)[::-1])
        return (num % 10 * 100) + (num % 100 // 10 * 10) + (num // 100)
    else:
        return 'Введите другое число'


print(task(int(input('Введите число от 1 до 999: '))))
