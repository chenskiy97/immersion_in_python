'''
✔ Напишите функцию для транспонирования матрицы
'''


def transpose(matrix):
    return list(map(list, zip(*matrix)))


m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(transpose(m))
