from project.animal import Animal


class Dog(Animal):
    def __init__(self):
        pass

    def bark(self):
        return "barking..."


dog = Dog()
print(dog.eat())
print(dog.bark())
