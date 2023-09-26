import random

_results = {}


def generic_puzzle():
    func_dict = {'Зимой и летом одним цветом': ['ёлка', 'ель', 'ёлочка'],
                 'Ни лает, ни кусает в дом не пускает': ['замок', 'замочек'],
                 'Висит груша нельзя скушать': ['лампочка', 'лампа']}
    while func_dict:
        key = random.choice(list(func_dict))
        yield key, func_dict.pop(key)


def puzzle_3(count: int, cnt: int) -> list:
    global _results
    puzzles = generic_puzzle()
    for _ in range(count):
        puzzle = next(puzzles)
        riddle, answer = puzzle
        temp_cnt = 1
        answer = list(map(lambda x: x.lower(), answer))
        while temp_cnt <= cnt:
            user_str = input(riddle + ' : ').lower()
            if user_str in answer:
                _results[riddle] = temp_cnt
                break
            temp_cnt += 1
        else:
            _results[riddle] = 0


def show_results():
    global _results
    result = ['Результаты:']
    max_len = len(max(list(_results), key=len))
    for riddle, count in _results.items():
        riddle += ': '
        result.append(f'{riddle:<{max_len+2}} Отгадано с {count} попытки')
    return '\n'.join(result)
