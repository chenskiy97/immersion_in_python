class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def type_of_triangle(self):
        if self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b:
            return 'Треугольника с заданными сторонами существовать не может!'
        elif self.a != self.b != self.c != self.a:
            return 'Треугольник разносторонний'
        elif (self.a != self.b == self.c != self.a) or (self.a != self.b != self.c == self.a) or (
                self.a == self.b != self.c != self.a):
            return 'Треугольник равнобедренный'
        else:
            return 'Треугольник равносторонний'


# Определить и вывести тип треугольника
t = Triangle(2, 3, 2)
print(t.type_of_triangle())
