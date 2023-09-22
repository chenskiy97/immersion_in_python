'''
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итератор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
'''

text = 'Hello World'
dict_letters = {char: ord(char) for char in text}

iter_dict = iter(dict_letters.items())

print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
