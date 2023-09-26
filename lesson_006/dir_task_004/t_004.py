def puzzle(str_puz: str, answer: list, cnt: int) -> int:
    print(str_puz)
    temp_cnt = 1
    answer = list(map(lambda x: x.lower(), answer))
    while temp_cnt <= cnt:
        user_str = input(f'Введите ответ: ').lower()
        if user_str in answer:
            return f'Вы отгадали с {temp_cnt} раз'
        temp_cnt += 1
    return 0
