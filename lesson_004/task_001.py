'''
Напишите функцию для транспонирования матрицы
'''


def transparent(*a_list):
    matrix = list(a_list)
    col = max([len(matrix[i]) for i in range(len(matrix))])
    for a in list(a_list):
        if len(a) != col:
            raise TransparentError(col, len(matrix))
    return list(zip(matrix))


print(transparent([1, 3, 5], [2, 4, 6, 4]))
