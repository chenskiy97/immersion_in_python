'''
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
  файлов в ней с учётом всех вложенных файлов и директорий.
'''

import os
import json
import csv
import pickle


def calculate_directory_size(directory):
    total = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total


def walk_directory(directory, file_format):
    if file_format == 'json':
        file_name = 'directory_contents.json'
        json_data = []
        for dirpath, dirnames, filenames in os.walk(directory):
            for f in filenames:
                json_data.append({
                    'type': 'file',
                    'name': f,
                    'parent_directory': dirpath,
                    'path': os.path.join(dirpath, f),
                    'size_bytes': os.path.getsize(os.path.join(dirpath, f))
                })
            for d in dirnames:
                json_data.append({
                    'type': 'directory',
                    'name': d,
                    'parent_directory': dirpath,
                    'path': os.path.join(dirpath, d),
                    'size_bytes': calculate_directory_size(os.path.join(dirpath, d))
                })

        with open(file_name, 'w') as f:
            json.dump(json_data, f)

    elif file_format == 'csv':
        file_name = 'directory_contents.csv'
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Type', 'Name', 'Parent Directory', 'Path', 'Size(Bytes)'])
            for dirpath, dirnames, filenames in os.walk(directory):
                for f in filenames:
                    writer.writerow(
                        ['file', f, dirpath, os.path.join(dirpath, f), os.path.getsize(os.path.join(dirpath, f))])
                for d in dirnames:
                    writer.writerow(['directory', d, dirpath, os.path.join(dirpath, d),
                                     calculate_directory_size(os.path.join(dirpath, d))])

    elif file_format == 'pickle':
        file_name = 'directory_contents.pkl'
        data = []
        for dirpath, dirnames, filenames in os.walk(directory):
            for f in filenames:
                data.append({
                    'type': 'file',
                    'name': f,
                    'parent_directory': dirpath,
                    'path': os.path.join(dirpath, f),
                    'size_bytes': os.path.getsize(os.path.join(dirpath, f))
                })
            for d in dirnames:
                data.append({
                    'type': 'directory',
                    'name': d,
                    'parent_directory': dirpath,
                    'path': os.path.join(dirpath, d),
                    'size_bytes': calculate_directory_size(os.path.join(dirpath, d))
                })

        with open(file_name, 'wb') as f:
            pickle.dump(data, f)

    else:
        print('Invalid file format')


directory = '/home/vladislav/Загрузки/Telegram Desktop'
file_formats = ['json', 'csv', 'pickle']

for file_format in file_formats:
    walk_directory(directory, file_format)
