'''
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
'''

# text = input("Введите строку текста: ")
# freq_dict = {}
# for char in text:
#     if char in freq_dict:
#         freq_dict[char] += 1
#     else:
#         freq_dict[char] = 1
#
# for key in sorted(freq_dict, key=lambda k: ord(k)):
#     print(key, freq_dict[key])

text = input("Введите строку текста: ")
freq_dict = {}

for char in text:
    if char not in freq_dict:
        freq_dict[char] = text.count(char)

for key in sorted(freq_dict, key=lambda k: ord(k)):
    print(key, freq_dict[key])
