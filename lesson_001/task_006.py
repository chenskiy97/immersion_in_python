def leap_year(year):
    if year >= 1582:
        return 'Високосный' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 'Не високосный'
    else:
        return 'год ввода Григорианского календаря 1582'


print(leap_year(int(input('Введите год: '))))
