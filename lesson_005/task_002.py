'''
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
'''

text = 'Hello World'
dict_letters = {char: ord(char) for char in text}
gen_dict = ({char: ord(char)} for char in text)

print(dict_letters)
print(*gen_dict)
