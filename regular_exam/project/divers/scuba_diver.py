from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch: int):
        reduction_value = int(0.3 * time_to_catch)
        self.oxygen_level = max(0, self.oxygen_level - reduction_value)

    def renew_oxy(self):
        self.oxygen_level = 540
