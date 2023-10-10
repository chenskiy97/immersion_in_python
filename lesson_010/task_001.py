'''
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        c = 2 * pi * self.radius
        return c

    def area(self):
        s = pi * (self.radius ** 2)
        return s


circle = Circle(5)
print("Длина окружности: ", circle.circumference())
print("Площадь круга: ", circle.area())
