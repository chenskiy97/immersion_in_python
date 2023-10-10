'''Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса'''
from task_006 import Animal


class Fish(Animal):
    def __init__(self, name, habitat, specific):
        super().__init__()
        self.specific = specific
        self.name = name
        self.habitat = habitat


class Bird(Animal):
    def __init__(self, name, habitat, specific):
        super().__init__()
        self.specific = specific
        self.name = name
        self.habitat = habitat


class Predator(Animal):
    def __init__(self, name, habitat, specific):
        super().__init__()
        self.specific = specific
        self.name = name
        self.habitat = habitat
