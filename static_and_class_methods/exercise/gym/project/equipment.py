class Equipment:
    id = 1

    def __init__(self, name):
        self.name = name
        self.equipment_id = Equipment.get_next_id()
        Equipment.id = 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Equipment <{self.equipment_id}> {self.name}"

    @staticmethod
    def get_next_id_static():
        return Equipment.id
