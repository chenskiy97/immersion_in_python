'''
Треугольник существует только тогда, когда summ любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
'''


# def triangle(a: int, b: int, c: int) -> str:
#     if a < b + c and b < a + c and c < a + b:
#         if a != b != c != a:
#             return 'Треугольник разносторонний'
#         if (a != b == c != a) or (a != b != c == a) or (a == b != c != a):
#             return 'Треугольник равнобедренный'
#         if a == b == c == a:
#             return 'Треугольник равносторонний'
#     else:
#         return 'Треугольника с заданными сторонами существовать не может!'
#
#
# print(triangle(10, 2, 2))

def triangle(a: int, b: int, c: int) -> str:
    if a > b + c or b > a + c or c > a + b:
        return 'Треугольника с заданными сторонами существовать не может!'
    elif a != b != c != a:
        return 'Треугольник разносторонний'
    elif (a != b == c != a) or (a != b != c == a) or (a == b != c != a):
        return 'Треугольник равнобедренный'
    else:
        return 'Треугольник равносторонний'


print(triangle(2, 3, 2))
