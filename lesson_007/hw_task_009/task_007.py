'''
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

import os
import shutil


def sort_files(input_folder):
    extensions = {
        'Видео': ['.mp4', '.avi', '.mov'],
        'Изображения': ['.jpg', '.png', '.gif'],
        'Текст': ['.txt', '.doc', '.pdf'],
    }

    for group in extensions:
        folder_path = os.path.join(input_folder, group)
        os.makedirs(folder_path, exist_ok=True)

    files = os.listdir(input_folder)
    for file in files:
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            for group, exts in extensions.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    dest_folder = os.path.join(input_folder, group)
                    shutil.move(file_path, dest_folder)
                    break
        else:
            continue

    remaining_files = os.listdir(input_folder)
    for file in remaining_files:
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


