'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''


def backpack_capacity(capacity, backpack):
    packaging_option = []
    for key, value in backpack.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


backpack = {'футболка': 1, 'шорты': 1, 'холодильник': 39, 'штаны': 2, 'кепка': 1, 'арбуз': 5}

print(backpack_capacity(15, backpack))
