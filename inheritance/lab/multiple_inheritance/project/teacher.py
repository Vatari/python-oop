from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    def __init__(self):
        pass

    def teach(self):
        return "teaching..."


man = Teacher()
print(man.sleep())
print(man.teach())
print(man.get_fired())

