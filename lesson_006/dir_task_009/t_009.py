def leap_check(year):
    return True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False


def is_valid_date_2(date_string):
    day, month, year = map(int, date_string.split('.'))
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 2 and day > 29:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if 1 > year > 9999:
        return False
    if month == 2 and day == 29:
        return leap_check(year)
    return True
