'''
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''


class Human:
    def __init__(self, last_name, first_name, patronymic, age):
        self._age = age
        self.patronymic = patronymic
        self.first_name = first_name
        self.last_name = last_name

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def check_age(self):
        return self._age


# h1 = Human('Belov', 'Alexandr', 'Victorivich', 22)
#
# h1.age = 33
# h1.birthday()
#
# print(h1.full_name())
# print(h1.check_age())
