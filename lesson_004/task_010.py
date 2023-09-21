'''
✔ Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление
'''


def my_func(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[key] = str(value) if not isinstance(value, dict) else my_func(**value)
    return result


print(my_func(key1=1, key2={"subkey1": 2, "subkey2": {"subsubkey": 3}}, key3=4))
