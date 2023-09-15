'''
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
'''

# example_list = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7]
#
# result = []
#
# for item in set(example_list):
#     result.extend(item for i in range(example_list.count(item)) if i % 2 == 0)
# print(result)
#
my_list = [2, 3, 4, 5, 3, 6, 7, 2, 4, 9, 5]
unique_items = list(set(my_list))
result_list = []

for item in my_list:
    if my_list.count(item) == 1:
        result_list.append(item)

print(result_list)