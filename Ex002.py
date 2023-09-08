def count_sheriff(s):
    words = [s.count('s'), s.count('h'), s.count('e'), s.count('r'), s.count('i'), s.count('f')]
    result = min(words)
    return result


s = input()
max_sheriff = count_sheriff(s)
print(max_sheriff)
