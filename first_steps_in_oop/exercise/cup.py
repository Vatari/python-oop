class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity
        self.free_space = self.size - self.quantity

    def fill(self, quantity_):
        if self.free_space >= quantity_:
            self.quantity += quantity_
            self.free_space = self.size - self.quantity

    def status(self):
        return self.free_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
