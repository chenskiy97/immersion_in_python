'''
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''

import random


def fills_file(num_lines, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(num_lines):
            rand_int = random.randint(-1000, 1000)
            rand_float = random.uniform(-1000, 1000)
            pair = f'{rand_int}|{rand_float}\n'
            f.write(pair)


nl = 5
fn = 'task_001.txt'
fills_file(nl, fn)
