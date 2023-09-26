import random


def generic_puzzle():
    func_dict = {'Зимой и летом одним цветом': ['ёлка', 'ель', 'ёлочка'],
                 'Ни лает, ни кусает в дом не пускает': ['замок', 'замочек'],
                 'Висит груша нельзя скушать': ['лампочка', 'лампа']}
    while func_dict:
        key = random.choice(list(func_dict))
        yield key, func_dict.pop(key)


def puzzle_2(count: int, cnt: int) -> list:
    result = []
    puzzles = generic_puzzle()
    for _ in range(count):
        puzzle = next(puzzles)
        riddle, answer = puzzle
        temp_cnt = 1
        answer = list(map(lambda x: x.lower(), answer))
        while temp_cnt <= cnt:
            user_str = input(riddle + ' : ').lower()
            if user_str in answer:
                result.append(temp_cnt)
                break
            temp_cnt += 1
        else:
            result.append(0)
    return result
