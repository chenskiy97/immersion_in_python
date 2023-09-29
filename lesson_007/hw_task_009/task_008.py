'''
✔ Напишите функцию группового переименования файлов. Она должна:
    ✔ принимать параметр желаемое конечное имя файлов.
    При переименовании в конце имени добавляется порядковый номер.
    ✔ принимать параметр количество цифр в порядковом номере.
    ✔ принимать параметр расширение исходного файла.
    Переименование должно работать только для этих файлов внутри каталога.
    ✔ принимать параметр расширение конечного файла.
    ✔ принимать диапазон сохраняемого оригинального имени. Например, для диапазона
    [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
    желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''

import os


def re_name(final_name, quantity, extension_old, extension_new, range_saves):
    files = [f for f in os.listdir() if f.endswith(extension_old)]
    for i, file in enumerate(files, 1):
        base_name = os.path.splitext(file)[0]
        new_name = base_name[range_saves[0]:range_saves[1]]
        new_name += final_name + str(i).zfill(quantity)
        new_name += extension_new
        os.rename(file, new_name)


re_name('video', 3, '.txt', '.csv', [3, 6])
