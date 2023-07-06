'''
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
'''

def task2(data):
    if data.isdigit():
        return int(data)
    elif data.count('.') == 1 or data.startswith('-') and data.count('.'):
        if data.replace('.', '').replace('-','').isdigit():
            return float(data)
    elif not data.islower():
        return data.lower()
    else: return data.upper()




print(task2(input('Enter data: ')))