'''
✔ Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
'''


def duplicate(data):
    return set(i for i in data if data.count(i) > 1)


my_list = [1, 2, 3, 2, 2, 5, 5, 1, 7, 6, 'f', 'f', 'f', 'q', 's', 'a']
print(duplicate(my_list))
