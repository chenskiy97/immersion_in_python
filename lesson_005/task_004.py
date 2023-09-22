'''
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
'''

# my_gen = (i for i in range(0, 101, 2) if sum(list(map(int, str(i)))) != 8)
#
# print(my_gen)
#
# for char in my_gen:
#     print(char, end=' ')

print(*(x for x in range(0, 101, 2) if x // 10 + x % 10 != 8))
print(*(x for x in range(0, 101, 2) if sum(map(int, str(x))) != 8))
