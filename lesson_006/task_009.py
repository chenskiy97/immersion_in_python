'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей
даты на проверку.
'''

import sys
from dir_task_009 import is_valid_date_2

if __name__ == '__main__':
    # print(is_valid_date_2('29.02.2001'))
    options = sys.argv
    date = options[1]
    print(is_valid_date_2(date))
