class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml_: int):
        diff = self.capacity - self.content
        if diff >= ml_:
            self.content += ml_
            self.capacity -= ml_
            return f"Glass filled with {ml_} ml"
        return f"Cannot add {ml_} ml"

    def empty(self):
        self.content = 0
        self.capacity = 250
        return f"Glass is now empty"

    def info(self):
        if self.capacity < 0:
            self.capacity = 0
        return f"{self.capacity} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
