'''
✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''
import os


def split_file_path(file_path):
    file_dir = os.path.dirname(file_path)
    file_name_ext = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(file_name_ext)
    return (file_dir, file_name, file_ext)


print(split_file_path('/c/d/dir/file.txt'))
