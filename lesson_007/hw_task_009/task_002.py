'''
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''

import random
import string

vowels = "aeiou"


def generate_pseudonyms(num_pseudonyms, min_length=4, max_length=7):
    pseudonyms = []
    while len(pseudonyms) < num_pseudonyms:
        length = random.randint(min_length, max_length)
        pseudonym = random.choice(string.ascii_uppercase)
        for _ in range(length - 1):
            pseudonym += random.choice(string.ascii_lowercase)
        if any(vowel in pseudonym for vowel in vowels):
            pseudonyms.append(pseudonym)

    with open("task_002.txt", "w") as file:
        for pseudonym in pseudonyms:
            file.write(pseudonym + "\n")


generate_pseudonyms(10)
