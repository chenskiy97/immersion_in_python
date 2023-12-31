'''
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
'''


def func(lst: list[int], lower: int, upper: int):
    lower, upper = sorted([lower, upper])
    return sum(lst[lower:upper+1])


print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 100, -55))
