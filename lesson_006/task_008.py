'''
� Создайте пакет с всеми модулями, которые вы
создали за время занятия.
� Добавьте в __init__ пакета имена модулей внутри
дандер __all__.
� В модулях создайте дандер __all__ и укажите только
те функции, которые могут верно работать за
пределами модуля.
'''

from dir_task_008 import ran, ran2, puzzle, puzzle_2, puzzle_3, show_results

if __name__ == '__main__':
    puzzle_3(2, 2)
    print(show_results())