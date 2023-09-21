'''
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''


def my_sort(lst):
    for i in range(1, len(lst)):
        for j in range(len(lst) - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


lstt = [10, 4, 8, 1, 3, 9, 5, 6, 1]
print(lstt)
my_sort(lstt)
print(lstt)
