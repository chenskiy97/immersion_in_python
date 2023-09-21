'''
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''


# def func(s):
#     res = []
#     for i in set(s):
#         res.append(ord(i))
#     res.sort(reverse=True)
#     return res


def func(s):
    return [ord(i) for i in sorted(list(set(s)), reverse=True)]


data = ('Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode '
        'каждого символа введённой строки отсортированный по убыванию.')
print(func(data))