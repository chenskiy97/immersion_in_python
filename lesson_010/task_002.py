'''
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''


class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width if width != 0 else length

    def calculate_perimeter_rectangle(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def calculate_area_rectangle(self):
        area = self.length * self.width
        return area


rectagle = Rectangle(2,5)
print('Периметр: ', rectagle.calculate_perimeter_rectangle())
print('Площадь: ', rectagle.calculate_area_rectangle())
