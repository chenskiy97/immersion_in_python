'''
def get_free_urinals(urinals):
    if '11' in urinals:
        return -1
    urinals = list(f'0{urinals}0')
    for i in range(1, len(urinals)-1):
        if urinals[i] == '1':
            for k in [-1, 0, 1]:
                urinals[i + k] = ' '
    free = ''.join(urinals[1:-1]).split()

    return sum([len(urinals) + 1] // 2 for urinals in free)


print(get_free_urinals('10001'))
'''
def running_average():


print(running_average(11))