'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''


def fit_backpack(items, capacity):
    items_list = list(items.items())
    num_items = len(items_list)
    max_val = 0
    max_combination = None

    for i in range(2 ** num_items):
        combination = []
        sum_wt = 0
        sum_val = 0
        for j in range(num_items):
            if i & (1 << j):
                combination.append(items_list[j])
                sum_wt += items_list[j][1]
                sum_val += items_list[j][1]

        if sum_wt <= capacity and sum_val > max_val:
            max_val = sum_val
            max_combination = combination

    return max_combination


items = {"спальник": 1200, "бутылка с водой": 2000, "фонарик": 500, "теплая одежда": 1500, "чайник": 800}

print(fit_backpack(items, 2500))



# def backpack_capacity(capacity, backpack):
#     packaging_option = []
#     for key, value in backpack.items():
#         if value <= capacity:
#             capacity -= value
#             packaging_option.append(key)
#     return packaging_option
#
#
# backpack = {'футболка': 1, 'шорты': 1, 'холодильник': 39, 'штаны': 2, 'кепка': 1, 'арбуз': 5}
#
# print(backpack_capacity(15, backpack))
