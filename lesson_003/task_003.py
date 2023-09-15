"""
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

example_tuple = ('string1', 42, True, None, 2.71828, 'hello world', b'bytes', [1, 2, 3], (1, 2), {'key1': 'value1'})

dict_of_lists = {}

for item in example_tuple:
    if type(item) not in dict_of_lists:
        dict_of_lists[type(item)] = [item]
    else:
        dict_of_lists[type(item)].append(item)

print(dict_of_lists)