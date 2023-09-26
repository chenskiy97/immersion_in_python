'''
� Улучшаем задачу 2
� Добавьте возможность запуска функции “угадайки”
из модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов:
параметры вызова функции.
� Для преобразования строковых аргументов
командной строки в числовые параметры
используйте генераторное выражение.
'''
import sys
from dir_task_003 import ran2

if __name__ == '__main__':
    options = list(map(int, sys.argv[1:]))
    low_limit = 1
    high_limit = 100
    count = 10
    if len(options) == 1:
        high_limit = options[0]
    elif len(options) == 2:
        low_limit, high_limit = options
    else:
        low_limit, high_limit, count, *_ = options
    ran2(low_limit, high_limit, count)
