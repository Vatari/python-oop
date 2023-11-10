from project.animal import Animal


class Cat(Animal):
    def __init__(self):
        pass

    def meow(self):
        return "meowing..."


cat = Cat()
print(cat.eat())
print(cat.meow())
