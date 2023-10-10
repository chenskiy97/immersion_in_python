'''
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
'''
from task_003 import Human


class Collaborator(Human):
    def __init__(self, employee_id, *args, **kwargs):
        self.employee_id = employee_id
        super().__init__(*args, **kwargs)

    def access_level(self):
        # print(sum(int(i) for i in str(self.employee_id)))
        level = sum(int(i) for i in str(self.employee_id)) % 7
        return level


collaborator = Collaborator(187456, 'Belov', 'Alexandr', 'Victorivich', 22)

print(collaborator.check_age())
print(collaborator.access_level())
