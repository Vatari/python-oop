from project.car import Car


class SportsCar(Car):
    def __init__(self):
        pass

    def race(self):
        return "racing..."


bmw = SportsCar()
print(bmw.move())
print(bmw.drive())
print(bmw.race())
