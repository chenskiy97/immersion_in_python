'''
Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
'''
from task_006 import Animal
from task_005 import Bird, Fish, Predator


class AnimalFactory:
    def create_animal(self, animal_type, name, habitat, specific):
        if animal_type == 'Рыба':
            return Fish(name, habitat, specific)
        elif animal_type == 'Птица':
            return Bird(name, habitat, specific)
        elif animal_type == 'Хищник':
            return Predator(name, habitat, specific)
        else:
            return "Invalid animal type"


factory = AnimalFactory()

a1 = factory.create_animal('Рыба', 'Форель', 'Океан', 'Плавает')

a2 = factory.create_animal('Птица', 'Дятел ', 'Лес', 'Стучит')

a3 = factory.create_animal('Хищник', 'Лев', 'Савана', 'Охотится')


print(a1.get_info())
print(a2.get_info())
print(a3.get_info())
