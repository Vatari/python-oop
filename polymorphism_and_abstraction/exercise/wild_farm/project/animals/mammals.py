from typing import List

from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD: List[str] = ["Vegetable", "Fruit"]
    WEIGHT_INCREMENT: float = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOOD: List[str] = ["Meat"]
    WEIGHT_INCREMENT: float = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOOD: List[str] = ["Vegetable", "Meat"]
    WEIGHT_INCREMENT: float = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOOD: List[str] = ["Meat"]
    WEIGHT_INCREMENT: float = 1.00

    def make_sound(self):
        return "ROAR!!!"
