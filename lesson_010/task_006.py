'''
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
'''


class Animal:
    def __init__(self):
        self.name = None
        self.specific = None
        self.habitat = None

    def get_habitat(self):
        return self.habitat

    def get_name(self):
        return self.name

    def get_specific(self):
        return self.specific

    def get_info(self):
        return f'{self.name}; Место обитания: {self.habitat}; Занятие: {self.specific}'
